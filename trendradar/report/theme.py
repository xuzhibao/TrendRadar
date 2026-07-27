"""Editorial visual system shared by TrendRadar HTML reports."""


def get_report_theme_css(accent: str = "#1f6fb2") -> str:
    """Return a warm-paper, long-form editorial theme."""
    return f"""
        :root {{
            color-scheme: light;
            --paper: #f7f3eb;
            --paper-deep: #eee8dc;
            --paper-soft: #fbf9f4;
            --ink: #302b25;
            --ink-soft: #6e675e;
            --ink-faint: #968e82;
            --rule: #d8cbb8;
            --rule-soft: #e8dfd2;
            --link: {accent};
            --link-hover: #174f7f;
            --danger: #a63c32;
            --success: #2d6f59;
            --radius: 3px;
            --measure: 920px;
            --ease: cubic-bezier(.2, .8, .2, 1);
        }}

        * {{ box-sizing: border-box; }}
        html {{
            scroll-behavior: smooth;
            background: var(--paper-deep);
        }}
        body {{
            min-height: 100dvh;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
            background: var(--paper);
            color: var(--ink);
            font-family: "Noto Serif SC", "Songti SC", SimSun, Georgia, serif;
            font-size: 16px;
            line-height: 1.82;
            text-rendering: optimizeLegibility;
            -webkit-font-smoothing: antialiased;
        }}
        body.no-overflow {{ overflow: hidden; }}
        a {{ color: var(--link); text-underline-offset: 3px; }}
        button, input {{
            font: inherit;
        }}
        button, a {{
            touch-action: manipulation;
        }}
        button:focus-visible,
        a:focus-visible,
        input:focus-visible {{
            outline: 2px solid var(--link);
            outline-offset: 3px;
        }}
        ::selection {{
            background: #d8e8f4;
            color: var(--ink);
        }}

        .reading-progress {{
            position: fixed;
            z-index: 1000;
            top: 0;
            left: 0;
            height: 2px;
            width: 0;
            background: var(--link);
        }}

        .container {{
            width: min(100%, 1080px);
            max-width: 1080px;
            min-height: 100dvh;
            margin: 0 auto;
            padding: 72px 80px 56px;
            background: var(--paper);
            box-shadow: 0 0 50px rgba(69, 57, 41, .08);
        }}
        body.wide-mode .container {{
            width: min(100%, 1240px);
            max-width: 1240px;
        }}

        .header {{
            position: relative;
            min-height: 0;
            padding: 0 0 34px;
            overflow: visible;
            border-radius: 0;
            background: none;
            color: var(--ink);
            box-shadow: none;
        }}
        .header::after {{
            content: "";
            display: block;
            height: 1px;
            margin-top: 30px;
            background: var(--rule);
        }}
        .header-watermark,
        .brand-mark,
        .brand-kicker {{
            display: none;
        }}
        .brand-lockup {{
            display: block;
            max-width: 680px;
            margin: 0 0 22px;
        }}
        .brand-copy {{
            min-width: 0;
        }}
        .header-title {{
            margin: 0;
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: clamp(28px, 3.4vw, 38px);
            font-weight: 700;
            line-height: 1.24;
            letter-spacing: .02em;
        }}
        .header-subtitle {{
            margin: 10px 0 0;
            color: var(--ink-soft);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 14px;
            line-height: 1.7;
            letter-spacing: .01em;
        }}

        .save-buttons {{
            position: absolute;
            z-index: 20;
            top: -10px;
            right: 0;
            display: flex;
            gap: 8px;
            align-items: center;
        }}
        .guide-link,
        .toggle-wide-btn,
        .toggle-dark-btn,
        .save-btn,
        .save-dropdown-trigger {{
            display: inline-flex;
            min-width: 44px;
            min-height: 44px;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 0 13px;
            border: 1px solid var(--rule);
            border-radius: var(--radius);
            background: transparent;
            color: var(--ink-soft);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 13px;
            line-height: 1;
            text-decoration: none;
            cursor: pointer;
            transition: border-color 180ms var(--ease), color 180ms var(--ease), background 180ms var(--ease);
        }}
        .guide-link:hover,
        .toggle-wide-btn:hover,
        .toggle-dark-btn:hover,
        .save-btn:hover,
        .save-dropdown-trigger:hover {{
            border-color: var(--ink-soft);
            background: var(--paper-soft);
            color: var(--ink);
        }}
        .guide-link svg,
        .toggle-wide-btn svg,
        .toggle-dark-btn svg,
        .save-btn svg {{
            width: 17px;
            height: 17px;
            flex: 0 0 auto;
        }}
        .save-btn-group {{
            position: relative;
            display: flex;
        }}
        .save-btn {{
            border-radius: var(--radius) 0 0 var(--radius);
        }}
        .save-dropdown-trigger {{
            width: 42px;
            min-width: 42px;
            padding: 0;
            border-left: 0;
            border-radius: 0 var(--radius) var(--radius) 0;
        }}
        .save-dropdown-trigger svg {{
            width: 15px;
            height: 15px;
        }}
        .save-dropdown-menu {{
            position: absolute;
            z-index: 100;
            top: calc(100% + 8px);
            right: 0;
            display: none;
            width: 190px;
            padding: 6px;
            border: 1px solid var(--rule);
            border-radius: var(--radius);
            background: var(--paper-soft);
            box-shadow: 0 12px 28px rgba(61, 50, 36, .12);
        }}
        .save-dropdown-menu.show {{
            display: block;
        }}
        .save-dropdown-item {{
            display: flex;
            width: 100%;
            min-height: 42px;
            align-items: center;
            gap: 10px;
            padding: 8px 11px;
            border: 0;
            border-radius: 2px;
            background: transparent;
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 13px;
            text-align: left;
            cursor: pointer;
        }}
        .save-dropdown-item:hover {{
            background: var(--paper-deep);
        }}
        .dropdown-icon {{
            width: 17px;
            height: 17px;
            color: var(--ink-soft);
        }}

        .header-info {{
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            margin: 0;
            border-top: 1px solid var(--rule);
            border-left: 3px solid var(--rule);
            background: rgba(232, 223, 210, .38);
        }}
        .info-item {{
            display: block;
            min-width: 0;
            padding: 12px 14px;
            border-right: 1px solid rgba(216, 203, 184, .65);
            border-bottom: 1px solid rgba(216, 203, 184, .65);
            background: transparent;
        }}
        .info-label {{
            display: block;
            margin-bottom: 2px;
            color: var(--ink-faint);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 11px;
            line-height: 1.4;
            letter-spacing: .08em;
        }}
        .info-value {{
            display: block;
            overflow-wrap: anywhere;
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 13px;
            font-weight: 600;
            line-height: 1.55;
            font-variant-numeric: tabular-nums;
        }}

        .content {{
            width: 100%;
            padding: 0;
            background: transparent;
        }}
        .search-bar {{
            position: sticky;
            z-index: 30;
            top: 0;
            margin: 0 0 34px;
            padding: 12px 0;
            border-bottom: 1px solid var(--rule);
            background: color-mix(in srgb, var(--paper) 94%, transparent);
            backdrop-filter: blur(8px);
        }}
        .search-label {{
            position: absolute;
            width: 1px;
            height: 1px;
            overflow: hidden;
            clip: rect(0 0 0 0);
        }}
        .search-input {{
            width: 100%;
            min-height: 44px;
            padding: 8px 12px 8px 38px;
            border: 1px solid var(--rule-soft);
            border-radius: var(--radius);
            outline: none;
            background:
                linear-gradient(var(--ink-soft), var(--ink-soft)) 15px 15px / 10px 1px no-repeat,
                linear-gradient(45deg, transparent 42%, var(--ink-soft) 43% 57%, transparent 58%) 24px 25px / 7px 7px no-repeat,
                var(--paper-soft);
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 14px;
        }}
        .search-input::placeholder {{
            color: var(--ink-faint);
        }}

        .error-section,
        .new-section,
        .rss-section,
        .standalone-section,
        .ai-section {{
            margin: 0 0 44px;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            box-shadow: none;
        }}
        .error-title,
        .new-section-title,
        .rss-section-title,
        .standalone-section-title,
        .ai-section-title {{
            margin: 0;
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 22px;
            font-weight: 700;
            line-height: 1.45;
            letter-spacing: .01em;
        }}
        .error-title::after,
        .new-section-title::after,
        .rss-section-header::after,
        .standalone-section-header::after,
        .ai-section-header::after {{
            content: "";
            display: block;
            height: 1px;
            margin-top: 12px;
            background: var(--rule);
        }}
        .error-list {{
            margin: 14px 0 0;
            padding-left: 24px;
        }}
        .error-item {{
            color: var(--danger);
        }}

        .tab-bar-wrapper {{
            position: sticky;
            z-index: 25;
            top: 69px;
            margin: 0 0 30px;
            padding: 8px 0;
            border-bottom: 1px solid var(--rule);
            background: color-mix(in srgb, var(--paper) 95%, transparent);
            backdrop-filter: blur(8px);
        }}
        .tab-bar {{
            display: flex;
            gap: 6px 18px;
            overflow-x: auto;
            scrollbar-width: thin;
        }}
        .tab-btn {{
            position: relative;
            display: inline-flex;
            min-height: 44px;
            flex: 0 0 auto;
            align-items: center;
            gap: 6px;
            padding: 0;
            border: 0;
            border-bottom: 2px solid transparent;
            background: transparent;
            color: var(--ink-soft);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 13px;
            cursor: pointer;
        }}
        .tab-btn:hover,
        .tab-btn.active {{
            border-bottom-color: var(--link);
            color: var(--ink);
        }}
        .tab-count {{
            color: var(--ink-faint);
            font-size: 11px;
            font-variant-numeric: tabular-nums;
        }}

        .hotlist-section {{
            display: block;
        }}
        .word-group {{
            margin: 0 0 44px;
            overflow: visible;
            border: 0;
            border-radius: 0;
            background: transparent;
            box-shadow: none;
        }}
        .word-group.hidden {{
            display: none;
        }}
        .word-header {{
            display: flex;
            min-height: 0;
            align-items: flex-end;
            justify-content: space-between;
            gap: 20px;
            padding: 0 0 10px;
            border-bottom: 1px solid var(--rule);
            background: none;
            cursor: pointer;
        }}
        .word-info {{
            display: flex;
            min-width: 0;
            align-items: baseline;
            gap: 12px;
        }}
        .word-name {{
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 20px;
            font-weight: 700;
            line-height: 1.4;
        }}
        .word-count,
        .word-index,
        .rss-section-count,
        .standalone-section-count,
        .feed-count,
        .standalone-count {{
            color: var(--ink-faint);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 12px;
            font-weight: 400;
            font-variant-numeric: tabular-nums;
        }}
        .word-count.hot,
        .word-count.warm {{
            color: var(--ink-soft);
        }}
        .word-index {{
            flex: 0 0 auto;
        }}
        .collapse-icon {{
            display: inline-block;
            margin-right: 7px;
            color: var(--ink-faint);
            font-size: 9px;
            transition: transform 180ms var(--ease);
        }}
        .word-group.collapsed .collapse-icon {{
            transform: rotate(-90deg);
        }}
        .word-group.collapsed .news-item {{
            display: none;
        }}

        .news-item,
        .new-item,
        .rss-item,
        .standalone-item {{
            display: flex;
            gap: 14px;
            align-items: flex-start;
            margin: 0;
            padding: 13px 2px;
            border: 0;
            border-bottom: 1px solid var(--rule-soft);
            border-radius: 0;
            background: transparent;
            transition: background 160ms var(--ease);
        }}
        .news-item:hover,
        .new-item:hover,
        .rss-item:hover,
        .standalone-item:hover {{
            background: rgba(255, 255, 255, .34);
        }}
        .news-number,
        .new-item-number {{
            display: flex;
            width: 24px;
            min-width: 24px;
            height: 24px;
            align-items: center;
            justify-content: center;
            margin-top: 2px;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: var(--ink-faint);
            font-family: Georgia, serif;
            font-size: 13px;
            font-variant-numeric: tabular-nums;
        }}
        .news-content,
        .new-item-content {{
            min-width: 0;
            flex: 1;
            padding: 0;
        }}
        .news-item.new .news-content {{
            padding-right: 0;
        }}
        .news-item.new::after {{
            top: 13px;
            right: 2px;
            padding: 0;
            border-radius: 0;
            background: var(--paper);
            color: var(--danger);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 9px;
            letter-spacing: .08em;
        }}
        .news-header,
        .rss-meta {{
            display: flex;
            min-height: 0;
            flex-wrap: wrap;
            align-items: center;
            gap: 4px 10px;
            margin: 0 0 3px;
            color: var(--ink-faint);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 11px;
            line-height: 1.5;
        }}
        .source-name,
        .keyword-tag {{
            color: var(--ink-soft);
            font-weight: 600;
        }}
        .rank-num {{
            min-width: 0;
            padding: 0;
            border: 0;
            border-radius: 0;
            background: transparent;
            color: var(--ink-faint);
        }}
        .rank-num::before {{
            content: "排名 ";
        }}
        .rank-num.top,
        .rank-num.high {{
            background: transparent;
            color: var(--ink-soft);
        }}
        .trend-up {{
            color: var(--danger);
        }}
        .trend-down {{
            color: var(--success);
        }}
        .time-info,
        .count-info,
        .rss-time,
        .rss-author {{
            color: var(--ink-faint);
            font-variant-numeric: tabular-nums;
        }}
        .news-title,
        .new-item-title,
        .rss-title {{
            color: var(--ink);
            font-size: 16px;
            font-weight: 400;
            line-height: 1.72;
        }}
        .news-link,
        .new-item-title a,
        .rss-link,
        .standalone-item a {{
            color: var(--link);
            font-family: inherit;
            font-weight: 500;
            text-decoration: none;
        }}
        .news-link:hover,
        .new-item-title a:hover,
        .rss-link:hover,
        .standalone-item a:hover {{
            color: var(--link-hover);
            text-decoration: underline;
        }}

        .new-section-title {{
            margin-bottom: 18px;
        }}
        .new-sources-grid,
        .rss-feeds-grid,
        .standalone-groups-grid,
        .ai-blocks-grid {{
            display: block;
        }}
        .new-source-group,
        .feed-group,
        .standalone-group {{
            margin: 0 0 34px;
            padding: 0;
            overflow: visible;
            border: 0;
            border-radius: 0;
            background: transparent;
            box-shadow: none;
        }}
        .new-source-title,
        .feed-header,
        .standalone-header {{
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 16px;
            padding: 0 0 9px;
            border-bottom: 1px solid var(--rule);
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 17px;
            font-weight: 700;
            line-height: 1.5;
        }}
        .feed-name,
        .standalone-name {{
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 17px;
            font-weight: 700;
        }}
        .new-item-rank {{
            color: var(--ink-faint);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 11px;
        }}

        .rss-section-header,
        .standalone-section-header,
        .ai-section-header {{
            display: flex;
            flex-wrap: wrap;
            align-items: baseline;
            justify-content: space-between;
            gap: 8px 18px;
            margin-bottom: 20px;
        }}
        .rss-section-header::after,
        .standalone-section-header::after,
        .ai-section-header::after {{
            width: 100%;
        }}
        .rss-item {{
            display: block;
        }}
        .rss-title {{
            margin: 0;
        }}
        .rss-summary {{
            max-width: 72ch;
            margin: 6px 0 0;
            color: var(--ink-soft);
            font-size: 14px;
            line-height: 1.75;
        }}
        .standalone-tab-bar {{
            margin-bottom: 26px;
        }}

        .ai-section {{
            padding: 24px 28px 12px;
            border-left: 3px solid var(--rule);
            background: rgba(232, 223, 210, .28);
        }}
        .ai-section-title {{
            font-size: 22px;
        }}
        .ai-section-badge {{
            padding: 1px 8px;
            border: 1px solid var(--rule);
            border-radius: 999px;
            background: transparent;
            color: var(--ink-soft);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 10px;
            font-weight: 600;
            letter-spacing: .1em;
        }}
        .ai-block {{
            margin: 0;
            padding: 17px 0;
            border: 0;
            border-bottom: 1px solid var(--rule-soft);
            border-radius: 0;
            background: transparent;
            box-shadow: none;
        }}
        .ai-block:last-child {{
            border-bottom: 0;
        }}
        .ai-block-title {{
            margin-bottom: 6px;
            color: var(--ink);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 16px;
            font-weight: 700;
        }}
        .ai-block-content {{
            color: var(--ink-soft);
            font-size: 15px;
            line-height: 1.82;
        }}
        .ai-warning,
        .ai-error,
        .ai-info {{
            padding: 16px 0;
            border: 0;
            background: transparent;
            color: var(--ink-soft);
        }}

        .footer {{
            margin: 58px 0 0;
            padding: 20px 0 0;
            border-top: 1px solid var(--rule);
            border-radius: 0;
            background: transparent;
            color: var(--ink-faint);
            box-shadow: none;
            text-align: left;
        }}
        .footer-content {{
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 12px;
        }}
        .project-name {{
            color: var(--ink-soft);
            font-weight: 600;
        }}
        .footer-link {{
            color: var(--link);
        }}

        .fab-bar {{
            position: fixed;
            z-index: 90;
            right: max(16px, calc((100vw - 1080px) / 2 + 18px));
            bottom: 22px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .fab-btn {{
            position: relative;
            display: flex;
            width: 44px;
            height: 44px;
            align-items: center;
            justify-content: center;
            border: 1px solid var(--rule);
            border-radius: 50%;
            background: var(--paper-soft);
            color: var(--ink-soft);
            box-shadow: 0 6px 18px rgba(61, 50, 36, .12);
            cursor: pointer;
        }}
        .fab-btn:hover {{
            border-color: var(--ink-soft);
            color: var(--ink);
        }}
        .fab-btn svg {{
            width: 18px;
            height: 18px;
        }}
        .fab-tooltip {{
            position: absolute;
            top: 50%;
            right: calc(100% + 10px);
            width: max-content;
            max-width: 220px;
            padding: 6px 9px;
            border: 1px solid var(--rule);
            border-radius: var(--radius);
            background: var(--paper-soft);
            color: var(--ink-soft);
            font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
            font-size: 11px;
            opacity: 0;
            pointer-events: none;
            transform: translateY(-50%);
            transition: opacity 160ms var(--ease);
        }}
        .fab-btn:hover .fab-tooltip,
        .fab-btn:focus-visible .fab-tooltip {{
            opacity: 1;
        }}

        body.dark-mode {{
            --paper: #201e1a;
            --paper-deep: #171612;
            --paper-soft: #28251f;
            --ink: #eee8dc;
            --ink-soft: #c5bbae;
            --ink-faint: #92887d;
            --rule: #4b443a;
            --rule-soft: #363129;
            --link: #7db7e7;
            --link-hover: #acd3f1;
            --danger: #e0877e;
            --success: #85bfa9;
            background: var(--paper);
            color: var(--ink);
        }}
        body.dark-mode .container,
        body.dark-mode .header,
        body.dark-mode .content,
        body.dark-mode .word-group,
        body.dark-mode .news-item,
        body.dark-mode .new-item,
        body.dark-mode .rss-item,
        body.dark-mode .feed-group,
        body.dark-mode .standalone-group,
        body.dark-mode .ai-block,
        body.dark-mode .footer {{
            background: transparent;
            color: var(--ink);
        }}
        body.dark-mode .header-info,
        body.dark-mode .ai-section {{
            background: rgba(75, 68, 58, .22);
        }}
        body.dark-mode .search-bar,
        body.dark-mode .tab-bar-wrapper {{
            background: color-mix(in srgb, var(--paper) 94%, transparent);
        }}
        body.dark-mode .search-input,
        body.dark-mode .guide-link,
        body.dark-mode .toggle-wide-btn,
        body.dark-mode .toggle-dark-btn,
        body.dark-mode .save-btn,
        body.dark-mode .save-dropdown-trigger,
        body.dark-mode .save-dropdown-menu,
        body.dark-mode .fab-btn,
        body.dark-mode .fab-tooltip {{
            background-color: var(--paper-soft);
            color: var(--ink-soft);
        }}
        body.dark-mode .news-title,
        body.dark-mode .rss-title,
        body.dark-mode .new-item-title,
        body.dark-mode .header-title,
        body.dark-mode .word-name,
        body.dark-mode .feed-name,
        body.dark-mode .new-source-title,
        body.dark-mode .standalone-name,
        body.dark-mode .ai-section-title,
        body.dark-mode .ai-block-title {{
            color: var(--ink);
        }}

        @media (max-width: 900px) {{
            .container {{
                padding: 54px 42px 44px;
                box-shadow: none;
            }}
            .save-buttons {{
                position: static;
                justify-content: flex-end;
                margin-bottom: 28px;
            }}
            .brand-lockup {{
                max-width: none;
            }}
            .header-info {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
        }}

        @media (max-width: 600px) {{
            body {{
                font-size: 16px;
                line-height: 1.72;
            }}
            .container {{
                width: 100%;
                padding: max(20px, env(safe-area-inset-top)) 20px 38px;
            }}
            .header {{
                padding-bottom: 24px;
            }}
            .save-buttons {{
                justify-content: flex-start;
                gap: 8px;
                margin-bottom: 28px;
            }}
            .guide-link span,
            .save-btn span {{
                position: absolute;
                width: 1px;
                height: 1px;
                overflow: hidden;
                clip: rect(0 0 0 0);
            }}
            .guide-link,
            .save-btn,
            .toggle-dark-btn,
            .save-dropdown-trigger {{
                width: 44px;
                min-width: 44px;
                min-height: 44px;
                padding: 0;
            }}
            .toggle-wide-btn {{
                display: none;
            }}
            .header-title {{
                font-size: 28px;
            }}
            .header-subtitle {{
                font-size: 13px;
            }}
            .header-info {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .info-item {{
                padding: 10px 11px;
            }}
            .search-bar {{
                margin-bottom: 26px;
            }}
            .tab-bar-wrapper {{
                top: 69px;
                margin-bottom: 24px;
            }}
            .word-group,
            .error-section,
            .new-section,
            .rss-section,
            .standalone-section,
            .ai-section {{
                margin-bottom: 38px;
            }}
            .word-name,
            .new-section-title,
            .rss-section-title,
            .standalone-section-title,
            .ai-section-title {{
                font-size: 19px;
            }}
            .news-item,
            .new-item,
            .standalone-item {{
                gap: 8px;
                padding: 12px 0;
            }}
            .news-number,
            .new-item-number {{
                width: 20px;
                min-width: 20px;
            }}
            .news-title,
            .new-item-title,
            .rss-title {{
                font-size: 15px;
            }}
            .ai-section {{
                padding: 20px 18px 8px;
            }}
            .fab-bar {{
                right: 12px;
                bottom: max(14px, env(safe-area-inset-bottom));
            }}
            .footer {{
                margin-top: 44px;
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            html {{
                scroll-behavior: auto;
            }}
            *,
            *::before,
            *::after {{
                animation-duration: .01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: .01ms !important;
                scroll-behavior: auto !important;
            }}
        }}
    """
