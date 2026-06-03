# ProjectForge — Open-Source Business Management Platform

ProjectForge is a web-based business management application covering project management,
time tracking, HR, finance, and team collaboration. Built with Kotlin/Spring Boot on the
backend and Apache Wicket for the web frontend.

## Quick Start

```bash
./gradlew build
./gradlew bootRun
```

Then open http://localhost:8080

## Features

- Project and task management
- Time tracking and timesheets
- Financial management (orders, invoices, contracts)
- Human resources (addresses, skills, teams)
- Calendar with team scheduling
- Document management (DMS)
- Access control and permission system
- Multi-language support (German, English)
- Plugin system for extensibility

## Technology Stack

- **Backend**: Kotlin, Spring Boot, Hibernate, PostgreSQL
- **Frontend**: Apache Wicket, Wicket jQuery UI
- **Build**: Gradle with Kotlin DSL

## Build

```bash
./gradlew build -x test     # Build without tests
./gradlew test               # Run all tests
./gradlew bootRun            # Start development server
```

Requires: JDK 17+, PostgreSQL
