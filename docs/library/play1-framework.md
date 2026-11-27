---
title: "Play1 Framework – Awesome List with 139 resources"
description: "139 curated Play1 Framework resources: Curated Play1 Framework resources."
---

# Play1 Framework

Curated Play1 Framework resources.

!!! info "Source"
    139 resources imported from [PerfectCarl/awesome-play1](https://github.com/PerfectCarl/awesome-play1), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Back-End Development**.

<!-- kb-about:start -->

## About this list

Play 1 is the original version of the Play Framework, a Java web framework known for hot reloading, a stateless architecture and a convention-over-configuration approach inspired by Rails. Later versions moved to Scala and a different API, so Play 1 applications remain a separate ecosystem.

This list collects modules, plugins and resources for teams still maintaining Play 1 apps. If you are starting a new project, consider a current framework; if you are maintaining one, these modules can save you from rewriting common features.

<!-- kb-about:end -->

### Database

- **[[carbonate] ](http://www.playframework.com/modules/carbonate) [Carbonate](https://github.com/huljas/play-carbonate)** [](http://www.playframework.com/modules/carbonate) Creates and runs database migrations using Hibernate schema update to automatically generate SQL to the migrations. See this blog [post](http://huljas.github.com/code/2011/04/04/managing-database-with-playcarbonate.html)
- **[[chronostamp] ](http://www.playframework.com/modules/chronostamp) [Chronostamp](https://github.com/omaroman/chronostamp)** [](http://www.playframework.com/modules/chronostamp) Enhances Models by adding and updating timestamp fields (created_at & updated_at).
- **[[db] ](http://www.playframework.com/modules/db) [Database module](http://github.com/pepite/play--database)** [](http://www.playframework.com/modules/db)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.db/play-db) Export your Play! domain model to a DDL file and import a database into your Play! domain model.
- **[[jpagen] ](http://www.playframework.com/modules/jpagen) [JpaGen](http://github.com/marcuspocus/jpagen)** [](http://www.playframework.com/modules/jpagen) Generates JPA Entities and Composite keys (when needed) from metadata or a file containing a list of tables.
- **[[liquibase] ](http://www.playframework.com/modules/liquibase) [Liquibase](https://github.com/7uc0/play-liquibase)** [](http://www.playframework.com/modules/liquibase) [Liquibase](http://www.liquibase.org) is a simple, reliable and elegant solution for database refactoring management
- **[[logisimayml] ](http://www.playframework.com/modules/logisimayml) [logisima-yml](http://github.com/sim51/logisima-play-yml)** [](http://www.playframework.com/modules/logisimayml) Exports your database into an yml file
- **[[migrate] ](http://www.playframework.com/modules/migrate) [Database migration](http://github.com/dcardon/play-migrate)** [](http://www.playframework.com/modules/migrate) Maintains database versions for your project.
- **[[multidb] ](http://www.playframework.com/modules/multidb) [Multiple Databases](http://github.com/dcardon/play-multidb)** [](http://www.playframework.com/modules/multidb) Scale your application to multiple databases with a common schema.

### Deployment

- **[[capistrano] ](http://www.playframework.com/modules/capistrano) [Capistrano](https://github.com/mandubian/play-capistrano)** [](http://www.playframework.com/modules/capistrano) Deploys a remote application using Capistrano + SSH + VCS and run it in nohup/background mode.
- **[[cargo] ](http://www.playframework.com/modules/cargo) [Cargo](https://github.com/dgouyette/play-cargo)** [](http://www.playframework.com/modules/cargo) Remotely deploys your application.
- **[[cloudbees] ](http://www.playframework.com/modules/cloudbees) [CloudBees](https://github.com/hadashi/play-cloudbees)** [](http://www.playframework.com/modules/cloudbees) Provides integration with CloudBees.
- **[[cloudfoundry] ](http://www.playframework.com/modules/cloudfoundry) [CloudFoundry](https://github.com/bcourtine/play--cloudfondry)** [](http://www.playframework.com/modules/cloudfoundry) Automatically configure the database your application is deployed in In CloudFoundry.
- **[[dotcloud] ](http://www.playframework.com/modules/dotcloud) [Dotcloud](https://github.com/lsinger/play-dotcloud)** [](http://www.playframework.com/modules/dotcloud) Deploys your application to dotcloud
- **[[gae] ](http://www.playframework.com/modules/gae) [Google App Engine](http://github.com/guillaumebort/play-gae)** [](http://www.playframework.com/modules/gae)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.gae/play-gae) Creates application for the Google App Engine platform.
- **[[heroku] ](http://www.playframework.com/modules/heroku) [Heroku](https://github.com/jamesward/play-heroku)** [](http://www.playframework.com/modules/heroku) Deploys your application on Heroku.
- **[[jelastic] ](http://www.playframework.com/modules/jelastic) [Jelastic Deployment Support](https://github.com/Fameing/play-jelastic)** [](http://www.playframework.com/modules/jelastic) Deploy your application in the Jelastic Platform.
- **[[openebay] ](http://www.playframework.com/modules/openebay) [Open eBay](https://bitbucket.org/kumaresan/openebay)** [](http://www.playframework.com/modules/openebay) Provides the basic plumbing to create an [Open eBay Application](http://apps.ebay.com/)
- **[[openshift] ](http://www.playframework.com/modules/openshift) [Openshift](https://github.com/opensas/openshift)** [](http://www.playframework.com/modules/openshift) Openshift is Red Hat’s free, auto-scaling, cloud-based platform-as-a-service for Java, Perl, PHP, Python, and Ruby applications.
- **[play-gae-q42]  [Q42's Google App Engine](https://github.com/Q42/play-gae)** [](https://github.com/Q42/play-gae) Maintained module for Google App Engine integration. Should be used instead of [gae]
- **[[playapps] ](http://www.playframework.com/modules/playapps) [playapps.net](http://github.com/zenexity/play-playapps)** [](http://www.playframework.com/modules/playapps) playapps.net is a streamlined deployment environment designed to get your Play applications up and running quickly and efficiently
- **[[reverseproxy] ](http://www.playframework.com/modules/reverseproxy) [ReverseProxy](https://github.com/omaroman/reverseproxy)** [](http://www.playframework.com/modules/reverseproxy) Configures your application to automatically switch between the HTTP and HTTPS protocols per page when used behind a front end.
- **[[router] ](http://www.playframework.com/modules/router) [Play Router Annotations](https://github.com/digiPlant/play-router-annotations)** [](http://www.playframework.com/modules/router)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.router/play-router) Adds routes through annotations, allowing you to declare your routes in your controllers.
- **[[stax] ](http://www.playframework.com/modules/stax) [Stax](http://github.com/erwan/playstax)** [](http://www.playframework.com/modules/stax) Easy deployment to Stax cloud hosting platform (http://www.stax.net).
- **[[vhost] ](http://www.playframework.com/modules/vhost) [VHost](https://github.com/lyubo/play-vhost)** [](http://www.playframework.com/modules/vhost) Adds some virtual hosts functionality with separate datasource and customizable application settings for each virtual host.

### Injection/dependencies

- **[[constretto] ](http://www.playframework.com/modules/constretto) [Constretto](https://github.com/zapodot/constretto-play)** [](http://www.playframework.com/modules/constretto)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.constretto/play-constretto) Makes integration with the Constretto configration framework easy
- **[[guice] ](http://www.playframework.com/modules/guice) [Guice](http://github.com/pk11/play-guice-module)** [](http://www.playframework.com/modules/guice)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.guice/play-guice) Injects Guice managed components into your application.
- **[[ivy] ](http://www.playframework.com/modules/ivy) [Ivy dependency management](http://github.com/pk11/play-ivy)** [](http://www.playframework.com/modules/ivy) Manages your dependencies with apache ivy.
- **[[maven] ](http://www.playframework.com/modules/maven) [Maven dependency management](http://github.com/wangyizhuo/play-maven)** [](http://www.playframework.com/modules/maven) Manages your dependencies with apache maven
- **[[spring] ](http://www.playframework.com/modules/spring) [Spring](http://github.com/pepite/Play--framework-Spring-module)** [](http://www.playframework.com/modules/spring)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.spring/play-spring) Allows to use Spring managed beans inside your play! 1.x applications.

### Language

- **[[googleclosure] ](http://www.playframework.com/modules/googleclosure) [Google Closure](http://code.google.com/p/mandubian-play-google-closure/)** [](http://www.playframework.com/modules/googleclosure) This module is aimed at integrating Google Closure tools with play!.
- **[[gwt] ](http://www.playframework.com/modules/gwt) [Google Web Toolkit](http://code.google.com/p/play-framework-gwt/)** [](http://www.playframework.com/modules/gwt) This module provides a helper to simplify the integration of a GWT UI with Play as an application server.
- **[[gwt2] ](http://www.playframework.com/modules/gwt2) [GWT2](http://github.com/vbuzzano/play-gwt2)** [](http://www.playframework.com/modules/gwt2) Integrates Play with GWT
- **[[scala] ](http://www.playframework.com/modules/scala) [Scala](http://www.playframework.com/modules/scala)** [](http://www.playframework.com/modules/scala)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.scala/play-scala) Play Scala enables you to use the Scala language for your application keeping key properties of the Play framework
- **[[scalagen] ](http://www.playframework.com/modules/scalagen) [Scala Gen](https://github.com/asinghal/Play-ScalaGen)** [](http://www.playframework.com/modules/scalagen) Scala code generators for the Play! framework
- **[[scalasecure] ](http://www.playframework.com/modules/scalasecure) [Scala secure](https://github.com/asinghal/Play-ScalaSecure)** [](http://www.playframework.com/modules/scalasecure) This module provides basic security (authentication/ authorization) for Play applications written in Scala.

### Messaging/events

- **[[akka] ](http://www.playframework.com/modules/akka) [Akka support](http://github.com/dwhitney/akka)** [](http://www.playframework.com/modules/akka) Allows you to configure [akka](http://akkasource.org) through The Play! framework’s conf/application.conf file.
- **[[camel] ](http://www.playframework.com/modules/camel) [Camel](https://github.com/marcuspocus/play-camel)** [](http://www.playframework.com/modules/camel) A EIP + Messaging module for the Play! Framework
- **[[pusher] ](http://www.playframework.com/modules/pusher) [Pusher](https://github.com/regisbamba/Play-Pusher)** [](http://www.playframework.com/modules/pusher) This module lets you easily add realtime functionality to your Play applications with [Pusher](http://www.pusher.com) using websockets.
- **[[rabbitmq] ](http://www.playframework.com/modules/rabbitmq) [RabbitMQ](http://geeks.aretotally.in/rabbitmq-module-for-play-framework)** [](http://www.playframework.com/modules/rabbitmq) RabbitMQ offers a highly available and scalable, and yet lightweight, messaging system.

### Monitoring

- **[[accesslog] ](http://www.playframework.com/modules/accesslog) [Accesslog](https://github.com/briannesbitt/play-accesslog)** [](http://www.playframework.com/modules/accesslog)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.accesslog/play-accesslog) A Play framework module that performs request logging similar to an access log file in nginx or apache.
- **[[betterlogs] ](http://www.playframework.com/modules/betterlogs) [BetterLogs](https://github.com/sgodbillon/BetterLogs)** [](http://www.playframework.com/modules/betterlogs) Enhances the default logs adding  the class and method names, where the log has been called, its signature, the file name and the line.
- **[[infoplay] ](http://www.playframework.com/modules/infoplay) [InfoPlay](http://code.google.com/p/infoplay/)** [](http://www.playframework.com/modules/infoplay) InfoPlay is a module which gives many informations like infophp in PHP language.
- **[[jpastats] ](http://www.playframework.com/modules/jpastats) [Jpastats](https://github.com/eamelink/play-jpastats/)** [](http://www.playframework.com/modules/jpastats) Record how many database queries were executed during a request
- **[[log4play] ](http://www.playframework.com/modules/log4play) [Log4Play](https://github.com/feliperazeek/log4play)** [](http://www.playframework.com/modules/log4play) Provides a log4j appender which publishes log entries to an EventStream
- **[play-hibernate-statistics]  [Hibernate statistics](https://github.com/francisdb/play-hibernate-statistics)** [](https://github.com/francisdb/play-hibernate-statistics) Displays MBean Hibernate statistics
- **[[playerrors] ](http://www.playframework.com/modules/playerrors) [Playerrors](https://github.com/marius0/playerrors)** [](http://www.playframework.com/modules/playerrors) Playerrors gathers and informs you about the errors in your production webapps, so you can fix them before your visitors get a chance to complain
- **[profiler]  [Mini-profiler](https://github.com/PerfectCarl/play-profiler)** [](https://github.com/PerfectCarl/play-profiler) Displays a mini profiler in your application
- **[[recordtracking] ](http://www.playframework.com/modules/recordtracking) [RecordTracking](https://github.com/omaroman/recordtracking)** [](http://www.playframework.com/modules/recordtracking) RecordTracking unobtrusively tracks the creation, updating and elimination events regarding to records.
- **[[statsd] ](http://www.playframework.com/modules/statsd) [Statsd](https://github.com/rkroll/play-statsd/)** [](http://www.playframework.com/modules/statsd) The module is a wrapper over [StatsD](https://github.com/etsy/statsd) which allow for dead simple statistic aggregation from within play.

### Persistence

- **[[associations] ](http://www.playframework.com/modules/associations) [Associations](https://github.com/pareis/play-associations)** [](http://www.playframework.com/modules/associations)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.associations/play-associations) This module reduces the code to manage bi-directional associations.
- **[[cream] ](http://www.playframework.com/modules/cream) [JCR for Play!](https://github.com/mfornos/Cream)** [](http://www.playframework.com/modules/cream) A module that seamlessly integrates Apache Jackrabbit(JCR 2.0) with Play framework
- **[[ebean] ](http://www.playframework.com/modules/ebean) [EBean ORM support](https://github.com/lyubo/play-ebean)** [](http://www.playframework.com/modules/ebean)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.ebean/play-ebean) Adds Ebean ORM to play!. Still in very experimental phase.
- **[[mongo] ](http://www.playframework.com/modules/mongo) [MongoDB](http://github.com/louth/play-mongo)** [](http://www.playframework.com/modules/mongo) Provides a simple, elegant solution for using models stored in mongodb. For a more complex use cases, please take a look at the morphia module.
- **[[morphia] ](http://www.playframework.com/modules/morphia) [MongoDB Integration](http://github.com/greenlaw110/play-morphia)** [](http://www.playframework.com/modules/morphia)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.morphia/play-morphia)[](http://github.com/greenlaw110/play-morphia) Seamlessly MongoDB access integration with Play’s Model interface.
- **[[mybatisplay] ](http://www.playframework.com/modules/mybatisplay) [MyBatisPlay](https://github.com/eamelink/play-navigation/wiki)** [](http://www.playframework.com/modules/mybatisplay) Provides support for MyBatis persistence framework.
- **[[neo4j] ](http://www.playframework.com/modules/neo4j) [logisima-neo4j](https://github.com/sim51/logisima-play-neo4j)** [](http://www.playframework.com/modules/neo4j) Integrate neo4j database into your play! project.
- **[[objectify] ](http://www.playframework.com/modules/objectify) [Objectify](http://code.google.com/p/play-framework-objectify/)** [](http://www.playframework.com/modules/objectify) Objectify is a flexible abstraction on Google App Engine/J which makes data access simple and elegant
- **[[orientdb] ](http://www.playframework.com/modules/orientdb) [OrientDB](https://github.com/mfornos/orientdb)** [](http://www.playframework.com/modules/orientdb) OrientDB for Play! Framework
- **[[redis] ](http://www.playframework.com/modules/redis) [Redis](https://github.com/tkral/play-redis)** [](http://www.playframework.com/modules/redis)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.redis/play-redis) The Redis Play! module helps you easily use Redis in your Play! applications
- **[[riak] ](http://www.playframework.com/modules/riak) [Riak](https://github.com/julienba/play-riak/)** [](http://www.playframework.com/modules/riak) Allow to use riak-java-client in play! way.
- **[[s3blobs] ](http://www.playframework.com/modules/s3blobs) [S3Blobs](https://github.com/jamesward/S3-Blobs-module-for-Play)** [](http://www.playframework.com/modules/s3blobs) The S3Blobs Play Framework Module provides an easy way to read an write files from Amazon S3 from within JPA entities.
- **[[siena] ](http://www.playframework.com/modules/siena) [Siena](http://github.com/mandubian/play-siena)** [](http://www.playframework.com/modules/siena)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.siena/play-siena)[](http://github.com/mandubian/play-siena) Enables Siena support to map your Java entities to GAE/MySQL/PostgreSQL/H2 from your play application
- **[[twig] ](http://www.playframework.com/modules/twig) [Twig](https://github.com/netmau5/Play-Twig)** [](http://www.playframework.com/modules/twig) Twig superpowers Google App Engine’s Datastore for Play applications. Get a fluid API, in-memory joins, and asynchronous queries out of the box.

### Presentation

- **[[coffee] ](http://www.playframework.com/modules/coffee) [CoffeeScript](https://github.com/robfig/play-coffee)** [](http://www.playframework.com/modules/coffee)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.coffee/play-coffee) CoffeeScript is a great way to produce javascript. This module provides support for it (Java and Scala).
- **[[excel] ](http://www.playframework.com/modules/excel) [Excel](http://github.com/greenlaw110/play-excel)** [](http://www.playframework.com/modules/excel)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.excel/play-excel) Template based Excel report generator
- **[[formee] ](http://www.playframework.com/modules/formee) [Formee](https://github.com/omaroman/formee)** [](http://www.playframework.com/modules/formee) Helps to write forms and add client and server side validation.
- **[[greenscript] ](http://www.playframework.com/modules/greenscript) [Minimize javascript/css files](http://github.com/greenlaw110/greenscript)** [](http://www.playframework.com/modules/greenscript) Play with your javascript/css files!
- **[[html5validation] ](http://www.playframework.com/modules/html5validation) [HTML5 Validation](https://github.com/oasits/play-html5-validation)** [](http://www.playframework.com/modules/html5validation) Client-side form validation based on your Play framework model annotations using HTML5 attributes.
- **[[jqueryui] ](http://www.playframework.com/modules/jqueryui) [Jqueryui](https://github.com/lunatech-labs/play-module-jqueryui)** [](http://www.playframework.com/modules/jqueryui) The jQuery UI module provides working examples of jQuery UI widgets, integrated with a Play application.
- **[[jqvalidate] ](http://www.playframework.com/modules/jqvalidate) [JQuery Validation](https://github.com/murz/play-jqvalidate)** [](http://www.playframework.com/modules/jqvalidate) Client-side form validation via jQuery, based on your model annotation
- **[[jqvalidation] ](http://www.playframework.com/modules/jqvalidation) [Jqvalidation](http://code.google.com/p/jqvalidate-play-framework/)** [](http://www.playframework.com/modules/jqvalidation) A jquery library API for validation, supports Ajax validation (per field or per form)
- **[[less] ](http://www.playframework.com/modules/less) [Less module](https://github.com/lunatech-labs/play-module-less)** [](http://www.playframework.com/modules/less)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.less/play-less) Converts [less](http://lesscss.org/) to CSS, and handles error reporting in your Play application
- **[[markdown] ](http://www.playframework.com/modules/markdown) [Markdown](https://github.com/orefalo/play-markdown)** [](http://www.playframework.com/modules/markdown)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.markdown/play-markdown) Easily bring markdown contents into your application.
- **[[menu] ](http://www.playframework.com/modules/menu) [Menu](http://github.com/greenlaw110/play-menu)** [](http://www.playframework.com/modules/menu) Eases the implementation of navigation menu.
- **[[navigation] ](http://www.playframework.com/modules/navigation) [Navigation](https://bitbucket.org/hlassiege/play-nemrod)** [](http://www.playframework.com/modules/navigation) Define and display navigation menus in your Play application.
- **[[paginate] ](http://www.playframework.com/modules/paginate) [Paginate](http://github.com/lmcalpin/Play--Paginate)** [](http://www.playframework.com/modules/paginate)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.paginate/play-paginate) A replacement for #{list} tags that allows for easy pagination.
- **[[pdf] ](http://www.playframework.com/modules/pdf) [PDF module](http://github.com/pepite/play--pdf)** [](http://www.playframework.com/modules/pdf)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.pdf/play-pdf) Renders PDF document from your HTML templates. This module is based on the YaHP Converter library.
- **[[pegdown] ](http://www.playframework.com/modules/pegdown) [PegDown Markdown](https://github.com/jagregory/play-pegdown)** [](http://www.playframework.com/modules/pegdown) Integrates the pegdown [Markdown](https://github.com/sirthias/pegdown) processor with your Play application
- **[[press] ](http://www.playframework.com/modules/press) [Minimize javascript/css files](http://github.com/dirkmc/press)** [](http://www.playframework.com/modules/press) A JavaScript, CSS and Less minimizer that is designed to be transparent to the application developer.
- **[[sass] ](http://www.playframework.com/modules/sass) [Syntactically Awesome Stylesheets](http://github.com/guillaumebort/play-sass)** [](http://www.playframework.com/modules/sass)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.sass/play-sass) Sass makes CSS fun again. Sass is CSS, plus nested rules, variables, mixins, and more, all in a concise, readable syntax.
- **[[table] ](http://www.playframework.com/modules/table) [Table](https://github.com/julienrf/play-table)** [](http://www.playframework.com/modules/table)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.table/play-table) Simplifies the code needed to display data in HTML tables.
- **[[tabularasa] ](http://www.playframework.com/modules/tabularasa) [Tabula Rasa](https://github.com/schaloner/tabula-rasa)** [](http://www.playframework.com/modules/tabularasa) Tabula Rasa provides support for user-customisable tables in views
- **[[twitterbootstrap] ](http://www.playframework.com/modules/twitterbootstrap) [Twitterbootstrap](http://www.playframework.com/modules/twitterbootstrap)** [](http://www.playframework.com/modules/twitterbootstrap) Bundles up the twitter-bootstrap stylekit and the play less plugin, easing the .less files edition (changes are dynamically taken into account).

### Rest

- **[[jersey] ](http://www.playframework.com/modules/jersey) [Jersey](https://bitbucket.org/psartini/play-jersey)** [](http://www.playframework.com/modules/jersey) Integrates Jersey into the Play! Framework.
- **[[resteasy] ](http://www.playframework.com/modules/resteasy) [RESTEasy Play! module](http://www.lunatech-labs.com/open-source/resteasy-play-module)** [](http://www.playframework.com/modules/resteasy) The RESTEasy Play! module allows you to define JAX-RS RESTful web services in the Play! Framework using RESTEasy.
- **[[resteasycrud] ](http://www.playframework.com/modules/resteasycrud) [RESTEasy CRUD module](http://www.lunatech-labs.com/open-source/resteasy-crud-play-module)** [](http://www.playframework.com/modules/resteasycrud) The Play! RESTEasy CRUD module which allows you to automagically generate your RESTful CRUD resources for a given model
- **[[swagger] ](http://www.playframework.com/modules/swagger) [Swagger](https://github.com/wordnik/swagger-play)** [](http://www.playframework.com/modules/swagger) Creates a self-documenting meta-description for REST APIs which allows for code-gen, UI-sandbox, and test framework.

### Scaffolding

- **[[crudsiena] ](http://www.playframework.com/modules/crudsiena) [CRUD for Siena](https://github.com/mandubian/play-crud-siena)** [](http://www.playframework.com/modules/crudsiena) Offers a fully usable web interface for your Siena Model objects with a few more features than default [crud] module.
- **[[mocha] ](http://www.playframework.com/modules/mocha) [Mocha](https://bitbucket.org/blobsmith/mocha/overview)** [](http://www.playframework.com/modules/mocha) An implementation of mocha UI javascript interface for Play!
- **[play-bootstrap]  [Basic bootstrap scaffolding](https://github.com/phaus/play-bootstrap)** [](https://github.com/phaus/play-bootstrap) Creating Bootstrap based applications (derived from the default [scaffold] module).
- **[[scaffold] ](http://www.playframework.com/modules/scaffold) [Scaffold](http://github.com/lmcalpin/Play--Scaffold)** [](http://www.playframework.com/modules/scaffold) Scaffold will generate basic scaffolding for bootstrapping a project from your JPA or Senia entities

### Search

- **[[elasticsearch] ](http://www.playframework.com/modules/elasticsearch) [ElasticSearch](http://geeks.aretotally.in/play-framework-module-elastic-search-distributed-searching-with-json-http-rest-or-java)** [](http://www.playframework.com/modules/elasticsearch) Elastic Search is a Distributed Search Solution based on Apache Lucene. This module provides an embedded Elastic Server instance for Rapid Development.
- **[[search] ](http://www.playframework.com/modules/search) [Search](http://github.com/jfp/play-search/)** [](http://www.playframework.com/modules/search)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.search/play-search) Search allows you to have basic full text search functionalities to your JPA Model. It is based on Lucene.

### Security

- **[[browserid] ](http://www.playframework.com/modules/browserid) [BrowserID](https://github.com/orefalo/play-browserid)** [](http://www.playframework.com/modules/browserid) BrowserID is an experimental new way of signing into websites. The goal with BrowserID is to design something safe and easy for users and the developers.
- **[[cas] ](http://www.playframework.com/modules/cas) [logisima-cas](http://github.com/sim51/logisima-play-cas)** [](http://www.playframework.com/modules/cas) This module is a CAS client for Play! application.
- **[[casino] ](http://www.playframework.com/modules/casino) [Casino](https://github.com/reyez/casino-play)** [](http://www.playframework.com/modules/casino) This project provides a simple method to integrate sign-up and password recovery to your project
- **[[deadbolt] ](http://www.playframework.com/modules/deadbolt) [Deadbolt](https://github.com/schaloner/deadbolt)** [](http://www.playframework.com/modules/deadbolt)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.deadbolt/play-deadbolt) Deadbolt is an authorisation mechanism for defining access rights to certain controller methods or parts of a view
- **[[fbconnect] ](http://www.playframework.com/modules/fbconnect) [Facebook connect](https://github.com/murz/play-fbconnect)** [](http://www.playframework.com/modules/fbconnect) Easily integrate Facebook based authentication into any Play framework application.
- **[[force] ](http://www.playframework.com/modules/force) [Force.com](https://github.com/jesperfj/play-force)** [](http://www.playframework.com/modules/force) Build Play! applications that integrates to Force.com. Provides OAuth authentication and REST API adapter.
- **[[linkedin] ](http://www.playframework.com/modules/linkedin) [LinkedIn OAuth Authentication](http://geeks.aretotally.in/projects/play-framework-linkedin-module)** [](http://www.playframework.com/modules/linkedin) Easily integrate LinkedIn’s OAuth authentication into your Play Framework application
- **[[oauth] ](http://www.playframework.com/modules/oauth) [OAuth Client](http://github.com/erwan/playoauthclient)** [](http://www.playframework.com/modules/oauth) This module provides tools to connect to an OAuth provider, such as Twitter or Google.
- **[[recaptcha] ](http://www.playframework.com/modules/recaptcha) [Recaptcha](https://github.com/orefalo/play-recaptcha)** [](http://www.playframework.com/modules/recaptcha)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.recaptcha/play-recaptcha) Quickly integrate reCaptcha.com challenge-response test in your applications.
- **[[securepermissions] ](http://www.playframework.com/modules/securepermissions) [Secure Permissions](http://www.lunatech-labs.com/open-source/secure-permissions-play-module)** [](http://www.playframework.com/modules/securepermissions) Extends the defaut secure module to add permission checks based on the rules in the Seam Framework (based on Drools rules).
- **[[securesocial] ](http://www.playframework.com/modules/securesocial) [SecureSocial](http://jaliss.github.com/securesocial/)** [](http://www.playframework.com/modules/securesocial)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.securesocial/play-securesocial) SecureSocial allows you to add an authentication UI to your app that works with services based on OAuth1, OAuth2, OpenID and OpenID+OAuth hybrid protocols
- **[[shibboleth] ](http://www.playframework.com/modules/shibboleth) [Shibboleth](https://github.com/TAMULib/Shibboleth-play)** [](http://www.playframework.com/modules/shibboleth) Allow users to login to your Play! application via Shibboleth.

### Template

- **[[fastergt] ](http://www.playframework.com/modules/fastergt) [Faster Groovy Templates](https://github.com/mbknor/faster-groovy-templates)** [](http://www.playframework.com/modules/fastergt)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.fastergt/play-fastergt) Replaces the default groovy template implementation with GT-Engine which is faster and uses less memory.
- **[[japid] ](http://www.playframework.com/modules/japid) [Japid Template Engine](http://github.com/branaway/Japid)** [](http://www.playframework.com/modules/japid)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.japid/play-japid) A pure Java-based fast statically typed template engine for the Play! framework version 1.2.x.
- **[[mustache] ](http://www.playframework.com/modules/mustache) [Mustache](https://github.com/murz/play-mustache)** [](http://www.playframework.com/modules/mustache) Allows you to define logic-less template snippets that can be used server-side in your Play! views as well as client-side in your JavaScript.
- **[[rythm] ](http://www.playframework.com/modules/rythm) [Rythm Template Engine](https://github.com/greenlaw110/play-rythm)** [](http://www.playframework.com/modules/rythm)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.rythm/play-rythm)[](https://github.com/greenlaw110/play-rythm) PlayRythm is a Razor like template engine.
- **[[scalate] ](http://www.playframework.com/modules/scalate) [Scalate](http://github.com/pk11/play-scalate)** [](http://www.playframework.com/modules/scalate) [Scalate](http://scalate.fusesource.org) Template engine support.
- **[[thymeleaf] ](http://www.playframework.com/modules/thymeleaf) [Thymeleaf](https://github.com/choreo/play-thymeleaf)** [](http://www.playframework.com/modules/thymeleaf) Play framework module to use [Thymeleaf 2.0](http://www.thymeleaf.org/)  as a template engine.

### Testing

- **[[cobertura] ](http://www.playframework.com/modules/cobertura) [Cobertura](http://github.com/julienba/play-cobertura)** [](http://www.playframework.com/modules/cobertura)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.cobertura/play-cobertura) Integrates with Cobertura to calculate the percentage of code accessed by tests (test coverage).
- **[[httpmock] ](http://www.playframework.com/modules/httpmock) [HttpMock](http://github.com/zenexity/play--httpmock)** [](http://www.playframework.com/modules/httpmock) Caches WebService requests to emulate them in order to overcome connection problems (lag, denial of service, HTTP errors) for fast developping.
- **[[mockito] ](http://www.playframework.com/modules/mockito) [Mockito](https://github.com/eamelink/play-mockito)** [](http://www.playframework.com/modules/mockito)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.mockito/play-mockito) Mockito is a mocking framework that tastes really good
- **[[qunit] ](http://www.playframework.com/modules/qunit) [QUnit](https://github.com/irregular-at/play-qunit)** [](http://www.playframework.com/modules/qunit)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.qunit/play-qunit) The QUnit module provides integration of JUnit Javascript tests with the Play! Framework.
- **[[spocktests] ](http://www.playframework.com/modules/spocktests) [Spock tests](http://github.com/peterlundberg/play-spock-tests)** [](http://www.playframework.com/modules/spocktests) Runs [Spock](https://code.google.com/p/spock/) specifications and to write BDD style tests (still wrapped as  junit) with the expressive power of groovy.
- **[[springtester] ](http://www.playframework.com/modules/springtester) [spring tester](https://github.com/digiarnie/springtester)** [](http://www.playframework.com/modules/springtester)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.springtester/play-springtester) Write tests that can auto-magically inject mocks (using Mockito) into Play applications wired up using the spring module.
- **[[tests] ](http://www.playframework.com/modules/tests) [Alternative Test module](https://github.com/GuyMograbi/play_test_module)** [](http://www.playframework.com/modules/tests) The Test Module for Play!Framework helps you write tests quicker, is a cleaner and reusable manner.
- **[[webdrive] ](http://www.playframework.com/modules/webdrive) [Webdrive](https://github.com/rkaippully/play-webdrive)** [](http://www.playframework.com/modules/webdrive)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.webdrive/play-webdrive) WebDrive module provides Selenium 2 testing support for Play framework

### Translation

- **[[i18ntools] ](http://www.playframework.com/modules/i18ntools) [I18ntools](http://github.com/naholyr/i18ntools)** [](http://www.playframework.com/modules/i18ntools) This module will add some tools to ease use of i18n in your Play! projects.
- **[[messages] ](http://www.playframework.com/modules/messages) [@messages](https://github.com/huljas/play-messages)** [](http://www.playframework.com/modules/messages)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.messages/play-messages) Module messages provides a web based tool for managing your application’s localizations.
- **[[nemrod] ](http://www.playframework.com/modules/nemrod) [Nemrod](https://github.com/sim51/logisima-play-neo4j)** [](http://www.playframework.com/modules/nemrod) This module helps to import and export translations from your application to a Nemrod instance automatically.
- **[play-i18ned]  [Play-i18ned](https://github.com/phaus/play-i18ned)** [](https://github.com/phaus/play-i18ned) Converts default i18n files from an Excel Sheet and the other way around.

### Misc

- **[[bespin] ](http://www.playframework.com/modules/bespin) [Bespin online editor](http://github.com/erwan/playbespin)** [](http://www.playframework.com/modules/bespin) Allows you to edit all the application sources directly in the browser using bespin, the web code editor.
- **[[bhave] ](http://www.playframework.com/modules/bhave) [Bhave](http://bhave.org/)** [](http://www.playframework.com/modules/bhave) Integrates with [bhave](http://bhave.org/), a web-based behavior driven development (BDD) framework, for web apps, done in a funky way!
- **[[cheese] ](http://www.playframework.com/modules/cheese) [Cheese](https://github.com/lmcalpin/Play--Cheese)** [](http://www.playframework.com/modules/cheese) Simplified API for integration your application with the CheddarGetter subscription management service.
- **[[cms] ](http://www.playframework.com/modules/cms) [Cms](http://code.google.com/p/play-cms/)** [](http://www.playframework.com/modules/cms) A very simple embedded CMS
- **[[cnm] ](http://www.playframework.com/modules/cnm) [Content Negotiation](http://github.com/oasits/play-content-negotiation)** [](http://www.playframework.com/modules/cnm) Helps using content types which are not directly supported by default such as VCard and Atom/RSS feeds using annotations.
- **[[externalconfig] ](http://www.playframework.com/modules/externalconfig) [External Config](https://github.com/rugbyhead/externalconfig)** [](http://www.playframework.com/modules/externalconfig) Allows easy loading of external config / properties files. This allows for easy configuration of an app deployed in a war.
- **[[featureflags] ](http://www.playframework.com/modules/featureflags) [Feature Flags](http://code.google.com/p/play-featureflags)** [](http://www.playframework.com/modules/featureflags) Enables you to easily use flags in your application that you can switch ON and OFF at runtime, using an admin screen.
- **[[googlecheckout] ](http://www.playframework.com/modules/googlecheckout) [Google Checkout](https://github.com/jagregory/play-google-checkout)** [](http://www.playframework.com/modules/googlecheckout) Enable your Play application to integrate with Google Checkout as a merchant.
- **[[gravatar] ](http://www.playframework.com/modules/gravatar) [Gravatar](https://github.com/mbarbieri/play-gravatar)** [](http://www.playframework.com/modules/gravatar)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.gravatar/play-gravatar) Integrate Gravatar into your Play application
- **[[hazelcast] ](http://www.playframework.com/modules/hazelcast) [Hazelcast](https://github.com/marcuspocus/hazelcast)** [](http://www.playframework.com/modules/hazelcast)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.hazelcast/play-hazelcast) Dropin replacement for EhCacheImpl or MemcachedImpl from Play
- **[[postmark] ](http://www.playframework.com/modules/postmark) [Postmark](https://github.com/FrostDigital/play-postmark)** [](http://www.playframework.com/modules/postmark)[](http://mvnrepository.com/artifact/com.google.code.maven-play-plugin.org.playframework.modules.postmark/play-postmark) Postmark module provides easy integration with postmarkapp.com for handling outgoing emails
- **[[useragentcheck] ](http://www.playframework.com/modules/useragentcheck) [UserAgentCheck](https://github.com/orefalo/play-useragentcheck)** [](http://www.playframework.com/modules/useragentcheck) UserAgentCheck displays a banner to notify users when their browser is outdated.
- **[[play1-chart] ](http://sant0s.github.io/play1-chart/) [Play1-Chart](https://github.com/sant0s/play1-chart)** [](https://github.com/sant0s/play1-chart) The Chart module allows for easy generation of chart images.
- [Mavenized modules](https://code.google.com/p/maven-play-plugin/wiki/MavenizedModules) and [how to use them](https://code.google.com/p/maven-play-plugin/wiki/Usage)
- [Using Play's controller](http://www.javabeat.net/using-controllers-in-play-framework/) with a nice roundup about caching, expiration and eTags
- Using [Luo](https://github.com/greenlaw110)'s `cache4` [annotation](http://www.playframework.com/modules/rythm-1.0.0-20121210/integration#cache4)

<!-- kb-related:start -->

## Related lists

More lists in the **Back-End Development** category of the [KEEBOX Library](index.md):

- [Pyramid](pyramid.md)
- [Reflex](reflex.md)
- [Slim](slim.md)
- [Symfony](symfony.md)
- [Kustomize](kustomize.md)
- [Lumen](lumen.md)
- [nginx](nginx.md)
- [OpenTofu](opentofu.md)

<!-- kb-related:end -->
