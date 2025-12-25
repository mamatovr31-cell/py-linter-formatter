def format_linter_error(error: dict) -> dict:
    def format_linter_error(error):
        return {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }

def format_single_linter_file(file_path: str, errors: list) -> dict:
        formatted_errors = [{"line": error["line_number"], "column": error["column_number"],
        "message": error["text"], "name": error["code"], "source": "flake8"}
        for error in errors]
        return {
            "errors": formatted_errors, "path": file_path,
            "status": "passed" if not formatted_errors else "failed"
        }

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path=path, errors=errs) for (path, errs) in linter_report.items()]

