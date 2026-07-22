"""Shared visual theme for generated TrendRadar HTML reports."""


def get_report_theme_css(accent: str = "#22c55e") -> str:
    """Return an accessible theme layered over the report's base styles."""
    return f"""
        :root {{
            color-scheme: light dark;
            --tr-bg: #f3f6f8;
            --tr-surface: rgba(255, 255, 255, 0.94);
            --tr-surface-strong: #ffffff;
            --tr-surface-soft: #f8fafc;
            --tr-text: #0f172a;
            --tr-muted: #526174;
            --tr-border: #dce4ea;
            --tr-accent: {accent};
            --tr-accent-strong: #15803d;
            --tr-header: #07111f;
            --tr-radius-lg: 22px;
            --tr-radius-md: 14px;
            --tr-shadow: 0 24px 70px rgba(15, 23, 42, 0.12);
            --tr-shadow-soft: 0 8px 28px rgba(15, 23, 42, 0.08);
        }}
        html {{ scroll-behavior: smooth; }}
        body {{
            min-height: 100dvh;
            padding: clamp(12px, 2.5vw, 32px);
            background: radial-gradient(circle at 12% 0%, rgba(34, 197, 94, 0.12), transparent 30rem), radial-gradient(circle at 90% 8%, rgba(14, 165, 233, 0.10), transparent 28rem), var(--tr-bg);
            color: var(--tr-text);
            font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 16px;
            line-height: 1.65;
        }}
        .container {{
            max-width: 960px;
            border: 1px solid rgba(148, 163, 184, 0.24);
            border-radius: var(--tr-radius-lg);
            background: var(--tr-surface);
            box-shadow: var(--tr-shadow);
        }}
        .header {{
            padding: clamp(34px, 6vw, 64px) clamp(20px, 5vw, 56px) 34px;
            background: linear-gradient(120deg, rgba(34, 197, 94, 0.18), transparent 42%), radial-gradient(circle at 85% 10%, rgba(56, 189, 248, 0.18), transparent 38%), var(--tr-header);
            border-bottom: 1px solid rgba(148, 163, 184, 0.18);
        }}
        .header-title {{
            margin-bottom: 24px;
            font-family: Newsreader, Georgia, "Noto Serif SC", serif;
            font-size: clamp(28px, 5vw, 46px);
            line-height: 1.12;
            letter-spacing: -0.025em;
        }}
        .header-watermark {{ opacity: 0.46; }}
        .header-info {{ gap: 10px; max-width: 720px; margin: 0 auto; }}
        .info-item {{
            min-width: 0;
            padding: 12px 14px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(12px);
        }}
        .info-label {{ color: rgba(255, 255, 255, 0.68); }}
        .info-value {{ font-variant-numeric: tabular-nums; }}
        .save-buttons {{ gap: 8px; }}
        .save-btn, .save-dropdown-trigger, .toggle-wide-btn, .toggle-dark-btn, .fab-btn {{
            min-width: 44px;
            min-height: 44px;
            border-color: rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.10);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            backdrop-filter: blur(14px);
            touch-action: manipulation;
        }}
        .save-btn:hover, .save-dropdown-trigger:hover, .toggle-wide-btn:hover, .toggle-dark-btn:hover {{ background: rgba(255, 255, 255, 0.20); }}
        button:focus-visible, a:focus-visible, input:focus-visible {{ outline: 3px solid #38bdf8; outline-offset: 3px; }}
        .content {{ padding: clamp(22px, 4.5vw, 48px); }}
        .word-group, .feed-group, .new-section, .rss-section, .standalone-section, .ai-section {{ scroll-margin-top: 20px; }}
        .word-header, .feed-header, .rss-section-header, .standalone-section-header, .ai-section-header {{ border-color: var(--tr-border); }}
        .word-name, .feed-name, .rss-section-title, .standalone-section-title, .ai-section-title {{ color: var(--tr-text); letter-spacing: -0.01em; }}
        .word-count, .feed-count, .news-meta, .rss-meta, .rss-summary {{ color: var(--tr-muted); }}
        .news-item, .rss-item, .standalone-item, .new-item, .ai-block {{
            border: 1px solid var(--tr-border);
            border-radius: var(--tr-radius-md);
            background: var(--tr-surface-strong);
            box-shadow: var(--tr-shadow-soft);
            transition: border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
        }}
        .news-item {{ margin-bottom: 12px; padding: 16px; }}
        .rss-item, .standalone-item, .new-item, .ai-block {{ border-left: 3px solid var(--tr-accent); }}
        .news-item:hover, .rss-item:hover, .standalone-item:hover, .new-item:hover {{
            border-color: var(--tr-accent);
            box-shadow: 0 14px 36px rgba(15, 23, 42, 0.12);
            transform: translateY(-1px);
        }}
        .news-title, .rss-title {{ color: var(--tr-text); }}
        .news-link, .rss-link, .footer-link {{ color: #0369a1; text-decoration-thickness: 1px; text-underline-offset: 3px; }}
        .news-link:hover, .rss-link:hover, .footer-link:hover {{ color: var(--tr-accent-strong); }}
        .search-input {{ min-height: 46px; border-color: var(--tr-border); border-radius: 12px; background: var(--tr-surface-strong); color: var(--tr-text); }}
        .tab-btn {{ min-height: 44px; touch-action: manipulation; }}
        .tab-btn.active {{ color: var(--tr-accent-strong); }}
        .reading-progress {{ background: linear-gradient(90deg, var(--tr-accent), #38bdf8); }}
        .footer {{ background: var(--tr-surface-soft); border-color: var(--tr-border); }}
        body.dark-mode {{
            --tr-bg: #020617;
            --tr-surface: rgba(8, 17, 31, 0.94);
            --tr-surface-strong: #0f1b2d;
            --tr-surface-soft: #0a1424;
            --tr-text: #f1f5f9;
            --tr-muted: #a9b7c8;
            --tr-border: #2d3b4f;
            --tr-accent-strong: #4ade80;
            --tr-shadow: 0 24px 80px rgba(0, 0, 0, 0.42);
            --tr-shadow-soft: 0 8px 28px rgba(0, 0, 0, 0.24);
            background: radial-gradient(circle at 12% 0%, rgba(34, 197, 94, 0.10), transparent 30rem), radial-gradient(circle at 90% 8%, rgba(14, 165, 233, 0.10), transparent 28rem), var(--tr-bg);
            color: var(--tr-text);
        }}
        body.dark-mode .container, body.dark-mode .news-item, body.dark-mode .rss-item, body.dark-mode .standalone-item, body.dark-mode .new-item, body.dark-mode .ai-block {{ background: var(--tr-surface-strong); border-color: var(--tr-border); }}
        body.dark-mode .content {{ background: var(--tr-surface); }}
        body.dark-mode .word-name, body.dark-mode .feed-name, body.dark-mode .news-title, body.dark-mode .rss-title, body.dark-mode .rss-section-title, body.dark-mode .standalone-section-title, body.dark-mode .ai-section-title {{ color: var(--tr-text); }}
        body.dark-mode .news-link, body.dark-mode .rss-link, body.dark-mode .footer-link {{ color: #7dd3fc; }}
        body.dark-mode .footer {{ background: var(--tr-surface-soft); border-color: var(--tr-border); }}
        @media (max-width: 640px) {{
            body {{ padding: 0; font-size: 16px; }}
            .container {{ width: 100%; border: 0; border-radius: 0; }}
            .header {{ padding: 76px 16px 24px; }}
            .header-info {{ grid-template-columns: 1fr 1fr; gap: 8px; }}
            .info-item {{ padding: 10px 8px; }}
            .content {{ padding: 20px 14px 28px; }}
            .save-buttons {{ position: absolute; top: 14px; right: 14px; width: auto; margin: 0; flex-direction: row; justify-content: flex-end; }}
            .save-btn {{ width: auto; }}
            .news-item {{ align-items: flex-start; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            html {{ scroll-behavior: auto; }}
            *, *::before, *::after {{ scroll-behavior: auto !important; animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; }}
        }}
    """
