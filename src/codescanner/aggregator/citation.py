"""Citation aggregator module."""
from . import Aggregator
from ..analyser import AnalyserType
from ..report import Report


class Citation(Aggregator):
    @classmethod
    def get_type(cls) -> AnalyserType:
        """Returns analyser type of the aggregator."""
        return AnalyserType.CITATION


    @classmethod
    def aggregate(cls, report: Report, results: dict):
        """Aggregates available analysis results.

        Args:
            report (Report): Analysis report.
            results (dict): Analyser results.
        """
        if not results:
            report.add_issue(cls, "No citation file.")

        else:
            report.add_notice(cls, "Citation file found.")
