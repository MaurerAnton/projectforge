#!/usr/bin/env python3
"""Generate all 50 HTML docs for ProjectForge source files #1351-#1400."""

import os
import html

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>#{num}</title>
<style>body{{font-family:system-ui,sans-serif;max-width:960px;margin:2em auto;padding:0 1em;background:#fafafa;color:#222;line-height:1.6}}h1{{border-bottom:2px solid #333;padding-bottom:.3em}}h2{{margin-top:2.5em;border-bottom:1px solid #ddd;padding-bottom:.2em;color:#333}}h3{{margin-top:2em;color:#444}}a{{color:#0366d6}}.c{{border-left:3px solid #ddd;padding:.5em 1em;margin:1em 0;background:#fff}}.nav{{font-size:.9em;color:#888;margin-bottom:1em}}.meta{{font-size:.9em;margin:1em 0;color:#555}}code{{background:#f0f0f0;padding:0 .2em;font-size:.93em}}pre{{background:#f5f5f5;padding:.8em 1em;border:1px solid #ddd;border-radius:4px;overflow-x:auto;font-size:.88em;line-height:1.4}}table{{border-collapse:collapse;width:100%;margin:1em 0}}th,td{{border:1px solid #ddd;padding:.5em .8em;text-align:left;font-size:.9em}}th{{background:#f5f5f5;font-weight:600}}.hist{{font-size:.85em;color:#555}}</style></head>
<body><div class="nav"><a href="https://maureranton.github.io/projectforge/">← Index</a> · <a href="file-index.html">← File index</a> · <a href="{prev}.html">← Prev</a> · <a href="{next}.html">Next →</a></div>
<h1>#{num}: <code>{filename}</code></h1>
<div class="meta">{role}, {source_path}</div>
<div class="c">{purpose_summary}</div>
<h2>Git History</h2><div class="hist"><pre>{git_log}</pre></div>
</body></html>"""

OUT = "/home/bym/projectforge-folder/projectforge/docs"

FILES = [
    (1351, "PasswordResetTokenStore.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/persistence/user/service/PasswordResetTokenStore.kt",
     "Internal singleton service for storing and managing expiring password reset tokens. Tokens are created per user ID, valid for 10 minutes, and automatically cleaned up. Uses a synchronized mutable map with alphanumeric secure-random tokens (30 chars).",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n4c04cfd65 MAJOR-CHANGE! Migration of integer id's to Long id's (including fk's etc.)\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n2f40675d8 WIP: CreateI18nKeys refactored.\n49c32afb0 Source file headers fixed.\nff4fe4442 WIP: Password reset\n5f1a8c9d3 WIP: Password reset with 2FA"),

    (1352, "CollectionDebugUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/persistence/utils/CollectionDebugUtils.kt",
     "Debug utility for comparing two collections and producing diff output. Uses DiffMatchPatch for string-level diffs, supports IdObject-based comparison, and can show added/removed/kept entries with ANSI-colored console output.",
     "868d6abb7 2025 -> 2026\n48a93dedb Colored console log. UserGroupCache export for debugging and comparing work now. CollectionUtil improved. KotlinStringExtension.shortenMiddle() added."),

    (1353, "CollectionUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/persistence/utils/CollectionUtils.kt",
     "Utility object for collection operations: comparing collections to find added/removed/kept entries (using IdObject equality), joining collections to CSV strings, and sorting entries by id or Comparable. Used extensively for history tracking of collection changes in DAOs.",
     "868d6abb7 2025 -> 2026\n48a93dedb Colored console log. UserGroupCache export for debugging and comparing work now. CollectionUtil improved. KotlinStringExtension.shortenMiddle() added.\n63081666f Source file headers: 2024-> 2025.\n61f05ce90 Migration stuff in progress...\n5989b32fd BaseDao: mechanism of onChangeLister refactored.\n2fd83d9af Migration stuff in progress... (all tests of all packages: OK).\nad91ccfa4 Migration stuff in progress...\n435a8b063 Migration stuff in progress...\nd6cc82832 Migration stuff in progress...\n93cba94c1 Migration stuff in progress...\n891fae3d8 Migration stuff in progress... (all tests of all packages: OK).\n9e30522ba Migration stuff in progress... (all tests of all packages: OK)."),

    (1354, "MyImportedElement.kt", "Utils/Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/persistence/utils/MyImportedElement.kt",
     "Custom ImportedElement subclass for Merlin Excel import framework. Extends ImportedElement<T> and overrides valueAsString() to format DisplayNameCapable values as their display name. Tracks diff properties for change detection during import.",
     "868d6abb7 2025 -> 2026\n312d5e61c Clean-up\n63081666f Source file headers: 2024-> 2025.\ne33c8b9c2 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\nb44cbb249 Merge stuff.\n3cc3090c1 WIP: Merlin importer...\n201a58195 ExcelImporter uses new ActionLog of Merlin.\nbcadd5f90 MyImportedElement supports now ShortDisplayNameCapable.\n793986fde WIP: ImportedElement (Merlin).\nbd25a85fb WIP: Setup wizard (Swing and Lanterna)\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1355, "SQLHelper.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/persistence/utils/SQLHelper.kt",
     "SQL helper utility providing year range generation from min/max dates (via Tuple or direct values), and SQL script splitting — parses SQL scripts into individual statements while handling string literals, single-line comments (--), and semicolon delimiters.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n98b618a26 WIP: Setup of ProjectForge...\nc1ae440e6 WIP: Setup of ProjectForge...\n2863b30b9 Migration stuff in progress...\nb6b5ca58b Migration stuff in progress...\nc25b14e78 Migration stuff in progress...\n67ce75fe9 Migration stuff in progress...\ne33c8b9c2 Migration stuff in progress...\n06828f490 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nb2c5db3c7 SQLHelper.queryToString shows now query string including all parameters.\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\nae182f8a1 Github issue #135, performance tuning with JProfiler (addresses are now much faster)\n8826ddf5d no message\n632916ad6 SQLHelper.kt: Add getYears method that takes Objects\na6a7aece4 Optimize Imports\n944c94a2f Replace DatePanel from Wicket pages with LocalDatePanels"),

    (1356, "DateFormats.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/DateFormats.kt",
     "Central date format service providing format strings and DateTimeFormatters for the logged-in user. Supports multiple precisions (DATE, DATE_TIME_MINUTES, ISO, etc.), time notations (12h/24h), Excel formats, and parse formats. Detects separator chars and month-first formats from pattern strings.",
     "868d6abb7 2025 -> 2026\nee32b3e3a Code deprecations.\n63081666f Source file headers: 2024-> 2025.\n67805f2fc ThreadLocalUserContext.user -> ThreadLocalUserContext.loggedInUser (renamed for avoiding mis-understandings in code).\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\n24236f214 DateFormats: NPE fix for tests.\n556b74ecd DateFormats -> Kotlin: supports now user different from ThreadLocalUser (for e-mails). Date formats in vacation mails in recipient's format."),

    (1357, "DateParser.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/DateParser.kt",
     "Parses date/time strings into Temporal objects (ZonedDateTime, LocalDateTime, LocalDate). Supports epoch seconds/millis, ISO 8601 formats with/without timezone offsets, compact date-time formats (yyyyMMddTHHmmss), and local dates. Uses regex matching with DateTimeFormatter instances.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n1964a7e73 PFDateTimeUtils/DateParser: parsing of epoch seconds/millis improved.\nc193e8288 Ical4j: migration stuff... (all tests OK)"),

    (1358, "DatePrecision.kt", "Enum",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/DatePrecision.kt",
     "Enum defining date/time precision levels: MILLISECOND, SECOND, MINUTE, MINUTE_5 (rounds down to nearest 5-min mark), MINUTE_15, HOUR_OF_DAY, and DAY. Each variant has an ensurePrecision() method that truncates/rounds a ZonedDateTime to the corresponding precision.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\n040690542 Fileheader of DatePrecision fixed.\n126906964 PFDateTime supports now DatePrecision and more fields (hours, minutes, seconds etc.)."),

    (1359, "IPFDate.kt", "Interface",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/IPFDate.kt",
     "Core date interface for ProjectForge date types. Defines contract for year, month, day, week, formatting, comparison (isBefore/isAfter/isSameDay), arithmetic (plusDays, minusMonths, etc.), and holiday/weekend checks. Implemented by both PFDateTime and PFDay.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\n7b417a67f WIP: DataTransfer: notification\n4827784b5 WIP: DataTransfer mail notification. IPFDate.isHoliday and isHolidayOrWeekend implemented.\n9f20b7577 WIP: time sheet mass update\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n66c1835a3 IPFDate.withDayOfWeek(DayOfWeek) added.\nbf7b36d61 PFDay and PFDateTime supports now formatting of dates in user's dateformat, locale and timezone.\n194ae2e64 Holidays -> Kotlin, PFDayUtilsTest.getNextWorkingDay implemented, ...\n7c79f1922 Copyright of source header -> 2020.\na1c287b49 Week of year is now globally the same (independant from user's locale, dependent on configured default locale in projectforge.properties.\n4b53b6562 PFDate -> PFDay, IPFDate introduced.."),

    (1360, "LocalDatePeriod.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/LocalDatePeriod.kt",
     "Simple data class holding a begin and end LocalDate, with companion factory methods for creating whole-year periods and year-spanning periods. Used for date range calculations throughout the framework.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\nb209e00ba PFDay.from -> from, fromOrNow, fromOrNull, PFDateTime.from -> from, fromOrNow, fromOrNull\n7fdd07b74 Vacations: Leave days over years (new year) are now supported.\ncccd16ed8 LocalDatePeriod as helper class added and minor things.\n7c79f1922 Copyright of source header -> 2020.\ndd5ca38ac CopyRight of all java file-header updated or created.\n2d86a8cd6 PROJECTFORGE-2306 Refactorings for keeping access check at update time\n9ebb88522 Initial commit"),

    (1361, "PFDateCompatibilityUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/PFDateCompatibilityUtils.kt",
     "Compatibility bridge between legacy Joda-Time DateMidnight and java.time. Converts Joda DateMidnight to LocalDate, maps day-of-week and month representations between old (Sunday=0) and new (Monday=1) conventions, and translates java.util.Calendar fields to ChronoUnit.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\nd732a9053 PFDateTimeUtils.parse supports now parameter parseWithZoneId\n9fcdf1b06 WTF: now, moment needs 0-sunday, 1-monday as first day of week.\n93ecd87d0 CalendarPanel.jsx supports now new firstDayOfWeek implementation.\n6874f66b4 FirstDayOfWeek...\n7c79f1922 Copyright of source header -> 2020.\n4b53b6562 PFDate -> PFDay, IPFDate introduced..\n8c31eba2a Heavy WIP: migration of Calendar, DateHolder, DayHolder etc."),

    (1362, "PFDateTime.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/PFDateTime.kt",
     "Immutable date-time holder wrapping ZonedDateTime. Core date/time class providing year, month, day, hour, minute, second, nano accessors; arithmetic (plus/minus days, weeks, months, years, hours); formatting (user locale, ISO, JS, HTTP-date, filename-safe); precision rounding; and conversion to java.util.Date, java.sql.Date/Timestamp. Companion object provides extensive factory methods (from/orNull/orNow) for Long, Instant, ZonedDateTime, LocalDateTime, LocalDate, Date, java.sql.Date, and Temporal.",
     "868d6abb7 2025 -> 2026\nb131193e7 Member variables refactored by using by lazy\n63081666f Source file headers: 2024-> 2025.\ndc2132fb5 Revert source change in previous commit\n5f9bbfbd3 Fix typos in projectforge-business directory\n6c1daac93 WIP: Carddav\n40e721b9c VCardUtils\nc193e8288 Ical4j: migration stuff... (all tests OK)\n61966790f Ical4j: migration stuff...\n9bffc8daf Migration stuff in progress...\n7bc8f49c9 Migration stuff in progress... (all tests of all packages: OK).\n3121b7ad6 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin"),

    (1363, "PFDateTimeUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/PFDateTimeUtils.kt",
     "Utility object providing date/time operations: begin/end of year, month, week, day calculations; UTC-based date conversion; date parsing (ISO 8601, epoch, various custom formats with timezone support); formatting; and date range checking (isBetween). Defines constant ZoneId/TimeZone references for UTC and Europe/Berlin.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nda93f5df8 WIP: orderbook storage.\n1964a7e73 PFDateTimeUtils/DateParser: parsing of epoch seconds/millis improved.\nc193e8288 Ical4j: migration stuff... (all tests OK)\n6b6a77efc Migration stuff in progress...\nb44fd93c6 Migration stuff in progress...\n6a9ba0372 Minor improvments in PFDateTimeUtils (regex as field), Companion in PFDayUtils and PFDateTimeUtils replaced by object class.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\n56a35f979 WIP: BigCalendar -> Fullcalendar\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\nee8dbaa4c Gantt PFDateTime -> PFDay and PFDayUtils.convertToUtilDate."),

    (1364, "PFDay.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/PFDay.kt",
     "Immutable date holder wrapping LocalDate. Date-only counterpart to PFDateTime, implementing IPFDate<PFDay>. Provides year, month, day, week accessors; arithmetic (plus/minus days, weeks, months, years); formatting (user locale, ISO); and conversion to java.util.Date and java.sql.Date. Companion object provides factory methods (from/orNull/orNow) for LocalDate, Date, java.sql.Date, and PFDateTime. Configurable week fields via projectforge.properties.",
     "868d6abb7 2025 -> 2026\nc80d7fb5f PFDay.weekFields modified for testing.\nb131193e7 Member variables refactored by using by lazy\n63081666f Source file headers: 2024-> 2025.\n5f9bbfbd3 Fix typos in projectforge-business directory\n2fbd0908f PFDay: hashCode, equals.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\n4827784b5 WIP: DataTransfer mail notification. IPFDate.isHoliday and isHolidayOrWeekend implemented.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n01bef429c PFDay/PFDateTime: weekOfYear is now configurable in projectforge.properties\n66c1835a3 IPFDate.withDayOfWeek(DayOfWeek) added.\n6a8d4e68d Liquidity: wip: support of base date in past."),

    (1365, "PFDayUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/PFDayUtils.kt",
     "Utility object for LocalDate/IPFDate operations: begin/end of year, month, week calculations; working day calculations using Holidays (getNumberOfWorkingDays, addWorkingDays, getNextWorkingDay); day-of-week mapping (ISO and compatibility); month validation; date parsing (ISO and user locale formats); and date range checking.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n5f9bbfbd3 Fix typos in projectforge-business directory\n6a9ba0372 Minor improvments in PFDateTimeUtils (regex as field), Companion in PFDayUtils and PFDateTimeUtils replaced by object class.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\n5f7ef41b8 Copyright 2021 -> 2022\ndb3b02da7 UserException moved from business to common package\nceb63e8a1 Source code header: (C) 2001-2021.\n62cf96b16 Code warnings.\n0e4d3b8d2 PFDayUtils.parseDate(str: String?) support now date strings including time of day.\n461831f76 Wicket: LocalDate converter.\nee8dbaa4c Gantt PFDateTime -> PFDay and PFDayUtils.convertToUtilDate.\nb209e00ba PFDay.from -> from, fromOrNow, fromOrNull"),

    (1366, "TimePeriod.kt", "Data Class/Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/TimePeriod.kt",
     "Represents a time period with fromDate/toDate (java.util.Date) and optional marker. Provides duration in millis, hours (BigDecimal with configurable rounding), and field decomposition (days, hours, minutes) based on configurable hours-of-day. Supports creation from LocalDate and includes human-readable formatted string output.",
     "868d6abb7 2025 -> 2026\nee53d43df AI savings: calculation of percent modified, TimesheetDO @Enumerated in database for unit. TimePeriod.getDurationFields rounds now seconds and minutes (half up).\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\nd2157e204 New calendar improved (timesheets with more info).\nb32a865ae DateFormats: time of day: leading space removed. TimePeriod.formattedString, UIAlert supports now Markdown-tables.\n5f7ef41b8 Copyright 2021 -> 2022\nf759829ec MonthlyReport: average working hours added, kost1 fixed.\nceb63e8a1 Source code header: (C) 2001-2021.\n0e8ed158b TimesheetStats supports now rounding modes. Migrated to Kotlin.\n88c6891f2 RoundUtils added.\n4380cf352 TimePeriod.getDurationHours with several rounding modes.\nce5d0895b ScriptExecutePage fixed.\nf65c71851 Review, compile errors fixed and first tests."),

    (1367, "TimeUnit.kt", "Enum",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/time/TimeUnit.kt",
     "Enum defining time units with millisecond equivalents: SECONDS (1000), MINUTE (60s), HOUR (60m), DAY (24h), WEEK (7d), MONTH (30d), YEAR (365d). Used for expiration calculations (e.g., password reset tokens) and time-ago/left formatting.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n10c495b5f TimeAgo: TimeUnit.MINUTE. 2FA BruteForce tested (incl. user deactivation and reactivation).\n5f7ef41b8 Copyright 2021 -> 2022\n481d52ee8 TimeAgo/Left: TimeUnit introduced.\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1368, "ToStringUtil.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/ToStringUtil.kt",
     "JSON serialization framework for toString() methods. Provides ObjectMapper caching with embedded serializers for key domain objects (PFUserDO, GroupDO, TaskDO, ProjektDO, KundeDO, Kost1DO/Kost2DO, EmployeeDO, AddressbookDO). Includes serializer classes for Date, Timestamp, LocalDate, LocalTime, PFDateTime, and Hibernate proxy handling. Supports configuration for preferring embedded serializers vs. id-only output.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n59519ee50 Json serialization refactored: IdOnlySerializer and IdsOnlySerializer introduced.\n5f9bbfbd3 Fix typos in projectforge-business directory\nddf02927d Migration stuff in progress...\n4942c854d Migration stuff in progress...\n9aff90908 Migration stuff in progress... (all tests of all packages: OK).\ne66d5f5f7 Migration stuff in progress... TaskTree -> Kotlin\n4c04cfd65 MAJOR-CHANGE! Migration of integer id's to Long id's (including fk's etc.)\n57935eb50 Java 11, but Wicket 9.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nc0f2b9de0 Tenants functionality removed everywhere (untested).\nceb63e8a1 Source code header: (C) 2001-2021."),

    (1369, "CurrencyHelper.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/CurrencyHelper.kt",
     "Currency calculation utility: computes gross amount from net + VAT, net amount from gross / (1 + VAT), and BigDecimal multiplication with optional rounding. All methods handle null inputs safely returning BigDecimal.ZERO.",
     "868d6abb7 2025 -> 2026\n7a88efc65 WIP: Import of creditor invoices\n63081666f Source file headers: 2024-> 2025.\nba2479571 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\n4bd7c11b2 CurrencyHelper: source file header fixed.\n9f21d879d RechnungCalculator: rounding issues in vat amounts fixed. CurrencyHelper converted to Kotlin.\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1370, "DiskUsage.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/DiskUsage.kt",
     "Queries disk usage statistics for a given directory path: total space, free/usable space, used space (directory size via Apache Commons FileUtils), and percentage. Initializes from File, String path, or no-arg constructor.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\ne63d62d2a WIP data transfer tool.\n7da04107c SystemStatisticsPage: backup dirs (disk usage) fixed.\n627e53367 SystemStatisticPageRest: DiskUsage added for JCR and backup dir.\nceb63e8a1 Source code header: (C) 2001-2021.\n88c6891f2 RoundUtils added.\n7c79f1922 Copyright of source header -> 2020.\n76a8fb69d Hibernate.Restrictions -> PF.QueryFilter\naba5af116 BaseDao.contains and BaseDao.getHistoryEntries are now public.\n507854213 WIP: MagicFilter...\ndd5ca38ac CopyRight of all java file-header updated or created."),

    (1371, "FileCheck.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/FileCheck.kt",
     "Validates uploaded files against allowed extensions and maximum file size. Returns localized error message keys for unsupported format or size exceeded; returns null if file passes validation. Uses FileUtils for extension checking and max size calculation.",
     "868d6abb7 2025 -> 2026\n6ce1f11ae WIP\na3c04e308 FileCheck / FileUtils"),

    (1372, "LocaleUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/LocaleUtils.kt",
     "Parses Locale from string representation using Locale.forLanguageTag(). Accepts language tags (e.g., 'de', 'en-US') and logs warnings on parse failures.",
     "868d6abb7 2025 -> 2026\nbf33c20a9 DevelopmentMainForRelease.main (i18n stuff fixed)\n6ed941a08 WIP: AdressImport/parser"),

    (1373, "MarkdownBuilder.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/MarkdownBuilder.kt",
     "Fluent builder for generating Markdown content with optional HTML span coloring. Supports headings, tables (with header row formatting), list items, multi-line text, and pipe-separated key-value pairs. Provides markdown and HTML escaping for security. Used for job monitor output, email rendering, and activity logs.",
     "868d6abb7 2025 -> 2026\n6dbd7e2ce AddressViewPageRest refactored, caching of favorite addresses fixed\n5b9dcf3f5 AddressViewPage fixed in display of addresses.\n03502905d MarkdownBuilder escapes now the input strings.\n5d4d9f90b Pagination page size removed for all rest pages\nffc71ab7e WIP: Import of creditor invoices\n363d3b836 WIP: Import of creditor invoices.\nb578c2b66 WIP: Import of creditor invoices. CheckBox supports now bool var inline.\n8a2ea847f MyMenuPagesRest: New Excel functionality for customizing the personal menu.\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n163492453 WIP: Jobs and Bank account records.\n09b3f0df7 WIP: Jobmonitor. ListStatisticsSupport -> MarkdownBuilder\na1646e91a WIP: Banking plugin (and new import module)."),

    (1374, "NumberFormatter.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/NumberFormatter.kt",
     "Formats numbers for display using the logged-in user's locale. Supports custom DecimalFormat patterns, currency formatting with optional symbol, month name display, percent formatting, and automatic fraction digits via scale parameter. Handles BigDecimal, BigInteger, Double, Float, Int, and Long types.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\ndcfc7c1a9 Old calendar moved to sub menu, ScriptingTask*, JiraUtils\n38bec971a ThreadLocal -> Kotlin\nd7b3e8751 AG grid: Copy and paste and Excel export improved.\n28f622031 WIP: CreateI18nKeys refactored.\n53b9bc462 WIP: AG-Grid\na10660bc8 WIP: scripting.\ne003882f0 Ace source editor supports now find-key. NumberFormatter.format(Number, pattern, ...) implemented.\n5f7ef41b8 Copyright 2021 -> 2022\n77f2d86ea NumberHelper.format: uses now BigDecimal, BigInteger, Int, Long etc.\nceb63e8a1 Source code header: (C) 2001-2021.\nb5932bb15 DTO: initialize -> copyFrom. formatBigDeimals removed."),

    (1375, "NumberHelper.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/NumberHelper.kt",
     "Comprehensive number utility: parsing (Integer, Long, Short, BigDecimal, currency with locale), formatting (bytes, fractions, percentages), BigDecimal operations (add, compare, scale), phone number extraction, random string generation (secure alphanumeric with various charsets), and value splitting/range checking. Central utility used across the entire application.",
     "868d6abb7 2025 -> 2026\nc624d79b8 PhoneNumberUtils.formatPhoneNumber and AddressTextParser\n6e9cfe0ae Improvements for CostSearchPagesRest\nc2ba57836 WIP: Parsing of creditor invoices.\nc21d9772b VacationDao: NPE fix. AITimeSavings.getFraction(...) added.\n47d42a5bb AI savings: mass update of time-sheets, improvements.\n946458bb7 Forecast supports now closes snapshot dates.\n63081666f Source file headers: 2024-> 2025.\n5f9bbfbd3 Fix typos in projectforge-business directory\n9f874e26c MAJOR-CHANGE! Migration of integer id's to Long id's\n4c04cfd65 MAJOR-CHANGE! Migration of integer id's to Long id's\nb6092df09 Copyright 2023 -> 2024\n8d38939ab DataTransferArea: Password for external access with increased security\n1854f91aa WIP Sipgate.\nc827ecd43 NNumberHelper.extractPhoneNumber removes now (0) in +49 (0) 123456."),

    (1376, "PhoneNumberUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/PhoneNumberUtils.kt",
     "Phone number normalization and comparison utility. Normalizes phone numbers to canonical format (+CC Area Number[-Ext]), detecting country codes from a comprehensive known-codes set, handling various input formats (with +, 00, leading 0, international prefixes, extensions). Also provides phone number equality comparison via normalization.",
     "868d6abb7 2025 -> 2026\n2b9888261 Numberformatting in Sipgate and vcard handling refactored.\na2608ee2e PhoneNumberUtils...\nc624d79b8 PhoneNumberUtils.formatPhoneNumber and AddressTextParser"),

    (1377, "RoundUnit.kt", "Enum",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/RoundUnit.kt",
     "Enum defining rounding precision levels for numeric values: INT (whole numbers), HALF (0.5 increments), QUARTER (0.25), FIFTH (0.2), and TENTH (0.1). Used by RoundUtils and TimePeriod for duration rounding.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n88c6891f2 RoundUtils added.\n7c79f1922 Copyright of source header -> 2020.\n76a8fb69d Hibernate.Restrictions -> PF.QueryFilter\naba5af116 BaseDao.contains and BaseDao.getHistoryEntries are now public.\n507854213 WIP: MagicFilter...\ndd5ca38ac CopyRight of all java file-header updated or created.\n9af6f6dbd PROJECTFORGE-2282 improve error handling on excel import"),

    (1378, "RoundUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/RoundUtils.kt",
     "Rounding utility for BigDecimal and Long values. Supports rounding to INT, HALF, QUARTER, FIFTH, and TENTH precision levels using configurable RoundingMode. Multiplies, rounds, then divides back to achieve the desired precision.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n0e8ed158b TimesheetStats supports now rounding modes. Migrated to Kotlin.\n88c6891f2 RoundUtils added."),

    (1379, "SourcesUtilsContext.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/SourcesUtilsContext.kt",
     "Simple data class holder for SourcesUtils context. Currently contains only a logger reference. Used as companion context for source code utilities.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n16b6494b4 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1380, "SourcesUtils.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/SourcesUtils.kt",
     "Utility for extracting class names from Kotlin/Java source files. Walks project directory tree to find src/main directories, parses source files removing comments and strings, detects class/interface/object/enum declarations (including nested classes), and returns fully qualified class names. Also provides comment/string removal functions for source code analysis.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\ne0c1ffb42 SourcesUtils failed in Linux-Environments (StackOverFlowException in regex).\ne21feaa61 Gradle games...\ne1539248d Migration stuff in progress... (all tests of all packages: OK).\n16b6494b4 Migration stuff in progress..."),

    (1381, "StringComparator.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/StringComparator.kt",
     "Locale-aware string comparison using Java's Collator. Provides a pre-configured German collator (SECONDARY strength: a==A, a<Ä) and a default collator from the system's default locale. Supports ascending/descending order and uses ThreadLocalUserContext locale when none specified.",
     "868d6abb7 2025 -> 2026\nb131193e7 Member variables refactored by using by lazy\n63081666f Source file headers: 2024-> 2025.\n5f9bbfbd3 Fix typos in projectforge-business directory\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n38bec971a ThreadLocal -> Kotlin\nb25f43c27 WIP: CreateI18nKeys refactored.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\n7c4884fdf StringComparator -> kotlin and uses now static members..."),

    (1382, "ValueParser.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/utils/ValueParser.kt",
     "Parses strings into Long or BigDecimal using configurable DecimalFormat patterns. Detects German vs. English number styles (comma vs. dot separators). Caches DecimalFormat instances by pattern for performance. Handles both integer-only and big decimal parsing with format pattern swapping for locale differences.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n87dd5b87c AuftragsCache refactored, migration stuff... (all tests OK)\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n2e11ec633 CsvImporter has now autodetection of number format (1.234,27; 1234,27; 1,234.27 or 1234.27).\n281a22b31 ValueParser.parseBigDecimal uses now only given pattern (no auto-convert)\n67eed70e4 WIP: Banking plugin (and new import module). JobHandler/monitor started."),

    (1383, "XStreamHelper.kt", "Utils",
     "projectforge-business/src/main/kotlin/org/projectforge/framework/xmlstream/XStreamHelper.kt",
     "Helper for XStream XML serialization/deserialization. Creates configured XStream instances with security permissions (any type, null, primitives, wildcard types for java.lang/java.util/org.projectforge), type allow-listing, and annotation processing. Provides toXml/fromXml methods with package alias support for migration.",
     "868d6abb7 2025 -> 2026\nee32b3e3a Code deprecations.\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\nf8be33f35 XStream security"),

    (1384, "JiraUtils.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/jira/JiraUtils.kt",
     "JIRA integration utility for detecting, parsing, and linking JIRA issue keys (PROJECT-123 format) in text, task descriptions, and timesheet entries. Supports multiple JIRA servers configured in config.xml, builds browse links, and can filter by project. Uses regex pattern [A-Z][A-Z_0-9]*-[0-9]+ for issue detection.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\n3bd8540df PF supports now multiple JIRA servers (configurable in config.xml) for external links in time sheets and tasks, such as PF-123.\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n0d73649c5 JiraUtils\ndcfc7c1a9 Old calendar moved to sub menu, ScriptingTask*, JiraUtils\n33773687c JiraUtils: NPE-Hotfix.\nac4e4d677 JiraUtils improved (in Kotlin)."),

    (1385, "LoginData.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/login/LoginData.kt",
     "Data class for login credentials. Extends My2FAData to include 2FA support. Holds username, password (as CharArray for security), and stayLoggedIn flag. Used by LoginService for authentication requests.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\nad2ec6534 WIP: 2FA after login\n07c3e2426 WIP: Refactoring of login handling...\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1386, "LoginService.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/login/LoginService.kt",
     "Spring @Service managing user authentication and session handling. Supports login with password checking, brute-force protection (LoginProtection), stay-logged-in cookies, 2FA requirement after login, session fixation prevention, and logout (clearing cookies, flushing user preferences to DB). Integrates with configurable LoginHandler implementations (LdapMaster, LdapSlave, or Default).",
     "c771cc445 Refactor projectforge-keycloak to projectforge-idp with Authentik support\nba267847c Improve Keycloak password sync robustness and diagnostics\nb78148558 Add Keycloak integration: new projectforge-keycloak module\n868d6abb7 2025 -> 2026\nbbdb5825b Scripts: exception -> log, UserContext.refreshUser() handling changed.\n63081666f Source file headers: 2024-> 2025.\n3c42485eb Migration stuff in progress... (all tests of all packages: OK).\ncba940301 Migration stuff in progress...\n4f5a458c9 Migration stuff in progress...\n77bade6df javax.* -> jakarta.*\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n3c429405c LoginService: show last 2FA as time-ago message.\nca914dbb9 WIP: 2FA after login\n4162bfe5c WIP: 2FA after login seems to work now fine..."),

    (1387, "LogoutListener.kt", "Interface",
     "projectforge-business/src/main/kotlin/org/projectforge/login/LogoutListener.kt",
     "Interface for listening to logout events. Registered listeners are called by LoginService during logout (e.g., for cleaning up Wicket sessions). Provides a single logout(request, response) method.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n77bade6df javax.* -> jakarta.*\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n87c3c773c WIP: Refactoring of login handling...\n07c3e2426 WIP: Refactoring of login handling...\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\ndd5ca38ac CopyRight of all java file-header updated or created.\n9ebb88522 Initial commit"),

    (1388, "IMailAttachment.kt", "Interface",
     "projectforge-business/src/main/kotlin/org/projectforge/mail/IMailAttachment.kt",
     "Interface for email attachments with mutable filename and content (ByteArray) properties.",
     "868d6abb7 2025 -> 2026\n96e97e738 Nothing real.\nb309e9be9 MailAttachments improved (effected BirthdayButler, Polls)."),

    (1389, "MailAttachment.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/mail/MailAttachment.kt",
     "Concrete implementation of IMailAttachment. Simple data class with filename and byte array content properties.",
     "868d6abb7 2025 -> 2026\n96e97e738 Nothing real.\nb309e9be9 MailAttachments improved (effected BirthdayButler, Polls)."),

    (1390, "SendMail.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/mail/SendMail.kt",
     "Spring @Service for creating and sending emails via Jakarta Mail. Supports SMTP with Plain/StartTLS/SSL, MIME multipart messages with inline text/html, iCal calendar invitations, and file attachments (MimeBodyPart with DataHandler). Provides Groovy template rendering for mail content, async email sending, and configurable sender/domain via application properties.",
     "868d6abb7 2025 -> 2026\nb309e9be9 MailAttachments improved (effected BirthdayButler, Polls).\n63081666f Source file headers: 2024-> 2025.\nb405cf643 WIP\n67805f2fc ThreadLocalUserContext.user -> ThreadLocalUserContext.loggedInUser\n77bade6df javax.* -> jakarta.*\nb6092df09 Copyright 2023 -> 2024\na25c868cb SendMail refactored (Genome part removed).\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n73b0be50b org.apache.commons.collections -> org.apache.commons.collections4\n38bec971a ThreadLocal -> Kotlin\neec260821 I18nHelper.getLocalizedMessage(user, ...)\n24a051884 SendMail -> Kotlin (fixes)\n71754f106 SendMail: data map allows null values.\n9b1017171 Test fixed."),

    (1391, "FavoritesMenuCreator.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/FavoritesMenuCreator.kt",
     "Spring @Component managing user-customizable favorite menus. Reads/writes favorite menu configuration from user XML preferences via FavoritesMenuReaderWriter. Creates default favorite menus based on user roles (admin sees administration entries, restricted users see password change only, regular users see project management, calendar, tasks, etc.). Integrates with plugins for custom menu entries.",
     "868d6abb7 2025 -> 2026\nd6e723000 MenuCustomizer finetuning (Claude Code)\n8a2ea847f MyMenuPagesRest: New Excel functionality for customizing the personal menu.\n261354a30 Visibility of menu items is now configurable (by groups).\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\nec5e5631f Menu customization works again.\n5f7ef41b8 Copyright 2021 -> 2022\n65555777a DataTransferPlugin: menu DataTransfer is automatically added\neb63e8a1 Source code header: (C) 2001-2021.\n6c67f4f91 MenuItemDefId supports now url.\n7c79f1922 Copyright of source header -> 2020.\n7886144df FavoritesMenuCreator: BadgeCounter for menus with sub menus"),

    (1392, "FavoritesMenuReaderWriter.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/FavoritesMenuReaderWriter.kt",
     "Serializes/deserializes user favorite menus to/from XML stored in user preferences. Supports XML format (current) and legacy CSV format. Builds DOM4J Element trees from MenuItem hierarchies and vice versa. Handles unique key generation for menu items without MenuItemDef. Validates max serialized length against UserXmlPreferencesDO limits.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n5f9bbfbd3 Fix typos in projectforge-business directory\n011000f03 Migration stuff in progress... (all tests of all packages: OK).\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\nec5e5631f Menu customization works again.\n5f7ef41b8 Copyright 2021 -> 2022\ndb3b02da7 UserException moved from business to common package\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\ndebb7ada2 Code cleanup\n05244ff19 CopyRight of all Kotlin file-header updated or created.\nf36be21d5 Fav-menu: unique key (for React) also for menus without MenuItemDef.\n8e5d35c00 Favorites menu: de/serialization fix."),

    (1393, "MenuCreatorContext.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/MenuCreatorContext.kt",
     "Context data class for menu creation, holding the target PFUserDO and a translate flag (whether to translate i18n keys to localized titles). Passed through menu building to customize the menu per user.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\n05244ff19 CopyRight of all Kotlin file-header updated or created.\n7cccf3be8 Wicket menu restructured, mobile pages removed.\nb0fd52b9f menu moved from jax-rs to business (for re-usage in Wicket)."),

    (1394, "MenuCreator.kt", "Service",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/MenuCreator.kt",
     "Spring @Component defining the master menu tree structure. Initializes all MenuItemDef entries in a hierarchy (COMMON, PROJECT_MANAGEMENT, HR, FIBU, COST, REPORTING, ORGA, ADMINISTRATION, MISC) with sub-menu items. Each menu item has configurable access checks (required groups, user rights, custom lambda checks), badge counters (e.g., pending vacation approvals, to-be-invoiced orders), and supports plugin menu registration. The build() method creates a user-specific Menu by filtering based on access rights.",
     "868d6abb7 2025 -> 2026\ned1b06fa0 WIP: currency conversion with Claude Code.\n7187b40f9 Menu customization\n2cf5332b3 Cost-Search added for Fakturafuexe\n8a2ea847f MyMenuPagesRest: New Excel functionality for customizing the personal menu.\n261354a30 Visibility of menu items is now configurable (by groups).\n46ec387f5 MenuItemDef.requiredUserRight removed\n63081666f Source file headers: 2024-> 2025.\n6b5594ea3 POLL-menu position fixed.\n144af40ca Merge pull request #230 from NikitaMic/develop\nd96924c09 Fixed ExcelExport synthax and added logs\n543f785af Menu: poll added to misc.\n1012e347a Migration stuff in progress... (all tests of all packages: OK).\n87dd5b87c AuftragsCache refactored\n67805f2fc ThreadLocalUserContext.user -> ThreadLocalUserContext.loggedInUser"),

    (1395, "MenuItemDefId.kt", "Enum",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/MenuItemDefId.kt",
     "Enum defining all menu item identifiers with their i18n keys and URLs. Each enum constant maps to a menu entry (e.g., CALENDAR, TIMESHEET_LIST, USER_LIST, etc.) with URLs constructed from React app paths (getReactListUrl, getReactDynamicPageUrl) or Wicket paths. Serves as the central registry of all possible menu items.",
     "868d6abb7 2025 -> 2026\ned1b06fa0 WIP: currency conversion with Claude Code.\n7187b40f9 Menu customization\n589434d7f Merge branch 'develop'\n2cf5332b3 Cost-Search added for Fakturafuexe\nf5bd7459c Claude CODE-Session (2h, 20$)\nb6d44a498 Menu /react/cost1 commented out.\n8a2ea847f MyMenuPagesRest: New Excel functionality\n261354a30 Visibility of menu items is now configurable\n63081666f Source file headers: 2024-> 2025.\n1012e347a Migration stuff in progress...\nb5dc26e24 Migration stuff in progress...\n55972f36a Migration stuff in progress...\ne33c8b9c2 Migration stuff in progress..."),

    (1396, "MenuItemDef.kt", "Data Class/Service",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/builder/MenuItemDef.kt",
     "Definition of a single menu item used by MenuCreator to dynamically build user menus. Holds id, i18nKey, url, badgeCounter function, badgeTooltipKey, access check lambda, required groups and user rights. Supports hierarchical structure with children. The createMenu() method instantiates a MenuItem with translated title, unique key, and optional badge.",
     "868d6abb7 2025 -> 2026\nee32b3e3a Code deprecations.\n261354a30 Visibility of menu items is now configurable (by groups).\n46ec387f5 MenuItemDef.requiredUserRight removed\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\n619addd5c Doubled menu creation fixed\nceb63e8a1 Source code header: (C) 2001-2021.\n685d7f9cc rest: optimizations for usage from Java classes.\n6c67f4f91 MenuItemDefId supports now url.\n7c79f1922 Copyright of source header -> 2020.\n611a8aaee Refactored (java, kt, less, jsx): childs -> children.\n05244ff19 CopyRight of all Kotlin file-header updated or created."),

    (1397, "MenuBadge.kt", "Data Class",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/MenuBadge.kt",
     "Serializable data class for menu item badges. Holds counter (number), value (string), tooltip, and style (e.g., 'danger' for red badges). Used to display notification counts on menu items.",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\n3121b7ad6 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n7c79f1922 Copyright of source header -> 2020.\n05244ff19 CopyRight of all Kotlin file-header updated or created.\nb0fd52b9f menu moved from jax-rs to business (for re-usage in Wicket)."),

    (1398, "MenuConfiguration.kt", "Configuration",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/MenuConfiguration.kt",
     "Spring @Configuration class managing menu item visibility. Maps application property entries (projectforge.menu.visibility.*) to a registry of MenuVisibility objects. Each menu item (addresses, calendars, books, etc.) can be toggled on/off via properties. Provides isVisible() method that checks both MenuItemDef and MenuItemDefId against the registry.",
     "868d6abb7 2025 -> 2026\n7187b40f9 Menu customization\n8a2ea847f MyMenuPagesRest: New Excel functionality for customizing the personal menu.\n261354a30 Visibility of menu items is now configurable (by groups)."),

    (1399, "MenuItem.kt", "Data Class/Service",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/MenuItem.kt",
     "Serializable menu item representing a node in the menu tree. Holds id, title, i18nKey, tooltip, url, unique key (for React), badge, and target type. Supports hierarchical structure via subMenu list. postProcess() method translates titles, auto-translates tooltips, accumulates badge counters from children to parents, and removes empty parent nodes. Also provides descendant traversal for flat listing.",
     "868d6abb7 2025 -> 2026\n261354a30 Visibility of menu items is now configurable (by groups).\n63081666f Source file headers: 2024-> 2025.\n3121b7ad6 Migration stuff in progress...\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\n65555777a DataTransferPlugin: menu DataTransfer is automatically added\neb63e8a1 Source code header: (C) 2001-2021.\n6c67f4f91 MenuItemDefId supports now url.\n6477edb8d Tooltips in Menu fixed.\n7c79f1922 Copyright of source header -> 2020.\n1a000b3af MenuCreator badge for orders, and badges for fav menus.\n05244ff19 CopyRight of all Kotlin file-header updated or created.\n00aa334ae MenuItem.targetType"),

    (1400, "MenuItemTargetType.kt", "Enum",
     "projectforge-business/src/main/kotlin/org/projectforge/menu/MenuItemTargetType.kt",
     "Enum defining how the client should handle a menu item's URL: REDIRECT (navigate to URL, default), MODAL (open in modal dialog), DOWNLOAD (trigger file download from REST service), and RESTCALL (call REST service and handle response).",
     "868d6abb7 2025 -> 2026\n63081666f Source file headers: 2024-> 2025.\nb6092df09 Copyright 2023 -> 2024\nab45d51fa Copyright 2001-2022 -> 2001-2023.\n5f7ef41b8 Copyright 2021 -> 2022\nceb63e8a1 Source code header: (C) 2001-2021.\n49f337220 move preferModal Option to TargetType.MODAL\n7c79f1922 Copyright of source header -> 2020.\n05244ff19 CopyRight of all Kotlin file-header updated or created.\n00aa334ae MenuItem.targetType"),
]

def write_doc(num, filename, role, source_path, purpose_summary, git_log):
    prev = num - 1
    next_num = num + 1
    # Escape HTML special chars
    git_log_escaped = html.escape(git_log)
    purpose_escaped = html.escape(purpose_summary)
    path_escaped = html.escape(source_path)
    filename_escaped = html.escape(filename)
    html_content = TEMPLATE.format(
        num=num,
        filename=filename_escaped,
        role=role,
        source_path=path_escaped,
        purpose_summary=purpose_escaped,
        git_log=git_log_escaped,
        prev=prev,
        next=next_num
    )
    filepath = os.path.join(OUT, f"{num}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Wrote {filepath}")

for item in FILES:
    write_doc(*item)

print(f"Done! Generated {len(FILES)} docs.")
