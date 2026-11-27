---
title: "Testing & QA – Curated Developer Resources"
description: "Curated testing and quality assurance tools: unit, end-to-end, API, load and visual testing, mocking and test data."
---

# Testing & QA

Curated testing and quality assurance tools: unit, end-to-end, API, load and visual testing, mocking and test data.

!!! tip "21 hand-picked resources"
    Every link on this page was checked in November 2026. Know a great project that is missing? [Suggest it on GitHub](https://github.com/andriksantos/keebox/issues/new) or read the [contribution guide](contributing.md).

## End-to-end & browser

- [Playwright](https://github.com/microsoft/playwright) - Reliable end-to-end testing for modern web apps.
- [Cypress](https://github.com/cypress-io/cypress) - Fast, easy and reliable testing for anything that runs in a browser.
- [Selenium](https://github.com/SeleniumHQ/selenium) - Browser automation framework and ecosystem.
- [WebdriverIO](https://github.com/webdriverio/webdriverio) - Next-gen browser and mobile automation test framework.
- [Puppeteer](https://github.com/puppeteer/puppeteer) - JavaScript API for Chrome and Firefox.

## Unit testing

- [Jest](https://github.com/jestjs/jest) - Delightful JavaScript testing.
- [Vitest](https://github.com/vitest-dev/vitest) - Next-generation testing framework powered by Vite.
- [pytest](https://github.com/pytest-dev/pytest) - Simple, powerful Python testing framework.
- [JUnit](https://github.com/junit-team/junit-framework) - The programmer-friendly testing framework for Java.

## Load & performance

- [k6](https://github.com/grafana/k6) - Modern load testing tool, using Go and JavaScript.
- [Locust](https://github.com/locustio/locust) - Scalable load testing written in Python.
- [Artillery](https://github.com/artilleryio/artillery) - Load testing at cloud scale.
- [Lighthouse](https://github.com/GoogleChrome/lighthouse) - Automated auditing, performance metrics and best practices for the web.

## Mocks, data & contracts

- [Mock Service Worker](https://github.com/mswjs/msw) - Industry standard API mocking for JavaScript.
- [WireMock](https://github.com/wiremock/wiremock) - Tool for mocking HTTP services.
- [Faker.js](https://github.com/faker-js/faker) - Generate massive amounts of fake data.
- [Testcontainers](https://github.com/testcontainers/testcontainers-java) - Throwaway containers for integration tests.
- [Pact](https://github.com/pact-foundation/pact-js) - Consumer-driven contract testing.

## Learn testing

- [JavaScript Testing Best Practices](https://github.com/goldbergyoni/javascript-testing-best-practices) - Comprehensive testing best practices guide.
- [Awesome Testing](https://github.com/TheJambo/awesome-testing) - Curated resources for software testers.
- [Awesome Test Automation](https://github.com/atinfo/awesome-test-automation) - Curated list of test automation frameworks and tools.

<!-- kb-guide:start -->

## Building a testing strategy

A useful way to plan tests is the testing pyramid: many fast unit tests, fewer integration and API tests, and a small set of end-to-end tests that cover the flows that make you money.

1. **Unit tests** (Jest, Vitest, pytest, JUnit) check functions and components in milliseconds. Run them on every save and every commit.
2. **API and contract tests** catch breaking changes between services before they reach users. Mock external services so tests stay reliable.
3. **End-to-end tests** (Playwright, Cypress) simulate a real user in a browser. Keep them focused on critical paths such as sign-up, checkout and login.
4. **Load tests** (k6, Locust) show how your system behaves under traffic before a launch or a marketing campaign.
5. **Visual tests** compare screenshots to catch layout bugs that functional tests miss.

Run everything in continuous integration, and treat flaky tests as bugs: a test suite nobody trusts is worse than a smaller one that always tells the truth.

## Frequently asked questions

??? question "Playwright or Cypress?"
    Both are excellent. Playwright supports Chromium, Firefox and WebKit, multiple tabs and several languages (JavaScript, Python, Java, .NET). Cypress has a very friendly interactive runner and is popular in JavaScript front-end teams. For new projects, Playwright is the more flexible default.

??? question "How much test coverage do I need?"
    There is no universal number. Aim for high coverage of business logic and critical flows, and do not chase 100% on simple glue code. A rising coverage trend matters more than a fixed target.

??? question "What should I test first in a project with no tests?"
    Start with an end-to-end test of the most important user flow, then add unit tests every time you fix a bug, so the same bug cannot return.

## Keep exploring

- [Testing resources in the Library](library/testing.md) · [Playwright](library/playwright.md) · [Selenium](library/selenium.md) · [k6 load testing](library/k6.md)
- [DevOps](devops.md) · [Security](security.md)

<!-- kb-guide:end -->
