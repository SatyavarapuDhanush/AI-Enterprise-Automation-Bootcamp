import csv

from pathlib import Path
class ReportGenerator:

    def __init__(self,output_dir="reports"):
        self.output_dir = Path(__file__).parent / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_report(self, repositories, file_name = "reports.csv"):
        file_path = self.output_dir / file_name
        headers = [
            "Name",
            "Full Name",
            "Visibility",
            "Stars",
            "Forks",
            "Open Issues",
            "URL",
            "Updated At",
                                                      
        ]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            for repo in repositories:
                writer.writerow(
                    [
                    repo.get("name", ""),
                    repo.get("full_name", ""),
                    repo.get("visibility", ""),
                    repo.get("stargazers_count", 0),
                    repo.get("forks_count", 0),
                    repo.get("open_issues_count", 0),
                    repo.get("html_url", ""),
                    repo.get("updated_at", ""),
                    ]
                )
        print(f"csv report generated: {file_path}")
        return file_path

    def generate_html(self, repositories,username='N/A', filename="repositories.html"):
        file_path = self.output_dir/filename

        rows_html= ""
        for repo in repositories:
            rows_html += f"""
            <tr>
            <td><a href="{repo.get('html_url')}" target="_blank"><strong>{repo.get('name')}</strong></a></td>
            <td><span class="badge">{repo.get('visibility')}</span></td>
            <td>{repo.get('language') or 'N/A'}</td>
                <td>⭐ {repo.get('stargazers_count', 0)}</td>
                <td>🍴 {repo.get('forks_count', 0)}</td>
                <td>{repo.get('updated_at', '')[:10]}</td>
            </tr>
            """

        html_content=f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>GitHub Automation Report</title>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                        background-color: #f6f8fa;
                        color: #24292f;
                        padding: 40px;
                    }}
                    .container {{
                        max-width: 1000px;
                        margin: 0 auto;
                        background: #ffffff;
                        border: 1px solid #d0d7de;
                        border-radius: 8px;
                        padding: 32px;
                        box-shadow: 0 3px 6px rgba(140,149,159,0.15);
                    }}
                    h1 {{ color: #0969da; border-bottom: 1px solid #d0d7de; padding-bottom: 12px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 16px; }}
                    th, td {{ text-align: left; padding: 12px 16px; border-bottom: 1px solid #d0d7de; }}
                    th {{ background-color: #f6f8fa; color: #57606a; }}
                    .badge {{
                        padding: 2px 8px; font-size: 12px; border-radius: 12px;
                        background-color: #ddf4ff; color: #0969da; border: 1px solid rgba(54,115,217,0.15);
                    }}
                    a {{ color: #0969da; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>📊 GitHub Repositories Report</h1>
                    <p>User Name : <strong>{username}</strong></p>
                    <p>Total repositories:<strong>{len(repositories)}</strong></p>
                    <table>
                        <thead>
                            <tr>
                                <th>Repository Name</th>
                                <th>Visibility</th>
                                <th>Language</th>
                                <th>Stars</th>
                                <th>Forks</th>
                                <th>Last Updated</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows_html}
                        </tbody>
                    </table>
                </div>
            </body>
        </html>
        """

        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_content)

        print(f"✅ HTML Report generated: {file_path}")
        return file_path


        