---
title: "Learning – Awesome List with 63 resources"
description: "63 curated Learning resources: Curated Learning resources."
---

# Learning

Curated Learning resources.

!!! info "Source"
    63 resources imported from [GustavBertram/awesome-common-lisp-learning](https://github.com/GustavBertram/awesome-common-lisp-learning), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Programming Languages**.

<!-- kb-about:start -->

## About this list

**Learning**. This page brings together 55 links about Learning, grouped into 7 sections. The largest sections are **Common Lisp Implementations**, **Online References**, **Online Books**, a good place to start if you are exploring the topic for the first time. It belongs to the **Programming Languages** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Lisp Environments** — 5 links
- **Online References** — 9 links
- **Online Books** — 9 links
- **Offline Books** — 7 links
- **Online Community** — 4 links
- **Library Management** — 4 links
- **Common Lisp Implementations** — 17 links

<!-- kb-about:end -->

## Lisp Environments

    - [Portacle](https://shinmera.github.io/portacle/) - A portable and multiplatform Common Lisp environment. It ships a slightly customized Emacs with SLIME, SBCL (a popular Common Lisp implementation), Quicklisp and Git. No installation needed, so it's a very quick and easy way to get going.
    - [Lispbox](https://common-lisp.net/project/lispbox/) - An IDE (Emacs + SLIME), Common Lisp implementation (Clozure Common Lisp) and library manager (Quicklisp), pre-packaged as archives for Windows, macOS and Linux. Descendant of "Lisp in a Box" [mentioned](http://www.gigamonkeys.com/book/lather-rinse-repeat-a-tour-of-the-repl.html) in Practical Common Lisp.
    - [Lispworks Personal Edition](http://www.lispworks.com/downloads/) - A non-Emacs based IDE for LispWorks Lisp, with some restrictions.
    - [Allegro Common Lisp](https://franz.com/products/allegrocl/) - Has a free [Express Edition](https://franz.com/downloads/clp/survey) IDE, and [training videos on YouTube](https://www.youtube.com/channel/UCN36UrxtyNBJPaG0kmBJNRw).
    - [Articulate Common Lisp](http://articulate-lisp.com) - A HOWTO for putting together a Lisp environment, and has information on [useful libraries](http://articulate-lisp.com/project/abcs.html) and how to [structure projects](http://articulate-lisp.com/project/new-project.html).
    - If you're an experienced [Emacs](https://www.gnu.org/software/emacs/) user, you can just install [SLIME](https://common-lisp.net/project/slime/) and a [supported Common Lisp implementation](https://common-lisp.net/project/slime/doc/html/Platforms.html#Platforms). See the [SLIME manual](https://common-lisp.net/project/slime/doc/html/) for more details.
    - The Common Lisp Cookbook has more information about [installing an implementation](https://lispcookbook.github.io/cl-cookbook/getting-started.html) using an implementation manager like [Roswell](https://github.com/roswell/roswell/wiki), or on Docker.

## Online References

- [The Common Lisp Hyperspec (CLHS)](http://www.lispworks.com/documentation/common-lisp.html) - *The* language reference document for Common Lisp. Bookmark it now.
    - [Chapter 7](http://www.lispworks.com/documentation/HyperSpec/Body/07_.htm) - Covers the Common Lisp Object System (CLOS).
- [The ANSI Common Lisp Standard Draft](http://cberr.us/tech_writings/notes/common_lisp_standard_draft.html) - The last draft version of the ANSI INCITS 226-1994 (previously ANSI X3.226-1994) standard.
- [The Common Lisp Cookbook](http://lispcookbook.github.io/cl-cookbook/) - A list of useful Lisp recipes. Also contains a list of other online sources of CL information.
- [Common Lisp the Language (2nd Edition) by Guy L. Steele](https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) - A description of the Common Lisp language from just before it was standardized by ANSI. Don't use it as a reference.
    - [Cliki on CLtL2](https://cliki.net/Getting+Started) - Claims it has more useful descriptions of [LOOP](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ai-repository/ai/html/cltl/clm/node235.html#SECTION003000000000000000000) and [FORMAT](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ai-repository/ai/html/cltl/clm/node200.html) than the CLHS does.
    - [Stack Overflow on CLtL2](https://stackoverflow.com/questions/108537/what-are-the-main-differences-between-cltl2-and-ansi-cl) - Some recommend using CLtL2 for insight and inspiration, but to use the CLHS when programming.
    - [A list of differences between CLtL2 and the ANSI Common Lisp specification.](http://linuxfinances.info/info/commonlisp.html#AEN9679)
    - [Chapter 28](https://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node260.html#SECTION003200000000000000000) - Covers the Common Lisp Object System.

## Online Books

- [Common Lisp: A Gentle Introduction to Symbolic Computation by David S. Touretzky](http://www.cs.cmu.edu/~dst/LispBook/) - a good introduction for people new to programming. Contains code for really useful utilities like [DTRACE](http://www.cs.cmu.edu/~dst/Lisp/dtrace/) and [SDRAW](http://www.cs.cmu.edu/~dst/Lisp/sdraw/).
- [Common Lisp: An interactive approach by Stuart C. Shapiro](https://www.cse.buffalo.edu/~shapiro/Commonlisp/) - A textbook that teaches mainly through the use of exercises.
- [Practical Common Lisp by Peter Seibel](http://www.gigamonkeys.com/book/) - A great introduction for experienced programmers, and tries to highlight from the very beginning what makes CL different to other languages.
- [Common Lisp Koans](https://github.com/google/lisp-koans) - Not exactly a book, but a set of koans to help you learn the language.
- [On Lisp by Paul Graham](http://www.paulgraham.com/onlisp.html) - A great book for intermediately experienced Lispers.
- [Let Over Lambda by Doug Hoyte](https://letoverlambda.com) - An advanced book on Lisp Macros.
    - [Comments on Let Over Lambda](https://www.reddit.com/r/lisp/comments/3actsc/let_over_lambda/) - Several people recommend that you be comfortable with On Lisp before reading this book, and that the start is slow.
    - [The chapter on closures](https://letoverlambda.com/index.cl/guest/chap2.html) - Has several non-trivial examples, and demonstrates the power of this feature.
- [Paradigms of Artificial Intelligence Programming by Peter Norvig](https://github.com/norvig/paip-lisp) - Has many interesting applications of Lisp, but is no longer a good reference for AI.

## Offline Books

- [Land of Lisp by Conrad Barski, MD](http://landoflisp.com) - A fun introduction to Lisp that uses comics and has you writing games.
    - Available as an [ebook](https://www.nostarch.com/lisp.htm).
    - Has an [errata page](http://landoflisp.com/errata.html).
- [ANSI Common Lisp by Paul Graham](http://www.paulgraham.com/acl.html) - Good as a reference, covers CLOS, and has several example program implementations.
    - Plaintext versions of [Chapter 1](http://lib.store.yahoo.net/lib/paulgraham/acl1.txt) and [Chapter 2](http://lib.store.yahoo.net/lib/paulgraham/acl2.txt) are available online.
- [Common Lisp Recipes by Edmund Weitz](http://weitz.de/cl-recipes/) - A great set of Common Lisp patterns.
- [Object-Oriented Programming in Common Lisp by Sonya E. Keene](https://www.amazon.com/Object-Oriented-Programming-COMMON-LISP-Programmers/dp/0201175894) - An in-depth description of the CLOS, and shows how to use it with example applications.
- [The Art of the Metaobject Protocol by Gregor Kiczales, Jim des Rivieres, and Daniel G. Bobrow](https://www.amazon.com/Art-Metaobject-Protocol-Gregor-Kiczales/dp/0262610744/) - Describes the CLOS Metaobject Protocol (MOP).
    - [Chapters 5 and 6 (available online)](http://metamodular.com/CLOS-MOP/) - The specification of a metaobject protocol extension to CLOS, by Robert Strandh.
        - Superseded by the [modern public domain CLOS MOP specification](https://clos-mop.hexstreamsoft.com/) by Jean-Philippe Paradis ([Hexstream](https://github.com/Hexstream)).
    - [Adam Tornhill on AMOP](http://www.adamtornhill.com/reviews/amop.htm) - Recommends reading Practical Common Lisp, then  Object-Oriented Programming in Common Lisp, and then AMOP.

## Online Community

- The [Cliki](http://cliki.net) - The Common Lisp Wiki. A great resource for all things CL. Has a great [Getting Started](http://cliki.net/Getting+Started) page and an extensive list of [Lisp books](http://cliki.net/Lisp%20books).
- The #clschool, #lisp, #ccl, #sbcl and [other rooms](https://www.cliki.net/IRC) on the [Libera.Chat](https://libera.chat/) network are great places for learning about Common Lisp. ([Freenode should be avoided.](https://gist.github.com/joepie91/df80d8d36cd9d1bde46ba018af497409))
- [Lisp Subreddit](http://www.reddit.com/r/lisp/) - An active community, and has loads of useful links and reference documents in the sidebar.
    - [Common Lisp Subreddit](https://www.reddit.com/r/Common_Lisp) - The Subreddit for Common Lisp.
- [Exercism's Common Lisp track](https://exercism.org/tracks/common-lisp) - An excellent way to learn the language through practice, have your code reviewed, and to discuss solutions with other people.
- [Lisp Discord server](https://discord.gg/7tSq5EaA6Z) - Is a Discord for Lisp. Has a channel dedicated to Common Lisp and will happily answer questions.

## Library Management

- [Quicklisp](https://www.quicklisp.org/beta) - A package management platform for Lisp libraries.
- [Quickdocs](http://quickdocs.org) - Documentation for projects in Quicklisp.
- [State of the Common Lisp Ecosystem, 2015](http://borretti.me/article/common-lisp-sotu-2015) - Article about what libraries you should use, and why.
- [Articulate Common Lisp](http://articulate-lisp.com/project/abcs.html) - Lists some useful libraries.

## Common Lisp Implementations

- [Allegro Common Lisp (ACL)](https://franz.com/products/allegrocl/) - Commercial, but has a free [Express Edition](https://franz.com/downloads/clp/survey).
    - [ACL manual](https://franz.com/support/documentation/)
    - [Training videos on YouTube](https://www.youtube.com/channel/UCN36UrxtyNBJPaG0kmBJNRw)
- [CLISP](https://clisp.sourceforge.io)
    - [CLISP Manual](https://clisp.sourceforge.io/impnotes.html)
- [Clozure Common Lisp (CCL)](https://ccl.clozure.com)
    - [CCL manual](https://ccl.clozure.com/manual/)
- [Carnegie Mellon University Common Lisp (CMUCL)](https://www.cons.org/cmucl/)
    - [CMUCL manual and other useful information](https://www.cons.org/cmucl/doc/index.html)
- [Embeddable Common Lisp (ECL)](https://common-lisp.net/project/ecl/)
    - [ECL manual](https://common-lisp.net/project/ecl/static/manual/)
- [LispWorks](http://www.lispworks.com/products/index.html) - Commercial, but as mentioned previously, has a [Personal Edition](http://www.lispworks.com/downloads/index.html) with minor limitations.
    - [LispWorks manual](http://www.lispworks.com/documentation/index.html)
- [Steel Bank Common Lisp (SBCL)](http://www.sbcl.org) - My personal favorite.
    - [SBCL manual](http://www.sbcl.org/manual/index.html)
- [Scieneer Common Lisp (SCL)](http://web.archive.org/web/20171014210404/http://www.scieneer.com/scl/) - A commercial Linux and Unix implementation, but has an unrestricted free evaluation and non-commercial use version.
    - [SCL manual](http://web.archive.org/web/20171014210404/http://www.scieneer.com/scl/doc/)

<!-- kb-related:start -->

## Related lists

More lists in the **Programming Languages** category of the [KEEBOX Library](index.md):

- [Learning](learning-2.md)
- [Lua](lua.md)
- [Mad Science npm Packages](mad-science-npm-packages.md)
- [MicroPython](micropython.md)
- [Functional Programming](functional-programming.md)
- [Imba](imba.md)
- [J2ME](j2me.md)
- [JavaScript](javascript.md)

<!-- kb-related:end -->
