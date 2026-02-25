#!/usr/bin/env python3
"""
Notebook Analyzer - Automatically generates descriptions for Jupyter notebooks
This script reads Jupyter notebook files and creates structured descriptions
based on their content, including titles, objectives, and key topics.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional


class NotebookAnalyzer:
    """Analyzes Jupyter notebooks and generates descriptions."""

    def __init__(self, notebook_path: str):
        """
        Initialize the analyzer with a notebook file.
        
        Args:
            notebook_path: Path to the Jupyter notebook (.ipynb file)
        """
        self.notebook_path = Path(notebook_path)
        self.notebook_data = None
        self.title = ""
        self.description = ""
        self.topics = []
        
    def load_notebook(self) -> bool:
        """
        Load the notebook JSON data.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.notebook_path, 'r', encoding='utf-8') as f:
                self.notebook_data = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading notebook: {e}")
            return False
    
    def extract_title(self) -> str:
        """
        Extract the title from the notebook.
        Looks for first H1 markdown heading or uses filename.
        
        Returns:
            The notebook title
        """
        if not self.notebook_data:
            return self.notebook_path.stem
        
        cells = self.notebook_data.get('cells', [])
        
        # Look for first H1 heading in markdown cells
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                h1_match = re.search(r'^#\s+(.+)$', source, re.MULTILINE)
                if h1_match:
                    return h1_match.group(1).strip()
        
        # Fallback to filename
        return self.notebook_path.stem.replace('_', ' ').replace('-', ' ').title()
    
    def extract_topics(self) -> List[str]:
        """
        Extract key topics from the notebook.
        Looks for H2 and H3 headings in markdown cells.
        
        Returns:
            List of topics found in the notebook
        """
        if not self.notebook_data:
            return []
        
        topics = []
        cells = self.notebook_data.get('cells', [])
        
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                # Find H2 and H3 headings
                headings = re.findall(r'^#{2,3}\s+(.+)$', source, re.MULTILINE)
                topics.extend([h.strip() for h in headings])
        
        return topics
    
    def count_code_cells(self) -> int:
        """
        Count the number of code cells in the notebook.
        
        Returns:
            Number of code cells
        """
        if not self.notebook_data:
            return 0
        
        cells = self.notebook_data.get('cells', [])
        return sum(1 for cell in cells if cell.get('cell_type') == 'code')
    
    def extract_description(self) -> str:
        """
        Extract or generate a description for the notebook.
        Looks for the first substantial markdown paragraph.
        
        Returns:
            Description text
        """
        if not self.notebook_data:
            return "No description available."
        
        cells = self.notebook_data.get('cells', [])
        
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                # Remove headings
                text = re.sub(r'^#+\s+.+$', '', source, flags=re.MULTILINE)
                # Get first paragraph
                paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
                if paragraphs:
                    # Return first substantial paragraph (more than 20 chars)
                    for para in paragraphs:
                        if len(para) > 20:
                            return para
        
        return f"A notebook covering {len(self.extract_topics())} topics with {self.count_code_cells()} code examples."
    
    def analyze(self) -> Dict[str, any]:
        """
        Perform complete analysis of the notebook.
        
        Returns:
            Dictionary with analysis results
        """
        if not self.load_notebook():
            return {
                'title': self.notebook_path.stem,
                'description': 'Error loading notebook',
                'topics': [],
                'code_cells': 0,
                'filename': self.notebook_path.name
            }
        
        self.title = self.extract_title()
        self.description = self.extract_description()
        self.topics = self.extract_topics()
        code_cells = self.count_code_cells()
        
        return {
            'title': self.title,
            'description': self.description,
            'topics': self.topics,
            'code_cells': code_cells,
            'filename': self.notebook_path.name
        }
    
    def generate_markdown_description(self) -> str:
        """
        Generate a markdown-formatted description.
        
        Returns:
            Markdown formatted description
        """
        analysis = self.analyze()
        
        md = f"### {analysis['title']}\n\n"
        md += f"{analysis['description']}\n\n"
        
        if analysis['topics']:
            md += "**Topics Covered:**\n"
            for topic in analysis['topics']:
                md += f"- {topic}\n"
            md += "\n"
        
        md += f"**Code Examples:** {analysis['code_cells']} cells\n"
        
        return md


def analyze_directory(directory: str, output_file: str = "NOTEBOOKS.md") -> None:
    """
    Analyze all notebooks in a directory and generate a summary file.
    
    Args:
        directory: Path to directory containing notebooks
        output_file: Name of output markdown file
    """
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"Directory not found: {directory}")
        return
    
    # Find all notebook files
    notebooks = sorted(directory_path.glob("**/*.ipynb"))
    
    # Filter out checkpoint files
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    if not notebooks:
        print(f"No notebooks found in {directory}")
        return
    
    # Generate summary
    output_path = directory_path / output_file
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Notebook Descriptions\n\n")
        f.write("This document provides automatically generated descriptions ")
        f.write("for all Jupyter notebooks in this repository.\n\n")
        f.write("---\n\n")
        
        for notebook in notebooks:
            print(f"Analyzing: {notebook.name}")
            analyzer = NotebookAnalyzer(notebook)
            
            # Get relative path from directory
            rel_path = notebook.relative_to(directory_path)
            
            f.write(f"## {rel_path}\n\n")
            f.write(analyzer.generate_markdown_description())
            f.write("\n---\n\n")
    
    print(f"\nSummary generated: {output_path}")


def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze Jupyter notebooks and generate descriptions'
    )
    parser.add_argument(
        'path',
        help='Path to notebook file or directory'
    )
    parser.add_argument(
        '-o', '--output',
        default='NOTEBOOKS.md',
        help='Output file name for directory analysis (default: NOTEBOOKS.md)'
    )
    
    args = parser.parse_args()
    path = Path(args.path)
    
    if path.is_file() and path.suffix == '.ipynb':
        # Single notebook analysis
        analyzer = NotebookAnalyzer(path)
        print(analyzer.generate_markdown_description())
    elif path.is_dir():
        # Directory analysis
        analyze_directory(args.path, args.output)
    else:
        print(f"Error: {args.path} is not a valid notebook file or directory")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
