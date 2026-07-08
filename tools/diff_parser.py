from unidiff import PatchSet


class DiffParser:

    def parse(self, diff_text: str) -> list[dict]:
        patch = PatchSet(diff_text)

        parsed_files = []

        for file in patch:

            file_data = {
                "file_path": file.path,
                "added_lines": [],
                "removed_lines": []
            }

            for hunk in file:

                for line in hunk:

                    if line.is_added:
                        file_data["added_lines"].append({
                            "line_number": line.target_line_no,
                            "content": line.value
                        })

                    elif line.is_removed:
                        file_data["removed_lines"].append({
                            "line_number": line.source_line_no,
                            "content": line.value
                        })

            parsed_files.append(file_data)

        return parsed_files
