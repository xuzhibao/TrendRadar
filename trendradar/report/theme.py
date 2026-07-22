"""Production visual system shared by TrendRadar HTML reports."""


def get_report_theme_css(accent: str = "#ec4899") -> str:
    """Return the Reframe bento/editorial visual system."""
    return f"""
        :root {{
            color-scheme: light dark;
            --primary: #7c3aed;
            --primary-strong: #5b21b6;
            --secondary: #4f46e5;
            --accent: {accent};
            --success: #059669;
            --warning: #d97706;
            --danger: #dc2626;
            --canvas: #f7f5fb;
            --canvas-deep: #ede9f7;
            --surface: #ffffff;
            --surface-soft: #faf9fc;
            --surface-raised: rgba(255, 255, 255, 0.88);
            --ink: #171427;
            --ink-soft: #565168;
            --ink-faint: #827c91;
            --line: #e8e3ef;
            --line-strong: #d8d0e4;
            --ring: #8b5cf6;
            --shadow-xs: 0 1px 2px rgba(36, 28, 53, .05);
            --shadow-sm: 0 8px 24px rgba(50, 36, 75, .07);
            --shadow-md: 0 18px 48px rgba(50, 36, 75, .11);
            --radius-sm: 10px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 32px;
            --ease: cubic-bezier(.2, .8, .2, 1);
        }}

        * {{ scrollbar-width: thin; scrollbar-color: #c4b5fd transparent; }}
        html {{ scroll-behavior: smooth; background: var(--canvas); }}
        body {{
            min-height: 100dvh;
            margin: 0;
            padding: 24px;
            overflow-x: hidden;
            background:
                radial-gradient(circle at 8% 0%, rgba(124, 58, 237, .13), transparent 32rem),
                radial-gradient(circle at 92% 6%, rgba(236, 72, 153, .10), transparent 28rem),
                linear-gradient(180deg, #fbfaff 0, var(--canvas) 34rem);
            color: var(--ink);
            font-family: Inter, "SF Pro Text", "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 16px;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}
        body.no-overflow {{ overflow: hidden; }}
        a {{ text-underline-offset: 3px; }}
        button, input {{ font: inherit; }}
        button, a {{ touch-action: manipulation; }}
        button:focus-visible, a:focus-visible, input:focus-visible {{
            outline: 3px solid color-mix(in srgb, var(--ring) 58%, white);
            outline-offset: 3px;
        }}

        .container,
        body.wide-mode .container {{
            width: min(100%, 1320px);
            max-width: 1320px;
            margin: 0 auto;
            overflow: visible;
            border: 0;
            border-radius: 0;
            background: transparent;
            box-shadow: none;
        }}

        .header {{
            position: relative;
            isolation: isolate;
            min-height: 390px;
            padding: 40px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,.14);
            border-radius: var(--radius-xl);
            background:
                linear-gradient(115deg, rgba(139, 92, 246, .26), transparent 38%),
                radial-gradient(circle at 88% 18%, rgba(236, 72, 153, .26), transparent 30%),
                linear-gradient(145deg, #1b1531 0%, #2c1754 52%, #11152a 100%);
            color: white;
            box-shadow: 0 32px 80px rgba(45, 28, 79, .24);
        }}
        .header::before {{
            content: "";
            position: absolute;
            inset: 0;
            z-index: -1;
            opacity: .22;
            background-image: linear-gradient(rgba(255,255,255,.08) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px);
            background-size: 48px 48px;
            -webkit-mask-image: linear-gradient(to bottom, black, transparent 82%);
            mask-image: linear-gradient(to bottom, black, transparent 82%);
        }}
        .header::after {{
            content: "";
            position: absolute;
            z-index: -1;
            right: -90px;
            bottom: -180px;
            width: 430px;
            height: 430px;
            border: 80px solid rgba(255,255,255,.055);
            border-radius: 50%;
        }}
        .header-watermark {{
            top: 30px;
            left: 40px;
            transform: none;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .24em;
            color: rgba(255,255,255,.48);
            -webkit-mask-image: none;
            mask-image: none;
        }}

        .save-buttons {{
            top: 24px;
            right: 24px;
            gap: 8px;
            align-items: center;
        }}
        .guide-link,
        .save-btn,
        .save-dropdown-trigger,
        .toggle-wide-btn,
        .toggle-dark-btn {{
            display: inline-flex;
            min-width: 44px;
            min-height: 44px;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin: 0;
            padding: 0 14px;
            border: 1px solid rgba(255,255,255,.16);
            border-radius: 12px;
            background: rgba(255,255,255,.09);
            color: white;
            box-shadow: none;
            text-decoration: none;
            backdrop-filter: blur(16px);
            transition: background 180ms var(--ease), border-color 180ms var(--ease), transform 180ms var(--ease);
        }}
        .guide-link:hover,
        .save-btn:hover,
        .save-dropdown-trigger:hover,
        .toggle-wide-btn:hover,
        .toggle-dark-btn:hover {{
            border-color: rgba(255,255,255,.34);
            background: rgba(255,255,255,.17);
            transform: translateY(-1px);
        }}
        .guide-link svg, .save-btn svg {{ width: 18px; height: 18px; flex: 0 0 auto; }}
        .toggle-wide-btn svg, .toggle-dark-btn svg {{ width: 20px; height: 20px; }}
        .save-btn {{ border-radius: 12px 0 0 12px; }}
        .save-dropdown-trigger {{ width: 42px; min-width: 42px; padding: 0; border-radius: 0 12px 12px 0; }}
        .save-dropdown-trigger svg {{ width: 16px; height: 16px; }}
        .save-dropdown-menu {{
            top: calc(100% + 8px);
            min-width: 180px;
            padding: 8px;
            border: 1px solid var(--line);
            border-radius: 14px;
            background: rgba(255,255,255,.96);
            box-shadow: var(--shadow-md);
        }}
        .save-dropdown-item {{ min-height: 44px; border-radius: 9px; color: var(--ink); }}
        .save-dropdown-item:hover {{ background: #f3effb; color: var(--primary-strong); }}

        .brand-lockup {{
            display: flex;
            max-width: 760px;
            align-items: center;
            gap: 24px;
            margin-top: 62px;
            text-align: left;
        }}
        .brand-mark {{
            display: grid;
            width: 82px;
            height: 82px;
            flex: 0 0 82px;
            place-items: center;
            border: 1px solid rgba(255,255,255,.24);
            border-radius: 24px;
            background: linear-gradient(145deg, rgba(255,255,255,.22), rgba(255,255,255,.06));
            box-shadow: inset 0 1px rgba(255,255,255,.28), 0 20px 42px rgba(0,0,0,.2);
            font-size: 22px;
            font-weight: 800;
            letter-spacing: -.04em;
            backdrop-filter: blur(18px);
        }}
        .brand-kicker {{ margin-bottom: 8px; color: #d8b4fe; font-size: 11px; font-weight: 750; letter-spacing: .22em; }}
        .header-title {{
            margin: 0;
            color: white;
            font-family: Inter, "PingFang SC", sans-serif;
            font-size: clamp(34px, 5vw, 62px);
            font-weight: 760;
            line-height: 1.08;
            letter-spacing: -.055em;
        }}
        .header-subtitle {{ max-width: 620px; margin: 12px 0 0; color: rgba(255,255,255,.68); font-size: 16px; line-height: 1.7; }}
        .header-info {{
            display: grid;
            max-width: none;
            margin: 32px 0 0;
            grid-template-columns: repeat(8, minmax(0, 1fr));
            gap: 10px;
        }}
        .info-item {{
            min-width: 0;
            padding: 14px;
            border: 1px solid rgba(255,255,255,.12);
            border-radius: 14px;
            background: rgba(255,255,255,.065);
            text-align: left;
            backdrop-filter: blur(12px);
        }}
        .info-label {{ margin-bottom: 4px; color: rgba(255,255,255,.5); font-size: 11px; letter-spacing: .04em; }}
        .info-value {{ color: white; font-size: 15px; font-weight: 680; font-variant-numeric: tabular-nums; }}

        .content {{ padding: 28px 0 0; background: transparent; }}
        .search-bar {{
            position: sticky;
            top: 12px;
            z-index: 40;
            display: block;
            margin-bottom: 16px;
            padding: 10px;
            border: 1px solid rgba(216,208,228,.82);
            border-radius: 18px;
            background: rgba(255,255,255,.84);
            box-shadow: var(--shadow-sm);
            backdrop-filter: blur(18px);
        }}
        .search-label {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }}
        .search-input {{
            width: 100%;
            min-height: 50px;
            padding: 0 18px 0 48px;
            border: 0;
            border-radius: 12px;
            background-color: #f7f4fb;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%237c3aed' stroke-width='1.8'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 16px center;
            color: var(--ink);
            box-shadow: none;
        }}
        .search-input::placeholder {{ color: var(--ink-faint); }}

        .error-section,
        .hotlist-section,
        .new-section,
        .rss-section,
        .standalone-section,
        .ai-section {{
            margin: 0 0 18px;
            padding: 24px;
            scroll-margin-top: 96px;
            border: 1px solid var(--line);
            border-radius: var(--radius-lg);
            background: var(--surface-raised);
            box-shadow: var(--shadow-sm);
            backdrop-filter: blur(14px);
        }}
        .section-divider {{ border-top: 0; }}
        .new-section, .rss-section, .standalone-section {{ margin-top: 0; padding-top: 24px; }}
        .ai-section {{
            border-color: #ddd2f7;
            background: linear-gradient(145deg, rgba(245,243,255,.96), rgba(253,242,248,.92));
        }}
        .error-section {{ border-color: #fecaca; background: #fff7f7; }}

        .tab-bar-wrapper {{
            position: sticky;
            top: 90px;
            z-index: 30;
            margin: -8px -8px 20px;
            padding: 8px;
            border: 1px solid var(--line);
            border-radius: 16px;
            background: rgba(255,255,255,.9);
            box-shadow: var(--shadow-xs);
            backdrop-filter: blur(16px);
        }}
        .tab-bar {{ gap: 8px; scrollbar-width: none; }}
        .tab-btn {{
            min-height: 42px;
            padding: 0 14px;
            border: 1px solid transparent;
            border-radius: 11px;
            color: var(--ink-soft);
            font-weight: 600;
            transition: color 160ms var(--ease), background 160ms var(--ease), border-color 160ms var(--ease);
        }}
        .tab-btn:hover {{ background: #f5f1fb; color: var(--primary-strong); }}
        .tab-btn.active {{ border-color: #ddd6fe; background: #ede9fe; color: var(--primary-strong); box-shadow: none; }}
        .tab-count {{ background: rgba(124,58,237,.10); color: currentColor; }}
        .tab-btn.active .tab-count {{ background: rgba(124,58,237,.18); }}
        .tab-arrow {{ min-width: 44px; min-height: 44px; color: var(--primary); }}

        .word-group {{
            margin: 0 0 14px;
            padding: 0;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: var(--radius-md);
            background: var(--surface);
            box-shadow: var(--shadow-xs);
        }}
        .word-group:last-child {{ margin-bottom: 0; }}
        .word-header {{
            min-height: 64px;
            margin: 0;
            padding: 12px 16px;
            border-bottom: 1px solid var(--line);
            background: linear-gradient(90deg, #fbfaff, #fff);
            cursor: pointer;
        }}
        .word-info {{ gap: 10px; }}
        .word-name {{ color: var(--ink); font-size: 17px; font-weight: 720; letter-spacing: -.02em; }}
        .word-count {{ padding: 3px 9px; border-radius: 999px; background: #f1edf7; color: var(--ink-soft); font-size: 12px; }}
        .word-count.hot {{ background: #fff1f2; color: #be123c; }}
        .word-count.warm {{ background: #fff7ed; color: #c2410c; }}
        .word-index {{ color: var(--ink-faint); font-variant-numeric: tabular-nums; }}

        .news-item {{
            min-height: 74px;
            margin: 0;
            padding: 14px 16px;
            gap: 14px;
            border: 0;
            border-bottom: 1px solid #f0ecf4;
            border-radius: 0;
            background: white;
            box-shadow: none;
            transition: background 160ms var(--ease);
        }}
        .news-item:last-child {{ border-bottom: 0; }}
        .news-item:hover {{ border-color: #f0ecf4; background: #fbf9fe; box-shadow: none; transform: none; }}
        .news-number, .new-item-number {{
            display: grid;
            width: 34px;
            height: 34px;
            flex: 0 0 34px;
            place-items: center;
            border: 1px solid #e4dded;
            border-radius: 10px;
            background: #f8f5fb;
            color: var(--primary-strong);
            font-size: 12px;
            font-weight: 750;
            font-variant-numeric: tabular-nums;
        }}
        .news-content {{ min-width: 0; padding-right: 54px; }}
        .news-header, .rss-meta {{ gap: 8px; margin-bottom: 5px; }}
        .source-name, .rss-source, .rss-author, .keyword-tag {{ color: var(--primary); font-size: 12px; font-weight: 650; }}
        .rank-num {{ border-radius: 6px; background: #f3eff9; color: var(--ink-soft); }}
        .rank-num.top {{ background: #fce7f3; color: #be185d; }}
        .rank-num.high {{ background: #ede9fe; color: #6d28d9; }}
        .news-title, .rss-title, .new-item-title {{ margin: 0; color: var(--ink); font-size: 15px; font-weight: 590; line-height: 1.55; }}
        .news-link, .rss-link {{ color: inherit; text-decoration: none; }}
        .news-link:hover, .rss-link:hover {{ color: var(--primary-strong); text-decoration: underline; }}
        .news-meta, .rss-time, .rss-summary, .time-info {{ color: var(--ink-faint); }}
        .badge-new {{ border-radius: 999px; background: #fce7f3; color: #be185d; box-shadow: none; }}

        .rss-feeds-grid, .new-sources-grid, .standalone-groups-grid, .ai-blocks-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }}
        .feed-group, .new-source-group, .standalone-group {{
            margin: 0;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: var(--radius-md);
            background: var(--surface);
        }}
        .feed-header, .new-source-title, .standalone-header {{ margin: 0; padding: 14px 16px; border-bottom: 1px solid var(--line); background: #fbfaff; }}
        .feed-name, .new-source-title, .standalone-name {{ color: var(--ink); font-weight: 700; }}
        .rss-item, .new-item, .standalone-item {{
            margin: 0;
            padding: 14px 16px;
            border: 0;
            border-bottom: 1px solid #f0ecf4;
            border-left: 0;
            border-radius: 0;
            background: white;
            box-shadow: none;
        }}
        .rss-item:last-child, .new-item:last-child, .standalone-item:last-child {{ border-bottom: 0; }}
        .rss-item:hover, .new-item:hover, .standalone-item:hover {{ border-color: #f0ecf4; background: #fbf9fe; box-shadow: none; transform: none; }}

        .rss-section-header, .standalone-section-header, .ai-section-header {{ margin: 0 0 18px; padding: 0; border: 0; }}
        .rss-section-title, .standalone-section-title, .ai-section-title, .new-section-title {{ color: var(--ink); font-size: 20px; font-weight: 740; letter-spacing: -.025em; }}
        .rss-section-count, .standalone-section-count {{ color: var(--ink-faint); }}
        .ai-section-badge {{ border-radius: 999px; background: var(--primary); }}
        .ai-block {{
            margin: 0;
            padding: 18px;
            border: 1px solid rgba(124,58,237,.16);
            border-left: 0;
            border-radius: var(--radius-md);
            background: rgba(255,255,255,.76);
            box-shadow: var(--shadow-xs);
        }}
        .ai-block-title {{ color: var(--primary-strong); font-size: 14px; font-weight: 720; }}
        .ai-block-content {{ color: #3f3950; line-height: 1.72; }}
        .ai-warning {{ border-color: #fde68a; background: #fffbeb; color: #92400e; }}
        .ai-error {{ border-color: #fecaca; background: #fff1f2; color: #991b1b; }}

        .footer {{
            margin: 18px 0 0;
            padding: 24px;
            border: 1px solid var(--line);
            border-radius: var(--radius-lg);
            background: rgba(255,255,255,.65);
            color: var(--ink-faint);
            backdrop-filter: blur(12px);
        }}
        .footer-link {{ color: var(--primary-strong); }}
        .project-name {{ color: var(--ink); }}
        .fab-bar {{ right: max(18px, env(safe-area-inset-right)); bottom: max(18px, env(safe-area-inset-bottom)); }}
        .fab-btn {{ min-width: 48px; min-height: 48px; border-radius: 15px; background: var(--primary); box-shadow: 0 12px 30px rgba(91,33,182,.28); }}
        .fab-btn:hover {{ background: var(--primary-strong); transform: translateY(-2px); }}
        .reading-progress {{ height: 3px; background: linear-gradient(90deg, var(--primary), var(--accent)); }}

        body.dark-mode {{
            --canvas: #0e0c16;
            --canvas-deep: #171321;
            --surface: #181520;
            --surface-soft: #1e1a28;
            --surface-raised: rgba(24, 21, 32, .9);
            --ink: #f6f2fb;
            --ink-soft: #c0b8cc;
            --ink-faint: #8d849a;
            --line: #302a3c;
            --line-strong: #443a52;
            background: radial-gradient(circle at 8% 0%, rgba(124,58,237,.16), transparent 32rem), radial-gradient(circle at 92% 6%, rgba(236,72,153,.10), transparent 28rem), #0e0c16;
            color: var(--ink);
        }}
        body.dark-mode .content {{ background: transparent; }}
        body.dark-mode .search-bar, body.dark-mode .tab-bar-wrapper {{ border-color: var(--line); background: rgba(24,21,32,.88); }}
        body.dark-mode .search-input {{ background-color: #211c2b; color: var(--ink); }}
        body.dark-mode .error-section, body.dark-mode .hotlist-section, body.dark-mode .new-section, body.dark-mode .rss-section, body.dark-mode .standalone-section, body.dark-mode .ai-section {{ border-color: var(--line); background: var(--surface-raised); }}
        body.dark-mode .word-group, body.dark-mode .feed-group, body.dark-mode .new-source-group, body.dark-mode .standalone-group, body.dark-mode .ai-block {{ border-color: var(--line); background: var(--surface); }}
        body.dark-mode .word-header, body.dark-mode .feed-header, body.dark-mode .new-source-title, body.dark-mode .standalone-header {{ border-color: var(--line); background: #1d1926; }}
        body.dark-mode .news-item, body.dark-mode .rss-item, body.dark-mode .new-item, body.dark-mode .standalone-item {{ border-color: var(--line); background: var(--surface); }}
        body.dark-mode .news-item:hover, body.dark-mode .rss-item:hover, body.dark-mode .new-item:hover, body.dark-mode .standalone-item:hover {{ background: #201b2a; }}
        body.dark-mode .word-name, body.dark-mode .feed-name, body.dark-mode .new-source-title, body.dark-mode .standalone-name, body.dark-mode .news-title, body.dark-mode .rss-title, body.dark-mode .new-item-title, body.dark-mode .rss-section-title, body.dark-mode .standalone-section-title, body.dark-mode .ai-section-title, body.dark-mode .new-section-title {{ color: var(--ink); }}
        body.dark-mode .news-link, body.dark-mode .rss-link {{ color: inherit; }}
        body.dark-mode .ai-block-content {{ color: var(--ink-soft); }}
        body.dark-mode .footer {{ border-color: var(--line); background: rgba(24,21,32,.68); }}
        body.dark-mode .save-dropdown-menu {{ border-color: var(--line); background: rgba(24,21,32,.98); }}
        body.dark-mode .save-dropdown-item {{ color: var(--ink); }}
        body.dark-mode .save-dropdown-item:hover {{ background: #292232; }}

        @media (max-width: 1080px) {{
            .header-info {{ grid-template-columns: repeat(4, minmax(0, 1fr)); }}
            .rss-feeds-grid, .new-sources-grid, .standalone-groups-grid, .ai-blocks-grid {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 720px) {{
            body {{ padding: 0; font-size: 16px; }}
            .container, body.wide-mode .container {{ width: 100%; }}
            .header {{ min-height: auto; padding: 82px 16px 22px; border: 0; border-radius: 0 0 26px 26px; }}
            .header-watermark {{ top: 22px; left: 16px; }}
            .save-buttons {{ top: 16px; right: 12px; }}
            .guide-link span, .save-btn span {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }}
            .guide-link, .save-btn {{ width: 44px; padding: 0; }}
            .brand-lockup {{ align-items: flex-start; gap: 14px; margin-top: 12px; }}
            .brand-mark {{ width: 56px; height: 56px; flex-basis: 56px; border-radius: 17px; font-size: 16px; }}
            .brand-kicker {{ margin-bottom: 5px; font-size: 9px; }}
            .header-title {{ font-size: clamp(28px, 9vw, 38px); letter-spacing: -.045em; }}
            .header-subtitle {{ margin-top: 8px; font-size: 14px; }}
            .header-info {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 24px; }}
            .info-item {{ padding: 11px 12px; }}
            .content {{ padding: 16px 12px 0; }}
            .search-bar {{ top: 8px; margin-bottom: 12px; padding: 7px; border-radius: 15px; }}
            .search-input {{ min-height: 48px; }}
            .error-section, .hotlist-section, .new-section, .rss-section, .standalone-section, .ai-section {{ margin-bottom: 12px; padding: 14px; border-radius: 18px; }}
            .tab-bar-wrapper {{ top: 77px; margin: -3px -3px 14px; }}
            .word-group {{ border-radius: 14px; }}
            .word-header {{ min-height: 58px; padding: 10px 12px; }}
            .news-item {{ padding: 13px 12px; gap: 10px; align-items: flex-start; }}
            .news-number, .new-item-number {{ width: 30px; height: 30px; flex-basis: 30px; border-radius: 9px; }}
            .news-content {{ padding-right: 38px; }}
            .rss-feeds-grid, .new-sources-grid, .standalone-groups-grid, .ai-blocks-grid {{ grid-template-columns: minmax(0, 1fr); }}
            .footer {{ margin: 12px 12px 0; border-radius: 18px; }}
        }}
        @media (max-width: 420px) {{
            .toggle-wide-btn {{ display: none; }}
            .header-title {{ font-size: 30px; }}
            .brand-mark {{ width: 50px; height: 50px; flex-basis: 50px; }}
            .save-buttons {{ gap: 6px; }}
            .guide-link, .save-btn, .toggle-dark-btn {{ min-width: 44px; width: 44px; min-height: 44px; }}
            .save-dropdown-trigger {{ min-width: 44px; width: 44px; min-height: 44px; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            html {{ scroll-behavior: auto; }}
            *, *::before, *::after {{ animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }}
        }}
    """
