---
title: "Event-Driven Architecture – Awesome List with 21 resources"
description: "21 curated Event-Driven Architecture resources: A software architecture approach where services collaborate by publishing and subscribing to events."
---

# Event-Driven Architecture

A software architecture approach where services collaborate by publishing and subscribing to events.

!!! info "Source"
    21 resources imported from [lutzh/awesome-event-driven-architecture](https://github.com/lutzh/awesome-event-driven-architecture), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Miscellaneous**.
## 📕 Articles

### Foundational

- [Going “Events-First” for Microservices with Event Storming and DDD](https://medium.com/russmiles/going-events-first-for-microservices-with-event-storming-and-ddd-8614437486f0) - By Russ Miles, October 2016. _"It is **not the things** that matter in early stages of design - **it is the things that happen**."_
- [Events As First-Class Citizens](https://hackernoon.com/events-as-first-class-citizens-8633e8479493?gi=5ecff3301dfa) - By Randy Shoup, January 2018. Focusses on the most important part of EDA: The actual events.
- [Why Event-First Programming Changes Everything](https://www.confluent.io/blog/journey-to-event-driven-part-1-why-event-first-thinking-changes-everything/) - By Neil Avery, January 2019. Somewhat lengthy article that's great in painting the "big picture".
- [Introduction to Event-Driven Architecture](https://medium.com/microservicegeeks/introduction-to-event-driven-architecture-e94ef442d824) - By Kacey Bui, February 2021. Good overview of the basics.
- [The Resurgence of Event Driven Architecture](https://kimjulianclark.medium.com/the-resurgence-of-event-driven-architecture-9c2daa41d9b6) - By Kim Clark, May 2021. Historical context for the renewed interest in EDA. Provides a high-level view of Kafka vs. Queues, and unusually clear about runtime decoupling vs. request/response.
- [Orchestration vs. Choreography](https://www.ben-morris.com/orchestration-vs-choreography-for-microservice-workflows/) - By Ben Morris, December 2021. Every non-trivial system involves workflows that span multiple services. There are opposing schools of thought on how to handle this. Ben Morris gives a short, balanced introduction.

### Experience Reports And Practicalities

- [Event Granularity: Modelling events in event driven applications](https://barryosull.com/blog/event-granularity-modelling-events-in-event-driven-applications/) - By Barry O'Sullivan, December 2017. About finding the right granularity for events.
- [Moving from orchestration to choreography](https://blogit.michelin.io/choregraphy-or-orchestration-thats-the-question/) - By Olivier Jauze, March 2021. Michelin's journey from BPM orchestration to event-driven choreography. It's the first of a series and continues with [part 2](https://blogit.michelin.io/moving-from-orchestration-to-choregraphy-part-2/) and [part 3](https://blogit.michelin.io/moving-from-orchestration-to-choreography-part-3/).
- [The different types of events in event-driven systems](https://blog.frankdejonge.nl/the-different-types-of-events-in-event-driven-systems/) - By Frank de Jonge, February 2022. There are different approaches to classifying events - this is a very good one.
- [Reliable event dispatching using a transactional outbox](https://blog.frankdejonge.nl/reliable-event-dispatching-using-a-transactional-outbox/) - By Frank de Jonge, February 2022. Transactional outbox is a crucial pattern for services basing their persistence on CRUD/RDBMS.
- [Behind the scenes: McDonald's event-driven architecture](https://medium.com/mcdonalds-technical-blog/behind-the-scenes-mcdonalds-event-driven-architecture-51a6542c0d86) - From the McDonald's tech blog, August 2022. Not very detailed, but an easily digestible case study about event-driven architecture at scale. Listing this here is not an endorsement of their products. There's a [second part](https://medium.com/mcdonalds-technical-blog/mcdonalds-event-driven-architecture-the-data-journey-and-how-it-works-4591d108821f), too.
- [Event Driven Architecture — 5 Pitfalls to Avoid](https://medium.com/wix-engineering/event-driven-architecture-5-pitfalls-to-avoid-b3ebf885bdb1) - By Natan Silnitsky, August 2022. Especially when you only just get started, check this to spare you some frustration later. You might also want to check the "Further Reading" section at the end.
- [5 pitfalls to avoid when implementing an Event-Driven Architecture](https://medium.com/@kris_22373/5-pitfalls-to-avoid-when-implementing-an-event-driven-architecture-7fb04d7fa7ca) - By Kris Van Vlaenderen, January 2024. Sounds very similar to the previous one. But it's not a case of duplicate events - it's actually 5 different pieces of advice.
- [Event-Driven Patterns for Cloud-Native Banking: Lessons from What Works and What Hurts](https://www.infoq.com/articles/event-driven-banking-architecture/) - By Chris Tacey-Green, March 2026. Based on production experience at Investec, the article covers both the benefits and the costs of running EDA in a regulated environment.

## 📺 Videos

### Foundational

- [Core Decisions in Event-Driven Architecture](https://www.youtube.com/watch?v=SKXS2h3MdPM&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Duana Stanley, October 2019. Overall a great talk, definitely worth watching. Below are some minor issues I have with it.
- [Event-Driven Architectures Done Right](https://www.youtube.com/watch?v=A_mstzRGfIE&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Tim Berglund, May 2021. Good overview, clear presentation.
- [Event Driven Architecture & Governance in Action](https://www.youtube.com/watch?v=9guR3CBTG44&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Wim Debreuck, June 2023. A talk that goes beyond the technical fundamentals, into the architecture and design process of event-driven applications. The shown approach might not be universal, but provides important insights. I especially like the clarity around business events.
- [Event-Driven Architecture Explained in 15 Minutes](https://www.youtube.com/watch?v=Fb_0UOD2X2I&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Dave Farley, July 2024. Watching videos by Dave Farley is always time well spent, and his short take on event-driven architecture is no exception.

### Experience Reports And Practicalities

- [EDA in Practice: Building an eCommerce Platform at Cinch](https://www.youtube.com/watch?v=wM-dTroS0FA&t=493s&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Toli Apostolidis, September 2022. You can ignore the first 8 minutes and 15 seconds (in fact the link will skip them), they are mostly promotion for AWS. But from there on follows a good talk on real-world experiences with event-driven architecture.
- [What is the Transactional Outbox Pattern?](https://www.youtube.com/watch?v=5YLpjPmsPCA&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Wade Waldron, February 2024. A short video (just over 5 minutes) explaining what the transactional outbox pattern is and how it works.
- [Shifting Gears: From Events to Event-Driven](https://www.youtube.com/watch?v=1dWJO31wpV8&list=PLXstpDPZ7AtX78V_JYUJX7z8RjdcB9HQq) - By Ryan Cormack, May 2024. He tells the story of Motorway's journey to event driven, and also includes a lot of foundational aspects.
