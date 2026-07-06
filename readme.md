PR URL
   │
   ▼
pr_url_parser
   │
   ▼
github_fetcher
   │
   ▼
diff_parser
   │
   ▼
parsed_files
   │
   ▼
                RunnableParallel
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
SecurityAgent  QualityAgent  TestCoverageAgent
      │              │              │
      └──────────────┼──────────────┘
                     ▼
               Orchestrator
                     ▼
                Final PRReview
                     ▼
         markdown_formatter
                     ▼
          comment_poster (GitHub)

          