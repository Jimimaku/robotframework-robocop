from robot.parsing.model.statements import Return, KeywordCall
from robocop.checkers import BaseChecker
from robocop.messages import MessageSeverity


def register(linter):
    linter.register_checker(MiscChecker(linter))


class MiscChecker(BaseChecker):
    msgs = {
        "0901": (
            "keyword-after-return",
            "Keyword call after [Return] statement",
            MessageSeverity.ERROR
        )
    }

    def visit_Keyword(self, node):
        returned = False
        for child in node.body:
            if isinstance(child, Return):
                returned = True
            elif isinstance(child, KeywordCall) and returned:
                self.report("keyword-after-return", node=child)