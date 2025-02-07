"""Documentation analyser module."""
from pathlib import Path

from . import Analyser, AnalyserType
from ..report import Report


class Documentation(Analyser):
    """Documentation analyser class."""

    @classmethod
    def get_type(cls) -> AnalyserType:
        """Returns analyser type."""
        return AnalyserType.DOCUMENTATION


    @classmethod
    def get_name(cls) -> str:
        """Returns analyser name."""
        return "Documentation"


    @classmethod
    def includes(cls, path: Path) -> list[str]:
        """Returns file and directory patterns to be included in the analysis.

        Args:
            path (Path): Path of the code base.

        Returns:
            List of file and directory patterns.
        """
        return [
            '/readme',
            '/readme.md',
            '/readme.rst',
        ]


    @classmethod
    def analyse_file(cls, path: Path, report: Report) -> dict:
        """Analyses a git file.

        Args:
            path (Path): Path of the git file.
            report (Report): Analyse report.

        Returns:
            Dictionary of the analysis results.
        """
        report.add_metadata(cls, 'readme_file', path.relative_to(report.path), path)
