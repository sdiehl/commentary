-   [GHC Source Code Abbreviations](#ghc-source-code-abbreviations)
-   [Aging in the generational GC](#aging-in-the-generational-gc)
-   [Improving LLVM Alias Analysis](#improving-llvm-alias-analysis)
    -   [LLVM Alias Analysis
        Infrastructure](#llvm-alias-analysis-infrastructure)
    -   [Max's Work](#maxs-work)
    -   [TBAA](#tbaa)
    -   [STG / Cmm Alias Properties](#stg-cmm-alias-properties)
    -   [How to Track TBAA information](#how-to-track-tbaa-information)
    -   [LLVM type system](#llvm-type-system)
    -   [Problems / Optmisations to
        Solve](#problems-optmisations-to-solve)
        -   [LLVM Optimisations](#llvm-optimisations)
        -   [Safe Loads
            (speculative load)](#safe-loads-speculative-load)
        -   [GHC Heap Check
            (case merging)](#ghc-heap-check-case-merging)
-   [GHC Commentary: The GHC API](#ghc-commentary-the-ghc-api)
    -   [Targets](#targets)
    -   [Dependency Analysis](#dependency-analysis)
    -   [The !ModSummary type](#the-modsummary-type)
    -   [Loading (compiling) the
        Modules](#loading-compiling-the-modules)
-   [GHC Commentary: Asynchronous
    Exceptions](#ghc-commentary-asynchronous-exceptions)
-   [GHC Commentary: Backends](#ghc-commentary-backends)
-   [Types in the back end (aka "The
    \`Rep\` swamp")](#types-in-the-back-end-aka-the-rep-swamp)
    -   [\`CmmType\`](#cmmtype)
    -   [The \`MachOp\` type](#the-machop-type)
    -   [Foreign calls and hints](#foreign-calls-and-hints)
    -   [Native code generation and the \`Size\`
        type](#native-code-generation-and-the-size-type)
-   [The Block Allocator](#the-block-allocator)
    -   [Structure of blocks](#structure-of-blocks)
-   [GHC Commentary: Garbage Collecting
    CAFs](#ghc-commentary-garbage-collecting-cafs)
    -   [Static Reference Tables](#static-reference-tables)
    -   [Evacuating Static Objects](#evacuating-static-objects)
-   [Calling Convention](#calling-convention)
-   [Return Convention](#return-convention)
    -   [Historical page](#historical-page)
-   [Cleanup after the new codegen is
    enabled](#cleanup-after-the-new-codegen-is-enabled)
    -   [Independent tasks](#independent-tasks)
    -   [Towards removing codeGen/Cg\*](#towards-removing-codegencg)
    -   [Towards removing \`OldCmm\`](#towards-removing-oldcmm)
    -   [Later](#later)
-   [Cmm: Implementing Exception
    Handling](#cmm-implementing-exception-handling)
    -   [An Integral Exception Example](#an-integral-exception-example)
    -   [A Floating Point Exception
        Example](#a-floating-point-exception-example)
    -   [Note To Reader](#note-to-reader)
-   [Table of Contents](#table-of-contents)
-   [The Cmm language](#the-cmm-language)
    -   [Additions in Cmm](#additions-in-cmm)
    -   [Compiling Cmm with GHC](#compiling-cmm-with-ghc)
    -   [Basic Cmm](#basic-cmm)
        -   [Code Blocks in Cmm](#code-blocks-in-cmm)
        -   [Variables, Registers and
            Types](#variables-registers-and-types)
        -   [Literals and Labels](#literals-and-labels)
        -   [Sections and Directives](#sections-and-directives)
        -   [Expressions](#expressions)
        -   [Statements and Calls](#statements-and-calls)
        -   [Operators and Primitive
            Operations](#operators-and-primitive-operations)
    -   [Cmm Design: Observations and Areas for Potential
        Improvement](#cmm-design-observations-and-areas-for-potential-improvement)
-   [GHC Commentary: What the hell is a \`.cmm\`
    file?](#ghc-commentary-what-the-hell-is-a-.cmm-file)
    -   [Reading references](#reading-references)
    -   [Other information](#other-information)
-   [Code Generator](#code-generator)
    -   [A brief history of code
        generator](#a-brief-history-of-code-generator)
    -   [Overview](#overview)
    -   [First stage: STG to Cmm
        conversion](#first-stage-stg-to-cmm-conversion)
    -   [Second stage: the Cmm pipeline](#second-stage-the-cmm-pipeline)
    -   [Dumping and debugging Cmm](#dumping-and-debugging-cmm)
    -   [Register Allocator Code](#register-allocator-code)
        -   [The register allocator](#the-register-allocator)
        -   [Graph coloring](#graph-coloring)
        -   [Miscellanea](#miscellanea)
-   [The GHC Commentary - Coding Style Guidelines for the
    compiler](#the-ghc-commentary---coding-style-guidelines-for-the-compiler)
    -   [General Style](#general-style)
    -   [Comments](#comments)
        -   [Comments on top-level
            entities](#comments-on-top-level-entities)
        -   [Comments in the source code](#comments-in-the-source-code)
        -   [Comments and examples](#comments-and-examples)
        -   [Longer comments or architectural
            commentary](#longer-comments-or-architectural-commentary)
        -   [Commit messages](#commit-messages)
    -   [Warnings](#warnings)
    -   [Exports and Imports](#exports-and-imports)
        -   [Exports](#exports)
        -   [Imports](#imports)
    -   [Compiler versions and language
        extensions](#compiler-versions-and-language-extensions)
        -   [](#section)
        -   [Literate Haskell](#literate-haskell)
        -   [The C Preprocessor (CPP)](#the-c-preprocessor-cpp)
        -   [Platform tests](#platform-tests)
    -   [Tabs vs Spaces](#tabs-vs-spaces)
-   [Coercions in GHC's core language](#coercions-in-ghcs-core-language)
    -   [Difficulties with the current
        approach](#difficulties-with-the-current-approach)
    -   [Main proposal](#main-proposal)
-   [Parsing of command line
    arguments](#parsing-of-command-line-arguments)
    -   [Static flags](#static-flags)
    -   [Dynamic flags](#dynamic-flags)
-   [The GHC Commentary](#the-ghc-commentary)
    -   [Editing the Commentary](#editing-the-commentary)
    -   [Contents](#contents)
    -   [Contributed Documentation](#contributed-documentation)
-   [Compiler and runtime system ways in
    GHC](#compiler-and-runtime-system-ways-in-ghc)
    -   [Available ways in a standard
        GHC](#available-ways-in-a-standard-ghc)
        -   [Ways for parallel execution on clusters and
            multicores](#ways-for-parallel-execution-on-clusters-and-multicores)
    -   [Combining ways](#combining-ways)
-   [Internals](#internals)
-   [GHC Commentary: The Compiler](#ghc-commentary-the-compiler)
    -   [Overall Structure](#overall-structure)
    -   [What problems do we need to
        solve?](#what-problems-do-we-need-to-solve)
    -   [Current mechanisms](#current-mechanisms)
    -   [New concepts for Backpack](#new-concepts-for-backpack)
    -   [Features](#features)
    -   [Constraints](#constraints)
-   [RTS Configurations](#rts-configurations)
    -   [Combinations](#combinations)
    -   [Other configuration options](#other-configuration-options)
-   [Contracts for Haskell](#contracts-for-haskell)
    -   [Involved](#involved)
    -   [Overview](#overview-1)
    -   [The plan](#the-plan)
    -   [Current status](#current-status)
    -   [Questions](#questions)
    -   [References](#references)
-   [The GHC Commentary: Coding Style Guidelines for RTS C
    code](#the-ghc-commentary-coding-style-guidelines-for-rts-c-code)
    -   [Comments](#comments-1)
    -   [References](#references-1)
    -   [Portability issues](#portability-issues)
        -   [Which C Standard?](#which-c-standard)
        -   [Other portability
            conventions](#other-portability-conventions)
    -   [Debugging/robustness tricks](#debuggingrobustness-tricks)
    -   [Syntactic details](#syntactic-details)
    -   [Inline functions](#inline-functions)
    -   [Source-control issues](#source-control-issues)
-   [Copying GC](#copying-gc)
-   [The type](#the-type)
    -   [Case expressions](#case-expressions)
    -   [Shadowing](#shadowing)
    -   [Human readable Core
        generation](#human-readable-core-generation)
-   [CPS Conversion](#cps-conversion)
    -   [Overview](#overview-2)
    -   [Design Aspects](#design-aspects)
    -   [Simple Design](#simple-design)
    -   [To be worked out](#to-be-worked-out)
    -   [Pipeline](#pipeline)
    -   [TODO](#todo)
    -   [Current Pipeline](#current-pipeline)
        -   [](#section-1)
    -   [Non-CPS Changes](#non-cps-changes)
    -   [Notes](#notes)
    -   [Loopholes](#loopholes)
        -   [GC Blocks](#gc-blocks)
        -   [Update Frames](#update-frames)
        -   [User defined continuations](#user-defined-continuations)
        -   [Branches to continuations](#branches-to-continuations)
    -   [Not in Scope of Current Work](#not-in-scope-of-current-work)
        -   [Static Reference Table
            Handling (SRT)](#static-reference-table-handling-srt)
        -   [Cmm Optimization assumed by
            CPS](#cmm-optimization-assumed-by-cps)
    -   [Notes on future development](#notes-on-future-development)
        -   [Handling GC](#handling-gc)
-   [The GHC Commentary: Data types and data
    constructors](#the-ghc-commentary-data-types-and-data-constructors)
    -   [Data types](#data-types)
-   [The life cycle of a data type](#the-life-cycle-of-a-data-type)
    -   [The constructor wrapper
        functions](#the-constructor-wrapper-functions)
    -   [The constructor worker
        functions](#the-constructor-worker-functions)
    -   [External Core](#external-core)
    -   [Unboxing strict fields](#unboxing-strict-fields)
    -   [Labels and info tables](#labels-and-info-tables)
-   [Demand analyser in GHC](#demand-analyser-in-ghc)
    -   [Demand signatures](#demand-signatures)
        -   [Demand descriptions](#demand-descriptions)
    -   [Worker-Wrapper split](#worker-wrapper-split)
    -   [Relevant compiler parts](#relevant-compiler-parts)
-   [Support for deriving , , and
    instances](#support-for-deriving-and-instances)
    -   [Example](#example)
    -   [Algorithm description](#algorithm-description)
        -   [](#section-2)
        -   [](#section-3)
        -   [](#section-4)
        -   [Covariant and contravariant
            positions](#covariant-and-contravariant-positions)
    -   [Requirements for legal
        instances](#requirements-for-legal-instances)
        -   [Relaxed universality check for
            ](#relaxed-universality-check-for)
    -   [Alternative strategy for deriving \`Foldable\` and
        \`Traversable\`](#alternative-strategy-for-deriving-foldable-and-traversable)
-   [LLVM Back-end Design](#llvm-back-end-design)
-   [Implementation](#implementation)
    -   [Framework](#framework)
    -   [LLVM Code Generation](#llvm-code-generation)
    -   [Register Pinning](#register-pinning)
    -   [Code Generation](#code-generation)
        -   [Unregisterised Vs.
            Registerised](#unregisterised-vs.-registerised)
    -   [!CmmData](#cmmdata)
        -   [1st Pass : Generation](#st-pass-generation)
    -   [!CmmStaticLit](#cmmstaticlit)
        -   [!CmmUninitialised](#cmmuninitialised)
        -   [!CmmAlign & !CmmDataLabel](#cmmalign-cmmdatalabel)
        -   [!CmmString](#cmmstring)
        -   [2nd Pass : Resolution](#nd-pass-resolution)
    -   [!CmmProc](#cmmproc)
-   [Desugaring instance
    declarations](#desugaring-instance-declarations)
    -   [Basic stuff](#basic-stuff)
    -   [Dictionary functions](#dictionary-functions)
    -   [The INLINE strategy](#the-inline-strategy)
    -   [The out-of-line (A) strategy](#the-out-of-line-a-strategy)
    -   [The out-of-line (B) strategy](#the-out-of-line-b-strategy)
    -   [User INLINE pragmas and
        out-of-line (A)](#user-inline-pragmas-and-out-of-line-a)
    -   [Summary](#summary)
-   [Bugs & Other Problems](#bugs-other-problems)
-   [Compiling more than one module at
    once](#compiling-more-than-one-module-at-once)
    -   [The overall driver](#the-overall-driver)
        -   [Dependency analysis](#dependency-analysis-1)
        -   [Recompilation checking and
            stability](#recompilation-checking-and-stability)
        -   [Compilation](#compilation)
-   [Eager Promotion](#eager-promotion)
-   [Eager Version Bumping Strategy](#eager-version-bumping-strategy)
-   [Data types for Haskell entities: , , , , and
    ](#data-types-for-haskell-entities-and)
    -   [Type variables and term
        variables](#type-variables-and-term-variables)
    -   [ and implict Ids](#and-implict-ids)
-   [HC files and the Evil Mangler](#hc-files-and-the-evil-mangler)
-   [Strictness analysis: examples](#strictness-analysis-examples)
-   [System FC: equality constraints and
    coercions](#system-fc-equality-constraints-and-coercions)
    -   [Coercions and Coercion Kinds](#coercions-and-coercion-kinds)
    -   [GADTs](#gadts)
    -   [Representation of coercion
        assumptions](#representation-of-coercion-assumptions)
    -   [Newtypes are coerced types](#newtypes-are-coerced-types)
    -   [Roles](#roles)
    -   [Simplification](#simplification)
-   [GHC Commentary: Runtime aspects of the
    FFI](#ghc-commentary-runtime-aspects-of-the-ffi)
    -   [Foreign Import "wrapper"](#foreign-import-wrapper)
-   [Function Calls](#function-calls)
    -   [Generic apply](#generic-apply)
-   [The Garbage Collector](#the-garbage-collector)
    -   [GC overview](#gc-overview)
    -   [GC data structures](#gc-data-structures)
        -   [generation](#generation)
        -   [nursery](#nursery)
-   [I know kung fu: learning STG by
    example](#i-know-kung-fu-learning-stg-by-example)
    -   [What is STG, exactly?](#what-is-stg-exactly)
    -   [An overview of the STG
        machine](#an-overview-of-the-stg-machine)
        -   [Components of the machine](#components-of-the-machine)
        -   [Important concepts in the
            machine](#important-concepts-in-the-machine)
        -   [Overview of execution model of the
            machine](#overview-of-execution-model-of-the-machine)
    -   [Saturated application to known
        functions](#saturated-application-to-known-functions)
        -   [Example 1: function application with sufficient stack
            space](#example-1-function-application-with-sufficient-stack-space)
        -   [Example 2: function application that needs to grow the
            stack](#example-2-function-application-that-needs-to-grow-the-stack)
    -   [Example 3: Unsaturated applications to known
        functions](#example-3-unsaturated-applications-to-known-functions)
    -   [Example 4: Applications to unknown
        functions](#example-4-applications-to-unknown-functions)
        -   [Dealing with generic
            application](#dealing-with-generic-application)
        -   [Making the call to the generic application
            code](#making-the-call-to-the-generic-application-code)
    -   [Example 5: oversaturated applications to known
        functions](#example-5-oversaturated-applications-to-known-functions)
    -   [Example 6: allocation of thunks and
        data](#example-6-allocation-of-thunks-and-data)
        -   [Checking for sufficient heap
            space](#checking-for-sufficient-heap-space)
        -   [Performing the actual
            allocation](#performing-the-actual-allocation)
        -   [Returning an allocated value to the
            caller](#returning-an-allocated-value-to-the-caller)
    -   [Example 7: \`case\` expressions](#example-7-case-expressions)
        -   [Forcing the scrutinee of the
            \`case\`](#forcing-the-scrutinee-of-the-case)
        -   [Dealing with the forced
            scrutinee](#dealing-with-the-forced-scrutinee)
    -   [Example 8: thunks and thunk
        update](#example-8-thunks-and-thunk-update)
        -   [Thunk entry point](#thunk-entry-point)
        -   [Continuation of the thunk](#continuation-of-the-thunk)
    -   [Conclusion](#conclusion)
-   [Support for generic programming](#support-for-generic-programming)
    -   [Status](#status)
    -   [Main components](#main-components)
    -   [Things that have been removed](#things-that-have-been-removed)
    -   [What already works](#what-already-works)
    -   [Testing](#testing)
-   [Kind polymorphic overhaul](#kind-polymorphic-overhaul)
    -   [Generic representation
        universe](#generic-representation-universe)
    -   [Universe interpretation](#universe-interpretation)
        -   [Names](#names)
    -   [Metadata representation](#metadata-representation)
    -   [Conversion between user datatypes and generic
        representation](#conversion-between-user-datatypes-and-generic-representation)
    -   [Example generic function: \`fmap\` (kind \`\*
        -&gt; \*\`)](#example-generic-function-fmap-kind--)
    -   [Example generic function: \`show\` (kind \`\*\`,
        uses metadata)](#example-generic-function-show-kind-uses-metadata)
    -   [Example datatype encoding: lists (derived by
        the compiler)](#example-datatype-encoding-lists-derived-by-the-compiler)
        -   [Digression](#digression)
    -   [GHC 8.0 and later](#ghc-8.0-and-later)
        -   [Type-level metadata
            encoding](#type-level-metadata-encoding)
        -   [Strictness](#strictness)
    -   [Source Tree Layout](#source-tree-layout)
    -   [Build System Basics](#build-system-basics)
    -   [Coding Style](#coding-style)
-   [The GHC Commentary: GHCi](#the-ghc-commentary-ghci)
    -   [Debugging the interpreter](#debugging-the-interpreter)
    -   [Useful stuff to know about the
        interpreter](#useful-stuff-to-know-about-the-interpreter)
        -   [Stack management](#stack-management)
        -   [Building constructors](#building-constructors)
        -   [Perspective](#perspective)
    -   [case returns between interpreted and compiled
        code](#case-returns-between-interpreted-and-compiled-code)
        -   [Returning to
            interpreted code.](#returning-to-interpreted-code.)
        -   [Returning to compiled code.](#returning-to-compiled-code.)
    -   [Unboxed tuples: a Right Royal Spanner In The
        Works](#unboxed-tuples-a-right-royal-spanner-in-the-works)
-   [Porting GHC using LLVM backend](#porting-ghc-using-llvm-backend)
    -   [Registerised Mode](#registerised-mode)
-   [Packages in GHC](#packages-in-ghc)
    -   [The problem](#the-problem)
    -   [Assumptions](#assumptions)
    -   [The open question](#the-open-question)
    -   [Plan A: GHC's current story](#plan-a-ghcs-current-story)
    -   [Plan B: package mounting](#plan-b-package-mounting)
    -   [Plan C: mention the package in the
        import](#plan-c-mention-the-package-in-the-import)
-   [Problems](#problems)
    -   [Breaking re-installations](#breaking-re-installations)
    -   [Type errors when using packages
        together](#type-errors-when-using-packages-together)
-   [Goals](#goals)
-   [Implementation Plan](#implementation-plan)
    -   [Persistent package store](#persistent-package-store)
    -   [Views](#views)
    -   [Consistent developer
        environment](#consistent-developer-environment)
    -   [Garbage collection](#garbage-collection)
    -   [cabal remove](#cabal-remove)
    -   [cabal upgrade](#cabal-upgrade)
    -   [Current Status](#current-status-1)
        -   [Unique Install Location](#unique-install-location)
        -   [ghc-pkg](#ghc-pkg)
        -   [Adhoc dependency resolution](#adhoc-dependency-resolution)
        -   [Detect whether an overwrite happens and warn about
            it](#detect-whether-an-overwrite-happens-and-warn-about-it)
        -   [Communicate the \`InstalledPackageId\` back to
            cabal-install](#communicate-the-installedpackageid-back-to-cabal-install)
        -   [Garbage Collection](#garbage-collection-1)
        -   [About Shadowing](#about-shadowing)
        -   [About Unique Identifier](#about-unique-identifier)
    -   [Original Plan](#original-plan)
    -   [Hashes and identifiers](#hashes-and-identifiers)
    -   [Install location of installed Cabal
        packages](#install-location-of-installed-cabal-packages)
        -   [Hash](#hash)
        -   [Unique number](#unique-number)
    -   [\`ghc-pkg\`](#ghc-pkg-1)
    -   [Simplistic dependency
        resolution](#simplistic-dependency-resolution)
    -   [Build flavours](#build-flavours)
        -   [The Cabal hash](#the-cabal-hash)
        -   [Released and Unreleased
            packages](#released-and-unreleased-packages)
    -   [Dependency resolution in
        cabal-install](#dependency-resolution-in-cabal-install)
    -   [Garbage Collection](#garbage-collection-2)
    -   [Currently open design
        decisions](#currently-open-design-decisions)
        -   [\`InstalledPackageId\` and install
            path](#installedpackageid-and-install-path)
        -   [Handling of dirty builds](#handling-of-dirty-builds)
        -   [Build flavours](#build-flavours-1)
        -   [\`InstalledPackageInfo\` and solver
            algorithm](#installedpackageinfo-and-solver-algorithm)
        -   [Simplistic dependency
            resolution](#simplistic-dependency-resolution-1)
    -   [Related topics](#related-topics)
        -   [Separating storage and selection of
            packages](#separating-storage-and-selection-of-packages)
        -   [First class environments](#first-class-environments)
    -   [Questions to remember](#questions-to-remember)
-   [The Haskell Execution Model](#the-haskell-execution-model)
-   [HEAP\_ALLOCED](#heap_alloced)
    -   [Speeding up \`HEAP\_ALLOCED()\`](#speeding-up-heap_alloced)
    -   [Eliminating \`HEAP\_ALLOCED\`
        completely](#eliminating-heap_alloced-completely)
        -   [Method 1: put static closures in an aligned
            section](#method-1-put-static-closures-in-an-aligned-section)
        -   [Method 2: copy static closures into a special area at
            startup](#method-2-copy-static-closures-into-a-special-area-at-startup)
-   [Heap and Stack checks](#heap-and-stack-checks)
-   [GHC Commentary: The Layout of Heap
    Objects](#ghc-commentary-the-layout-of-heap-objects)
    -   [Terminology](#terminology)
    -   [Heap Objects](#heap-objects)
    -   [Info Tables](#info-tables)
        -   [](#section-5)
    -   [Types of Payload Layout](#types-of-payload-layout)
        -   [Pointers-first layout](#pointers-first-layout)
        -   [Bitmap layout](#bitmap-layout)
    -   [Dynamic vs. Static objects](#dynamic-vs.-static-objects)
        -   [Dynamic objects](#dynamic-objects)
        -   [Static objects](#static-objects)
    -   [Types of object](#types-of-object)
        -   [Data Constructors](#data-constructors)
        -   [Function Closures](#function-closures)
        -   [Thunks](#thunks)
        -   [Selector thunks](#selector-thunks)
        -   [Partial applications](#partial-applications)
        -   [Generic application](#generic-application)
        -   [Stack application](#stack-application)
        -   [Indirections](#indirections)
        -   [Byte-code objects](#byte-code-objects)
        -   [Black holes](#black-holes)
        -   [Arrays](#arrays)
        -   [MVars](#mvars)
        -   [Weak pointers](#weak-pointers)
        -   [Stable Names](#stable-names)
        -   [Thread State Objects](#thread-state-objects)
        -   [STM objects](#stm-objects)
        -   [Forwarding Pointers](#forwarding-pointers)
    -   [How to add new heap objects](#how-to-add-new-heap-objects)
    -   [Change History](#change-history)
    -   [Speculation and Commentary](#speculation-and-commentary)
    -   [Record of performance improvements made to the Hoopl library
        starting January
        2012](#record-of-performance-improvements-made-to-the-hoopl-library-starting-january-2012)
-   [Haskell Program Coverage](#haskell-program-coverage)
    -   [Binary Tick Boxes](#binary-tick-boxes)
    -   [Machine Generated Haskell](#machine-generated-haskell)
-   [Compiling one module: !HscMain](#compiling-one-module-hscmain)
-   [The Diagram](#the-diagram)
-   [Picture of the main compiler
    pipeline](#picture-of-the-main-compiler-pipeline)
-   [The types](#the-types)
    -   [Decorating \`HsSyn\` with type
        information](#decorating-hssyn-with-type-information)
    -   [Source Locations](#source-locations)
-   [Interface files](#interface-files)
    -   [When is an interface file
        loaded?](#when-is-an-interface-file-loaded)
-   [Immix Garbage Collector](#immix-garbage-collector)
-   [The patches](#the-patches)
    -   [The main patch](#the-main-patch)
    -   [Line before inscreasing block
        size](#line-before-inscreasing-block-size)
    -   [Allocate in lines in minor
        GCs](#allocate-in-lines-in-minor-gcs)
    -   [Remove partial list](#remove-partial-list)
-   [To do](#to-do)
-   [GHC Source Tree Roadmap:
    includes/](#ghc-source-tree-roadmap-includes)
    -   [External APIs](#external-apis)
    -   [Derived Constants](#derived-constants)
    -   [Used when compiling via C](#used-when-compiling-via-c)
    -   [The RTS external APIs](#the-rts-external-apis)
    -   [Included into C-- (\`.cmm\`)
        code](#included-into-c---.cmm-code)
-   [Installing & Using the LLVM
    Back-end](#installing-using-the-llvm-back-end)
    -   [Installing](#installing)
    -   [LLVM Support](#llvm-support)
    -   [Using](#using)
    -   [Supported Platforms &
        Correctness](#supported-platforms-correctness)
    -   [Shared Libraries](#shared-libraries)
    -   [Performance](#performance)
-   [GHC Commentary:
    Libraries/Integer](#ghc-commentary-librariesinteger)
    -   [Selecting an Integer
        implementation](#selecting-an-integer-implementation)
    -   [The Integer interface](#the-integer-interface)
    -   [How Integer is handled inside
        GHC](#how-integer-is-handled-inside-ghc)
-   [An Integrated Code Generator for
    GHC](#an-integrated-code-generator-for-ghc)
    -   [Design elements](#design-elements)
    -   [Design philosophy](#design-philosophy)
    -   [Proposed compilation pipeline](#proposed-compilation-pipeline)
        -   [Convert from STG to control flow
            graph](#convert-from-stg-to-control-flow-graph)
        -   [Instruction selection](#instruction-selection)
        -   [Optimisation](#optimisation)
        -   [Proc-point analysis](#proc-point-analysis)
        -   [Register allocation](#register-allocation)
        -   [Stack layout](#stack-layout)
        -   [Tidy up](#tidy-up)
    -   [Machine-dependence](#machine-dependence)
-   [GHC Commentary: The byte-code interpreter and dynamic
    linker](#ghc-commentary-the-byte-code-interpreter-and-dynamic-linker)
    -   [Linker](#linker)
    -   [Bytecode Interpreter](#bytecode-interpreter)
-   [The I/O Manager](#the-io-manager)
-   [Key data types](#key-data-types)
-   [Kinds](#kinds)
    -   [Representing kinds](#representing-kinds)
    -   [Kind subtyping](#kind-subtyping)
-   [Linearity](#linearity)
-   [Ticky](#ticky)
    -   [Declarations for ticky
        counters](#declarations-for-ticky-counters)
-   [Strictness and let-floating](#strictness-and-let-floating)
-   [Coercions](#coercions)
-   [WARN: arity /](#warn-arity)
-   [Explaining demand transformers](#explaining-demand-transformers)
-   [Nofib stuff](#nofib-stuff)
-   [GHC Commentary: Libraries](#ghc-commentary-libraries)
-   [Building packages that GHC doesn't depend
    on](#building-packages-that-ghc-doesnt-depend-on)
-   [Classifying boot packages](#classifying-boot-packages)
    -   [Required or optional](#required-or-optional)
    -   [Coupling to GHC](#coupling-to-ghc)
    -   [Zero-boot packages](#zero-boot-packages)
    -   [Installation](#installation)
-   [Boot packages dependencies](#boot-packages-dependencies)
    -   [WARNING: Pattern matching in \`ghc-prim\`, \`integer-simple\`,
        and
        \`integer-gmp\`](#warning-pattern-matching-in-ghc-prim-integer-simple-and-integer-gmp)
-   [Repositories](#repositories)
-   [The LLVM backend](#the-llvm-backend)
-   [Loopification](#loopification)
-   [LLVM Mangler](#llvm-mangler)
    -   [TABLES\_NEXT\_TO\_CODE (TNTC)](#tables_next_to_code-tntc)
    -   [Stack Alignment](#stack-alignment)
    -   [SIMD / AVX](#simd-avx)
-   [Migrating Old Commentary](#migrating-old-commentary)
    -   [Before the Show Begins](#before-the-show-begins)
    -   [Genesis](#genesis)
    -   [The Beast Dissected](#the-beast-dissected)
    -   [RTS & Libraries](#rts-libraries)
    -   [Extensions, or Making a Complicated System More
        Complicated](#extensions-or-making-a-complicated-system-more-complicated)
-   [The Marvellous Module Structure of
    GHC](#the-marvellous-module-structure-of-ghc)
    -   [Compilation order is as
        follows:](#compilation-order-is-as-follows)
    -   [Typechecker stuff](#typechecker-stuff)
    -   [!HsSyn stuff](#hssyn-stuff)
    -   [Library stuff: base package](#library-stuff-base-package)
    -   [High-level Dependency Graph](#high-level-dependency-graph)
-   [Module Types](#module-types)
    -   [Module](#module)
    -   [!ModIface](#modiface)
    -   [!ModDetails](#moddetails)
        -   [!ModGuts](#modguts)
    -   [!ModSummary](#modsummary)
    -   [!HomeModInfo](#homemodinfo)
    -   [!HomePackageTable](#homepackagetable)
    -   [!ExternalPackageState](#externalpackagestate)
-   [Multi-instance packages](#multi-instance-packages)
    -   [!ToDo list](#todo-list)
    -   [Next step: dealing with ways](#next-step-dealing-with-ways)
-   [The type](#the-type-1)
    -   [The of a Name](#the-of-a-name)
    -   [Entities and ](#entities-and)
-   [Native Code Generator (NCG)](#native-code-generator-ncg)
    -   [Files, Parts](#files-parts)
    -   [Overview](#overview-3)
        -   [Translation into the Stix
            representation](#translation-into-the-stix-representation)
        -   [Instruction selection](#instruction-selection-1)
        -   [Register allocation](#register-allocation-1)
        -   [Spilling](#spilling)
        -   [Dealing with common cases
            fast](#dealing-with-common-cases-fast)
    -   [Complications, observations, and possible
        improvements](#complications-observations-and-possible-improvements)
        -   [Real vs virtual registers in the instruction
            selectors](#real-vs-virtual-registers-in-the-instruction-selectors)
    -   [Selecting insns for 64-bit values/loads/stores on 32-bit
        platforms](#selecting-insns-for-64-bit-valuesloadsstores-on-32-bit-platforms)
    -   [Shortcomings and inefficiencies in the register
        allocator](#shortcomings-and-inefficiencies-in-the-register-allocator)
        -   [Redundant reconstruction of the control flow
            graph](#redundant-reconstruction-of-the-control-flow-graph)
        -   [Really ridiculous method for doing
            spilling](#really-ridiculous-method-for-doing-spilling)
        -   [Redundant-move support for revised instruction selector
            suggestion](#redundant-move-support-for-revised-instruction-selector-suggestion)
    -   [x86 arcana that you should know
        about](#x86-arcana-that-you-should-know-about)
    -   [Generating code for ccalls](#generating-code-for-ccalls)
    -   [Duplicate implementation for many STG
        macros](#duplicate-implementation-for-many-stg-macros)
    -   [How to debug the NCG without losing your
        sanity/hair/cool](#how-to-debug-the-ncg-without-losing-your-sanityhaircool)
    -   [Historical page](#historical-page-1)
-   [Overview of modules in the new code
    generator](#overview-of-modules-in-the-new-code-generator)
    -   [The new Cmm data type](#the-new-cmm-data-type)
    -   [Module structure of the new code
        generator](#module-structure-of-the-new-code-generator)
        -   [Basic datatypes and
            infrastructure](#basic-datatypes-and-infrastructure)
        -   [Analyses and
            transformations](#analyses-and-transformations)
        -   [Linking the pipeline](#linking-the-pipeline)
        -   [Dead code](#dead-code)
    -   [Historical page](#historical-page-2)
-   [Design of the new code
    generator](#design-of-the-new-code-generator)
    -   [Overview](#overview-4)
    -   [The Cmm pipeline](#the-cmm-pipeline)
        -   [Branches to continuations and the "Adams
            optimisation"](#branches-to-continuations-and-the-adams-optimisation)
    -   [Runtime system](#runtime-system)
-   [NOTE: Historical page](#note-historical-page)
-   [Stupidity in the New Code
    Generator](#stupidity-in-the-new-code-generator)
    -   [Cantankerous Comparisons](#cantankerous-comparisons)
    -   [Dead stack/heap checks](#dead-stackheap-checks)
    -   [Instruction reordering](#instruction-reordering)
    -   [Stack space overuse](#stack-space-overuse)
    -   [Double temp-use means no
        inlinining?](#double-temp-use-means-no-inlinining)
    -   [Stupid spills](#stupid-spills)
    -   [Noppy proc-points](#noppy-proc-points)
    -   [Lots of temporary variables](#lots-of-temporary-variables)
    -   [Double proc points](#double-proc-points)
    -   [Rewriting stacks](#rewriting-stacks)
    -   [Spilling Hp/Sp](#spilling-hpsp)
    -   [Up and Down](#up-and-down)
    -   [Sp is generally stupid](#sp-is-generally-stupid)
    -   [Heap and R1 aliasing](#heap-and-r1-aliasing)
    -   [Historical page](#historical-page-3)
-   [GHC's glorious new code
    generator](#ghcs-glorious-new-code-generator)
    -   [Workflow for the new code generator and
        Hoopl](#workflow-for-the-new-code-generator-and-hoopl)
    -   [Status report April 2011](#status-report-april-2011)
-   [Old Code Generator (prior to
    GHC 7.8)](#old-code-generator-prior-to-ghc-7.8)
    -   [Storage manager
        representations](#storage-manager-representations)
    -   [Generated Cmm Naming
        Convention](#generated-cmm-naming-convention)
    -   [Modules](#modules)
        -   [](#section-6)
        -   [](#section-7)
        -   [](#section-8)
        -   [](#section-9)
        -   [](#section-10)
        -   [Memory and Register
            Management](#memory-and-register-management)
        -   [Function Calls and Parameter
            Passing](#function-calls-and-parameter-passing)
        -   [Misc utilities](#misc-utilities)
        -   [Special runtime support](#special-runtime-support)
-   [Ordering the Core-to-Core optimisation
    passes](#ordering-the-core-to-core-optimisation-passes)
    -   [This ordering obeys all the constraints
        except (5)](#this-ordering-obeys-all-the-constraints-except-5)
    -   [Constraints](#constraints-1)
        -   [1. float-in before strictness](#float-in-before-strictness)
        -   [2. Don't simplify between float-in and
            strictness](#dont-simplify-between-float-in-and-strictness)
        -   [3. Want full-laziness before
            foldr/build](#want-full-laziness-before-foldrbuild)
        -   [4. Want strictness after
            foldr/build](#want-strictness-after-foldrbuild)
        -   [5. Want full laziness after
            strictness](#want-full-laziness-after-strictness)
        -   [6. Want float-in after
            foldr/build](#want-float-in-after-foldrbuild)
        -   [7. Want simplify after
            float-inwards](#want-simplify-after-float-inwards)
        -   [8. If full laziness is ever done after
            strictness](#if-full-laziness-is-ever-done-after-strictness)
        -   [9. Ignore-inline-pragmas flag for final
            simplification](#ignore-inline-pragmas-flag-for-final-simplification)
        -   [10. Run Float Inwards once more after
            strictness-simplify](#run-float-inwards-once-more-after-strictness-simplify)
-   [Overall organisation of GHC](#overall-organisation-of-ghc)
-   [GHC source code](#ghc-source-code)
-   [Updates](#updates)
    -   [Unique](#unique)
    -   [Redesign (2014)](#redesign-2014)
-   [The data type and its friends](#the-data-type-and-its-friends)
    -   [Views of types](#views-of-types)
    -   [The representation of ](#the-representation-of)
    -   [Overloaded types](#overloaded-types)
    -   [Classifying types](#classifying-types)
-   [Package Compatibility](#package-compatibility)
    -   [1. Don't reorganise packages](#dont-reorganise-packages)
    -   [2. Provide older version(s) of base with a new GHC
        release](#provide-older-versions-of-base-with-a-new-ghc-release)
    -   [4. Allow packages to re-export
        modules](#allow-packages-to-re-export-modules)
    -   [4.1 Provide backwards-compatible versions of
        base](#provide-backwards-compatible-versions-of-base)
    -   [4.2 Rename base, and provide a compatibility
        wrapper](#rename-base-and-provide-a-compatibility-wrapper)
    -   [4.3 Don't rename base](#dont-rename-base)
    -   [5. Do some kind of provides/requires interface in
        Cabal](#do-some-kind-of-providesrequires-interface-in-cabal)
        -   [5.1 Make API specifications more
            symmetric](#make-api-specifications-more-symmetric)
        -   [5.2 Make API specifications
            explicit](#make-api-specifications-explicit)
        -   [5.3 Make API specifications more
            specific](#make-api-specifications-more-specific)
    -   [6. Distributions at the Hackage
        level](#distributions-at-the-hackage-level)
    -   [7. Allow package overlaps](#allow-package-overlaps)
    -   [The problem of lax version
        dependencies](#the-problem-of-lax-version-dependencies)
-   [Note about this page](#note-about-this-page)
-   [Explicit package imports](#explicit-package-imports)
    -   [Is the 'from <package>' compulsory?](#is-the-from-compulsory)
    -   [Package versions](#package-versions)
    -   [Importing from the home
        package](#importing-from-the-home-package)
    -   [The 'as P' alias](#the-as-p-alias)
    -   [Qualified names](#qualified-names)
    -   [Exporting modules from other
        packages](#exporting-modules-from-other-packages)
    -   [Syntax](#syntax)
        -   [Syntax formalised and
            summarised](#syntax-formalised-and-summarised)
        -   [Proposal for Package
            Mounting](#proposal-for-package-mounting)
        -   [Evaluation](#evaluation)
        -   [Note on Package Grafting](#note-on-package-grafting)
    -   [Alternative Proposal for Packages (with
        explicit namespaces)](#alternative-proposal-for-packages-with-explicit-namespaces)
    -   [A different, but related,
        problem](#a-different-but-related-problem)
    -   [Proposal](#proposal)
        -   [Naming a namespace](#naming-a-namespace)
        -   [What namespaces are available by
            default?](#what-namespaces-are-available-by-default)
        -   [Namespace resolution](#namespace-resolution)
        -   [Syntax](#syntax-1)
        -   [Exports](#exports-1)
        -   [Implicit imports](#implicit-imports)
        -   [Exposed vs Hidden packages](#exposed-vs-hidden-packages)
        -   [What if you wanted to import A.B.C from P1 and A.B.C from
            P2 into the *same*
            module?](#what-if-you-wanted-to-import-a.b.c-from-p1-and-a.b.c-from-p2-into-the-same-module)
-   [Package Reorg](#package-reorg)
    -   [Goals](#goals-1)
    -   [Proposal](#proposal-1)
        -   [What is in the Core
            Packages?](#what-is-in-the-core-packages)
        -   [Requirements to libraries to be included in core
            set](#requirements-to-libraries-to-be-included-in-core-set)
        -   [The base package](#the-base-package)
        -   [Other packages](#other-packages)
    -   [Testing](#testing-1)
    -   [Implementation-specific notes](#implementation-specific-notes)
        -   [Notes about GHC](#notes-about-ghc)
        -   [Notes about Hugs](#notes-about-hugs)
-   [Commentary: The Package System](#commentary-the-package-system)
    -   [Architecture](#architecture)
    -   [Identifying Packages](#identifying-packages)
    -   [Design constraints](#design-constraints)
    -   [The Plan](#the-plan-1)
        -   [Detecting ABI
            incompatibility](#detecting-abi-incompatibility)
        -   [Allowing ABI compatibilty](#allowing-abi-compatibilty)
-   [The Parser](#the-parser)
    -   [Principles](#principles)
    -   [Avoiding right-recursion](#avoiding-right-recursion)
    -   [Indentation](#indentation)
    -   [Syntax extensions](#syntax-extensions)
-   [Pinned Objects](#pinned-objects)
-   [Overview](#overview-5)
-   [The driver pipeline](#the-driver-pipeline)
-   [The compiler pipeline](#the-compiler-pipeline)
-   [Video](#video)
-   [Platforms](#platforms)
    -   [Limitations](#limitations)
    -   [Macros](#macros)
-   [Pointer Tagging](#pointer-tagging-1)
    -   [Meaning of the tag bits](#meaning-of-the-tag-bits)
    -   [Optimisations enabled by tag
        bits](#optimisations-enabled-by-tag-bits)
    -   [Garbage collection with tagged
        pointers](#garbage-collection-with-tagged-pointers)
    -   [Invariants](#invariants)
    -   [Compacting GC](#compacting-gc)
    -   [Dealing with tags in the code](#dealing-with-tags-in-the-code)
-   [Position-Independent Code and Dynamic
    Linking](#position-independent-code-and-dynamic-linking)
    -   [How to access symbols](#how-to-access-symbols)
    -   [CLabel.labelDynamic](#clabel.labeldynamic)
    -   [Info Tables](#info-tables-1)
    -   [Imported labels in
        SRTs (Windows)](#imported-labels-in-srts-windows)
    -   [PIC and dynamic linking support in the
        NCG](#pic-and-dynamic-linking-support-in-the-ncg)
    -   [How things are done on different
        platforms](#how-things-are-done-on-different-platforms)
        -   [Position dependent code](#position-dependent-code)
        -   [Position independent code](#position-independent-code)
    -   [Linking on ELF](#linking-on-elf)
    -   [Mangling dynamic library
        names](#mangling-dynamic-library-names)
-   [GHC Commentary: The C code
    generator](#ghc-commentary-the-c-code-generator)
    -   [Header files](#header-files)
    -   [Prototypes](#prototypes)
-   [Primitive Operations (!PrimOps)](#primitive-operations-primops)
    -   [The primops.txt.pp file](#the-primops.txt.pp-file)
    -   [Implementation of !PrimOps](#implementation-of-primops)
        -   [Inline !PrimOps](#inline-primops)
        -   [Out-of-line !PrimOps](#out-of-line-primops)
        -   [Foreign out-of-line !PrimOps and \`foreign import
            prim\`](#foreign-out-of-line-primops-and-foreign-import-prim)
    -   [Adding a new !PrimOp](#adding-a-new-primop)
-   [Profiling](#profiling)
    -   [Cost-centre profiling](#cost-centre-profiling)
    -   [Ticky-ticky profiling](#ticky-ticky-profiling)
-   [, , and ](#and)
    -   [The \`Module\` and \`ModuleName\`
        types](#the-module-and-modulename-types)
    -   [The type](#the-type-2)
-   [Recompilation Avoidance](#recompilation-avoidance)
    -   [What is recompilation
        avoidance?](#what-is-recompilation-avoidance)
    -   [Example](#example-2)
    -   [Why do we need recompilation
        avoidance?](#why-do-we-need-recompilation-avoidance)
        -   [GHCi and \`--make\`](#ghci-and---make)
        -   [\`make\`](#make)
    -   [How does it work?](#how-does-it-work)
        -   [Deciding whether to
            recompile](#deciding-whether-to-recompile)
        -   [Example](#example-3)
        -   [How does fingerprinting
            work?](#how-does-fingerprinting-work)
        -   [Mutually recursive groups of
            entities](#mutually-recursive-groups-of-entities)
        -   [Fixities](#fixities)
        -   [Instances](#instances)
        -   [Orphans](#orphans)
        -   [Rules](#rules)
        -   [On ordering](#on-ordering)
        -   [Packages](#packages)
        -   [Package version changes](#package-version-changes)
    -   [Interface stability](#interface-stability)
-   [The Register Allocator](#the-register-allocator-1)
    -   [Overview](#overview-6)
    -   [Code map](#code-map)
    -   [References](#references-2)
    -   [Register pressure in Haskell
        code](#register-pressure-in-haskell-code)
    -   [Hacking/Debugging](#hackingdebugging)
    -   [Runtime performance](#runtime-performance)
    -   [Possible Improvements](#possible-improvements)
-   [Haskell Excecution: Registers](#haskell-excecution-registers)
-   [Relevant GHC parts for Demand Analysis
    results](#relevant-ghc-parts-for-demand-analysis-results)
-   [Remembered Sets](#remembered-sets)
    -   [Remembered set maintenance during
        mutation](#remembered-set-maintenance-during-mutation)
        -   [Thunk Updates](#thunk-updates)
        -   [Mutable objects: MUT\_VAR,
            MVAR](#mutable-objects-mut_var-mvar)
        -   [Arrays: MUT\_ARR\_PTRS](#arrays-mut_arr_ptrs)
        -   [Threads: TSO](#threads-tso)
    -   [Remembered set maintenance during
        GC](#remembered-set-maintenance-during-gc)
-   [The renamer](#the-renamer)
    -   [The global renamer environment,
        ](#the-global-renamer-environment)
    -   [Unused imports](#unused-imports)
    -   [Name Space Management](#name-space-management)
    -   [Rebindable syntax](#rebindable-syntax)
-   [Replacing the Native Code
    Generator](#replacing-the-native-code-generator)
-   [Resource Limits](#resource-limits)
    -   [Code generation changes](#code-generation-changes)
        -   [Dynamic closure allocation](#dynamic-closure-allocation)
        -   [CAF Allocation](#caf-allocation)
        -   [Thunk code](#thunk-code)
        -   [Foreign calls](#foreign-calls)
    -   [Case split](#case-split)
    -   [Front-end changes](#front-end-changes)
-   [Garbage Collection Roots](#garbage-collection-roots)
-   [GHC Source Tree Roadmap: rts/](#ghc-source-tree-roadmap-rts)
    -   [Subdirectories of rts/](#subdirectories-of-rts)
    -   [Haskell Execution](#haskell-execution)
    -   [The \[wiki:Commentary/Rts/Storage Storage
        Manager\]](#the-wikicommentaryrtsstorage-storage-manager)
    -   [Data Structures](#data-structures)
    -   [The \[wiki:Commentary/Rts/Scheduler
        Scheduler\]](#the-wikicommentaryrtsscheduler-scheduler)
    -   [C files: the \[wiki:Commentary/Rts/FFI
        FFI\]](#c-files-the-wikicommentaryrtsffi-ffi)
    -   [The \[wiki:Commentary/Rts/Interpreter Byte-code
        Interpreter\]](#the-wikicommentaryrtsinterpreter-byte-code-interpreter)
    -   [\[wiki:Commentary/Profiling
        Profiling\]](#wikicommentaryprofiling-profiling)
    -   [RTS Debugging](#rts-debugging)
    -   [The Front Panel](#the-front-panel)
    -   [Other](#other)
    -   [OLD stuff](#old-stuff)
-   [Sanity Checking](#sanity-checking)
-   [The Scheduler](#the-scheduler)
    -   [OS Threads](#os-threads)
    -   [Haskell threads](#haskell-threads)
-   [Seq magic](#seq-magic)
    -   [The baseline position](#the-baseline-position)
        -   [Problem 1 (Trac \#1031)](#problem-1-trac-1031)
        -   [Problem 2 (Trac \#2273)](#problem-2-trac-2273)
        -   [Problem 3 (Trac \#5262)](#problem-3-trac-5262)
        -   [Problem 4: seq in the IO
            monad](#problem-4-seq-in-the-io-monad)
        -   [Problem 5: the need for special
            rules](#problem-5-the-need-for-special-rules)
-   [A better way](#a-better-way)
-   [The GHC Commentary: Signals](#the-ghc-commentary-signals)
    -   [Signal handling in the RTS](#signal-handling-in-the-rts)
        -   [The timer signal](#the-timer-signal)
    -   [The interrupt signal](#the-interrupt-signal)
    -   [Signal handling in Haskell
        code](#signal-handling-in-haskell-code)
    -   [RTS Alarm Signals and Foreign
        Libraries](#rts-alarm-signals-and-foreign-libraries)
-   [Slop](#slop)
    -   [Why do we want to avoid slop?](#why-do-we-want-to-avoid-slop)
    -   [How does slop arise?](#how-does-slop-arise)
    -   [What do we do about it?](#what-do-we-do-about-it)
-   [Layout of important files and
    directories](#layout-of-important-files-and-directories)
    -   [Files in \`\$(TOP)\`](#files-in-top)
    -   [\`libraries/\`](#libraries)
    -   [\`compiler/\`, \`docs/\`, \`ghc/\`](#compiler-docs-ghc)
    -   [\`rts/\`](#rts)
    -   [\`includes/\`](#includes)
    -   [\`utils/\`, \`libffi/\`](#utils-libffi)
    -   [\`driver/\`](#driver)
    -   [\`ghc-tarballs/\` (Windows only)](#ghc-tarballs-windows-only)
    -   [\`testsuite/\`, \`nofib/\`](#testsuite-nofib)
    -   [\`mk/\`, \`rules/\`](#mk-rules)
    -   [\`distrib/\`](#distrib)
    -   [Stuff that appears only in a build
        tree](#stuff-that-appears-only-in-a-build-tree)
        -   [\`inplace/\`](#inplace)
        -   [\`.../dist\*/\`](#dist)
    -   [Stack Layout](#stack-layout-1)
        -   [Representing Stack Slots](#representing-stack-slots)
        -   [Laying out the stack](#laying-out-the-stack)
        -   [A greedy algorithm](#a-greedy-algorithm)
-   [Layout of the stack](#layout-of-the-stack)
    -   [Info tables for stack frames](#info-tables-for-stack-frames)
    -   [Layout of the payload](#layout-of-the-payload)
    -   [Kinds of Stack Frame](#kinds-of-stack-frame)
-   [The STG syntax data types](#the-stg-syntax-data-types)
-   [GHC Commentary: Software Transactional
    Memory (STM)](#ghc-commentary-software-transactional-memory-stm)
-   [Background](#background)
    -   [Definitions](#definitions)
        -   [Useful RTS terms](#useful-rts-terms)
        -   [Transactional Memory terms](#transactional-memory-terms)
-   [Overview of Features](#overview-of-features)
    -   [Reading and Writing](#reading-and-writing)
    -   [Blocking](#blocking)
    -   [Choice](#choice)
    -   [Data Invariants](#data-invariants)
    -   [Exceptions](#exceptions)
-   [Overview of the Implementation](#overview-of-the-implementation)
    -   [Transactions that Read
        and Write.](#transactions-that-read-and-write.)
        -   [Transactional Record](#transactional-record)
        -   [Starting](#starting)
        -   [Reading](#reading)
        -   [Writing](#writing)
        -   [Validation](#validation)
        -   [Committing](#committing)
        -   [Aborting](#aborting)
        -   [Exceptions](#exceptions-1)
    -   [Blocking with ](#blocking-with)
    -   [Choice with ](#choice-with)
    -   [Invariants](#invariants-1)
        -   [Details](#details)
        -   [Changes from Choice](#changes-from-choice)
    -   [Other Details](#other-details)
        -   [Detecting Long Running
            Transactions](#detecting-long-running-transactions)
        -   [Transaction State](#transaction-state)
        -   [GC and ABA](#gc-and-aba)
        -   [Management of s](#management-of-s)
        -   [Tokens and Version Numbers.](#tokens-and-version-numbers.)
        -   [Implementation Invariants](#implementation-invariants)
        -   [Fine Grain Locking](#fine-grain-locking)
    -   [Bibliography](#bibliography)
-   [GHC Commentary: Storage](#ghc-commentary-storage)
-   [General overview](#general-overview)
-   [IMPORTANT NOTE](#important-note)
-   [The demand analyzer](#the-demand-analyzer)
    -   [Important datatypes](#important-datatypes)
-   [Symbol Names](#symbol-names)
    -   [Tuples](#tuples)
    -   [Unboxed Tuples](#unboxed-tuples)
    -   [Alphanumeric Characters](#alphanumeric-characters)
    -   [Constructor Characters](#constructor-characters)
    -   [Variable Characters](#variable-characters)
    -   [Other](#other-1)
    -   [Examples](#examples)
-   [The monad for renaming, typechecking,
    desugaring](#the-monad-for-renaming-typechecking-desugaring)
-   [Kirsten's sketchy notes on getting ticky to
    work](#kirstens-sketchy-notes-on-getting-ticky-to-work)
-   [The GHC Commentary: Checking
    Types](#the-ghc-commentary-checking-types)
    -   [The Overall Flow of Things](#the-overall-flow-of-things)
        -   [Entry Points Into the Type
            Checker](#entry-points-into-the-type-checker)
        -   [Renaming and Type Checking a
            Module](#renaming-and-type-checking-a-module)
    -   [Type Checking a Declaration
        Group](#type-checking-a-declaration-group)
    -   [Type checking Type and Class
        Declarations](#type-checking-type-and-class-declarations)
    -   [More Details](#more-details)
        -   [Types Variables and Zonking](#types-variables-and-zonking)
        -   [Type Representation](#type-representation)
        -   [Type Checking Environment](#type-checking-environment)
        -   [Expressions](#expressions-1)
        -   [Handling of Dictionaries and Method
            Instances](#handling-of-dictionaries-and-method-instances)
    -   [Connection with GHC's Constraint
        Solver](#connection-with-ghcs-constraint-solver)
    -   [Generating Evidence](#generating-evidence)
    -   [The Solver](#the-solver)
        -   [Given Constraints](#given-constraints)
        -   [Derived Constraints](#derived-constraints)
        -   [Wanted Constraints](#wanted-constraints)
-   [The data type and its friends](#the-data-type-and-its-friends-1)
    -   [Views of types](#views-of-types-1)
    -   [The representation of ](#the-representation-of-1)
    -   [Overloaded types](#overloaded-types-1)
    -   [Classifying types](#classifying-types-1)
    -   [Unique](#unique-1)
    -   [Current design](#current-design)
        -   [Known-key things](#known-key-things)
        -   [Interface files](#interface-files-1)
    -   [Redesign (2014)](#redesign-2014-1)
-   [Unpacking primitive fields](#unpacking-primitive-fields)
    -   [Goals and non-goals](#goals-and-non-goals)
    -   [Detailed design](#detailed-design)
    -   [Benchmarks](#benchmarks)
-   [Unused imports](#unused-imports-1)
    -   [The current story](#the-current-story)
    -   [Examples](#examples-1)
    -   [Specfication](#specfication)
    -   [Implementation](#implementation-1)
    -   [Algorithm](#algorithm)
-   [Updates](#updates-1)
-   [The user manual](#the-user-manual)
-   [GHC Boot Library Version
    History](#ghc-boot-library-version-history)
-   [GHC Commentary: Weak Pointers and
    Finalizers](#ghc-commentary-weak-pointers-and-finalizers)
-   [Work in Progress on the LLVM
    Backend](#work-in-progress-on-the-llvm-backend)
    -   [LLVM IR Representation](#llvm-ir-representation)
    -   [TABLES\_NEXT\_TO\_CODE](#tables_next_to_code-1)
    -   [LLVM Alias Analysis Pass](#llvm-alias-analysis-pass)
    -   [Optimise LLVM for the type of Code GHC
        produces](#optimise-llvm-for-the-type-of-code-ghc-produces)
    -   [Update the Back-end to use the new Cmm data types / New Code
        Generator](#update-the-back-end-to-use-the-new-cmm-data-types-new-code-generator)
    -   [LLVM's Link Time Optimisations](#llvms-link-time-optimisations)
    -   [LLVM Cross Compiler / Port](#llvm-cross-compiler-port)
    -   [Get rid of Proc Point
        Splitting](#get-rid-of-proc-point-splitting)
    -   [Don't Pass Around Dead STG
        Registers](#dont-pass-around-dead-stg-registers)
-   [Wired-in and known-key things](#wired-in-and-known-key-things)
    -   [Wired-in things](#wired-in-things)
    -   [Known-key things](#known-key-things-1)
    -   [Initialisation](#initialisation)
    -   [\`Orig\` \`RdrName\` things](#orig-rdrname-things)
-   [GHC Commentary: The Word](#ghc-commentary-the-word)

GHC Source Code Abbreviations
=============================

Certain abbreviations are used pervasively throughout the GHC source
code. This page gives a partial list of them and their expansion:

-   **ANF**: A-normal form

<!-- -->

-   **CAF**: Constant Applicative Form

<!-- -->

-   **Class**: Type Class

<!-- -->

-   **Cmm**: The final IR used in GHC, based on the C-- language

<!-- -->

-   **Core**: GHC core language. Based on System FC (variant of
    System F). Represents a type-checked and desugared program in some
    (out of several) intermediate compilation step

<!-- -->

-   **CoreFV**: Free variables in core

<!-- -->

-   **!CoreLint**: Type and sanity-checking of core. (Lint: Jargon for a
    program analysis that looks for bug-suspicious code.)

<!-- -->

-   **!CoreSubst**: Substitution in core

<!-- -->

-   **!CoreSyn**: Core abstract syntax

<!-- -->

-   **!DataCon**: Data constructor

<!-- -->

-   **Ds**: Desugarer

<!-- -->

-   **Gbl**: Global

<!-- -->

-   **Hs**: Haskell Syntax (generally as opposed to Core, for example,
    Expr vs !HsExpr)

<!-- -->

-   **Hsc**: Haskell compiler. Means it Deals with compiling a single
    module and no more.

<!-- -->

-   **!HsSyn**: Haskell abstract syntax

<!-- -->

-   **Id**: Synonym for Var, but indicating a term variable

<!-- -->

-   **Iface**: Interface, as in Haskell interface (.hi) files

<!-- -->

-   **!IfaceSyn**: Interface abstract syntax

<!-- -->

-   **LHs**: Located Haskell something

<!-- -->

-   **Loc**: Location, as in !SrcLoc

<!-- -->

-   **Located**: Something annotated with a !SrcSpan

<!-- -->

-   **Lcl**: Local

<!-- -->

-   **nativeGen**: Native code generator (generates assembly from Cmm)

<!-- -->

-   **Occ**: Occurrence

` * However, in the context of `[`OccName`](http://hackage.haskell.org/trac/ghc/wiki/Commentary/Compiler/RdrNameType#TheOccNametype)`, "occurrence" actually means "classified (i.e. as a type name, value name, etc) but not qualified and not yet resolved"`

-   **PId**: Package ID

<!-- -->

-   **!PprCore**: Pretty-printing core

<!-- -->

-   **Rdr**: Parser (or reader)

<!-- -->

-   **Rn**: Rename or Renamer

<!-- -->

-   **Rts**: Run Time System

<!-- -->

-   **!SimplCore**: Simplify core (the so-called simplifier belongs to
    this, as does the strictness analyser)

<!-- -->

-   **!SrcLoc**: Source location (filename, line number,
    character position)

<!-- -->

-   **!SrcSpan**: Source location span (filename, start line number and
    character position, end line number and character position)

<!-- -->

-   **STG**: \[Commentary/Compiler/StgSynType Spineless Tagless
    G-machine\]

<!-- -->

-   **Tc**: !TypeCheck{ing,er}

<!-- -->

-   **TSO**: [Thread State
    Object](https://ghc.haskell.org/trac/ghc/wiki/Commentary/Rts/Storage/HeapObjects#ThreadStateObjects)

<!-- -->

-   **!TyCon**: Type constructor

<!-- -->

-   **!TyThing**: Something that is type-checkable

<!-- -->

-   **Ty**: Type

<!-- -->

-   **!TyVar**: Synonym for Var, but indicating a type variable

<!-- -->

-   **Var**: A variable with some information about its type (or kind)

Aging in the generational GC
============================

Aging is an important technique in generational GC: the idea is that
objects that have only recently been allocated have not had sufficient
chance to die, and so promoting them immediately to the next generation
may lead to retention of unnecessary data. The problem is amplified if
the prematurely promoted objects are thunks that are subsequently
updated, leading to retention of an arbitrary amount of live data until
the next collection of the old generation, which may be a long time
coming.

The idea is that instead of promoting live objects directly from
generation 0 into generation 1, they stay in generation 0 for a "while",
and if they live long enough, they get promoted. The simplest way is to
segment the objects in generation 0 by the number of collections they
have survived, up to a maximum. GHC 6.12 used to do this: each
generation had a tunable number of *steps*. Objects were initially
promoted to step 0, copied through each subsequent step on following GC
cycles, and then eventually promoted to the next generation.

Measurement we made showed that the optimal number of steps was
somewhere between 1 and 3 (2 was almost always better than either 1 or
3). In priniciple it is possible to have a fractional number of steps,
although GHC 6.12 only supported integral numbers.

In GHC 6.13 and later, we made the following change: each block now
points to the generation to which objects in that block will be copied
in the next GC (the \`dest\` field of \`bdescr\`). This lets us decide
on a block-by-block basis which objects to promote and which to retain
in a generation, and lets us implement fractional numbers of steps. At
the same time, we dropped the notion of explicit steps, so each
generation just has a single list of blocks. This means that we can no
longer do aging of more than 2 GC cycles, but since the measurements
showed that this was unlikely to be beneficial, and the new structure is
much simpler, we felt it was worthwhile.

Blocks in the nursery have a \`dest\` field pointing to generation 0,
and blocks of live objects in generation 0 have a \`dest\` field
pointing to generation 1. This gives us the same effect as 2 steps did
in the GHC 6.12, except that intermediate generations (e.g. gen 1 in a
3-gen setup) now only have one step rather than 2. We could implement
aging in the intermediate generations too if that turns out to be
beneficial (more than 2 generations is rarely better than 2, according
to our measurements).

Improving LLVM Alias Analysis
=============================

This page tracks the information and progress relevant to improving the
alias analysis pass for the LLVM backend of GHC.

This correspond to bug \#5567.

LLVM Alias Analysis Infrastructure
----------------------------------

Some links to the various documentation on LLVM's AA support:

`* `[`LLVM` `Alias` `Analysis`
`Infrastructure`](http://llvm.org/docs/AliasAnalysis.html)\
`* `[`LLVM's` `Analysis` `and` `Transform`
`Passes`](http://llvm.org/docs/Passes.html)\
`* `[`The` `Often` `Misunderstood` `GEP`
`Instruction`](http://llvm.org/docs/GetElementPtr.html)\
`* `[`LLVM` `Language` `Reference`](http://llvm.org/docs/LangRef.html)\
`* `[`LLVM` `Dev` `List:` `Comparison` `of` `Alias` `Analysis` `in`
`LLVM`](http://groups.google.com/group/llvm-dev/browse_thread/thread/2a5944692508bcc2/363c96bb1c6a506d?show_docid=363c96bb1c6a506d&pli=1)

Max's Work
----------

Max had a crack at writing a custom alias analysis pass for LLVM,
relevant links are:

`* `[`Email` `to` `LLVM`
`dev`](http://lists.cs.uiuc.edu/pipermail/llvmdev/2011-September/043603.html)\
`* `[`Blog` `post` `about`
`results`](http://blog.omega-prime.co.uk/?p=135)\
`* `[`A` `port` `to` `LLVM`
`3.6`](https://github.com/bgamari/ghc-llvm-analyses)

TBAA
----

LLVM as of version 2.9 includes Type Based Alias Analysis. This mean
using metadata you can specify a type hierarchy (with alias properties
between types) and annotate your code with these types to improve the
alias information. This should allow us to improve the alias analysis
without any changes to LLVM itself like Max made.

`* `[`LLVM` `TBBA` `Doc`](http://llvm.org/docs/LangRef.html#tbaa)

STG / Cmm Alias Properties
--------------------------

**Question** (David Terei): What alias properties does the codegen obey?
Sp and Hp never alias? R<n> registers never alias? ....

**Answer** (Simon Marlow): Sp\[\] and Hp\[\] never alias, R\[\] never
aliases with Sp\[\], and that's about it.

*' Simon*': As long as it propagates properly, such that every F(Sp) is
a stack pointer, where F() is any expression context except a
dereference. That is, we better be sure that

is "stack", not "heap".

How to Track TBAA information
-----------------------------

Really to be sound and support Cmm in full we would need to track and
propagate TBAA information. It's Types after all! At the moment we
don't. We simply rely on the fact that the Cmm code generated for loads
and stores is nearly always in the form of:

That is to say, it has the values it depends on for the pointer
derivation in-lined in the load or store expression. It is very rarely
of the form:

And when it is, 'it is' (unconfirmed) always deriving a "heap" pointer,
"stack" pointers are always of the in-line variety. This assumption if
true allows us to look at just a store or load in isolation to properly
Type it.

There are two ways to type this 'properly'.

1\. Do data flow analysis. This is the only proper way to do it but also
annoying. 2. Do block local analysis. Instead of doing full blow data
flow analysis, just track the type of pointers stored to CmmLocal regs
at the block level. This is safe but just may miss some opportunities
when a CmmLocal's value is assigned in another block... My hunch is this
is quite rare so this method should be fairly effective (and easier to
implement and quicker to run that 1.)

LLVM type system
----------------

The above aliasing information can be encoded as follows:

The fact that \`R\[\]\` never aliases with \`Sp\[\]\` is never used as
the one way relation isn't expressible in LLVM.

Stores/loads needs to be annotated with \`!tbaa\` and one of the above
four types e.g.

Problems / Optmisations to Solve
--------------------------------

### LLVM Optimisations

Roman reported that running 'opt -std-compile-opts' gives much better
code than running 'opt -O3'.

**Following is from Roman Leschinskiy**

'-O2 -std-compile-opts' does the trick but it's obviously overkill
because it essentially executes the whole optimisation pipeline twice.
The crucial passes seem to be loop rotation and loop invariant code
motion. These are already executed twice by -O2 but it seems that they
don't have enough information then and that something interesting
happens in later passes which allows them to work much better the third
time.

### Safe Loads (speculative load)

We want to allow LLVM to speculatively hoist loads out of conditional
blocks. Relevant LLVM source code is here:

`* `[`SimplifyCFG` `Source`
`Code`](http://llvm.org/docs/doxygen/html/SimplifyCFG_8cpp_source.html)\
`* `[`llvm::isSafeToSpeculativelyExecute`](http://llvm.org/docs/doxygen/html/namespacellvm.html#a4899ff634bf732c16dd22ecfdafdea7d)\
`* `[`LLVM` `Mailing` `List` `Discussion` `about` `'Safe`
`loads'`](http://lists.cs.uiuc.edu/pipermail/llvmdev/2012-January/046958.html)

**Following is from Roman Leshchinskiy**

I've poked around a bit and things are rather complicated. So far I've
identified two problems. Here is a small example function:

This is the interesting C-- bit:

Look at what indexDoubleArray\# compiles to: F64\[I32\[Sp + 12\] + ((R1
&lt;&lt; 3) + 8)\]. We would very much like LLVM to hoist the
I32\[Sp+12\] bit (i.e., loading the pointer to the ByteArray data) out
of the loop because that might allow all sorts of wonderful optimisation
such as promoting it to a register. But alas, this doesn't happen, LLVM
leaves the load in the loop. Why? Because it assumes that the load might
fail (for instance, if Sp is NULL) and so can't move it past
conditionals. We know, of course, that this particular load can't fail
and so can be executed speculatively but there doesn't seem to be a way
of communicating this to LLVM.

As a quick experiment, I hacked LLVM to accept "safe" annotations on
loads and then manually annotated the LLVM assembly generated by GHC and
that helped quite a bit. I suppose that's the way to go - we'll have to
get this into LLVM in some form and then the backend will have to
generate those annotations for loads which can't fail. I assume they are
loads through the stack pointer and perhaps the heap pointer unless
we're loading newly allocated memory (those loads can't be moved past
heap checks). In any case, the stack pointer is the most important
thing. I can also imagine annotating pointers (such as Sp) rather than
instructions but that doesn't seem to be the LLVM way and it's also less
flexible.

### GHC Heap Check (case merging)

See bug \#1498

**Following is from Roman Leshchinskiy**

I investigated heap check a bit more and it seems to me that it's
largely GHC's fault. LLVM does do loop unswitching which correctly pulls
out loop-invariant heap checks but that happens fairly late in its
pipeline and heap checks interfere with optimisations before that.

However, we really shouldn't be generating those heap checks in the
first place. Here is a small example loop:

This is the C-- that GHC generates:

Note how in each loop iteration, we add 12 to Hp, then do the heap check
and then subtract 12 from Hp again. I really don't think we should be
generating that and then relying on LLVM to optimise it away.

This happens because GHC commons up heap checks for case alternatives
and does just one check before evaluating the case. The relevant comment
from CgCase.lhs is this:

A more interesting situation is this:

where !x! indicates a possible heap-check point. The heap checks in the
alternatives **can** be omitted, in which case the topmost heapcheck
will take their worst case into account.

This certainly makes sense if A allocates. But with vector-based code at
least, a lot of the time neither A nor C will allocate **and** C will
tail-call A again so by pushing the heap check into !A!, we are now
doing it **in** the loop rather than at the end.

It seems to me that we should only do this if A actually allocates and
leave the heap checks in the alternatives if it doesn't (perhaps we
could also use a common heap check if **all** alternatives allocate). I
tried to hack this and see what happens but found the code in CgCase and
friends largely incomprehensible. What would I have to change to
implement this (perhaps controlled by a command line flag) and is it a
good idea at all?

GHC Commentary: The GHC API
===========================

This section of the commentary describes everything between
\[wiki:Commentary/Compiler/HscMain HscMain\] and the front-end; that is,
the parts of GHC that coordinate the compilation of multiple modules.

The GHC API is rather stateful; the state of an interaction with GHC is
stored in an abstract value of type . The only fundamental reason for
this choice is that the models the state of the RTS's linker, which must
be single-threaded.

Although the GHC API apparently supports multiple clients, because each
can be interacting with a different , in fact it only supports one
client that is actually executing code, because the
\[wiki:Commentary/Rts/Interpreter\#Linker RTS linker\] has a single
global symbol table.

This part of the commentary is not a tutorial on *using* the GHC API:
for that, see [Using GHC as a
Library](http://haskell.org/haskellwiki/GHC/As_a_library). Here we are
going to talk about the implementation.

A typical interaction with the GHC API goes something like the
following:

`* You probably want to wrap the whole program in `` to get error messages`\
`* Create a new session: `\
`* Set the flags: ``, ``.`\
`* Add some `*`targets`*`: ``, ``, `\
`* Perform `[`ref(Dependency`
`Analysis)`](ref(Dependency_Analysis) "wikilink")`: `\
`* Load (compile) the source files: `

Warning: Initializing GHC is tricky! Here is a template that seems to
initialize GHC and a session. Derived from ghc's Main.main function.

You must pass the path to as an argument to .

The field of tells the compiler what kind of output to generate from
compilation. There is unfortunately some overlap between this and the
passed to ; we hope to clean this up in the future, but for now it's
probably a good idea to make sure that these two settings are consisent.
That is, if , then , if then .

Targets
-------

The targets specify the source files or modules at the top of the
dependency tree. For a Haskell program there is often just a single
target , but for a library the targets would consist of every visible
module in the library.

The type is defined in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink").
Note that a includes not just the file or module name, but also
optionally the complete source text of the module as a : this is to
support an interactive development environment where the source file is
being edited, and the in-memory copy of the source file is to be used in
preference to the version on disk.

Dependency Analysis
-------------------

The dependency analysis phase determines all the Haskell source files
that are to be compiled or loaded in the current session, by traversing
the transitive dependencies of the targets. This process is called the
*downsweep* because we are traversing the dependency tree downwards from
the targets. (The *upsweep*, where we compile all these files happens in
the opposite direction of course).

The function takes the targets and returns a list of consisting of all
the modules to be compiled/loaded.

The !ModSummary type
--------------------

A (defined in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink"))
contains various information about a module:

`* Its ``, which includes the package that it belongs to`\
`* Its ``, which lists the pathnames of all the files associated with the module`\
`* The modules that it imports`\
`* The time it was last modified`\
`* ... some other things`

We collect information for all the modules we are interested in during
the *downsweep*, below. Extracting the information about the module name
and the imports from a source file is the job of
[GhcFile(compiler/main/HeaderInfo.hs)](GhcFile(compiler/main/HeaderInfo.hs) "wikilink")
which partially parses the source file.

Converting a given module name into a is done by in
[GhcFile(compiler/main/GHC.hs)](GhcFile(compiler/main/GHC.hs) "wikilink").
Similarly, if we have a filename rather than a module name, we generate
a using .

Loading (compiling) the Modules
-------------------------------

When the dependency analysis is complete, we can load these modules by
calling . The same interface is used regardless of whether we are
loading modules into GHCi with the command, or compiling a program with
: we always end up calling .

The process in principle is fairly simple:

`* Visit each module in the dependency tree from the bottom up, invoking [wiki:Commentary/Compiler/HscMain HscMain]`\
`  to compile it (the `*`upsweep`*`).`\
`* Finally, link all the code together.  In GHCi this involves loading all the object code into memory and linking it`\
`  with the [wiki:Commentary/Rts/Interpreter#Linker RTS linker], and then linking all the byte-code together.  In`\
`  `` mode this involves invoking the external linker to link the object code into a binary.`

The process is made more tricky in practice for two reasons:

`* We might not need to compile certain modules, if none of their dependencies have changed.  GHC's `\
`  [wiki:Commentary/Compiler/RecompilationAvoidance recompilation checker] determines whether a module really needs`\
`  to be compiled or not.`\
`* In GHCi, we might just be reloading the program after making some changes, so we don't even want to re-link`\
`  modules for which no dependencies have changed.`

GHC Commentary: Asynchronous Exceptions
=======================================

GHC Commentary: Backends
========================

After \[wiki:Commentary/Compiler/CmmType Cmm\] has been generated, we
have a choice of targets to compile to:

`* [wiki:Commentary/Compiler/Backends/PprC The C code generator]`\
`* [wiki:Commentary/Compiler/Backends/NCG  The native code generator]`\
`* [wiki:Commentary/Compiler/Backends/LLVM The LLVM code generator]`\
`* [wiki:Commentary/Compiler/Backends/GHCi The GHCi code generator]`

These backends are completely interchangeable. Our preferred route is
the native code generator. The C code generator is used for portable,
non-optimised, or unregisterised compilation (Note that the LLVM backend
also supports building GHC in unregisterised mode as well as
registerised mode so it is usually the preferred route for porting GHC).

Types in the back end (aka "The \`Rep\` swamp")
===============================================

I have completed a major representation change, affecting both old and
new code generators, of the various \`Rep\` types. It's pervasive in
that it touches a lot of files; and in the native code-gen very many
lines are changed. The new situation is much cleaner.

Here are the highlights of the new design.

\`CmmType\`
-----------

There is a new type \`CmmType\`, defined in module \`CmmExpr\`, which is
just what it sounds like: it's the type of a \`CmmExpr\` or a
\`CmmReg\`.

``   * A `CmmType` is  ``*`abstract`*`` : its representation is private to `CmmExpr`.  That makes it easy to change representation. ``\
``   * A `CmmType` is actually just a pair of a `Width` and a category (`CmmCat`). ``\
``   * The `Width` type is exported and widely used in pattern-matching, but it does what it says on the tin: width only.   ``\
``   * In contrast, the `CmmCat` type is entirely private to `CmmExpr`.  It is just an enumeration that allows us to distinguish: floats, gc pointers, and other.  ``

Other important points are these:

`` * Each `LocalReg` has a `CmmType` attached; this replaces the previous unsavoury combination of `MachRep` and `CmmKind`.  Indeed, both of the latter are gone entirely. ``

`` * Notice that a `CmmType` accurately knows about gc-pointer-hood. Ultimately we will abandon static-reference-table generation in STG syntax, and instead generate SRTs from the Cmm code.  We'll need to update the RTS `.cmm` files to declare pointer-hood. ``

`` * The type `TyCon.PrimRep` remains; it enumerates the representations that a Haskell value can take.  Differences from `CmmType`: ``\
``   * `PrimRep` contains `VoidRep`, but `CmmType` has no zero-width form. ``\
``   * `CmmType` includes sub-word width values (e.g. 8-bit) which `PrimRep` does not. ``\
``   The function `primRepCmmType` converts a non-void `PrimRep` to a `CmmType`. ``

`` * `CmmLint` is complains if you assign a gc-ptr to a non-gc-ptr and vice versa.  It treats "gc-ptr + constant" as a gc-ptr.   ``

`   `*`NB:` `you'd` `better` `not` `make` `an` `interior` `pointer`
`live` `across` `a`
`call`*`, else we'll save it on the stack and treat it as a GC root.  It's not clear how to guarantee this doesn't happen as the result of some optimisation.`

**Parsing \`.cmm\` RTS files.** The global register \`P0\` is a
gc-pointer version of \`R0\`. They both map to the same physical
register, though!

The \`MachOp\` type
-------------------

The \`MachOp\` type enumerates (in machine-independent form) the
available machine instructions. The principle they embody is that
*everything except the width is embodied in the opcode*. In particular,
we have

`` * `MO_S_Lt`, `MO_U_Lt`, and `MO_F_Lt` for comparison (signed, unsigned, and float). ``\
`` * `MO_SS_Conv`, `MO_SF_Conv` etc, for conversion (`SS` is signed-to-signed, `SF` is signed-to-float, etc). ``

These constructor all take \`Width\` arguments.

The \`MachOp\` data type is defined in \`CmmExpr\`, not in a separate
\`MachOp\` module.

Foreign calls and hints
-----------------------

In the new Cmm representation (\`ZipCfgCmmRep\`), but not the old one,
arguments and results to all calls, including foreign ones, are ordinary
\`CmmExpr\` or \`CmmReg\` respectively. The extra information we need
for foreign calls (is this signed? is this an address?) are kept in the
calling convention. Specifically:

`` * `MidUnsafeCall` calls a `MidCallTarget` ``\
`` * `MidCallTarget` is either a `CallishMachOp` or a `ForeignTarget` ``\
`` * In the latter case we supply a `CmmExpr` (the function to call) and a `ForeignConvention` ``\
`` * A `ForeignConvention` contains the C calling convention (stdcall, ccall etc), and a list of `ForiegnHints` for arguments and for results. (We might want to rename this type.) ``

This simple change was horribly pervasive. The old Cmm rep (and Michael
Adams's stuff) still has arguments and results being (argument,hint)
pairs, as before.

Native code generation and the \`Size\` type
--------------------------------------------

The native code generator has an instruction data type for each
architecture. Many of the instructions in these data types used to have
a \`MachRep\` argument, but now have a \`Size\` argument instead. In
fact, so far as the native code generators are concerned, these \`Size\`
types (which can be machine-specific) are simply a plug-in replacement
for \`MachRep\`, with one big difference: **\`Size\` is completely local
to the native code generator** and hence can be changed at will without
affecting the rest of the compiler.

\`Size\` is badly named, but I inherited the name from the previous
code.

I rather think that many instructions should have a \`Width\` parameter,
not a \`Size\` parameter. But I didn't feel confident to change this.
Generally speaking the NCG is a huge swamp and needs re-factoring. I'm
working on getting Backtraces in GHC. Progress can be seen here:
<https://github.com/abacathoo/ghc>

The Block Allocator
===================

Source:
[GhcFile(includes/rts/storage/Block.h)](GhcFile(includes/rts/storage/Block.h) "wikilink"),
[GhcFile(rts/sm/BlockAlloc.h)](GhcFile(rts/sm/BlockAlloc.h) "wikilink"),
[GhcFile(rts/sm/BlockAlloc.c)](GhcFile(rts/sm/BlockAlloc.c) "wikilink"),
[GhcFile(includes/rts/storage/MBlock.h)](GhcFile(includes/rts/storage/MBlock.h) "wikilink"),
[GhcFile(rts/sm/MBlock.c)](GhcFile(rts/sm/MBlock.c) "wikilink").

The block allocator is where the storage manager derives much of its
flexibilty. Rather than keep our heap in a single contiguous region of
memory, or one contiguous region per generation, we manage linked lists
of memory blocks. Managing contiguous regions is difficult, especially
when you want to change the size of some of the areas. A
block-structured storage arrangement has several advantages:

`* resizing areas of memory is easy: just chain more blocks onto the list.`

`* managing large objects without copying is easy: allocate each one a complete block, and use the block linkage to`\
`  chain them together.`

`* free memory can be recycled faster, because a block is a block.`

The concept relies on the property that most data objects are
significantly smaller than a block, and only rarely do we need to
allocate objects that approach or exceed the size of a block.

Structure of blocks
-------------------

We want to allocate memory in units of a small block (around 4k, say).
Furthermore, we want each block to have an associated small structure
called a *block descriptor*, which contains information about the block:
its link field, which generation it belongs to, and so on. This is
similar to the well-known "BiBOP" (Big Bag of Pages) technique, where
objects with similar tags are collected together on a page so as to
avoid needing to store an individual tag with each object.

We want a function \`Bdescr(p)\`, that, given an arbitrary pointer into
a block, returns the address of the block descriptor that corresponds to
the block containing that pointer.

There are two options:

`` * Put the block descriptor at the start of the block.  `Bdescr(p) = p & ~BLOCK_SIZE`.  This option has problems if ``\
`  we need to allocate a contiguous region larger than a single block (GHC does this occasionally when allocating`\
`  a large number of objects in one go).`

`* Allocate memory in larger units (a `*`megablock`*`), divide the megablock into blocks, and put all the block`\
`  descriptors at the beginning.  The megablock is aligned, so that the address of the block descriptor for`\
`  a block is a simple function of its address.  The 'Bdescr' function is more complicated than the first`\
`  method, but it is easier to allocate contiguous regions (unless the contiguous region is larger than`\
`  a megablock...).`

We adopt the second approach. The following diagram shows a megablock:

[Image(sm-block.png)](Image(sm-block.png) "wikilink")

We currently have megablocks of 1Mb in size (m = 20) with blocks of 4k
in size (k = 12), and these sizes are easy to change
([GhcFile(includes/rts/Constants.h)](GhcFile(includes/rts/Constants.h) "wikilink")).

Block descriptors are currently 32 or 64 bytes depending on the word
size (d = 5 or 6). The block descriptor itself is the structure
\`bdescr\` defined in
[GhcFile(includes/rts/storage/Block.h)](GhcFile(includes/rts/storage/Block.h) "wikilink"),
and that file also defines the \`Bdescr()\` macro.

The block allocator has a the following structure:

`* At the bottom, talking to the OS, is the megablock allocator (`[`GhcFile(rts/sm/MBlock.c)`](GhcFile(rts/sm/MBlock.c) "wikilink")`, `[`GhcFile(includes/rts/storage/MBlock.h)`](GhcFile(includes/rts/storage/MBlock.h) "wikilink")`).`\
`  It is responsible for delivering megablocks, correctly aligned, to the upper layers.  It is also responsible for`\
`  implementing [wiki:Commentary/HeapAlloced HEAP_ALLOCED()]: the predicate that tests whether a pointer points to dynamically allocated memory`\
`  or not.  This is implemented as a simple bitmap lookup on a 32-bit machine, and something more complex on`\
`  64-bit addressed machines.  See `[`GhcFile(includes/rts/storage/MBlock.h)`](GhcFile(includes/rts/storage/MBlock.h) "wikilink")` for details.`\
`  `[`br`](br "wikilink")[`br`](br "wikilink")\
`  Currently, megablocks are never freed back to the OS, except at the end of the program.  This is a potential`\
`  improvement that could be made.`

`* Sitting on top of the megablock allocator is the block layer (`[`GhcFile(includes/rts/storage/Block.h)`](GhcFile(includes/rts/storage/Block.h) "wikilink")`, `[`GhcFile(rts/sm/BlockAlloc.c)`](GhcFile(rts/sm/BlockAlloc.c) "wikilink")`).`\
`  This layer is responsible for providing:`

` These functions allocate and deallocate a block `*`group`*`: a contiguous sequence of blocks (the degenerate, and common, case`\
` is a single block).  The block allocator is responsible for keeping track of free blocks.  Currently it does this by`\
` maintaining an ordered (by address) list of free blocks, with contiguous blocks coallesced.  However this is certanly`\
` not optimal, and has been shown to be a bottleneck in certain cases - improving this allocation scheme would be good.`

GHC Commentary: Garbage Collecting CAFs
=======================================

Files: [GhcFile(rts/sm/GC.c)](GhcFile(rts/sm/GC.c) "wikilink"), function
scavange\_srt in
[GhcFile(rts/sm/Scav.h)](GhcFile(rts/sm/Scav.h) "wikilink")

Constant Applicative Forms, or CAFs for short, are top-level values
defined in a program. Essentially, they are objects that are not
allocated dynamically at run-time but, instead, are part of the static
data of the program. Sometimes, a CAF may refer to many values in the
heap. To avoid memory leaks in such situations, we need to know when a
CAF is never going to be used again, and so we can deallocate the values
that it refers to.

See Note \[CAF management\] in
[GhcFile(rts/sm/Storage.c)](GhcFile(rts/sm/Storage.c) "wikilink") for
more information.

Static Reference Tables
-----------------------

File:
[GhcFile(includes/rts/storage/InfoTables.h)](GhcFile(includes/rts/storage/InfoTables.h) "wikilink")

The info table of various closures may contain information about what
static objects are referenced by the closure. This information is stored
in two parts:

` 1. a static reference table (SRT), which is an array of references to static objects`\
` 2. a bitmask which specifies which of the objects are actually used by the closure.`

There are two different ways to access this information depending on the
size of the SRT:

` * "small": if `` is a small bitmap, not all 1s, then GET_FUN?_SRT contains the SRT.`\
` * "large": if `` is all 1s, then GET_FUN?_SRT contains a large bitmap, and the actual SRT.`

Evacuating Static Objects
-------------------------

Files:
[GhcFile(rts/sm/GCThread.h)](GhcFile(rts/sm/GCThread.h) "wikilink"),
[GhcFile(rts/sm/Evac.c)](GhcFile(rts/sm/Evac.c) "wikilink"),
[GhcFile(rts/sm/GC.c)](GhcFile(rts/sm/GC.c) "wikilink")

While scavenging objects, we also process (aka "evacuate") any static
objects that need to be kept alive. When a GC thread discovers a live
static object, it places it on its list. Later, this list is used to
scavange the static objects, potentially finding more live objects. Note
that this process might find more static objects, and thus further
extend the list.

When a static object is scavenged, it is removed from and placed on
another list, called . Later, we use this list to "clean up" the
liveness markers from these static objects, so that we can repeat the
process on the next garbage collection. Note that we can't "clean up"
the liveness markers as we go along because we use them to notice cycles
among the static objects.

Calling Convention
==================

Entry conventions are very conventional: the first N argumements in
registers and the rest on the stack.

Return Convention
=================

All returns are now *direct*; that is, a return is made by jumping to
the code associated with the
\[wiki:Commentary/Rts/Storage/HeapObjects\#InfoTables info table\] of
the topmost \[wiki:Commentary/Rts/Storage/Stack stack frame\].

GHC used to have a more complex return convention called vectored
returns in which some stack frames pointed to vectors of return
addresses; this was dropped in GHC 6.8 after measurements that showed it
was not (any longer) worthwhile.

Historical page
---------------

This page is a bunch of notes on the new code generator. It is outdated
and is here only for historical reasons.It should probably be removed.
See \[wiki:Commentary/Compiler/CodeGen Code Generator\] page for a
description of current code generator.

Cleanup after the new codegen is enabled
========================================

The new codegen was enabled by default in
832077ca5393d298324cb6b0a2cb501e27209768. Now that the switch has been
made, we can remove all the cruft associated with the old code
generator. There are dependencies between some of the components, so we
have to do things in the right order. Here is a list of the cleanup
tasks, and notes about dependencies:

Independent tasks
-----------------

`` * Use `BlockId` or `Label` consistently, currently we use a mixture of the two.  Maybe get rid of the `BlockId` module. ``

`` * Remove live-var and CAF lists from `StgSyn`, and then clean up `CoreToStg` ``

`` * DONE: Remove the SRT pass in `simplStg/SRT.lhs` ``

`* DONE: remove RET_DYN from the RTS`

`` * DONE: remove `-fnew-codegen`, related `HscMain` bits and the `CodeGen` module. ``

`` * DONE: remove `CmmOpt.cmmMiniInline`, it is not used any more ``

`` * Fix the layering: `cmm` modules should not depend on `codeGen/StgCmm*` ``

Towards removing codeGen/Cg\*
-----------------------------

`` * DONE: `CmmParse` should produce new `Cmm`.  ``\
``   * We will probably want two kinds of `.cmm` file, one that is to be fed through `CmmLayoutStack` and one that isn't. ``\
``   * primops will be fed through `CmmLayoutStack`, and will use the native calling convention, with the code generator inserting the copyin/copyout for us. ``

`` * DONE: Remove all the `Cg*` modules ``

Towards removing \`OldCmm\`
---------------------------

`` * IN PROGRESS (Simon M): Change the NCG over to consume new `Cmm`.  We possibly also want the generated native code to use the Hoopl Block representation, although that will mean changing branch instructions to have both true and false targets, rather than true and fallthrough as we have now. ``

`` * Remove `cmm/CmmCvt` (this will save some compile-time too) ``

`` * Remove `cmm/OldCmm*`, `cmm/PprOldCmm` etc. ``

Later
-----

`* Do the new SRT story (!ToDo: write a wiki page about this)`

Cmm: Implementing Exception Handling
====================================

The IEEE 754 specification for floating point numbers defines exceptions
for certain floating point operations, including:

`* range violation (overflow, underflow); `\
`* rounding errors (inexact); `\
`` * invalid operation (invalid operand, such as comparison with a `NaN` value, the square root of a negative number or division of zero by zero); and, ``\
`* zero divide (a special case of an invalid operation).  `

Many architectures support floating point exceptions by including a
special register as an addition to other exception handling registers.
The IBM PPC includes the \`FPSCR\` ("Floating Point Status Control
Register"); the Intel x86 processors use the \`MXCSR\` register. When
the PPC performs a floating point operation it checks for possible
errors and sets the \`FPSCR\`. Some processors allow a flag in the
Foating-Point Unit (FPU) status and control register to be set that will
disable some exceptions or the entire FPU exception handling facility.
Some processors disable the FPU after an exception has occurred while
others, notably Intel's x86 and x87 processors, continue to perform FPU
operations. Depending on whether quiet !NaNs (QNaNs) or signaling !NaNs
(SNaNs) are used by the software, an FPU exception may signal an
interrupt for the software to pass to its own exception handler.

Some higher level languages provide facilities to handle these
exceptions, including Ada, Fortran (F90 and later), C++ and C (C99,
fenv.h, float.h on certain compilers); others may handle such exceptions
without exposing a low-level interface. There are three reasons to
handle FPU exceptions, and these reasons apply similarly to other
exceptions:

`* the facilities provide greater control; `\
`* the facilities are efficient--more efficient than a higher-level software solution; and, `\
`* FPU exceptions may be unavoidable, especially if several FPU operations are serially performed at the machine level so the higher level software has no opportunity to check the results in between operations. `

#### An Integral Exception Example

There has been at least one problem in GHC that would benefit from
exception handling--in some cases, for \`Integral\`s. See bug ticket
\#1042. The bug occurs in \`show\`ing the number, in
\[GhcFile(libraries/base/GHC/Show.lhs) GHC.Show\], \`showSignedInt\`,
before conversion from base\_2 to base\_10, where a negative \`Int\`
(always \`Int32\`) is negated in order to process it as a positive value
when converting it to a string, base\_10, causing an overflow error on
some architectures. (Bear in mind that it would show up here in the
example for \#1042 because the function would be evaluated in GHCi here;
the negation is the problem and the exception shows up in the *next*
instruction on that operand, here \`DIV\`.)

The exception example in \#1042 does not occur on PowerPC machines,
which dutifully print the two's complement of : \`0\`. (\`-2147483648\`
is the minimum bound for signed Ints, so negating it should properly
become, bitwise, a positive \`2147483647\` (all but bit 31 set); once
negated again when divided by \`-1\` this would be \`0\`; \`-0\` is
converted to \`0\`.) On some architectures such as Intel 64 and IA-32,
negating the minimum bound does not wrap around to \`0\` but overflows,
which is reported as a floating point "overflow" (\`\#O\`) exception:
the \`NEG\` instruction modifies the \`OF\` flag (bit 11) in the
\`EFLAGS\` register--curiously enough, the \`DIV\` and \`IDIV\`
instructions have *undefined* effects on the \`OF\` flag.

The workaround was to avoid negating \`minBound\` \`Int\`s; note that no
Intel instructions allow one to modify the \`OF\` flag directly.
Alternative solutions might be to

`` 1. mask the "exception" by clearing the interrupt flag, `IF`, using the `CLI` instruction; or,  ``\
`` 1. conditionally unset the flag by using the `PUSHF` instruction on the `EFLAGS` register to push its lower word (bits 15-0, including the offending bit 11 (`OF`)) onto the stack, reset the `OF` bit, then push that back onto the stack and pop it into EFLAGS with `POPF`.  Depending on variable register used, the assembler output would look similar to: ``

#### A Floating Point Exception Example

There was a long message thread on the Haskell-prime mailing list,
"realToFrac Issues," beginning with [John Meacham's
message](http://www.haskell.org/pipermail/haskell-prime/2006-February/000791.html)
and ending with [Simon Marlow's
message](http://www.haskell.org/pipermail/haskell-prime/2006-March/000840.html).
The following code for converting a Float to a Double will *fail* to
produce a floating point exception or NaN on x86 machines (recall that
0.0/0.0 is NaN *and* a definite FPU exception):

\[in GHCi-6.6 on PowerPC, OS X\]:

This bug is not due to the lack of FPU exceptions in Cmm but bears
mention as the internal conversion performed in 'realToFrac' on 'Float's
would benefit from FPU exceptions: with Haskell-support for FPU
exceptions this realToFrac would be able to issue an exception for NaN,
Infinity or rounding errors when converting a Float to a Double and vice
versa. There is a related problem with rounding errors in the functions
'encodeFloat', 'decodeFloat', 'encodeDouble' and 'decodeDouble', see
\[wiki:ReplacingGMPNotes/TheCurrentGMPImplementation\].

On 5 May 2008, Isaac Dupree asked

` Is there documentation (e.g. on the GHC Commentary somewhere I can't`\
` find) an explanation of what C-- "kinds" are or how they're useful/used? `

Probably not. GHC Cmm is a sort of pidgin version of C-- 2.0, and true
C-- kinds are explained in the [C-- specification, section
5.1](http://www.cminusminus.org/code.html).

` When I was portabilizing that code area a while ago I had ignorantly `\
` changed some of the uses of "kind" to "hint" for consistency (both names `\
` had been being used for the same thing via type-synonym.) and because I `\
` could guess how the code make sense if it was, informally, a hint about `\
` what to do.`

Hint was the word used originally, and several people (including
reviewers) objected to it on the grounds that the 'hints' are actually
mandatory to get the compiler to do what you want (e.g., pass arguments
in floating-point registers). So we changed the name to 'kind'.

If you like dense, indigestible academic papers full of formalism,
there's [one I'm quite proud
of](http://www.cs.tufts.edu/~nr/pubs/staged-abstract.html). It explains
in detail how kinds are useful for specifying and implementing procedure
calling conventions, which is the use to which they are put within GHC.

Norman Ramsey

### Note To Reader

This page was written with more detail than usual since you may need to
know how to work with Cmm as a programming language. Cmm is the basis
for the future of GHC, Native Code Generation, and if you are interested
in hacking Cmm at least this page might help reduce your learning curve.
As a finer detail, if you read the \[wiki:Commentary/Compiler/HscMain
Compiler pipeline\] wiki page or glanced at the diagram there you may
have noticed that whether you are working backward from an
\`intermediate C\` (Haskell-C "HC", \`.hc\`) file or an Assembler file
you get to Cmm before you get to the STG language, the Simplifier or
anything else. In other words, for really low-level debugging you may
have an easier time if you know what Cmm is about. Cmm also has
opportunities for implementing small and easy hacks, such as little
optimisations and implementing new Cmm Primitive Operations.

A portion of the \[wiki:Commentary/Rts RTS\] is written in Cmm:
[GhcFile(rts/Apply.cmm)](GhcFile(rts/Apply.cmm) "wikilink"),
[GhcFile(rts/Exception.cmm)](GhcFile(rts/Exception.cmm) "wikilink"),
[GhcFile(rts/HeapStackCheck.cmm)](GhcFile(rts/HeapStackCheck.cmm) "wikilink"),
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink"),
[GhcFile(rts/StgMiscClosures.cmm)](GhcFile(rts/StgMiscClosures.cmm) "wikilink"),
[GhcFile(rts/StgStartup.cmm)](GhcFile(rts/StgStartup.cmm) "wikilink")
and [GhcFile(StgStdThunks.cmm)](GhcFile(StgStdThunks.cmm) "wikilink").
(For notes related to \`PrimOps.cmm\` see the \[wiki:Commentary/PrimOps
PrimOps\] page; for much of the rest, see the
\[wiki:Commentary/Rts/HaskellExecution HaskellExecution\] page.) Cmm is
optimised before GHC outputs either HC or Assembler. The C compiler
(from HC, pretty printed by
[GhcFile(compiler/cmm/PprC.hs)](GhcFile(compiler/cmm/PprC.hs) "wikilink"))
and the \[wiki:Commentary/Compiler/Backends/NCG Native Code Generator\]
(NCG) \[wiki:Commentary/Compiler/Backends Backends\] are closely tied to
data representations and transformations performed in Cmm. In GHC, Cmm
roughly performs a function similar to the intermediate [Register
Transfer Language (RTL)](http://gcc.gnu.org/onlinedocs/gccint/RTL.html)
in GCC.

Table of Contents
=================

` 1. [wiki:Commentary/Compiler/CmmType#AdditionsinCmm Additions in Cmm]`\
` 1. [wiki:Commentary/Compiler/CmmType#CompilingCmmwithGHC Compiling Cmm with GHC]`\
` 1. [wiki:Commentary/Compiler/CmmType#BasicCmm Basic Cmm]`\
`  1. [wiki:Commentary/Compiler/CmmType#CodeBlocksinCmm Code Blocks in Cmm]`\
`    * [wiki:Commentary/Compiler/CmmType#BasicBlocksandProcedures Basic Blocks and Procedures]`\
`  1. [wiki:Commentary/Compiler/CmmType#VariablesRegistersandTypes Variables, Registers and Types]`\
`    1. [wiki:Commentary/Compiler/CmmType#LocalRegisters Local Registers]`\
`    1. [wiki:Commentary/Compiler/CmmType#GlobalRegistersandHints Global Registers and Hints]`\
`    1. [wiki:Commentary/Compiler/CmmType#DeclarationandInitialisation Declaration and Initialisation]`\
`    1. [wiki:Commentary/Compiler/CmmType#MemoryAccess Memory Access]`\
`  1. [wiki:Commentary/Compiler/CmmType#LiteralsandLabels Literals and Labels]`\
`    * [wiki:Commentary/Compiler/CmmType#Labels Labels]`\
`  1. [wiki:Commentary/Compiler/CmmType#SectionsandDirectives Sections and Directives]`\
`    * [wiki:Commentary/Compiler/CmmType#TargetDirective Target Directive]`\
`  1. [wiki:Commentary/Compiler/CmmType#Expressions Expressions]`\
`    * [wiki:Commentary/Compiler/CmmType#QuasioperatorSyntax Quasi-operator Syntax]`\
`  1. [wiki:Commentary/Compiler/CmmType#StatementsandCalls Statements and Calls]`\
`    * [wiki:Commentary/Compiler/CmmType#CmmCalls Cmm Calls]`\
`  1. [wiki:Commentary/Compiler/CmmType#OperatorsandPrimitiveOperations Operators and Primitive Operations]`\
`    1. [wiki:Commentary/Compiler/CmmType#Operators Operators]`\
`    1. [wiki:Commentary/Compiler/CmmType#PrimitiveOperations Primitive Operations]`\
` 1. [wiki:Commentary/Compiler/CmmType#CmmDesign:ObservationsandAreasforPotentialImprovement Cmm Design: Observations and Areas for Potential Improvement]`

The Cmm language
================

\`Cmm\` is the GHC implementation of the \`C--\` language; it is also
the extension of Cmm source code files: \`.cmm\` (see
\[wiki:Commentary/Rts/Cmm What the hell is a .cmm file?\]). The GHC
\[wiki:Commentary/Compiler/CodeGen Code Generator\] (\`CodeGen\`)
compiles the STG program into \`C--\` code, represented by the \`Cmm\`
data type. This data type follows the [definition of
\`C--\`](http://www.cminusminus.org/) pretty closely but there are some
remarkable differences. For a discussion of the Cmm implementation
noting most of those differences, see the
\[wiki:Commentary/Compiler/CmmType\#BasicCmm Basic Cmm\] section, below.

`* `[`GhcFile(compiler/cmm/Cmm.hs)`](GhcFile(compiler/cmm/Cmm.hs) "wikilink")`: the main data type definition.`\
`* `[`GhcFile(compiler/cmm/MachOp.hs)`](GhcFile(compiler/cmm/MachOp.hs) "wikilink")`` : data types defining the machine operations (e.g. floating point divide) provided by `Cmm`. ``\
`* `[`GhcFile(compiler/cmm/CLabel.hs)`](GhcFile(compiler/cmm/CLabel.hs) "wikilink")`` : data type for top-level `Cmm` labels. ``

`* `[`GhcFile(compiler/cmm/PprCmm.hs)`](GhcFile(compiler/cmm/PprCmm.hs) "wikilink")`` : pretty-printer for `Cmm`. ``\
`* `[`GhcFile(compiler/cmm/CmmUtils.hs)`](GhcFile(compiler/cmm/CmmUtils.hs) "wikilink")`` : operations over `Cmm` ``

`* `[`GhcFile(compiler/cmm/CmmLint.hs)`](GhcFile(compiler/cmm/CmmLint.hs) "wikilink")`: a consistency checker.`\
`* `[`GhcFile(compiler/cmm/CmmOpt.hs)`](GhcFile(compiler/cmm/CmmOpt.hs) "wikilink")`` : an optimiser for `Cmm`. ``

`* `[`GhcFile(compiler/cmm/CmmParse.y)`](GhcFile(compiler/cmm/CmmParse.y) "wikilink")`, `[`GhcFile(compiler/cmm/CmmLex.x)`](GhcFile(compiler/cmm/CmmLex.x) "wikilink")`: parser and lexer for [wiki:Commentary/Rts/Cmm .cmm files].`

`* `[`GhcFile(compiler/cmm/PprC.hs)`](GhcFile(compiler/cmm/PprC.hs) "wikilink")`` : pretty-print `Cmm` in C syntax, when compiling via C. ``

Additions in Cmm
----------------

Although both Cmm and C-- allow foreign calls, the \`.cmm\` syntax
includes the

The \[R2\] part is the (set of) register(s) that you need to save over
the call.

Other additions to C-- are noted throughout the
\[wiki:Commentary/Compiler/CmmType\#BasicCmm Basic Cmm\] section, below.

Compiling Cmm with GHC
----------------------

GHC is able to compile \`.cmm\` files with a minimum of user-effort. To
compile \`.cmm\` files, simply invoke the main GHC driver but remember
to:

`` * add the option `-dcmm-lint` if you have handwritten Cmm code; ``\
`* add appropriate includes, especially `[`GhcFile(includes/Cmm.h)`](GhcFile(includes/Cmm.h) "wikilink")``  if you are using Cmm macros or GHC defines for certain types, such as `W_` for `bits32` or `bits64` (depending on the machine word size)--`Cmm.h` is in the `/includes` directory of every GHC distribution, i.e., `usr/local/lib/ghc-6.6/includes`; and, ``\
`` * if you do include GHC header files, remember to pass the code through the C preprocessor by adding the `-cpp` option. ``

For additional fun, you may pass GHC the \`-keep-s-file\` option to keep
the temporary assembler file in your compile directory. For example:
This will only work with very basic Cmm files. If you noticed that GHC
currently provides no \`-keep-cmm-file\` option and \`-keep-tmp-files\`
does not save a \`.cmm\` file and you are thinking about redirecting
output from \`-ddump-cmm\`, beware. The output from \`-ddump-cmm\`
contains equal-lines and dash-lines separating Cmm Blocks and Basic
Blocks; these are unparseable. The parser also cannot handle \`const\`
sections. For example, the parser will fail on the first \`0\` or
alphabetic token after \`const\`: Although GHC's Cmm pretty printer
outputs C-- standard parenthetical list of arguments after procedure
names, i.e., \`()\`, the Cmm parser will fail at the \`(\` token. For
example: The Cmm procedure names in
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") are not
followed by a (possibly empty) parenthetical list of arguments; all
their arguments are Global (STG) Registers, anyway, see
\[wiki:Commentary/Compiler/CmmType\#VariablesRegistersandTypes
Variables, Registers and Types\], below. Don't be confused by the
procedure definitions in other handwritten \`.cmm\` files in the RTS,
such as [GhcFile(rts/Apply.cmm)](GhcFile(rts/Apply.cmm) "wikilink"):
all-uppercase procedure invocations are special reserved tokens in
[GhcFile(compiler/cmm/CmmLex.x)](GhcFile(compiler/cmm/CmmLex.x) "wikilink")
and
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink").
For example, \`INFO\_TABLE\` is parsed as one of the tokens in the Alex
\`info\` predicate:

GHC's Cmm parser also cannot parse nested code blocks. For example: The
C-- specification example in section 4.6.2, "Procedures as section
contents" also will not parse in Cmm: Note that if \`p (bits32 i) { ...
}\` were written as a Cmm-parseable procedure, as \`p { ... }\`, the
parse error would occur at the closing curly bracket for the \`section
"data" { ... p { ... } }\`&lt;- here.

Basic Cmm
---------

FIXME: The links in this section are dead. But the files can be found
here: [1](http://www.cs.tufts.edu/~nr/c--/index.html). Relevant
discussion about the documentations of C--:
[2](https://mail.haskell.org/pipermail/ghc-devs/2014-September/006301.html)

Cmm is a high level assembler with a syntax style similar to C. This
section describes Cmm by working up from assembler--the C-- papers and
specification work down from C. At the least, you should know what a
"high level" assembler is, see ["What is a High Level
Assembler?"](http://webster.cs.ucr.edu/AsmTools/HLA/HLADoc/HLARef/HLARef3.html#1035157).
Cmm is different than other high level assembler languages in that it
was designed to be a semi-portable intermediate language for compilers;
most other high level assemblers are designed to make the tedium of
assembly language more convenient and intelligible to humans. If you are
completely new to C--, I highly recommend these papers listed on the
[C-- Papers](http://cminusminus.org/papers.html) page:

`* `[`C--:` `A` `Portable` `Assembly` `Language` `that` `Supports`
`Garbage` `Collection`
`(1999)`](http://cminusminus.org/abstracts/ppdp.html)` (Paper page with Abstract)`\
`* `[`C--:` `A` `Portable` `Assembly` `Language`
`(1997)`](http://cminusminus.org/abstracts/pal-ifl.html)` (Paper page with Abstract)`\
`* `[`A` `Single` `Intermediate` `Language` `That` `Supports` `Multiple`
`Implementations` `of` `Exceptions`
`(2000)`](http://cminusminus.org/abstracts/c--pldi-00.html)` (Paper page with Abstract)`\
`* `[`The` `C--` `Language` `Specification` `Version` `2.0` `(CVS`
`Revision` `1.128,` `23` `February`
`2005)`](http://cminusminus.org/extern/man2.pdf)` (PDF)`

Cmm is not a stand alone C-- compiler; it is an implementation of C--
embedded in the GHC compiler. One difference between Cmm and a C--
compiler like [Quick C--](http://cminusminus.org/code.html) is this: Cmm
uses the C preprocessor (cpp). Cpp lets Cmm *integrate* with C code,
especially the C header defines in
[GhcFile(includes)](GhcFile(includes) "wikilink"), and among many other
consequences it makes the C-- \`import\` and \`export\` statements
irrelevant; in fact, according to
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
they are ignored. The most significant action taken by the Cmm modules
in the Compiler is to optimise Cmm, through
[GhcFile(compiler/cmm/CmmOpt.hs)](GhcFile(compiler/cmm/CmmOpt.hs) "wikilink").
The Cmm Optimiser generally runs a few simplification passes over
primitive Cmm operations, inlines simple Cmm expressions that do not
contain global registers (these would be left to one of the
\[wiki:Commentary/Compiler/Backends Backends\], which currently cannot
handle inlines with global registers) and performs a simple loop
optimisation.

### Code Blocks in Cmm

The Haskell representation of Cmm separates contiguous code into:

`* `*`modules`*``  (compilation units; a `.cmm` file); and ``\
`* `*`basic` `blocks`*

Cmm modules contain static data elements (see
\[wiki:Commentary/Compiler/CmmType\#LiteralsandLabels Literals and
Labels\]) and \[wiki:Commentary/Compiler/CmmType\#BasicBlocks:Procedures
Basic Blocks\], collected together in \`Cmm\`, a type synonym for
\`GenCmm\`, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
\`CmmStmt\` is described in
\[wiki:Commentary/Compiler/CmmType\#StatementsandCalls Statements and
Calls\];[BR](BR "wikilink") \`Section\` is described in
\[wiki:Commentary/Compiler/CmmType\#SectionsandDirectives Sections and
Directives\];[BR](BR "wikilink") the static data in \`\[d\]\` is
\[\`CmmStatic\`\] from the type synonym \`Cmm\`;[BR](BR "wikilink")
\`CmmStatic\` is described in
\[wiki:Commentary/Compiler/CmmType\#LiteralsandLabels Literals and
Labels\].

#### Basic Blocks and Procedures

Cmm procedures are represented by the first constructor in \`GenCmmTop d
i\`: For a description of Cmm labels and the \`CLabel\` data type, see
the subsection \[wiki:Commentary/Compiler/CmmType\#LiteralsandLabels
Literals and Labels\], below.

Cmm Basic Blocks are labeled blocks of Cmm code ending in an explicit
jump. Sections (see
\[wiki:Commentary/Compiler/CmmType\#SectionsandDirectives Sections and
Directives\]) have no jumps--in Cmm, Sections cannot contain nested
Procedures (see, e.g.,
\[wiki:Commentary/Compiler/CmmType\#CompilingCmmwithGHC Compiling Cmm
with GHC\]). Basic Blocks encapsulate parts of Procedures. The data type
\`GenBasicBlock\` and the type synonym \`CmmBasicBlock\` encapsulate
Basic Blocks; they are defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
The \`BlockId\` data type simply carries a \`Unique\` with each Basic
Block. For descriptions of \`Unique\`, see

`* the [wiki:Commentary/Compiler/Renamer Renamer] page;`\
`* the [wiki:Commentary/Compiler/WiredIn#Knownkeythings Known Key Things] section of the [wiki:Commentary/Compiler/WiredIn Wired-in and Known Key Things] page; and, `\
`* the [wiki:Commentary/Compiler/EntityTypes#Typevariablesandtermvariables Type variables and term variables] section of the [wiki:Commentary/Compiler/EntityTypes Entity Types] page.`

### Variables, Registers and Types

Like other high level assembly languages, all variables in C-- are
machine registers, separated into different types according to bit
length (8, 16, 32, 64, 80, 128) and register type (integral or floating
point). The C-- standard specifies little more type information about a
register than its bit length: there are no distinguishing types for
signed or unsigned integrals, or for "pointers" (registers holding a
memory address). A C-- standard compiler supports additional information
on the type of a register value through compiler *hints*. In a foreign
call, a \`"signed" bits8\` would be sign-extended and may be passed as a
32-bit value. Cmm diverges from the C-- specification on this point
somewhat (see below). C-- and Cmm do not represent special registers,
such as a Condition Register (\`CR\`) or floating point unit (FPU)
status and control register (\`FPSCR\` on the PowerPC, \`MXCSR\` on
Intel x86 processors), as these are a matter for the
\[wiki:Commentary/Compiler/Backends Backends\].

C-- and Cmm hide the actual number of registers available on a
particular machine by assuming an "infinite" supply of registers. A
backend, such as the NCG or C compiler on GHC, will later optimise the
number of registers used and assign the Cmm variables to actual machine
registers; the NCG temporarily stores any overflow in a small memory
stack called the *spill stack*, while the C compiler relies on C's own
runtime system. Haskell handles Cmm registers with three data types:
\`LocalReg\`, \`GlobalReg\` and \`CmmReg\`. \`LocalReg\`s and
\`GlobalRegs\` are collected together in a single \`Cmm\` data type:

#### Local Registers

Local Registers exist within the scope of a Procedure: For a list of
references with information on \`Unique\`, see the
\[wiki:Commentary/Compiler/CmmType\#BasicBlocksandProcedures Basic
Blocks and Procedures\] section, above.

A \`MachRep\`, the type of a machine register, is defined in
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink"):
There is currently no register for floating point vectors, such as
\`F128\`. The types of Cmm variables are defined in the Happy parser
file
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
and the Alex lexer file
[GhcFile(compiler/cmm/CmmLex.x)](GhcFile(compiler/cmm/CmmLex.x) "wikilink").
(Happy and Alex will compile these into \`CmmParse.hs\` and
\`CmmLex.hs\`, respectively.) Cmm recognises the following \`C--\` types
as parseable tokens, listed next to their corresponding s in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink") and their
STG types: || **Cmm Token** || **Cmm.h \#define** || **STG type** || ||
\`bits8\` || \`I8\` || \`StgChar\` or \`StgWord8\` || || \`bits16\` ||
\`I16\` || \`StgWord16\` || || \`bits32\` || \`I32\`, \`CInt\`,
\`CLong\` || \`StgWord32\`; \`StgWord\` (depending on architecture) ||
|| \`bits64\` || \`I64\`, \`CInt\`, \`CLong\`, \`L\_\` || \`StgWord64\`;
\`StgWord\` (depending on architecture) || || \`float32\` || \`F\_\` ||
\`StgFloat\` || || \`float64\` || \`D\_\` || \`StgDouble\` ||

[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink") also
defines \`L\_\` for \`bits64\`, so \`F\_\`, \`D\_\` and \`L\_\`
correspond to the \`GlobalReg\` data type constructors \`FloatReg\`,
\`DoubleReg\` and \`LongReg\`. Note that although GHC may generate other
register types supported by the \`MachRep\` data type, such as \`I128\`,
they are not parseable tokens. That is, they are internal to GHC. The
special defines \`CInt\` and \`CLong\` are used for compatibility with C
on the target architecture, typically for making \`foreign "C"\` calls.

**Note**: Even Cmm types that are not explicit variables (Cmm literals
and results of Cmm expressions) have implicit \`MachRep\`s, in the same
way as you would use temporary registers to hold labelled constants or
intermediate values in assembler functions. See:

`` * [wiki:Commentary/Compiler/CmmType#LiteralsandLabels Literals and Labels] for information related to the Cmm literals `CmmInt` and `CmmFloat`; and, ``\
`` * [wiki:Commentary/Compiler/CmmType#Expressions Expressions], regarding the `cmmExprRep` function defined in  ``[`GhcFile(compiler/cmm/Cmm.hs)`](GhcFile(compiler/cmm/Cmm.hs) "wikilink")`.`

#### Global Registers and Hints

These are universal both to a Cmm module and to the whole compiled
program. Variables are global if they are declared at the top-level of a
compilation unit (outside any procedure). Global Variables are marked as
external symbols with the \`.globl\` assembler directive. In Cmm, global
registers are used for special STG registers and specific registers for
passing arguments and returning values. The Haskell representation of
Global Variables (Registers) is the \`GlobalReg\` data type, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
For a description of the \`Hp\` and \`Sp\` *virtual registers*, see
\[wiki:Commentary/Rts/HaskellExecution The Haskell Execution Model\]
page. General \`GlobalReg\`s are clearly visible in Cmm code according
to the following syntax defined in
[GhcFile(compiler/cmm/CmmLex.x)](GhcFile(compiler/cmm/CmmLex.x) "wikilink"):
|| **\`GlobalReg\` Constructor** || **Syntax** || **Examples** || ||
\`VanillaReg Int\` || \`R ++ Int\` || \`R1\`, \`R10\` || || \`FloatReg
Int\` || \`F ++ Int\` || \`F1\`, \`F10\` || || \`DoubleReg Int\` || \`D
++ Int\` || \`D1\`, \`D10\` || || \`LongReg Int\` || \`L ++ Int\` ||
\`L1\`, \`L10\` || General \`GlobalRegs\` numbers are decimal integers,
see the \`parseInteger\` function in
[GhcFile(compiler/utils/StringBuffer.lhs)](GhcFile(compiler/utils/StringBuffer.lhs) "wikilink").
The remainder of the \`GlobalReg\` constructors, from \`Sp\` to
\`BaseReg\` are lexical tokens exactly like their name in the data type;
\`PicBaseReg\` does not have a lexical token since it is used only
inside the NCG. See \[wiki:Commentary/PositionIndependentCode Position
Independent Code and Dynamic Linking\] for an in-depth description of
PIC implementations in the NCG.

\`GlobalRegs\` are a very special case in Cmm, partly because they must
conform to the STG register convention and the target C calling
convention. That the Cmm parser recognises \`R1\` and \`F3\` as
\`GlobalRegs\` is only the first step. The main files to look at for
more information on this delicate topic are:

`* `[`GhcFile(compiler/codeGen/CgCallConv.hs)`](GhcFile(compiler/codeGen/CgCallConv.hs) "wikilink")` (the section on "Register assignment")`\
`* `[`GhcFile(includes/stg/Regs.h)`](GhcFile(includes/stg/Regs.h) "wikilink")` (defining STG registers)`\
`* `[`GhcFile(includes/stg/MachRegs.h)`](GhcFile(includes/stg/MachRegs.h) "wikilink")` (target-specific mapping of machine registers for `*`registerised`*` builds of GHC)`\
`* `[`GhcFile(rts/PrimOps.cmm)`](GhcFile(rts/PrimOps.cmm) "wikilink")``  (examples of `GlobalReg` register usage for out-of-line primops) ``

All arguments to out-of-line !PrimOps in
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") are STG
registers.

Cmm recognises all C-- syntax with regard to *hints*. For example: Hints
are represented in Haskell as \`MachHint\`s, defined near \`MachRep\` in
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink"):

Although the C-- specification does not allow the C-- type system to
statically distinguish between floats, signed ints, unsigned ints or
pointers, Cmm does. Cmm \`MachRep\`s carry the float or int kind of a
variable, either within a local block or in a global register.
\`GlobalReg\` includes separate constructors for \`Vanilla\`, \`Float\`,
\`Double\` and \`Long\`. Cmm still does not distinguish between signed
ints, unsigned ints and pointers (addresses) at the register level, as
these are given *hint* pseudo-types or their real type is determined as
they run through primitive operations. \`MachHint\`s still follow the
C-- specification and carry kind information as an aide to the backend
optimisers.

Global Registers in Cmm currently have a problem with inlining: because
neither
[GhcFile(compiler/cmm/PprC.hs)](GhcFile(compiler/cmm/PprC.hs) "wikilink")
nor the NCG are able to keep Global Registers from clashing with C
argument passing registers, Cmm expressions that contain Global
Registers cannot be inlined into an argument position of a foreign call.
For more thorough notes on inlining, see the comments in
[GhcFile(compiler/cmm/CmmOpt.hs)](GhcFile(compiler/cmm/CmmOpt.hs) "wikilink").

#### Declaration and Initialisation

Cmm variables hold the same values registers do in assembly languages
but may be declared in a similar way to variables in C. As in C--, they
may actually be declared anywhere in the scope for which they are
visible (a block or file)--for Cmm, this is done by the \`loopDecls\`
function in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink").
In
[GhcFile(compiler/rts/PrimOps.cmm)](GhcFile(compiler/rts/PrimOps.cmm) "wikilink"),
you will see Cmm variable declarations like this one: Remember that Cmm
code is run through the C preprocessor. \`W\_\` will be transformed into
\`bits32\`, \`bits64\` or whatever is the \`bits\`*size* of the machine
word, as defined in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink"). In
Haskell code, you may use the
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink")
functions \`wordRep\` and \`halfWordRep\` to dynamically determine the
machine word size. For a description of word sizes in GHC, see the
\[wiki:Commentary/Rts/Word Word\] page.

The variables \`w\`, \`code\` and \`val\` should be real registers. With
the above declaration the variables are uninitialised. Initialisation
requires an assignment *statement*. Cmm does not recognise C-- "\`{\`
*literal*, ... \`}\`" initialisation syntax, such as \`bits32{10}\` or
\`bits32\[3\] {1, 2, 3}\`. Cmm does recognise initialisation with a
literal: The typical method seems to be to declare variables and then
initialise them just before their first use. (Remember that you may
declare a variable anywhere in a procedure and use it in an expression
before it is initialised but you must initialise it before using it
anywhere else--statements, for example.)

#### Memory Access

If the value in \`w\` were the address of a memory location, you would
obtain the value at that location similar to Intel assembler syntax. In
Cmm, you would write: compare the above statement to indirect addressing
in Intel assembler:

The code between the brackets (\`w\` in \`\[w\]\`, above) is an
*expression*. See the \[wiki:Commentary/Compiler/CmmType\#Expressions
Expressions\] section. For now, consider the similarity between the
Cmm-version of indexed memory addressing syntax, here: and the
corresponding Intel assembler indexed memory addressing syntax, here:
You will generally not see this type of syntax in either handwritten or
GHC-produced Cmm code, although it is allowed; it simply shows up in
macros. C-- also allows the \`\*\` (multiplication) operator in
addressing expressions, for an approximation of *scaled* addressing
(\`\[base \* (2\^n)\]\`); for example, \`n\` (the "scale") must be
\`0\`, \`1\`, \`2\` or \`4\`. C-- itself would not enforce alignment or
limits on the scale. Cmm, however, could not process it: since the NCG
currently outputs GNU Assembler syntax, the Cmm or NCG optimisers would
have to reduce \`n\` in (\`\* n\`) to an absolute address or relative
offset, or to an expression using only \`+\` or \`-\`. This is not
currently the case and would be difficult to implement where one of the
operands to the \`\*\` is a relative address not visible in the code
block. [GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink")
defines macros to perform the calculation with a constant. For example:
is used in: The function \`cmmMachOpFold\` in
[GhcFile(compiler/cmm/CmmOpt.hs)](GhcFile(compiler/cmm/CmmOpt.hs) "wikilink")
will reduce the resulting expression \`Sp + (n \* SIZEOF\_W)\` to \`Sp +
N\`, where \`N\` is a constant. A very large number of macros for
accessing STG struct fields and the like are produced by
[GhcFile(includes/mkDerivedConstants.c)](GhcFile(includes/mkDerivedConstants.c) "wikilink")
and output into the file \`includes/DerivedConstants.h\` when GHC is
compiled.

Of course, all this also holds true for the reverse (when an assignment
is made to a memory address): or, for an example of a macro from
\`DerivedConstants.h\`: this will be transformed to:

### Literals and Labels

Cmm literals are exactly like C-- literals, including the Haskell-style
type syntax, for example: \`0x00000001::bits32\`. Cmm literals may be
used for initialisation by assignment or in expressions. The \`CmmLit\`
and \`CmmStatic\` data types, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink")
together represent Cmm literals, static information and Cmm labels: Note
how the \`CmmLit\` constructor \`CmmInt Integer MachRep\` contains sign
information in the \`Integer\`, the representation of the literal
itself: this conforms to the C-- specification, where integral literals
contain sign information. For an example of a function using \`CmmInt\`
sign information, see \`cmmMachOpFold\` in
[GhcFile(compiler/cmm/CmmOpt.hs)](GhcFile(compiler/cmm/CmmOpt.hs) "wikilink"),
where sign-operations are performed on the \`Integer\`.

The \`MachRep\` of a literal, such as \`CmmInt Integer MachRep\` or
\`CmmFloat Rational MachRep\` may not always require the size defined by
\`MachRep\`. The NCG optimiser,
[GhcFile(compiler/nativeGen/MachCodeGen.hs)](GhcFile(compiler/nativeGen/MachCodeGen.hs) "wikilink"),
will test a literal such as \`1::bits32\` (in Haskell, \`CmmInt
(1::Integer) I32\`) for whether it would fit into the bit-size of
Assembler instruction literals on that particular architecture with a
function defined in
[GhcFile(compiler/nativeGen/MachRegs.lhs)](GhcFile(compiler/nativeGen/MachRegs.lhs) "wikilink"),
such as \`fits16Bits\` on the PPC. If the Integer literal fits, the
function \`makeImmediate\` will truncate it to the specified size if
possible and store it in a NCG data type, \`Imm\`, specifically \`Maybe
Imm\`. (These are also defined in
[GhcFile(compiler/nativeGen/MachRegs.lhs)](GhcFile(compiler/nativeGen/MachRegs.lhs) "wikilink").)

The Haskell representation of Cmm separates unchangeable Cmm values into
a separate data type, \`CmmStatic\`, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
Note the \`CmmAlign\` constructor: this maps to the assembler directive
\`.align N\` to set alignment for a data item (hopefully one you
remembered to label). This is the same as the \`align\` directive noted
in Section 4.5 of the [C-- specification
(PDF)](http://cminusminus.org/extern/man2.pdf). In the current
implementation of Cmm the \`align\` directive seems superfluous because
[GhcFile(compiler/nativeGen/PprMach.hs)](GhcFile(compiler/nativeGen/PprMach.hs) "wikilink")
translates \`Section\`s to assembler with alignment directives
corresponding to the target architecture (see
\[wiki:Commentary/Compiler/CmmType\#SectionsandDirectives Sections and
Directives\], below).

#### Labels

Remember that C--/Cmm names consist of a string where the first
character is:

`* ASCII alphabetic (uppercase or lowercase);`\
`` * an underscore:    `_` ; ``\
`` * a period:         `.` ; ``\
`` * a dollar sign:    `$` ; or, ``\
`` * a commercial at:  `@` . ``

Cmm labels conform to the C-- specification. C--/Cmm uses labels to
refer to memory locations in code--if you use a data directive but do
not give it a label, you will have no means of referring to the memory!
For \`GlobalReg\`s (transformed to assembler \`.globl\`), labels serve
as both symbols and labels (in the assembler meaning of the terms). The
Haskell representation of Cmm Labels is contained in the \`CmmLit\` data
type, see \[wiki:Commentary/Compiler/CmmType\#Literals Literals\]
section, above. Note how Cmm Labels are \`CLabel\`s with address
information. The \`Clabel\` data type, defined in
[GhcFile(compiler/cmm/CLabel.hs)](GhcFile(compiler/cmm/CLabel.hs) "wikilink"),
is used throughout the Compiler for symbol information in binary files.
Here it is:

### Sections and Directives

The Haskell representation of Cmm Section directives, in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink")
as the first part of the "Static Data" section, is: Cmm supports the
following directives, corresponding to the assembler directives
pretty-printed by the \`pprSectionHeader\` function in
[GhcFile(compiler/nativeGen/PprMach.hs)](GhcFile(compiler/nativeGen/PprMach.hs) "wikilink"):
|| **\`Section\` Constructor** || **Cmm section directive** ||
**Assembler Directive** || || \`Text\` || \`"text"\` || \`.text\` || ||
\`Data\` || \`"data"\` || \`.data\` || || \`ReadOnlyData\` ||
\`"rodata"\` || \`.rodata\`[BR](BR "wikilink")(generally; varies by
arch,OS) || || \`RelocatableReadOnlyData\` || no parse (GHC internal),
output: \`"relreadonly"\` ||
\`.const\_data\`[BR](BR "wikilink")\`.section
.rodata\`[BR](BR "wikilink")(generally; varies by arch,OS) || ||
\`UninitialisedData\` || \`"bss"\`, output: \`"uninitialised"\` ||
\`.bss\` || || \`ReadOnlyData16\` || no parse (GHC internal), output:
none || \`.const\`[BR](BR "wikilink")\`.section
.rodata\`[BR](BR "wikilink")(generally; on
x86\_64:[BR](BR "wikilink")\`.section .rodata.cst16\`) || You probably
already noticed I omitted the alignment directives (for clarity). For
example, \`pprSectionHeader\` would pretty-print \`ReadOnlyData\` as on
an i386 with the Darwin OS. If you are really on the ball you might have
noticed that the \`PprMach.hs\` output of "\`.section .data\`" and the
like is really playing it safe since on most OS's, using GNU Assembler,
the \`.data\` directive is equivalent to \`.section \_\_DATA .data\`, or
simply \`.section .data\`. Note that \`OtherSection String\` is not a
catch-all for the Cmm parser. If you wrote: The Cmm parser (through GHC)
would panic, complaining, "\`PprMach.pprSectionHeader: unknown
section\`."

While the C-- specification allows a bare \`data\` keyword directive,
Cmm does not:

Cmm does not recognise the C-- "\`stack\`" declaration for allocating
memory on the system stack.

GHC-produced Cmm code is replete with \`data\` sections, each of which
is stored in \`.data\` section of the binary code. This contributes
significantly to the large binary size for GHC-compiled code.

` ==== Target Directive ====`

The C-- specification defines a special \`target\` directive, in section
4.7. The \`target\` directive is essentially a code block defining the
properties of the target architecture: This is essentially a
custom-coded version of the GNU Assembler (\`as\`) \`.machine\`
directive, which is essentially the same as passing the \`-arch
\[cpu\_type\]\` option to \`as\`.

Cmm does not support the \`target\` directive. This is partly due GHC
generally lacking cross-compiler capabilities. Should GHC move toward
adding cross-compilation capabilities, the \`target\` might not be a bad
thing to add. Target architecture parameters are currently handled
through the \[wiki:Attic/Building/BuildSystem Build System\], which
partly sets such architectural parameters through
[GhcFile(includes/mkDerivedConstants.c)](GhcFile(includes/mkDerivedConstants.c) "wikilink")
and
[GhcFile(includes/ghcconfig.h)](GhcFile(includes/ghcconfig.h) "wikilink").

### Expressions

Expressions in Cmm follow the C-- specification. They have:

`* no side-effects; and,`\
`* one result: `\
`  * a `*`k`*`-bit value`[`BR`](BR "wikilink")`` --these expressions map to the `MachOp` data type, defined in  ``[`GhcFile(compiler/cmm/MachOp.hs)`](GhcFile(compiler/cmm/MachOp.hs) "wikilink")`, see [wiki:Commentary/Compiler/CmmType#OperatorsandPrimitiveOperations Operators and Primitive Operations], the `*`k`*`-bit value may be:`\
``     * a Cmm literal (`CmmLit`); or, ``\
``     * a Cmm variable (`CmmReg`, see [wiki:Commentary/Compiler/CmmType#VariablesRegistersandTypes Variables, Registers and Types]); ``[`BRor`](BR "wikilink")`, `\
`  * a boolean condition.`

Cmm expressions may include

`` * a literal or a name (`CmmLit` contains both, see [wiki:Commentary/Compiler/CmmType#LiteralsandLabels Literals and Labels], above); ``\
`` * a memory reference (`CmmLoad` and `CmmReg`, see [wiki:Commentary/Compiler/CmmType#MemoryAccess Memory Access], above); ``\
`` * an operator (a `MachOp`, in `CmmMachOp`, below); or, ``\
`` * another expression (a `[CmmExpr]`, in `CmmMachOp`, below). ``

These are all included as constructors in the \`CmmExpr\` data type,
defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
Note that \`CmmRegOff reg i\` is only shorthand for a specific
\`CmmMachOp\` application: The function \`cmmRegRep\` is described
below. Note: the original comment following \`CmmExpr\` in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink")
is erroneous (cf., \`mangleIndexTree\` in
[GhcFile(compiler/nativeGen/MachCodeGen.hs)](GhcFile(compiler/nativeGen/MachCodeGen.hs) "wikilink"))
but makes the same point described here. The offset, \`(CmmLit (CmmInt i
rep))\`, is a literal (\`CmmLit\`), not a name (\`CLabel\`). A
\`CmmExpr\` for an offset must be reducible to a \`CmmInt\` *in
Haskell*; in other words, offsets in Cmm expressions may not be external
symbols whose addresses are not resolvable in the current context.

Boolean comparisons are not boolean conditions. Boolean comparisons
involve relational operators, such as \`&gt;\`, \`&lt;\` and \`==\`, and
map to \`MachOp\`s that are converted to comparison followed by branch
instructions. For example, \`&lt;\` would map to \`MO\_S\_Lt\` for
signed operands,
[GhcFile(compiler/nativeGen/MachCodeGen.hs)](GhcFile(compiler/nativeGen/MachCodeGen.hs) "wikilink")
would transform \`MO\_S\_Lt\` into the \`LTT\` constructor of the
\`Cond\` union data type defined in
[GhcFile(compiler/nativeGen/MachInstrs.hs)](GhcFile(compiler/nativeGen/MachInstrs.hs) "wikilink")
and
[GhcFile(compiler/nativeGen/PprMach.hs)](GhcFile(compiler/nativeGen/PprMach.hs) "wikilink")
would transform \`LTT\` to the distinguishing comparison type for an
assembler comparison instruction. You already know that the result of a
comparison instruction is actually a change in the state of the
Condition Register (CR), so Cmm boolean expressions do have a kind of
side-effect but that is to be expected. In fact, it is necessary since
at the least a conditional expression becomes two assembler
instructions, in PPC Assembler: This condition mapping does have an
unfortunate consequence: conditional expressions do not fold into single
instructions. In Cmm, as in C--, expressions with relational operators
may evaluate to an integral (\`0\`, nonzero) instead of evaluating to a
boolean type. For certain cases, such as an arithmetic operation
immediately followed by a comparison, extended mnemonics such as
\`addi.\` might eliminate the comparison instruction. See
\[wiki:Commentary/Compiler/CmmType\#CmmDesignObservationsandAreasforPotentialImprovement
Cmm Design: Observations and Areas for Potential Improvement\] for more
discussion and potential solutions to this situation.

Boolean conditions include: \`&&\`, \`||\`, \`!\` and parenthetical
combinations of boolean conditions. The \`if expr { }\` and \`if expr {
} else { }\` statements contain boolean conditions. The C-- type
produced by conditional expressions is \`bool\`, in Cmm, type
\`BoolExpr\` in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink"):
The type \`BoolExpr\` maps to the \`CmmCondBranch\` or \`CmmBranch\`
constructors of type \`CmmStmt\`, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"),
see \[wiki:Commentary/Compiler/CmmType\#StatementsandCalls Statements
and Calls\].

The \`CmmExpr\` constructor \`CmmMachOp MachOp \[CmmExpr\]\` is the core
of every operator-based expression; the key here is \`MachOp\`, which in
turn depends on the type of \`MachRep\` for each operand. See
\[wiki:Commentary/Compiler/CmmType\#FundamentalandPrimitiveOperators
Fundamental and PrimitiveOperators\]. In order to process \`CmmExpr\`s,
the data type comes with a deconstructor function to obtain the relevant
\`MachRep\`s, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
The deconstructors \`cmmLitRep\` and \`cmmRegRep\` (with its supporting
deconstructor \`localRegRep\`) are also defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink").

In PPC Assembler you might add two 32-bit integrals by: while in Cmm you
might write: Remember that the assignment operator, \`=\`, is a
statement since it has the "side effect" of modifying the value in
\`res\`. The \`+\` expression in the above statement, for a 32-bit
architecture, would be represented in Haskell as: The \`expr\`
production rule in the Cmm Parser
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
maps tokens to "values", such as \`+\` to an addition operation,
\`MO\_Add\`. The \`mkMachOp\` function in the Parser determines the
\`MachOp\` type in \`CmmMachOp MachOp \[CmmExpr\]\` from the token value
and the \`MachRep\` type of the \`head\` variable. Notice that the
simple \`+\` operator did not contain sign information, only the
\`MachRep\`. For \`expr\`, signed and other \`MachOps\`, see the
\`machOps\` function in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink").
Here is a table of operators and the corresponding \`MachOp\`s
recognised by Cmm (listed in order of precedence): || **Operator** ||
**\`MachOp\`** || || \`/\` || \`MO\_U\_Quot\` || || \`\*\` ||
\`MO\_Mul\` || || \`%\` || \`MO\_U\_Rem\` || || \`-\` || \`MO\_Sub\` ||
|| \`+\` || \`MO\_Add\` || || \`&gt;&gt;\` || \`MO\_U\_Shr\` || ||
\`&lt;&lt;\` || \`MO\_Shl\` || || \`&\` || \`MO\_And\` || || \`\^\` ||
\`MO\_Xor\` || || \`|\` || \`MO\_Or\` || || \`&gt;=\` || \`MO\_U\_Ge\`
|| || \`&gt;\` || \`MO\_U\_Gt\` || || \`&lt;=\` || \`MO\_U\_Le\` || ||
\`&lt;\` || \`MO\_U\_Lt\` || || \`!=\` || \`MO\_Ne\` || || \`==\` ||
\`MO\_Eq\` || || \`\~\` || \`MO\_Not\` || || \`-\` || \`MO\_S\_Neg\` ||

#### Quasi-operator Syntax

If you read to the end of \`expr\` in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink"),
in the next production rule, \`expr0\`, you will notice that Cmm
expressions also recognise a set of name (not symbol) based operators
that would probably be better understood as *quasi-operators*. The
syntax for these quasi-operators is in some cases similar to syntax for
Cmm statements and generally conform to the C-- specification, sections
3.3.2 (\`expr\`) and 7.4.1 (syntax of primitive operators), *except
that* 3. *and, by the equivalence of the two,* 1. *may return*
**multiple** '' arguments''. In Cmm, quasi-operators may have side
effects. The syntax for quasi-operators may be:

`` 1. `expr0`  ````  `expr0` ``[`BR`](BR "wikilink")`(just like infix-functions in Haskell);`\
`` 1. `type[ expression ]` ``[`BR`](BR "wikilink")`` (the memory access quasi-expression described in [wiki:Commentary/Compiler/CmmType#MemoryAccess Memory Access]; the Haskell representation of this syntax is `CmmLoad CmmExpr MachRep`);  ``\
`` 1. `%name( exprs0 )` ``[`BR`](BR "wikilink")`(standard prefix form, similar to C-- `*`statement`*``  syntax for procedures but with the distinguishing prefix `%`; in Cmm this is  ``*`also`
`used` `as` `statement` `syntax` `for` `calls,` `which` `are` `really`
`built-in`
`procedures`*`, see [wiki:Commentary/Compiler/CmmType#CmmCalls Cmm Calls]) `

A \`expr0\` may be a literal (\`CmmLit\`) integral, floating point,
string or a \`CmmReg\` (the production rule \`reg\`: a \`name\` for a
local register (\`LocalReg\`) or a \`GlobalReg\`).

Note that the \`name\` in \`expr0\` syntax types 1. and 3. must be a
known *primitive* (primitive operation), see
\[wiki:Commentary/Compiler/CmmType\#OperatorsandPrimitiveOperations
Operators and Primitive Operations\]. The first and third syntax types
are interchangeable: The primitive operations allowed by Cmm are listed
in the \`machOps\` production rule, in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink"),
and largely correspond to \`MachOp\` data type constructors, in
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink"),
with a few additions. The primitive operations distinguish between
signed, unsigned and floating point types.

Cmm adds some expression macros that map to Haskell Cmm functions. They
are listed under \`exprMacros\` in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
and include:

`` * `ENTRY_CODE` ``\
`` * `INFO_PTR` ``\
`` * `STD_INFO` ``\
`` * `FUN_INFO` ``\
`` * `GET_ENTRY` ``\
`` * `GET_STD_INFO` ``\
`` * `GET_FUN_INFO` ``\
`` * `INFO_TYPE` ``\
`` * `INFO_PTRS` ``\
`` * `INFO_NPTRS` ``\
`` * `RET_VEC` ``

### Statements and Calls

Cmm Statements generally conform to the C-- specification, with a few
exceptions noted below. Cmm Statements implement:

`` * no-op; the empty statement: `;` ``\
`` * C-- (C99/C++ style) comments: `// ... \n` and `/* ... */` ``\
`` * the assignment operator: `=` ``\
`` * store operation (assignment to a memory location): `type[expr] =` ``\
`` * control flow within procedures (`goto`) and between procedures (`jump`, returns) (note: returns are  ``*`only`*` Cmm macros)`\
`` * foreign calls (`foreign "C" ...`) and calls to Cmm Primitive Operations (`%`) ``\
`* procedure calls and tail calls`\
`` * conditional statement (`if ... { ... } else { ... }`) ``\
`` * tabled conditional (`switch`) ``

Cmm does not implement the C-- specification for Spans (sec. 6.1) or
Continuations (sec. 6.7).[BR](BR "wikilink") Although Cmm supports
primitive operations that may have side effects (see
\[wiki:Commentary/Compiler/CmmType\#PrimitiveOperations Primitive
Operations\], below), it does not parse the syntax \`%%\` form mentioned
in section 6.3 of the C-- specification. Use the \`%name(arg1,arg2)\`
expression-syntax instead. [BR](BR "wikilink") Cmm does not implement
the \`return\` statement (C-- spec, sec. 6.8.2) but provides a set of
macros that return a list of tuples of a \`CgRep\` and a \`CmmExpr\`:
\`\[(CgRep,CmmExpr)\]\`. For a description of \`CgRep\`, see comments in
[GhcFile(compiler/codeGen/SMRep.lhs)](GhcFile(compiler/codeGen/SMRep.lhs) "wikilink").
The return macros are defined at the end of the production rule
\`stmtMacros\` in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink"):

`` * `RET_P` ``\
`` * `RET_N` ``\
`` * `RET_PP` ``\
`` * `RET_NN` ``\
`` * `RET_NP` ``\
`` * `RET_PPP` ``\
`` * `RET_NNP` ``\
`` * `RET_NNNP` ``\
`` * `RET_NPNP` ``

In the above macros, \`P\` stands for \`PtrArg\` and \`N\` stands for
\`NonPtrArg\`; both are \`CgRep\` constructors. These return macros
provide greater control for the \[wiki:Commentary/Compiler/CodeGen
CodeGen\] and integrate with the RTS but limit the number and type of
return arguments in Cmm: you may only return according to these macros!
The returns are processed by the \`emitRetUT\` function in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink"),
which in turn calls several functions from
[GhcFile(compiler/codeGen/CgMonad.lhs)](GhcFile(compiler/codeGen/CgMonad.lhs) "wikilink"),
notably \`emitStmts\`, which is the core Code Generator function for
emitting \`CmmStmt\` data.

The Haskell representation of Cmm Statements is the data type
\`CmmStmt\`, defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink"):
Note how the constructor \`CmmJump\` contains \`\[LocalReg\]\`: this is
the Cmm implementation of the C-- \`jump\` statement for calling another
procedure where the parameters are the arguments passed to the other
procedure. None of the parameters contain the address--in assembler, a
label--of the caller, to return control to the caller. The \`CmmCall\`
constructor also lacks a parameter to store the caller's address. Cmm
implements C-- jump nesting and matching returns by *tail calls*, as
described in section 6.8 of the C-- specification. Tail calls are
managed through the \[wiki:Commentary/Compiler/CodeGen CodeGen\], see
[GhcFile(compiler/codeGen/CgTailCall.lhs)](GhcFile(compiler/codeGen/CgTailCall.lhs) "wikilink").
You may have already noticed that the call target of the \`CmmJump\` is
a \`CmmExpr\`: this is the Cmm implementation of computed procedure
addresses, for example: The computed procedure address, in this case
\`(bits32\[x+4\])\`, should always be the first instruction of a \`Cmm\`
procedure. You cannot obtain the address of a code block *within* a
procedure and \`jump\` to it, as an alternative way of computing a
*continuation*.

\`CmmBranch BlockId\` represents an unconditional branch to another
\[wiki:Commentary/Compiler/CmmType\#BasicBlocksandProcedures Basic
Block\] in the same procedure. There are two unconditional branches in
Cmm/C--:

`` 1. `goto` statement; and ``\
`` 1. a branch from the `else` portion of an `if-then-else` statement. ``

\`CmmCondBranch CmmExpr BlockId\` represents a conditional branch to
another \[wiki:Commentary/Compiler/CmmType\#BasicBlocksandProcedures
Basic Block\] in the same procedure. This is the \`if expr\` statement
where \`expr\` is a \`CmmExpr\`, used in both the unary \`if\` and
\`if-then-else\` statements. \`CmmCondBranch\` maps to more complex
Assembler instruction sets or HC code
([GhcFile(compiler/cmm/PprC.hs)](GhcFile(compiler/cmm/PprC.hs) "wikilink")).
For assembler, labels are created for each new Basic Block. During
parsing, conditional statements map to the \`BoolExpr\` data type which
guides the encoding of assembler instruction sets.

\`CmmSwitch\` represents the \`switch\` statement. It is parsed and
created as with the \`doSwitch\` function in
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
or created from \`case\` expressions with the \`emitSwitch\` and
\`mk\_switch\` functions in
[GhcFile(compiler/codeGen/CgUtils.hs)](GhcFile(compiler/codeGen/CgUtils.hs) "wikilink").
In the NCG, a \`CmmSwitch\` is generated as a jump table using the
\`genSwitch\` function in
[GhcFile(compiler/nativeGen/MachCodeGen.hs)](GhcFile(compiler/nativeGen/MachCodeGen.hs) "wikilink").
There is currently no implementation of any optimisations, such as a
cascade of comparisons for switches with a wide deviation in values or
binary search for very wide value ranges--for output to HC, earlier
versions of GCC could not handle large if-trees, anyway.

#### Cmm Calls

Cmm calls include both calls to foreign functions and calls to Cmm
quasi-operators using expression syntax (see
\[wiki:Commentary/Compiler/CmmType\#QuasioperatorSyntax Quasi-operator
Syntax\]). Although Cmm does not implement any of the control flow
statements of C-- specification (section 6.8.1), foreign calls from Cmm
are one of the most complex components of the system due to various
differences between the Cmm and C calling conventions.

The data type, \`CmmCallTarget\` is defined in
[GhcFile(compiler/cmm/Cmm.hs)](GhcFile(compiler/cmm/Cmm.hs) "wikilink")
as: \`CCallConv\` is defined in
[GhcFile(compiler/prelude/ForeignCall.lhs)](GhcFile(compiler/prelude/ForeignCall.lhs) "wikilink");
for information on register assignments, see comments in
[GhcFile(compiler/codeGen/CgCallConv.hs)](GhcFile(compiler/codeGen/CgCallConv.hs) "wikilink").

\`CallishMachOp\` is defined in
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink");
see, also, below \[wiki:Commentary/Compiler/CmmType\#PrimitiveOperations
Primitive Operations\]. \`CallishMachOp\`s are generally used for
floating point computations (without implementing any floating point
exceptions). Here is an example of using a \`CallishMachOp\` (not yet
implemented):

### Operators and Primitive Operations

Cmm generally conforms to the C-- specification for operators and
"primitive operations". The C-- specification, in section 7.4, refers to
both of these as "primitive operations" but there are really two
different types:

`* `*`operators`*`, as I refer to them, are: `\
``   * parseable tokens, such as `+`,`-`,`*` or `/`;  ``\
`  * generally map to a single machine instruction or part of a machine instruction;`\
`  * have no side effects; and, `\
``   * are represented in Haskell using the `MachOp` data type;  ``\
`* `*`primitive`
`operations`*` (Cmm `*`quasi-operators`*`` ) are special, usually inlined, procedures, represented in Haskell using the `CallishMachOp` data type; primitive operations may have side effects. ``

The \`MachOp\` and \`CallishMachOp\` data types are defined in
[GhcFile(compiler/cmm/MachOp.hs)](GhcFile(compiler/cmm/MachOp.hs) "wikilink").

Both Cmm Operators and Primitive Operations are handled in Haskell as
\[wiki:Commentary/PrimOps\#InlinePrimOps Inline PrimOps\], though what I
am calling Cmm *primitive operations* may be implemented as out-of-line
foreign calls.

#### Operators

 Each \`MachOp\` generally corresponds to a machine instruction but may
have its value precomputed in the Cmm, NCG or HC optimisers.

#### Primitive Operations

Primitive Operations generally involve more than one machine instruction
and may not always be inlined.

 For an example, the floating point sine function, \`sinFloat\#\` in
[GhcFile(compiler/prelude/primops.txt.pp)](GhcFile(compiler/prelude/primops.txt.pp) "wikilink")
is piped through the \`callishOp\` function in
[GhcFile(compiler/codeGen/CgPrimOp.hs)](GhcFile(compiler/codeGen/CgPrimOp.hs) "wikilink")
to become \`Just MO\_F32\_Sin\`. The \`CallishMachOp\` constructor
\`MO\_F32\_Sin\` is piped through a platform specific function such as
[GhcFile(compiler/nativeGen/X86/CodeGen.hs)](GhcFile(compiler/nativeGen/X86/CodeGen.hs) "wikilink")
on X86, where the function \`genCCall\` will call \`outOfLineFloatOp\`
to issue a call to a C function such as \`sin\`.

Cmm Design: Observations and Areas for Potential Improvement
------------------------------------------------------------

"If the application of a primitive operator causes a system exception,
such as division by zero, this is an unchecked run-time error. (A future
version of this specification may provide a way for a program to recover
from such an exception.)" C-- spec, Section 7.4. Cmm may be able to
implement a partial solution to this problem, following the paper: [A
Single Intermediate Language That Supports Multiple Implementations of
Exceptions (2000)](http://cminusminus.org/abstracts/c--pldi-00.html).
(TODO: write notes to wiki and test fix.)

The IEEE 754 specification for floating point numbers defines exceptions
for certain floating point operations, including:

`* range violation (overflow, underflow); `\
`* rounding errors (inexact); `\
`` * invalid operation (invalid operand, such as comparison with a `NaN` value, the square root of a negative number or division of zero by zero); and, ``\
`* zero divide (a special case of an invalid operation).  `

Many architectures support floating point exceptions by including a
special register as an addition to other exception handling registers.
The IBM PPC includes the \`FPSCR\` ("Floating Point Status Control
Register"); the Intel x86 processors use the \`MXCSR\` register. When
the PPC performs a floating point operation it checks for possible
errors and sets the \`FPSCR\`. Some processors allow a flag in the
Foating-Point Unit (FPU) status and control register to be set that will
disable some exceptions or the entire FPU exception handling facility.
Some processors disable the FPU after an exception has occurred while
others, notably Intel's x86 and x87 processors, continue to perform FPU
operations. Depending on whether quiet !NaNs (QNaNs) or signaling !NaNs
(SNaNs) are used by the software, an FPU exception may signal an
interrupt for the software to pass to its own exception handler.

Some higher level languages provide facilities to handle these
exceptions, including Ada, Fortran (F90 and later), C++ and C (C99,
fenv.h, float.h on certain compilers); others may handle such exceptions
without exposing a low-level interface. There are three reasons to
handle FPU exceptions, and these reasons apply similarly to other
exceptions:

`* the facilities provide greater control; `\
`* the facilities are efficient--more efficient than a higher-level software solution; and, `\
`* FPU exceptions may be unavoidable, especially if several FPU operations are serially performed at the machine level so the higher level software has no opportunity to check the results in between operations. `

A potential solution to the problem of implementing Cmm exceptions,
especially for floating point operations, is at
\[wiki:Commentary/CmmExceptions Cmm: Implementing Exception Handling\].

The C-- Language Specification mentions over 75 primitive operators. The
Specification lists separate operators for integral and floating point
(signed) arithmetic (including carry, borrow and overflow checking),
logical comparisons and conversions (from one size float to another,
from float to integral and vice versa, etc.). C-- also includes special
operators for floating point number values, such as \`NaN\`,
\`mzero\`*k* and \`pzero\`*k*, and rounding modes; integral kinds also
include bitwise operators, unsigned variants, and bit extraction for
width changing and sign or zero-extension. A C-- implementation may
conveniently map each of these operators to a machine instruction, or to
a simulated operation on architectures that do not support a single
instruction. There seem to be two main problems with the current
GHC-implementation of Cmm:

`1. not enough operators`\
`` 1. no implementation of vector (SIMD) registers (though there is a `I128` `MachRep`) ``

If a particular architecture supports it, assembler includes
instructions such as mnemonics with the \`.\` ("dot") suffix (\`add.,
fsub.\`), which set the Condition Register (CR) thereby saving you at
least one instruction. (Extended mnemonics can save you even more.)
Extended mnemonics with side effects may be implemented as new
\`CallishMachOps\`, see
\[wiki:Commentary/Compiler/CmmType\#PrimitiveOperations Primitive
Operations\] and \[wiki:Commentary/Compiler/CmmType\#CmmCalls Cmm
Calls\]. Assembler also supports machine exceptions, especially
exceptions for floating-point operations, invalid storage access or
misalignment (effective address alignment). The current implementation
of Cmm cannot model such exceptions through flow control because no flow
control is implemented, see \[wiki:Commentary/Compiler/CmmType\#CmmCalls
Cmm Calls\].

Hiding the kinds of registers on a machine eliminates the ability to
handle floating point exceptions at the Cmm level and to explicitly
vectorize (use SIMD extensions). The argument for exposing vector types
may be a special case since such low-level operations are exposed at the
C-level, as new types of variables or "intrinsics," that are C-language
extensions provided by special header files and compiler support
(\`vector unsigned int\` or \`\_\_m128i\`, \`vector float\` or
\`\_\_m128\`) and operations (\`vec\_add()\`, \`+\` (with at least one
vector operand), \`\_mm\_add\_epi32()\`).

GHC Commentary: What the hell is a \`.cmm\` file?
=================================================

A \`.cmm\` file is rather like C--. The syntax is almost C-- (a few
constructs are missing), and it is augmented with some macros that are
expanded by GHC's code generator (eg. \`INFO\_TABLE()\`). A \`.cmm\`
file is compiled by GHC itself: the syntax is parsed by
[GhcFile(compiler/cmm/CmmParse.y)](GhcFile(compiler/cmm/CmmParse.y) "wikilink")
and
[GhcFile(compiler/cmm/CmmLex.x)](GhcFile(compiler/cmm/CmmLex.x) "wikilink")
into the \[wiki:Commentary/Compiler/CmmType Cmm\] data type, where it is
then passed through one of the \[wiki:Commentary/Compiler/Backends
back-ends\].

We use the C preprocessor on \`.cmm\` files, making extensive use of
macros to make writing this low-level code a bit less tedious and
error-prone. Most of our C-- macros are in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink"). One
useful fact about the macros is \`P\_\` is an alias for \`gcptr\`, and
you should not use it for non-garbage-collected pointers.

Reading references
------------------

Reading material for learning Cmm is somewhat scattered, so I (Arash)
have created a list of useful links. Since the Cmm language is changing
as GHC changes, I have prioritized resources that are not too old.
(*Feel free to add/remove/modify this list! :)*)

`* An overview of Cmm is given in `[`David` `Terei's` `bachelor`
`thesis`](https://davidterei.com/downloads/papers/terei:2009:honours_thesis.pdf)` (chapter 2.4.3).`\
`* The comments in the beginning of `[`GhcFile(compiler/cmm/CmmParse.y)`](GhcFile(compiler/cmm/CmmParse.y) "wikilink")` is super-useful and kept up to date. The rest of the file contains the `*`grammar`*` of the language. Afraid of grammars? Edward Yang wrote this fantastic `[`blog`
`post`](http://blog.ezyang.com/2013/07/no-grammar-no-problem/)` on how to understand the constructs of Cmm by using the grammar.  `\
`* Cmm has a preprocessor like the one in C and many of the macros are defined in `[`GhcFile(includes/Cmm.h)`](GhcFile(includes/Cmm.h) "wikilink")`. `\
`* In 2012, Simon Marlow extended the Cmm language by adding a new high-level syntax which can be used when you don't need low-level access (like registers). The `[`commit`](https://github.com/ghc/ghc/commit/a7c0387d20c1c9994d1100b14fbb8fb4e28a259e)` explains the details.`\
`* Cmm is also described [wiki:Commentary/Compiler/CmmType on this wiki], but it is written before the new syntax was introduced.`\
`` * Stack frame types are created using `INFO_TABLE_RET`, the syntax can be confusing since there are both  ``*`arguments`*` and `*`fields`*`, I (Arash) have not seen anything like it in other programming languages. I tried to explain it in my `[`master`
`thesis`](http://arashrouhani.com/papers/master-thesis.pdf)` (sections 4.2 and 4.2.1).`

Other information
-----------------

It can take time to learn Cmm. One unintuitive thing to watch out for is
that there are no function calls in low-level cmm code. The new syntax
from 2012 allows function calls but you should know that they are kind
of magical.

We say that **Cmm** is GHC's implementation of **C--**. This naming
scheme is not done consistently everywhere, unfortunately. If you are
interested in C-- (which have diverged from Cmm), you can check out the
[website](http://www.cminusminus.org/) and the
[specification](http://www.cs.tufts.edu/~nr/c--/extern/man2.pdf).

Code Generator
==============

This page describes code generator ("codegen") in GHC. It is meant to
reflect current state of the implementation. If you notice any
inaccuracies please update the page (if you know how) or complain on
ghc-devs.

A brief history of code generator
---------------------------------

You might occasionally hear about "old" and "new" code generator. GHC
7.6 and earlier used the old code generator. New code generator was
being developed since 2007 and it was
\[changeset:832077ca5393d298324cb6b0a2cb501e27209768/ghc enabled by
default on 31 August 2012\] after the release of GHC 7.6.1. The first
stable GHC to use the new code generator is 7.8.1 released in early
2014. The commentary on the old code generator can be found
\[wiki:Commentary/Compiler/OldCodeGen here\]. Notes from the development
process of the new code generator are located in a couple of pages on
the wiki - to find them go to \[wiki:TitleIndex Index\] and look for
pages starting with "!NewCodeGen".

There are some plans for the future development of code generator. One
plan is to expand the capability of the pipeline so that it does native
code generation too so that existing backends can be discarded - see
\[wiki:Commentary/Compiler/IntegratedCodeGen IntegratedCodeGen\] for
discussion of the design. It is hard to say if this will ever happen as
currently there is no work being done on that subject and in the
meanwhile there was an alternative proposal to
\[wiki:Commentary/Compiler/Backends/LLVM/ReplacingNCG replace native
code generator with LLVM\].

Overview
--------

The goal of the code generator is to convert program from
\[wiki:Commentary/Compiler/GeneratedCode STG\] representation to
\[wiki:Commentary/Compiler/CmmType Cmm\] representation. STG is a
functional language with explicit stack. Cmm is a low-level imperative
language - something between C and assembly - that is suitable for
machine code generation. Note that terminology might be a bit confusing
here: the term "code generator" can refer both to STG-&gt;Cmm pass and
the whole STG-&gt;Cmm-&gt;assembly pass. The Cmm-&gt;assembly conversion
is performed by one the backends, eg. NCG (Native Code Generator or
LLVM.

The top-most entry point to the codegen is located in
[GhcFile(compiler/main/HscMain.hs)](GhcFile(compiler/main/HscMain.hs) "wikilink")
in the \`tryNewCodegen\` function. Code generation is done in two
stages:

` 1. Convert STG to Cmm with implicit stack, and native Cmm calls. This whole stage lives in `[`GhcFile(compiler/codeGen)`](GhcFile(compiler/codeGen) "wikilink")``  directory with the entry point being `codeGen` function in  ``[`GhcFile(compiler/codeGen/StgCmm.hs)`](GhcFile(compiler/codeGen/StgCmm.hs) "wikilink")` module.`\
` 2. Optimise the Cmm, and CPS-convert it to have an explicit stack, and no native calls. This lives in `[`GhcFile(compiler/cmm)`](GhcFile(compiler/cmm) "wikilink")``  directory with the `cmmPipeline` function from  ``[`GhcFile(compiler/cmm/CmmPipeline.hs)`](GhcFile(compiler/cmm/CmmPipeline.hs) "wikilink")` module being the entry point.`

The CPS-converted Cmm is fed to one of the backends. This is done by
\`codeOutput\` function
([GhcFile(compiler/main/CodeOutput.lhs)](GhcFile(compiler/main/CodeOutput.lhs) "wikilink")
called from \`hscGenHardCode\` after returning from \`tryNewCodegen\`.

First stage: STG to Cmm conversion
----------------------------------

`* `**`Code`
`generator`**``  converts STG to `CmmGraph`.  Implemented in `StgCmm*` modules (in directory `codeGen`).  ``\
``   * `Cmm.CmmGraph` is pretty much a Hoopl graph of `CmmNode.CmmNode` nodes. Control transfer instructions are always the last node of a basic block. ``\
``   * Parameter passing is made explicit; the calling convention depends on the target architecture.  The key function is `CmmCallConv.assignArgumentsPos`.  ``\
`    * Parameters are passed in virtual registers R1, R2 etc. [These map 1-1 to real registers.] `\
`    * Overflow parameters are passed on the stack using explicit memory stores, to locations described abstractly using the [wiki:Commentary/Compiler/StackAreas `*`Stack`
`Area`*` abstraction].   `\
``     * Making the calling convention explicit includes an explicit store instruction of the return address, which is stored explicitly on the stack in the same way as overflow parameters. This is done (obscurely) in `StgCmmMonad.mkCall`. ``

Second stage: the Cmm pipeline
------------------------------

The core of the Cmm pipeline is implemented by the \`cpsTop\` function
in
[GhcFile(compiler/cmm/CmmPipeline.hs)](GhcFile(compiler/cmm/CmmPipeline.hs) "wikilink")
module. Below is a high-level overview of the pipeline. See source code
comments in respective modules for a more in-depth explanation of each
pass.

`* `**`Control` `Flow`
`Optimisations`**`` , implemented in `CmmContFlowOpt`, simplifies the control flow graph by: ``\
`  * Eliminating blocks that have only one predecessor by concatenating them with that predecessor`\
`  * Shortcuting targets of branches and calls (see Note [What is shortcutting])`\
` `\
`If a block becomes unreachable because of shortcutting it is eliminated from the graph. However, `**`it`
`is` `theoretically` `possible` `that` `this` `pass` `will` `produce`
`unreachable`
`blocks`**`. The reason is the label renaming pass performed after block concatenation has been completed.`

`This pass might be optionally called for the second time at the end of the pipeline.`

`* `**`Common` `Block`
`Elimination`**`` , implemented in `CmmCommonBlockElim`, eliminates blocks that are identical (except for the label on their first node). Since this pass traverses blocks in depth-first order any unreachable blocks introduced by Control Flow Optimisations are eliminated.  ``**`This`
`pass` `is` `optional.`**

`* `**`Determine`
`proc-points`**`` , implemented in `CmmProcPoint`. The idea behind the "proc-point splitting" is that we first determine proc-points, ie. blocks in the graph that can be turned into entry points of procedures, and then split a larger function into many smaller ones, each having a proc-point as its entry point. This is required for the LLVM backend. The proc-point splitting itself is done later in the pipeline, but here we only determine the set of proc-points. We first call `callProcPoints`, which assumes that entry point to a Cmm graph and every continuation of a call is a procpoint. If we are splitting proc-points we update the list of proc-points by calling `minimalProcPointSet`, which adds all blocks reachable from more than one block in the graph. The set of proc-points is required by the stack layout pass. ``

`* `**`Figure` `out` `the` `stack`
`layout`**`` , implemented in `CmmStackLayout`. The job of this pass is to: ``\
`  * replace references to abstract stack Areas with fixed offsets from Sp.`\
`  * replace the !CmmHighStackMark constant used in the stack check with`\
`    the maximum stack usage of the proc.`\
`  * save any variables that are live across a call, and reload them as`\
`  necessary.`\
**`Important`**`: It may happen that stack layout will invalidate the computed set of proc-points by making a proc-point unreachable. This unreachable block is eliminated by one of subsequent passes that performs depth-first traversal of a graph: sinking pass (if optimisations are enabled), proc-point analysis (if optimisations are disabled and we're doing proc-point splitting) or at the very end of the pipeline (if optimisations are disabled and we're not doing proc-point splitting). This means that starting from this point in the pipeline we have inconsistent data and subsequent steps must be prepared for it.`\
\
`* `**`Sinking`
`assignments`**`` , implemented in `CmmSink`, performs these optimizations: ``\
`  * moves assignments closer to their uses, to reduce register pressure`\
`  * pushes assignments into a single branch of a conditional if possible`\
`  * inlines assignments to registers that are mentioned only once`\
`  * discards dead assignments`\
**`This` `pass` `is`
`optional.`**` It currently does not eliminate dead code in loops (#8327) and has some other minor deficiencies (eg. #8336).`

` * `**`CAF`
`analysis`**`` , implemented in `CmmBuildInfoTables`. Computed CAF information is returned from `cmmPipeline` and used to create Static Reference Tables (SRT). See [wiki:Commentary/Rts/Storage/GC/CAFs here] for some more detail on CAFs and SRTs. This pass is implemented using Hoopl (see below). ``

` * `**`Proc-point` `analysis` `and`
`splitting`**``  (only when splitting proc-points), implemented by `procPointAnalysis` in `CmmProcPoint`, takes a list of proc-points and for each block and determines from which proc-point the block is reachable. This is implemented using Hoopl. ``\
``  Then the call to `splitAtProcPoints` splits the Cmm graph into multiple Cmm graphs (each represents a single function) and build info tables to each of them. ``\
` When doing this we must be prepared for the fact that a proc-point does not actually exist in the graph since it was removed by stack layout pass (see #8205).`

` * `**`Attach` `continuations'` `info`
`tables`**``  (only when NOT splitting proc-points), implemented by `attachContInfoTables` in `CmmProcPoint` attaches info tables for the continuations of calls in the graph.  ``*`[PLEASE`
`WRITE` `MORE` `IF` `YOU` `KNOW` `WHY` `THIS` `IS` `!DONE]`*

` * `**`Update` `info` `tables` `to` `include` `stack`
`liveness`**`` , implemented by `setInfoTableStackMap` in `CmmLayoutStack`. Populates info tables of each Cmm function with stack usage information. Uses stack maps created by the stack layout pass. ``

` * `**`Control` `Flow`
`Optimisations`**`` , same as the beginning of the pipeline, but this pass runs only with `-O1` and `-O2`. Since this pass might produce unreachable blocks it is followed by a call to `removeUnreachableBlocksProc` (also in `CmmContFlowOpt.hs`) ``

Dumping and debugging Cmm
-------------------------

You can dump the generated Cmm code using \`-ddump-cmm\` flag. This is
helpful for debugging Cmm problems. Cmm dump is divided into several
sections:

"Cmm produced by new codegen" is emited in \`HscMain\` module after
converting STG to Cmm. This Cmm has not been processed in any way by the
Cmm pipeline. If you see that something is incorrect in that dump it
means that the problem is located in the STG-&gt;Cmm pass. The last
section, "Output Cmm", is also dumped in \`HscMain\` but this is done
after the Cmm has been processed by the whole Cmm pipeline. All other
sections are dumped by the Cmm pipeline. You can dump only selected
passes with more specific flags. For example, if you know (or suspect)
that the sinking pass is performing some incorrect transformations you
can make the dump shorter by adding \`-ddump-cmm-sp -ddump-cmm-sink\`
flags. This will produce only the "Layout Stack" dump (just before
sinking pass) and "Sink assignments" dump (just after the sinking pass)
allowing you to focus on the changes introduced by the sinking pass.

Register Allocator Code
-----------------------

The register allocator code is split into two main sections, the
register allocator proper and a generic graph coloring library. The
graph coloring library is also used by the Stg-&gt;Cmm converter.

### The register allocator

`* `[`GhcFile(compiler/nativeGen/RegLiveness.hs)`](GhcFile(compiler/nativeGen/RegLiveness.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines `` and `` which carry native machine instructions annotated with register liveness information. It also provides functions to annotate native code (``) with this liveness information, and to slurp out sets of register conflicts for feeding into the coloring allocator.`

`* `[`GhcFile(compiler/nativeGen/RegAllocColor.hs)`](GhcFile(compiler/nativeGen/RegAllocColor.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines ``, the main driver function for the graph coloring allocator. The driver accepts ``s which use virtual regs, and produces`` which use real machine regs. This module also provides functions to help build and deep seq the register conflict graph.`

`* `[`GhcFile(compiler/nativeGen/RegAllocLinear.hs)`](GhcFile(compiler/nativeGen/RegAllocLinear.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines the linear scan allocator. Its interface is identical to the coloring allocator.`

`* `[`GhcFile(compiler/nativeGen/RegAllocInfo.hs)`](GhcFile(compiler/nativeGen/RegAllocInfo.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines the register information function, ``, which takes a set of real and virtual registers and returns the actual registers used by a particular ``; register allocation is in AT&T syntax order (source, destination), in an internal function, ``; defines the `` data type`[`BR`](BR "wikilink")[`BR`](BR "wikilink")

`* `[`GhcFile(compiler/nativeGen/RegSpillCost.hs)`](GhcFile(compiler/nativeGen/RegSpillCost.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines `` which is responsible for selecting a virtual reg to spill to the stack when not enough real regs are available.`

`* `[`GhcFile(compiler/nativeGen/RegSpill.hs)`](GhcFile(compiler/nativeGen/RegSpill.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines `` which takes ``s and inserts spill/reload instructions virtual regs that wouldn't fit in real regs. ``'s strategy is to simply inserts spill/reloads for every use/def of a particular virtual reg. This inefficient code is cleaned up by the spill cleaner after allocation.`\
\
`* `[`GhcFile(compiler/nativeGen/RegSpillClean.hs)`](GhcFile(compiler/nativeGen/RegSpillClean.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  The spill cleaner is run after real regs have been allocated. It erases spill/reload instructions inserted by `` that weren't strictly nessesary.`

`* `[`GhcFile(compiler/nativeGen/RegAllocStats.hs)`](GhcFile(compiler/nativeGen/RegAllocStats.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines data types and pretty printers used for collecting statistics and debugging info from the coloring allocator.`

### Graph coloring

`* `[`GhcFile(compiler/utils/GraphBase.hs)`](GhcFile(compiler/utils/GraphBase.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines the basic ``, `` and `` types used by the coloring algorithm.`

`* `[`GhcFile(compiler/utils/GraphColor.hs)`](GhcFile(compiler/utils/GraphColor.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines the function `` which is responsible for assigning colors (real regs) to nodes (virtual regs) in the register conflict graph.`

`* `[`GhcFile(compiler/utils/GraphOps.hs)`](GhcFile(compiler/utils/GraphOps.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines functions to perform basic operations on the graphs such as adding, deleting, and coalescing nodes.`

`* `[`GhcFile(compiler/utils/GraphPps.hs)`](GhcFile(compiler/utils/GraphPps.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines functions for pretty print graphs in human readable-ish and graphviz format.`

### Miscellanea

`* `[`GhcFile(compiler/nativeGen/RegCoalesce.hs)`](GhcFile(compiler/nativeGen/RegCoalesce.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines a function `` that does aggressive coalescing directly on ``, without using the graph. This isn't used at the moment but has been left in incase we want to rejig the allocator when the new CPS converter comes online.`

`* `[`GhcFile(compiler/nativeGen/RegArchBase.hs)`](GhcFile(compiler/nativeGen/RegArchBase.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Defines utils for calculating whether a register in the conflict graph is trivially colorable, in a generic way which handles aliasing between register classes. This module is not used directly by GHC.`

`* `[`GhcFile(compiler/nativeGen/RegArchX86.hs)`](GhcFile(compiler/nativeGen/RegArchX86.hs) "wikilink")` `[`BR`](BR "wikilink")\
`  Contains a description of the aliasing constraints between the register sets on x86. This module is not used directly by GHC.`

[PageOutline](PageOutline "wikilink")

The GHC Commentary - Coding Style Guidelines for the compiler
=============================================================

This is a rough description of some of the coding practices and style
that we use for Haskell code inside . For run-time system code see the
\[wiki:Commentary/Rts/Conventions Coding Style Guidelines for RTS C
code\]. Also see the wiki page on \[wiki:WorkingConventions Working
Conventions\] for issues related to version control, workflow, testing,
bug tracking and other miscellany.

General Style
-------------

The general rule is to stick to the same coding style as is already used
in the file you're editing. If you must make stylistic changes, commit
them separately from functional changes, so that someone looking back
through the change logs can easily distinguish them.

It's much better to write code that is transparent than to write code
that is short.

Often it's better to write out the code longhand than to reuse a generic
abstraction (not always, of course). Sometimes it's better to duplicate
some similar code than to try to construct an elaborate generalisation
with only two instances. Remember: other people have to be able to
quickly understand what you've done, and overuse of abstractions just
serves to obscure the *really* tricky stuff, and there's no shortage of
that in GHC.

Comments
--------

There are two kinds of comments in source code, comments that describe
the interface (i.e. how is this supposed to be used) and comments that
describe the implementation (e.g. subtle gotchas).

### Comments on top-level entities

Every top-level entity should have a Haddock comment that describes what
it does and, if needed, why it's there. Example:

We use Haddock so that the comment is included in the generated HTML
documentation.

There's a bit of a broken window effect going on, but please try to
follow this rule for new functions you add.

### Comments in the source code

Commenting is good but

` * long comments `*`interleaved` `with` `the`
`code`*` can make the code itself incredibly hard to read, and`\
` * long comments `*`detached` `from` `the`
`code`*` are easy to miss when you are editing the code itself, and soon become out of date or even misleading.`

We have adopted a style that seems to help. Here's an example: Notice
that

`* `**`Interleaved` `with` `the`
`code`**``  is a short link `Note [Float coercions]`. You can't miss it when you are editing the code, but you can still see the code itself. ``\
`* `**`Detached` `from` `the`
`code`**``  is the linked comment, starting with the same string `Note [Float coercions]`.  It can be long, and often includes examples. ``

The standard format "\`Note \[Float coercions\]\`" serves like an URL,
to point to an out-of-line comment. Usually the target is in the same
module, but not always. Sometimes we say

Please use this technique. It's robust, and survives successive changes
to the same lines of code. When you are changing code, it draws
attention to non-obvious things you might want to bear in mind. When you
encounter the note itself you can search for the string to find the code
that implements the thoughts contained in the comment.

### Comments and examples

When writing a comment to explain a subtle point, consider including an
example code snippet that illustrates the point. For example, the above
\`Note \[Float coercions\]\` continues thus: These kind of code snippets
are extremely helpful to illustrate the point in a concrete way. Other
ways of making the comment concrete are:

`* Cite a particular Trac ticket that this bit of code deals with`\
`* Cite a test case in the test suite that illustrates it`

### Longer comments or architectural commentary

Comments with a broad scope, describing the architecture or workings of
more than one module, belong here in the commentary rather than in the
code. Put the URL for the relevant commentary page in a comment in the
code itself, and also put URLs for all relevant commentary pages in a
comment at the top of each module.

### Commit messages

Please do not use commit messages to describe how something works, or
give examples, *even if the patch is devoted to a single change*. The
information is harder to find in a commit message, and (much worse)
there is no explicit indication in the code that there is
carefully-written information available about that particular line of
code. Instead, you can refer to the Note from the commit message.

Commit messages can nevertheless contain substantial information, but it
is usually of a global nature. E.g. "This patch modifies 20 files to
implement a new form of inlining pragma". They are also a useful place
to say which ticket is fixed by the commit, summarise the changes
embodied in the commit etc.

In short, commit messages describe *changes*, whereas comment explain
the code *as it now is*.

Warnings
--------

We are aiming to make the GHC code warning-free, for all warnings turned
on by The build automatically sets these flags for all source files (see
\`mk/warnings.mk\`).

The \[wiki:TestingPatches validate script\], which is used to test the
build before commiting, additionally sets the \`-Werror\` flag, so that
the code **must** be warning-free to pass validation. The \`-Werror\`
flag is not set during normal builds, so warnings will be printed but
won't halt the build.

Currently we are some way from our goal, so some modules have a pragma;
you are encouraged to remove this pragma and fix any warnings when
working on a module.

Exports and Imports
-------------------

### Exports

 We usually (99% of the time) include an export list. The only
exceptions are perhaps where the export list would list absolutely
everything in the module, and even then sometimes we do it anyway.

It's helpful to give type signatures inside comments in the export list,
but hard to keep them consistent, so we don't always do that.

### Imports

List imports in the following order:

`* Local to this subsystem (or directory) first `\
`* Compiler imports, generally ordered from specific to generic (ie. modules from utils/ and basicTypes/ usually come last) `\
`* Library imports `\
`* Standard Haskell 98 imports last `

Import library modules from the \[wiki:Commentary/Libraries boot
packages\] only (boot packages are those packages in the file
\[source:packages\] that have a '-' in the "tag" column). Use
\`\#defines \`in \`HsVersions.h\` when the modules names differ between
versions of GHC. For code inside \`\#ifdef GHCI\`, don't worry about GHC
versioning issues, because this code is only ever compiled by the this
very version of GHC.

**Do not use explicit import lists**, except to resolve name clashes.
There are several reasons for this:

`* They slow down development: almost every change is accompanied by an import list change.`

`* They cause spurious conflicts between developers.`

`* They lead to useless warnings about unused imports, and time wasted trying to`\
`  keep the import declarations "minimal".`

`` * GHC's warnings are useful for detecting unnecessary imports: see `-fwarn-unused-imports`. ``

`` * TAGS is a good way to find out where an identifier is defined (use `make tags` in `ghc/compiler`, ``\
``   and hit `M-.` in emacs). ``

If the module can be compiled multiple ways (eg. GHCI vs. non-GHCI),
make sure the imports are properly \`\#ifdefed\` too, so as to avoid
spurious unused import warnings.

Compiler versions and language extensions
-----------------------------------------

GHC must be compilable and validate by the previous two major GHC
releases, and itself. It isn't necessary for it to be compilable by
every intermediate development version.

To maintain compatibility, use
\[wiki:Commentary/CodingStyle\#HsVersions.h HsVersions.h\] (see below)
where possible, and try to avoid using \#ifdef in the source itself.

### 

 is a CPP header file containing a number of macros that help smooth out
the differences between compiler versions. It defines, for example,
macros for library module names which have moved between versions. Take
a look
[GhcFile(compiler/HsVersions.h)](GhcFile(compiler/HsVersions.h) "wikilink").

### Literate Haskell

In GHC we use a mixture of literate () and non-literate () source. I
(Simon M.) prefer to use non-literate style, because I think the }
clutter up the source too much, and I like to use Haddock-style comments
(we haven't tried processing the whole of GHC with Haddock yet, though).

### The C Preprocessor (CPP)

Whenever possible we try to avoid using CPP, as it can hide code from
the compiler (which means changes that work on one platform can break
the build on another) and code using CPP can be harder to understand.

The following CPP symbols are used throughout the compiler:

**`DEBUG`**`:: `\
` Used to enables extra checks and debugging output in the compiler. The ASSERT macro (see ``) provides assertions which disappear when DEBUG is not defined. `

`` However, whenever possible, it is better to use `debugIsOn` from the `Util` module, which is defined to be `True` when `DEBUG` is defined and `False` otherwise.  The ideal way to provide debugging output is to use a Haskell expression "`when debugIsOn $ ...`" to arrange that the compiler will be silent when `DEBUG` is off (unless of course something goes wrong or the verbosity level is nonzero). When option `-O` is used, GHC will easily sweep away the unreachable code. ``

`` As a last resort, debugging code can be placed inside `#ifdef DEBUG`, but since this strategy guarantees that only a fraction of the code is seen be the compiler on any one compilation, it is to be avoided when possible. ``

`` Regarding performance, a good rule of thumb is that `DEBUG` shouldn't add more than about 10-20% to the compilation time. This is the case at the moment. If it gets too expensive, we won't use it. For more expensive runtime checks, consider adding a flag - see for example `-dcore-lint`. ``

**Trap, pitfall for using the ASSERT macro**:

The ASSERT macro uses CPP, and if you are unwise enough to try to write
assertions using primed variables (), one possible outcome is that CPP
silently fails to expand the ASSERT, and you get this very baffling
error message: Now you can Google for this error message :-)

**`GHCI`**`:: `\
` Enables GHCi support, including the byte code generator and interactive user interface. This isn't the default, because the compiler needs to be bootstrapped with itself in order for GHCi to work properly. The reason is that the byte-code compiler and linker are quite closely tied to the runtime system, so it is essential that GHCi is linked with the most up-to-date RTS. Another reason is that the representation of certain datatypes must be consistent between GHCi and its libraries, and if these were inconsistent then disaster could follow. `

### Platform tests

Please refer to \[wiki:Commentary/PlatformNaming Platforms and
Conventions\] wiki page for an overview of how to handle target specific
code in GHC.

Tabs vs Spaces
--------------

GHCs source code is indented with a mixture of tabs and spaces, and is
standardised on a tabstop of 8.

Most of the Haskell source code in GHC is free of tabs. We'd like to
move away from tabs in the long term, and so a git hook on
darcs.haskell.org will reject series of commits that add tabs to a file
that is currently tab-free. (Note that there are no restrictions on
adding tabs to a file already containing them.)

In order to avoid angering this git hook, you should set your editor to
indent using spaces rather than tabs:

``  * In Emacs, add `(setq-default indent-tabs-mode nil)` to your `.emacs` file ( ``[`more`
`discussion`](http://cscs.umich.edu/~rlr/Misc/emacs_tabs.htm)`)`\
``  * In Sublime Text, save the following to files at `Packages/User/Haskell.sublime-settings` and `Packages/User/Literate Haskell.sublime-settings`: ``

` * In !TextMate, in the tabs pop-up menu at the bottom of the window, select "Soft Tabs", as show in the following screenshot where the blue rectangle is:`

` `[`Image(TextMate-tabs-menu.png)`](Image(TextMate-tabs-menu.png) "wikilink")`  `

`Alternatively, open the Bundle Editor and add a new Preference called Indentation to the bundle editor. Give it the following contents:`

Coercions in GHC's core language
================================

Ever since coercions were introduced into GHC's Core language I have
treated

`* Coercions like types`\
`* Coercion variables like type variables`

In particular, casts, coercion applications, and coercion abstractoins
are all erased before we generate code.

I now think that this is the wrong approach. This note describes why.

Difficulties with the current approach
--------------------------------------

Ther are two problems with the current approach

`* Equality evidence variables ("type variables") are treated differently to dictionary evidence variables ("term varaibles"). This leads to lots of tiresome non-uniformities.`\
`` * In an abstraction `/\a\x:a.e` the type variable `a` can appear in the type of a term-variable binder `x`.  In contrast `x` can't appear in the type of another binder.  Coercion binders behave exactly like term binders in this way, and quite unlike type binders. ``\
`* More seriously, we don't have a decent way to handle superclass equalities.`

The last problem is the one that triggered this note, and needs a bit
more explanation. Consider The dictionary for C looks like this: Now
imagine typechecking a function like this The Core program we generate
looks something like this: The \`nd\` binding extracts the \`Num\`
superclass dictionary from the \`C\` dictionary; the case expression is
called a *superclass selector*.

Now suppose that we needed to use the equality superclass rather than
the \`Num\` superclass: The obvious translation would look like this:
But Core doesn't (currently) have a let-binding form that binds a
coercion variable, and whose right-hand side is a term (in this example,
a case expression) rather than a literal coercion! So the current plan
is to generate this instead: This non-uniformity of equality and
dictionary evidence is extremely awkward in the desugarer. Moreover, it
means that we can't abstract the superclass selector; we'd really like
to have: And it interacts poorly with the class-op rules that GHC uses
to simplify dictinary selectors. Imagine the call ...unfinished...

Main proposal
-------------

Recall our basic types Note that

`` * `Var` can be a type variable, coercion variable, or term variable.  You can tell which with a dynamic test (e.g. `isId :: Var -> Bool`). ``

`` * `Lam` is used for type abstractions, coercion abstractions, and value abstractions.  The `Var` can tell you which. ``

`` * Type applications (in a term) look like `(App f (Type t))`.  The `(Type t)` part must literally appear there,  with no intervening junk.  This is not statically enforced, but it turns out to be much more convenient than having a constructor `TyApp CoreExpr Type`. ``

OK now the new proposal is to *treat equality evidence just like any
other sort of evidence*.

`  * A coercion variable is treated like term-level identifier, not a type-level identifier. (More on what that means below.)`

``   * A coercion is an `CoreExpr`, of form `Coercion g`, whose type is `(s ~ t)`, of form `PredTy (EqPred s t)`. ``

``   * Unlike type applications, coercion applications are not required to have a `(Coercion g)` as the argument.  For example, suppose we have ``

``   Then the term `(f x (id (x~Int) c))` would be fine. Notice that the coercion argument is an appplication of the identity function.  (Yes it's a bit contrived.)  In `CoreExpr` form it would look like: ``

`  * Similarly a let-binding can bind a coercion`

`  * Coercion application is call-by value.  Ditto let-bindings.  You must have the evidence before calling the function.`\
\
`  * So it doesn't make sense to have recursive coercion bindings.`

``   * If we see `Let (NonRec c (Coercion g)) e` we can substitute `(Coercion g)` for any term-level occurrences of `c` in the term `e`, and `g` for `c` in any occurrences of `c` in coercions inside `e`.  (This seems a bit messy.) ``

Parsing of command line arguments
=================================

GHC's many flavours of command line flags make the code interpreting
them rather involved. The following provides a brief overview of the
processing of these options. Since the addition of the interactive
front-end to GHC, there are two kinds of flags: static and dynamic.
Static flags can only be set once on the command line. They remain the
same throughout the whole GHC session (so for example you cannot change
them within GHCi using \`:set\` or with \`OPTIONS\_GHC\` pragma in the
source code). Dynamic flags are the opposite: they can be changed in
GHCi sessions using \`:set\` command or \`OPTIONS\_GHC\` pragma in the
source code. There are few static flags and it is likely that in the
future there will be even less. Thus, you won't see many static flag
references in the source code, but you will see a lot of functions that
use dynamic flags.

Command line flags are described by Flag data type defined in
[GhcFile(compiler/main/CmdLineParser.hs)](GhcFile(compiler/main/CmdLineParser.hs) "wikilink"):

This file contains functions that actually parse the command line
parameters.

Static flags
------------

Static flags are managed by functions in
[GhcFile(compiler/main/StaticFlags.hs)](GhcFile(compiler/main/StaticFlags.hs) "wikilink").

Function \`parseStaticFlags ::\` is an entry point for parsing static
flags. It is called by the \`main :: IO ()\` function of GHC in
[GhcFile(ghc/Main.hs)](GhcFile(ghc/Main.hs) "wikilink"). Two global
IORefs are used to parse static flags: \`v\_opt\_C\_ready\` and
\`v\_opt\_C\`. These are defined using \`GLOBAL\_VAR\` macro from
[GhcFile(compiler/HsVersions.h)](GhcFile(compiler/HsVersions.h) "wikilink").
First IORef is a flag that checks whether the static flags are parsed at
the right time. Initialized to \`False\`, it is set to \`True\` after
the parsing is done. \`v\_opt\_C\` is a \`\[String\]\` used to store
parsed flags (see \`addOpt\` and \`removeOpt\` functions).

In
[GhcFile(compiler/main/StaticFlags.hs)](GhcFile(compiler/main/StaticFlags.hs) "wikilink"),
\`flagsStatic :: \[Flag IO\]\` defines a list of static flags and what
actions should be taken when these flags are encountered (see \`Flag\`
data type above). It also contains some helper functions to check
whether particular flags have been set. Functions \`staticFlags ::
\[String\]\` and \`packed\_staticFlags :: \[FastString\]\` return a list
of parsed command line static flags, provided that parsing has been done
(checking the value of \`v\_opt\_C\_ready\`).

Dynamic flags
-------------

They are managed by functions in
[GhcFile(compiler/main/DynFlags.hs)](GhcFile(compiler/main/DynFlags.hs) "wikilink")
file. Looking from the top you will find data types used to described
enabled dynamic flags: \`DumpFlag\`, \`GeneralFlag\`, \`WarningFlag\`,
\`Language\`, \`SafeHaskellMode\`, \`ExtensionFlag\` and finally
\`DynFlags\`. Function \`defaultDynFlags :: Settings -&gt; DynFlags\`
initializes some of the flags to default values. Available dynamic flags
and their respective actions are defined by \`dynamic\_flags :: \[Flag
(CmdLineP DynFlags)\]\`. Also, \`fWarningFlags :: \[FlagSpec
WarningFlag\]\`, \`fFlags :: \[FlagSpec GeneralFlag\]\`, \`xFlags ::
\[FlagSpec ExtensionFlag\]\` and a few more smaller functions define
even more flags needed for example for language extensions, warnings and
other things. These flags are descibred by the data type \`FlagSpec f\`:

 Flags described by \`FlagSpec\` can be reversed, e.g. flags that start
with \`-f\` prefix are reversed by using \`-fno-\` prefix instead.

The GHC Commentary
==================

This tree of wiki pages is a "commentary" on the GHC source code. It
contains all the explanatory material that doesn't belong in comments in
the source code itself, because the material is wide-ranging, usually
covers multiple source files, and is more architectural in nature. The
commentary can also be considered a design document for GHC.

For the beginners there is \[wiki:Newcomers a short getting started
guide\].

For the dedicated, there are \[wiki:AboutVideos videos of Simon and
Simon giving an overview of GHC\], at the 2006 \[wiki:Hackathon GHC
Hackathon\].

Also check out the \[wiki:ReadingList GHC Reading List\], which gives
lots of background reading that will help you understand the actual
implementation. Here's [another reading
list](http://www.stephendiehl.com/posts/essential_compilers.html) from
Stephen Diehl.

Editing the Commentary
----------------------

Please feel free to add material to the rest of the wiki: don't worry
too much about accuracy (in due course someone will edit your
contribution). When unsure though please indicate this and its best to
ask on the GHC mailing list so you can correct the commentary. Please
give some thought to where in the commentary your contribution belongs.
GHC has an older commentary (non wiki based) that read like a single
coherent narrative, made sure to define terms before using them, and
introduced concepts in the order which made them easiest to understand.
Please do try to preserve those properties in this wiki commentary. If
you're unsure or in a hurry, consider creating a wiki page outside the
commentary and linking to it from the commentary (or the "contributed
documentation" section below).

Try to link to source files as much as possible by using this macro: .
Also try to add appropriate links to other parts of the commentary.

Contents
--------

`* [wiki:Commentary/GettingStarted Getting Started]`\
`  * [wiki:Commentary/SourceTree Source Tree Roadmap]`\
`  * [wiki:Commentary/ModuleStructure Module Structure]`\
`  * [wiki:Commentary/CodingStyle Coding Style]`\
`  * [wiki:Commentary/Abbreviations Abbreviations in GHC]`\
`  * [wiki:Commentary/PlatformNaming Platforms and their Naming Convention]`

`* [wiki:Commentary/Compiler The Compiler]`

`* [wiki:Commentary/Libraries The Libraries on which GHC depends]`\
``   * [wiki:Commentary/Libraries/Integer The Integer libraries (`integer-gmp` and `integer-simple`)] ``

`* [wiki:Commentary/Rts The Runtime System (RTS)]`\
`   * [wiki:Commentary/Rts/Conventions RTS Coding Conventions]`\
`   * [wiki:Commentary/Rts/HaskellExecution The Haskell Execution Model]`\
`   * [wiki:Commentary/Rts/Storage The memory layout of heap and stack objects]`\
\
`* Cross-cutting concerns: topics which span both the compiler and the runtime system`\
`   * [wiki:Commentary/Profiling Profiling]`\
`   * [wiki:Commentary/Compiler/WiredIn Wired-in and known-key things]`\
`   * [wiki:Commentary/PrimOps Primitive Operations (PrimOps)]`\
`   * [wiki:Commentary/Packages The Package System]`\
\
`* [wiki:Commentary/UserManual The User Manual] (formatting guidelines etc)`

Contributed Documentation
-------------------------

The above commentary covers the source code of GHC. For material that
doesn't concern this topic (such as proposals, work-in-progress and
status reports) or that don't fit into the existing structure, you will
find them below. Feel free to add new material here but please
categorise it correctly.

`* General Notes on the GHC compiler`\
`  * Edward Yang's blog post about `[`the` `entire` `complilation`
`pipeline` `for`
`` `factorial` ``](http://blog.ezyang.com/2011/04/tracing-the-compilation-of-hello-factorial/)\
`  * [wiki:AddingNewPrimitiveOperations New Prim Ops]: How to add new primitive operations to GHC Haskell.`\
`  * [wiki:ReplacingGMPNotes Replacing GMP]: Notes from an effort to replace GMP with another Bignum library.`\
`  * [wiki:ExternalCore External Core]: Describes the process of bringing External Core up to speed. Once finished, this will simply describe what External Core is, and how it works. `\
`  * `[`The` `Scrap` `your` `boilerplate`
`homepage`](http://sourceforge.net/apps/mediawiki/developers/index.php?title=ScrapYourBoilerplate)`.`\
`  * [wiki:Commentary/Compiler/OptOrdering Optimisation Ordering] Describe the ordering and interaction of optimisation passes (Old).`\
`  * `[`GHC`
`Illustrated`](https://github.com/takenobu-hs/haskell-ghc-illustrated)` (follow the PDF link), a very insightful tutorial on GHC's internals.`\
`  * `[`Ollie` `Charles's` `24` `days` `of` `GHC`
`Extensions`](https://ocharles.org.uk/blog/pages/2014-12-01-24-days-of-ghc-extensions.html)`, and `[`Lennart`
`Augstsson's`
`commentary`](http://augustss.blogspot.com/2014/12/a-commentary-on-24-days-of-ghc.html)\
`    * `[`Welcome`](https://ocharles.org.uk/blog/posts/2014-12-01-24-days-of-ghc-extensions.html)\
`    * `[`Static`
`Pointers`](https://ocharles.org.uk/blog/guest-posts/2014-12-23-static-pointers.html)\
`    * `[`Template`
`Haskell`](https://ocharles.org.uk/blog/guest-posts/2014-12-22-template-haskell.html)\
`    * `[`Arrows`](https://ocharles.org.uk/blog/guest-posts/2014-12-21-arrows.html)\
`    * `[`Scoped` `Type`
`Variables`](https://ocharles.org.uk/blog/guest-posts/2014-12-20-scoped-type-variables.html)\
`    * `[`Existential`
`Quantification`](https://ocharles.org.uk/blog/guest-posts/2014-12-19-existential-quantification.html)\
`    * `[`Rank` `N`
`Types`](https://ocharles.org.uk/blog/guest-posts/2014-12-18-rank-n-types.html)\
`    * `[`Overloaded`
`Strings`](https://ocharles.org.uk/blog/posts/2014-12-17-overloaded-strings.html)\
`    * `[`DeriveGeneric`](https://ocharles.org.uk/blog/posts/2014-12-16-derive-generic.html)\
`    * `[`Deriving`](https://ocharles.org.uk/blog/guest-posts/2014-12-15-deriving.html)\
`    * `[`Functional`
`Dependencies`](https://ocharles.org.uk/blog/posts/2014-12-14-functional-dependencies.html)\
`    * `[`Multi-parameter` `Type`
`Classes`](https://ocharles.org.uk/blog/posts/2014-12-13-multi-param-type-classes.html)\
`    * `[`Type`
`Families`](https://ocharles.org.uk/blog/posts/2014-12-12-type-families.html)\
`    * `[`Implicit`
`Parameters`](https://ocharles.org.uk/blog/posts/2014-12-11-implicit-params.html)\
`    * `[`Nullary` `Type`
`Classes`](https://ocharles.org.uk/blog/posts/2014-12-10-nullary-type-classes.html)\
`    * `[`Recursive`
`Do`](https://ocharles.org.uk/blog/posts/2014-12-09-recursive-do.html)\
`    * `[`Type`
`Operators`](https://ocharles.org.uk/blog/posts/2014-12-08-type-operators.html)\
`    * `[`List`
`Comprehensions`](https://ocharles.org.uk/blog/guest-posts/2014-12-07-list-comprehensions.html)\
`    * `[`Rebindable`
`Syntax`](https://ocharles.org.uk/blog/guest-posts/2014-12-06-rebindable-syntax.html)\
`    * `[`Bang`
`Patterns`](https://ocharles.org.uk/blog/posts/2014-12-05-bang-patterns.html)\
`    * `[`Record`
`Wildcards`](https://ocharles.org.uk/blog/posts/2014-12-04-record-wildcards.html)\
`    * `[`Pattern`
`Synonyms`](https://ocharles.org.uk/blog/posts/2014-12-03-pattern-synonyms.html)\
`    * `[`View`
`Patterns`](https://ocharles.org.uk/blog/posts/2014-12-02-view-patterns.html)\
`    * `[`Thanks`](https://ocharles.org.uk/blog/posts/2014-12-24-conclusion.html)\
`  * [wiki:Commentary/Rts/CompilerWays]: Compiler `*`ways`*` in GHC, what, how, and where`

`* Notes on implemented GHC features:`\
`  * `[`Evaluation` `order` `and` `state`
`tokens`](https://www.fpcomplete.com/tutorial-preview/4431/z0KpB0ai2R)`: notes written by Michael Snoyberg in response to #9390.`\
`  * [wiki:FoldrBuildNotes Notes on fusion] (eg foldr/build)`\
`  * [wiki:OverloadedLists Overloaded list syntax] allows you to use list notation for things other than lists.`\
`  * [wiki:GhcKinds Kind polymorphism and data type promotion]`\
`  * [wiki:KindFact A kind for class constraints. Implemented as ConstraintKinds]`\
`  * [wiki:Commentary/Compiler/Backends/LLVM LLVM back end]`\
`  * [wiki:Commentary/Compiler/GenericDeriving Support for generic programming]`\
`  * [wiki:TemplateHaskell Notes about Template Haskell]`\
`  * [wiki:RewriteRules Rewrite Rules]: Notes about the implementation of RULEs in GHC`\
`  * [wiki:MonadComprehensions Monad Comprehensions]: Translation rules and some implementation details `\
`  * [wiki:HaddockComments Haddock]: Some notes about how the Haddock comment support is implemented.  `\
`  * [wiki:IntermediateTypes Intermediate Types]: Notes about the type system of GHC's new intermediate language (in the HEAD since ICFP'06)  `\
`  * [wiki:TypeFunctions Type families/type functions]: Notes concerning the implementation of type families, associated types, and equality constraints as well as the extension of the type checker with a contraint solver for equality constraints.`\
``   * [wiki:Commentary/Compiler/SeqMagic Magic to do with `seq` and friends] ``\
`  * [wiki:NewPlugins Compiler plug-ins]`\
`  * [wiki:MemcpyOptimizations memcpy/memmove/memset optimizations]  `\
`  * [wiki:BackEndNotes Backend Ideas]: Some ideas and notes about the back end.`\
`  * [wiki:Commentary/Compiler/NewCodeGen Notes about the new code generator]`\
`  * [wiki:Commentary/Compiler/HooplPerformance A record of improvements made to the performance of the Hoopl library for dataflow optimisation]`\
`  * [wiki:DataParallel DPH]: Notes about the implementation of Data Parallel Haskell`\
`  * [wiki:SafeHaskell Safe Haskell]: The design of the GHC Safe Haskell extension`\
`  * [wiki:SQLLikeComprehensions SQL-Like Comprehensions]: Notes on SPJs "Comprehensive Comprehensions" (!TransformComprehensions)`\
``   * [wiki:DeferErrorsToRuntime Deferring compilation type errors to runtime (`-fdefer-type-errors`)] ``\
`  * [wiki:Commentary/Compiler/Demand Demand analyser] Notes on the meanings, worker-wrapper splitting of demand signatures and relevant components of the compiler`\
`  * [wiki:NewAxioms Closed type families]`\
``   * [wiki:OneShot] The magic `oneShot` function. ``\
`  * [wiki:Commentary/Compiler/DeriveFunctor Deriving Functor, Foldable, and Traversable]`

`* Notes on proposed or in progress (but out of tree) GHC compiler features:`\
`  * [wiki:LanguageStrict Making Haskell strict]`\
`  * [wiki:PatternMatchCheck Improving pattern-match overlap and exhaustiveness checks]`\
`  * [wiki:GhcAstAnnotations Source-locations on HsSyn]`\
`  * [wiki:CabalDependency How GHC inter-operates with Cabal] and [wiki:Backpack]`\
`  * [wiki:StaticValues] and ticket #7015`\
`  * [wiki:PartialTypeSignatures Partial type signatures] and its ticket #9478`\
`  * [wiki:LateLamLift Late lambda-lifting], and its ticket #9476`\
`  * [wiki:Roles Roles in Haskell]`\
`  * [wiki:DependentHaskell Dependent types in Haskell]`\
`  * [wiki:NestedCPR Nested CPR analysis]`\
`  * [wiki:TemplateHaskell/Annotations Giving Template Haskell full access to annotations]`\
`  * [wiki:FunDeps Checking consistency of functional dependencies]`\
`  * [wiki:Commentary/GSoCMultipleInstances Allowing multiple instances of the same package to be installed], each instance having different dependencies`\
`  * [wiki:Commentary/Contracts Contracts in Haskell]`\
`  * [wiki:Holes Agda-style holes in terms] which supports writing partial programs.`\
`  * [wiki:Records Records]`\
`  * `[`Cloud`
`Haskell`](http://haskell.org/haskellwiki/GHC/CouldAndHPCHaskell)\
`  * [wiki:PackageLanguage A modular package language for Haskell] Scott Kilpatrick and Derek Dreyer are designing a new `

Compiler and runtime system ways in GHC
=======================================

GHC can compile programs in different *ways*. For instance, a program
might be compiled with profiling enabled (\`-prof\`), or for
multithreaded execution (\`-threaded\`), or maybe making some debugging
tools available (\`-debug\`, see Debugging/RuntimeSystem for a
description).

There are two types of GHC ways, RTS-only ways and full ways.

-   **Runtime system (RTS) ways** affect the way that the runtime system
    is built. As an example, \`-threaded\` is a runtime system way. When
    you compile a program with \`-threaded\`, it will be linked to
    a (precompiled) version of the RTS with multithreading enabled.

Obviously, the compiler's RTS must have been built for this way (the
threaded RTS is activated by default BTW). In customised builds, an RTS
way can be added in the build configuration \`mk/build.mk\` (see
[GhcFile(mk/build.mk.sample)](GhcFile(mk/build.mk.sample) "wikilink")),
by adding its *short name* to the variable \`GhcRTSWays\`.

-   **Full ways**

Full compiler ways are ways which affect both the generated code and the
runtime system that runs it.

The profiling way \`-prof\` is such a way. The machine code of a program
compiled for profiling differs from a normal version's code by all code
that gathers the profiling information, and the runtime system has
additional functionality to access and report this information.
Therefore, all libraries used in a profiling-enabled program need to
also have profiling enabled, i.e. a separate library version for
profiling needs to be installed to compile the program with \`prof\`.
(If the library was installed without this profiling version, the
program cannot be linked).

In customised builds, a full way is added in the build configuration
\`mk/build.mk\` by adding its tag to the variable \`GhcLibWays\`.

Available ways in a standard GHC
--------------------------------

Ways are identified internally by a way name, and enabled by specific
compilation flags. In addition, there are short names (tags) for the
available ways, mainly used by the build system.

Here is a table of available ways in a standard GHC, as of May 2015.

||=Way flag =||= Way name =||= Tag =||= Type =||= Description =|| ||= -
=|| - || \`v\` || Full || (vanilla way) default || ||=\`-threaded\` =||
WayThreaded || \`thr\` || RTS || multithreaded runtime system ||
||=\`-debug\` =|| WayDebug || \`debug\` || RTS || debugging, enables
trace messages and extra checks || ||=\`-prof\` =|| WayProf || \`p\` ||
Full || profiling, enables cost centre stacks and profiling reports ||
||=\`-eventlog\` =|| WayEventLog || \`l\` || RTS || Event logging (for
ghc-events, threadscope, and EdenTV) || ||=\`-dyn\` =|| WayDyn ||
\`dyn\` || Full || Dynamic linking ||

The standard (*vanilla*) way of GHC has a name (*vanilla*), but it could
(probably?) even be switched off in a custom build if desired.
Obviously, the libraries would still need to be built in the vanilla way
for all RTS-only ways, so one would need \`GhcLibWays=v\` when building
any other RTS-only way.

The code (see below) contains another way, for Glasgow parallel Haskell,
which is currently unmaintained (\`WayPar\`).

### Ways for parallel execution on clusters and multicores

The parallel Haskell runtime system for Eden (available from
<http://github.com/jberthold/ghc>) defines several RTS-only ways for
Eden. All these ways execute the RTS in multiple instances with
distributed heaps, they differ in the communication substrate (and
consequently in the platform).

||=Way flag =||= Way name =||= Tag =||= Type =||= communication (OS) =||
||=\`-parpvm\` =|| WayParPvm ||\`pp\`|| RTS || PVM (Linux) ||
||=\`-parmpi\` =|| WayParMPI ||\`pm\`|| RTS || MPI (Linux) ||
||=\`-parcp\` =|| WayParCp ||\`pc\`|| RTS || OS-native shared memory
(Windows/Linux) || ||=\`-parms\` =|| WayParMSlot ||\`ms\`|| RTS ||
Windows mail slots (Windows) ||

Combining ways
--------------

The alert reader might have noticed that combinations like "threaded
with dynamic linking" or "profiled with eventlog" are not covered in the
table. Some ways can be used together (most prominently, debugging can
be used together with any other way), others are mutually excluding each
other (like profiling with eventlog).

The allowed combinations are defined inside the compiler, in
[GhcFile(compiler/main/DynFlags.hs)](GhcFile(compiler/main/DynFlags.hs) "wikilink").
Which brings us to discussing some of the internals.

Internals
=========

Ways are defined in
[GhcFile(compiler/main/DynFlags.hs)](GhcFile(compiler/main/DynFlags.hs) "wikilink")
as a Haskell data structure \`Way\`.

Function \`dynamic\_flags\` defines the actual flag strings for the ghc
invocation (like \`-prof\`, \`-threaded\`), which activate the
respective \`Way\`.

The short name tags for ways are defined in \`wayTag\`. The tags are
used in the suffixes of \*.o and \*.a files for RTS and libraries, for
instance \`\*.p\_o\` for profiling, \`\*.l\_o\` for eventlog.

A number of other functions in there customise behaviour depending on
the ways. Note \`wayOptc\` which sets some options for the C compiler,
like \`-DTRACING\` for the \`-eventlog\` way.

However, this is not the full truth. For instance, there is no
\`-DDEBUG\` for the debug way here, but the RTS is full of \`\#ifdef
DEBUG\`.

In [GhcFile(mk/ways.mk)](GhcFile(mk/ways.mk) "wikilink"), we find all
the short names and all combinations enumerated, and some more options
are defined here (\`WAY\_\*\_HC\_OPTS\`). These definitions are for the
driver script, and pass on the right (long-name) options to the Haskell
compiler to activate what is inside DynFlags (like -prof for
WAY\_p\_HC\_OPTS). Here we find \`\`\`WAY\_debug\_HC\_OPTS= -static
-optc-DDEBUG -ticky -DTICKY\_TICKY\`\`\` so we can learn that ticky
profiling is activated by compiling with \`debug\`.

(TODO be more precise on where the options from ways.mk are used.)

GHC Commentary: The Compiler
============================

The compiler itself is written entirely in Haskell, and lives in the
many sub-directories of the
[GhcFile(compiler)](GhcFile(compiler) "wikilink") directory.

`* [wiki:ModuleDependencies Compiler Module Dependencies] (deals with the arcane mutual recursions among GHC's many data types)`\
`* [wiki:Commentary/CodingStyle Coding guidelines]`

`* [wiki:Commentary/Compiler/CommandLineArgs Command line arguments] `\
`* [wiki:Commentary/Pipeline The compilation pipeline]`

`* `**`Compiling` `one` `module:` `!HscMain`**\
`  * [wiki:Commentary/Compiler/HscMain Overview] gives the big picture. `\
`  * Some details of the [wiki:Commentary/Compiler/Parser parser]`\
`  * Some details of the [wiki:Commentary/Compiler/Renamer renamer]`\
`  * Some details of the [wiki:Commentary/Compiler/TypeChecker typechecker]`\
`  * Some details of the [wiki:Commentary/Compiler/Core2CorePipeline simplifier]`\
`  * Some details of the [wiki:Commentary/Compiler/CodeGen code generator] converts STG to Cmm`\
`  * [wiki:Commentary/Compiler/Backends Backends] convert Cmm to native code:`\
`    * [wiki:Commentary/Compiler/Backends/PprC C code generator]`\
`    * [wiki:Commentary/Compiler/Backends/NCG Native code generator]`\
`    * [wiki:Commentary/Compiler/Backends/LLVM LLVM backend]`\
`    * [wiki:Commentary/Compiler/Backends/GHCi GHCi backend]`\
`  * A guide to the [wiki:Commentary/Compiler/GeneratedCode generated assembly code]`

`* [wiki:Commentary/Compiler/KeyDataTypes Key data types]`\
`  * [wiki:Commentary/Compiler/HsSynType The source language: HsSyn] `\
`  * [wiki:Commentary/Compiler/RdrNameType RdrNames, Modules, and OccNames]`\
`  * [wiki:Commentary/Compiler/ModuleTypes ModIface, ModDetails, ModGuts]`\
`  * [wiki:Commentary/Compiler/NameType Names]`\
`  * [wiki:Commentary/Compiler/EntityTypes Entities]: variables, type constructors, data constructors, and classes.`\
`  * Types: `\
`    * [wiki:Commentary/Compiler/TypeType Types]`\
`    * [wiki:Commentary/Compiler/Kinds Kinds]`\
`    * [wiki:Commentary/Compiler/FC Equality types and coercions]`\
`  * [wiki:Commentary/Compiler/CoreSynType The core language]`\
`  * [wiki:Commentary/Compiler/StgSynType The STG language]`\
`  * [wiki:Commentary/Compiler/CmmType The Cmm language]`\
`  * [wiki:Commentary/Compiler/BackEndTypes Back end types]`\
\
`* [wiki:Commentary/Compiler/Driver Compiling more than one module at once]`\
`* [wiki:Commentary/Compiler/DataTypes How data type declarations are compiled]`\
`* [wiki:Commentary/Compiler/API The GHC API]`\
`* [wiki:Commentary/Compiler/SymbolNames Symbol names and the Z-encoding]`\
`* [wiki:TemplateHaskell/Conversions Template Haskell]`\
`* [wiki:Commentary/Compiler/WiredIn Wired-in and known-key things]`\
`* [wiki:Commentary/Compiler/Packages Packages]`\
`* [wiki:Commentary/Compiler/RecompilationAvoidance Recompilation Avoidance]`

Case studies:

`* [wiki:Commentary/Compiler/CaseStudies/Bool Implementation of wired-in Bool data type]`

Overall Structure
-----------------

Here is a block diagram of its top-level structure:

[Image(ghc-top.png)](Image(ghc-top.png) "wikilink")

The part called \[wiki:Commentary/Compiler/HscMain HscMain\] deals with
compiling a single module. On top of this is built the **compilation
manager** (in blue) that manages the compilation of multiple modules. It
exports an interface called the **GHC API**. On top of this API are four
small front ends:

`* GHCi, the interactive environment, is implemented in `[`GhcFile(ghc/InteractiveUI.hs)`](GhcFile(ghc/InteractiveUI.hs) "wikilink")` and `[`GhcFile(compiler/main/InteractiveEval.hs)`](GhcFile(compiler/main/InteractiveEval.hs) "wikilink")`. It sits squarely on top of the GHC API.`\
\
`* `` is almost a trivial client of the GHC API, and is implemented in `[`GhcFile(compiler/main/GhcMake.hs)`](GhcFile(compiler/main/GhcMake.hs) "wikilink")`. `

`* ``, the Makefile dependency generator, is also a client of the GHC API and is implemented in `[`GhcFile(compiler/main/DriverMkDepend.hs)`](GhcFile(compiler/main/DriverMkDepend.hs) "wikilink")`. `

`* The "one-shot" mode, where GHC compiles each file on the command line separately (eg. ``). This mode bypasses the GHC API, and is implemented`\
`  directly on top of [wiki:Commentary/Compiler/HscMain HscMain], since it compiles only one file at a time. In fact, this is all that   `\
``   GHC consisted of prior to version 5.00 when GHCi and `--make` were introduced. ``

GHC is packaged as a single binary in which all of these front-ends are
present, selected by the command-line flags indicated above. There is a
single command-line interface implemented in
[GhcFile(ghc/Main.hs)](GhcFile(ghc/Main.hs) "wikilink").

In addition, GHC is compiled, without its front ends, as a *library*
which can be imported by any Haskell program; see
\[wiki:Commentary/Compiler/API the GHC API\]. Package keys, installed
package IDs, ABI hashes, package names and versions, Nix-style hashes,
... there's so many different identifiers, what do they all mean? I
think the biggest source of confusion (for myself included) is keeping
straight not only what these terms mean, but also what people want them
to mean in the future, and what we //actually// care about. So I want to
help clarify this a bit, by clearly separating the //problem you are
trying to solve// from //how you are solving the problem//.

The content here overlaps with wiki:Commentary/Packages but is looking
at the latest iteration of the multi-instances and Backpack work.

See also \`Note \[The identifier lexicon\]\` in
\`compiler/basicTypes/Module.hs\`.

Some relevant tickets: \#10622

What problems do we need to solve?
----------------------------------

When we come up with identification schemes for packages, we are trying
to solve a few problems:

`[SYMBOL]::`\
`  What symbol names should we put in the binary? (e.g., the "foozm0zi1" in   "foozm0zi1_A_DZCF_closure")`\
`       - It must be unique enough that for all libraries we would`\
`         like to be able to link together, there should not be`\
`         conflicts.`\
`       - HOWEVER, it must be stable enough that if we make a minor`\
`         source code change, we don't have to gratuitously recompile`\
`         every dependency.`

`[ABI]::`\
` When can I swap out one compiled package with another WITHOUT recompiling, i.e. what is the ABI of the package? Equal ABIs implies equal symbols, though not vice versa. ABI is usually computed after compilation is complete.`\
`       - ABI can serve as correctness condition: if we link against a specific ABI, we can be sure that anything with an equivalent ABI won't cause our package to segfault.`\
`       - ABI can also serve as an indirection: we linked against an ABI, anything that is compatible can be hotswapped in without compilation. In practice, this capability is rarely used by users because it's quite hard to compile a package multiple times with the same ABI, because (1) compilation is nondeterministic, and (2) even if no types change, a change in implementation can cause a different exported unfolding, which is ABI relevant.`

`[SOURCE]::`\
` What is the unit of distribution? In other words, when a maintainer uploads an sdist to Hackage, how do you identify that source tarball?`\
`       - On Hackage, a package name plus version uniquely identifies an`\
`         sdist.  This is enforced by community standards; in a local`\
`         development environment, this may not hold since devs will edit`\
`         code without updating the version number. Call this [WEAK SOURCE].`\
`       - Alternately, a cryptographic hash of the source code uniquely`\
`         identifies the stream of bytes.  This is enforced by math. Call this [STRONG SOURCE].`

`[LIBRARY]::`\
``   When you build a library, you get an `libfoo.so` file. What identifies an OS level library? ``

`[NIX]::`\
`  What is the full set of source which I can use to reproduceably build a build product?`\
`       - In today's Cabal, you could approximate this by taking [WEAK SOURCE] of a package, as well as all of its transitive dependencies. Call this [WEAK NIX].`\
`       - The Nix approach is to ensure deterministic builds by taking the hash of the source [STRONG SOURCE] and also recursively including the [NIX] of each direct dependency. Call this [STRONG NIX].`\
`       - Note that [ABI] does NOT imply [NIX]; a package might be binary compatible but do something different, and in a Nix model they should be recorded differently.`

`[TYPES]::`\
`  When are two types the same?  If there are from differing packages, they are obviously different; if they are from the same package, they might still be different if the dependencies were different in each case.`\
`       - Types show up in error message, so this is a USER VISIBLE`\
`         notion.  Many people have (cogently) argued that this should`\
`         be AS SIMPLE as possible, because there's nothing worse`\
`         than being told that Data.ByteString.ByteString is not`\
`         equal to Data.ByteString.ByteString (because they were from`\
`         different packages.)`

Current mechanisms
------------------

Today, we have a lot of different MECHANISMS for identifying these:

`   Package Name::`\
`       Something like "lens"`

`   Package Version::`\
`       Something like "0.1.2"`

`   (Source) Package ID::`\
`       Package name plus version.  With Hackage today, this identifies a unit of distribution: given a package ID you can download a source tarball [SOURCE] of a package (but not build it). Pre-GHC 7.10, the package ID was used for library identification, symbols and type-checking ([LIBRARY], [SYMBOL] and [TYPES]), but this is no longer the case.`

`   Installed Package ID::`\
`       Package name, package version, and the output of ghc --abi-hash.  This is currently used to uniquely identify a built package, although technically it only identifies [ABI].`

`   Package Key (new in 7.10)::`\
`       Hash of package name, package version, the package keys of all`\
`       textual dependencies the package included, and in Backpack`\
`       a mapping from hole name to module by package key.`\
`       In GHC 7.10 this is used for library identification, symbols and type-checking ([LIBRARY], [SYMBOL] and [TYPES]).  Because it includes package keys of textual dependencies, it also distinguishes between different dependency resolutions, ala [WEAK NIX].`

New concepts for Backpack
-------------------------

First, we have to take the concept of an InstalledPackageId and make it
more precise, having it identity components rather than packages.

`   Component ID::`\
``        The package name, the package version, the name of the component (blank in the case of the default library component), and the hash of source code sdist tarball, selected Cabal flags (not the command line flags), GHC flags, hashes of direct dependencies of the component (the `build-depends` of the library in the Cabal file). ``

Then in Backpack we have these concepts:

`   Indefinite/definite unit::`\
`       An indefinite unit is a single unit which hasn't been instantiated; a definite unit is one that has an instantiation of its holes.  Units without holes are both definite and indefinite (they can be used for both contexts).`

`   Indefinite unit record (in "logical" indefinite unit database)::`\
`       An indefinite unit record is the most general result of type-checking a unit without any of its holes instantiated.  It consists of the types of the modules in the unit (ModIfaces) as well as the source code of the unit (so that it can be recompiled into a definite unit). Indefinite unit records can be installed in the "indefinite unit database."`

`   Definite unit record (previously installed package record, in the definite unit database, previously the installed package database)::`\
`       A definite unit record is a fully-instantiated unit with its associated library. It consists of the types and objects of the compiled unit; they also contain metadata for their associated package.  Definite unit records can be installed in the "definite unit database" (previously known as the "installed package database.")`

To handle these, we need some new identifiers:

`   Unit Id (previously named Package Key)::`\
`       For Backpack units, the unit ID is the component ID plus a mapping from holes to modules (unit key plus module name). For non-Backpack units, the unit ID is equivalent to the component source hash (the hole mapping is empty). These serve the role of [SYMBOL, LIBRARY, TYPES]. (Partially definite unit keys can occur on-the-fly during type checking.) When all of the requirements are filled (so there is no occurrence of HOLE), the unit key serves as the primary key for the installed unit database. (We might call this an "installed unit ID" in this context) The unit ID "HOLE" is a distinguished unit ID, which is for the "hole package", representing modules which are not yet implemented (there is not actually a unit named hole, it's just a notational convention).`

`   Module::`\
`       A unit ID plus a module name.`

Features
--------

There are a number of enhancements proposed for how Cabal handles
packages, which have often been conflated together. I want to clearly
separate them out here:

` Non-destructive installs::`\
`   If I have package foo-0.2 compiled against bar-0.1, and a different build compiled against bar-0.2, I should be able to put them in the same installed package database.  THIS IS HIGH PRIORITY.`

` Views::`\
`   If I have package foo compiled against bar-0.1, and baz compiled against bar-0.2, these two packages aren't usable together (modulo private dependencies, see below).  Views are a UI paradigm making it easier for users to work in a universe where foo is available, or a universe where baz is available, but not both simultaneously. Cabal sandboxes are views but without a shared installed package database.  This is lower priority, because if you use cabal-install to get a coherent dependency set, you'll never see both foo and baz at the same time; the primary benefit of this is to assist with direct use of GHC/GHCi, however, it is generally believed that non-destructive installs will make it difficult to use GHC/GHCi by itself.`

` Private dependencies::`\
`   If I have a package foo-0.2 which depends on a library bar-0.1, but not in any externally visible way, it should be allowed for a client to separately use bar-0.2. This is LOW priority; amusingly, in 7.10, this is already supported by GHC, but not by Cabal.`

` Hot swappable libraries::`\
`   If I install a library and it's assigned ABI hash 123abc, and then I install a number of libraries that depend on it, hot swappable library means that I can replace that installed library with another version with the same ABI hash, and everything will keep working. This feature is accidentally supported by GHC today, but no one uses it (because ABIs are not stable enough); we are willing to break this mode of use to support other features.`

Constraints
-----------

For an implementer, it is best if each problem is solved separately.
However, Simon has argued strongly it is best if we REDUCE the amount of
package naming concepts. You can see this in pre-7.10 GHC, where the
package ID (package name + version) was used fulfill many functions:
linker symbols, type identity as well as being a unit of distribution.

So the way I want to go about arguing for the necessity of a given
identifier is by showing that it is IMPOSSIBLE (by the intended
functions) for a single identifier to serve both roles. Here are the
main constraints:

`- [SYMBOL] and [STRONG NIX]/[STRONG SOURCE] don't play nicely together.  If you modify your source code, a [STRONG NIX/SOURCE] identifier must change; if this means [SYMBOL] changes too, you will have to recompile everything. However, you can work around this problem by using fake identifiers during development to avoid recompilation, recompiling with the correct NIX identifier when it's finally time to install.`

`- [SOURCE] and [TYPES] are incompatible under non-destructive installs and private dependencies. With private dependencies (which GHC supports!), I may link against the multiple instances of the same source but compiled against different dependencies; we MUST NOT consider these types to be the same. Note: GHC used to use package ID for both of these; so coherence was guaranteed by requiring destructive installs.`

`- [NIX] and [TYPES] are incompatible under Backpack.  In Backpack, a library author may distribute a package with the explicit intent that it may be used in the same client multiple times with different instantiations of its holes; these types must be kept distinct.`

RTS Configurations
==================

The RTS can be built in several different ways, corresponding to global
CPP defines. The flavour of the RTS is chosen by GHC when compiling a
Haskell program, in response to certain command-line options: , , etc.

The CPP symbols and their corresponding command-line flags are:

`::`\
` Enables profiling.`[`br`](br "wikilink")\
` GHC option: `[`br`](br "wikilink")\
` RTS suffix: `

`::`\
` Enables multithreading in the RTS, bound threads, and SMP execution.`[`br`](br "wikilink")\
` GHC option: `[`br`](br "wikilink")\
` RTS suffix: `

`::`\
` Enables extra debugging code, assertions, traces, and the `` options.`[`br`](br "wikilink")\
` GHC option: `[`br`](br "wikilink")\
` RTS suffix: `

`::`\
` Enables RTS tracing and event logging, see `[`GhcFile(rts/Trace.c)`](GhcFile(rts/Trace.c) "wikilink")`` .  Implied by `DEBUG`. ``[`br`](br "wikilink")\
` GHC option: `[`br`](br "wikilink")\
` RTS suffix: `

So for example, is the version of the runtime compiled with and , and
will be linked in if you use the and options to GHC.

The ways that the RTS is built in are controlled by the Makefile
variable.

Combinations
------------

All combinations are allowed. Only some are built by default though; see
\[source:mk/config.mk.in\] to see how the \`GhcRTSWays\` variable is
set.

Other configuration options
---------------------------

`::`\
``  Disabled the use of hardware registers for the stack pointer (`Sp`), heap pointer (`Hp`), etc.  This is ``\
``  enabled when building "unregisterised" code, which is controlled by the `GhcUnregisterised` build option. ``\
` Typically this is necessary when building GHC on a platform for which there is no native code generator`\
` and LLVM does not have a GHC calling convention.`

`::`\
` Enables the use of the RTS "mini-interpreter", which simulates tail-calls.  Again, this is enabled by`\
``  `GhcUnregisterised` in the build system. ``

`::`\
` Controls whether the info table is placed directly before the entry code for a closure or return continuation.`\
``  This is normally turned on if the platform supports it, but is turned off by `GhcUnregisterised`. ``

Contracts for Haskell
=====================

Involved
--------

`* Simon Peyton-Jones`\
`* Dimitrios Vytiniotis`\
`* Koen Claessen`\
`* Charles-Pierre Astolfi`

Overview
--------

Contracts, just as types, give a specification of the arguments and
return values of a function. For example we can give to head the
following contract:

Where Ok means that the result of head is not an error/exception as long
as the argument isn't.

Any Haskell boolean expression can be used in a contract, for example is
a contract that means that for every a which is an actual integer (not
an error), then fac a &gt;= a

We can also use a higher-order contracts: This contract means that if we
apply map to a non-empty list with a function that takes a non-negative
integer and returns an positive integer then map returns a list of
values without errors.

For a formal introduction, one can read \[1\].

The plan
--------

Verifying that a function satisfies a given contract is obviously
undecidable, but that does not mean that we can't prove anything
interesting. Our plan is to translate Haskell programs to first-order
logic (with equality) and then use Koen's automated theorem prover to
check contract satisfaction. Given that first-order logic is only
semi-decidable, the theorem prover can (and in fact does) hang when fed
with contracts that are in contradiction with the function definition.

Current status
--------------

The current status is described in \[3\] and some code and examples can
be found in \[2\]. Note that given it's just a prototype the input
syntax is slightly different from Haskell. In the end, we should get a
ghc extension for contracts.

Questions
---------

`* Do we need cfness predicate anymore? It was important in the POPL paper but is still relevant?`\
`* UNR should be renamed to a less confusing name.`\
`* Hoare logic vs liquid types`\
`* Semantics & domain theory to prove the correctness of the translation`\
`* Unfolding for proving contracts on recursive functions`

References
----------

\[1\] :
<http://research.microsoft.com/en-us/um/people/simonpj/papers/verify/index.htm>
[BR](BR "wikilink") \[2\] : <https://github.com/cpa/haskellcontracts>
and <https://github.com/cpa/haskellcontracts-examples>
[BR](BR "wikilink") \[3\] :
<https://github.com/cpa/haskellcontracts/blob/master/draft2.pdf>

The GHC Commentary: Coding Style Guidelines for RTS C code
==========================================================

Comments
--------

These coding style guidelines are mainly intended for use in and . See
\[wiki:Commentary/CodingStyle Coding Style Guidelines\] for code in .

These are just suggestions. They're not set in stone. Some of them are
probably misguided. If you disagree with them, feel free to modify this
document (and make your commit message reasonably informative) or mail
someone (eg. [The GHC mailing
list](mailto:glasgow-haskell-users@haskell.org))

References
----------

If you haven't read them already, you might like to check the following.
Where they conflict with our suggestions, they're probably right.

`* The C99 standard.  One reasonable reference is `[`here`](http://home.tiscalinet.ch/t_wolf/tw/c/c9x_changes.html)`.`

`* Writing Solid Code, Microsoft Press. (Highly recommended.)`

`* Autoconf documentation. See also`\
`  `[`The` `autoconf` `macro`
`archive`](http://peti.gmd.de/autoconf-archive/)\
`  and `[`Cyclic` `Software's`
`description`](http://www.cyclic.com/cyclic-pages/autoconf.html)`.`

`* `[`Indian` `Hill` `C` `Style` `and` `Coding`
`Standards`](http://www.cs.arizona.edu/~mccann/cstyle.html)

`* `[`A` `list` `of` `C` `programming` `style`
`links`](http://www.cs.umd.edu/users/cml/cstyle/)

`* `[`A` `very` `large` `list` `of` `C` `programming`
`links`](http://www.lysator.liu.se/c/c-www.html)

Portability issues
------------------

### Which C Standard?

We try to stick to C99 where possible. We use the following C99 features
relative to C89, some of which were previously GCC extensions (possibly
with different syntax):

`* Variable length arrays as the last field of a struct.  GCC has`\
`  a similar extension, but the syntax is slightly different: in GCC you`\
`  would declare the array as ``, whereas in C99 it is`\
`  declared as ``.`

`* Inline annotations on functions (see later)`

`* Labeled elements in initialisers.  Again, GCC has a slightly`\
`  different syntax from C99 here, and we stick with the GCC syntax`\
`  until GCC implements the C99 proposal.`

`* C++-style comments.  These are part of the C99 standard, and we`\
`  prefer to use them whenever possible.`

In addition we use ANSI-C-style function declarations and prototypes
exclusively. Every function should have a prototype; static function
prototypes may be placed near the top of the file in which they are
declared, and external prototypes are usually placed in a header file
with the same basename as the source file (although there are exceptions
to this rule, particularly when several source files together implement
a subsystem which is described by a single external header file).

`* We use the following GCC extensions, but surround them with ``:`\
`  * Function attributes (mostly just `` and ``)`\
`  * Inline assembly.`

### Other portability conventions

`* char can be signed or unsigned - always say which you mean`

`* Our POSIX policy: try to write code that only uses POSIX`\
`  (`[`IEEE` `Std`
`1003.1`](http://www.opengroup.org/onlinepubs/009695399/toc.htm)`)`\
`  interfaces and APIs.  We used to define `` by`\
`  default, but found that this caused more problems than it solved, so`\
`  now we require any code that is POSIX-compliant to explicitly say so`\
`  by having `` at the top.  Try to do this`\
`  whenever possible.`

`* Some architectures have memory alignment constraints.  Others don't`\
`  have any constraints but go faster if you align things.  These`\
`  macros (from ``) tell you which alignment to use`

`* Use ``, `` and `` when`\
`  reading/writing ints and ptrs to the stack or heap.  Note that, by`\
`  definition, ``, `` and `` are the`\
`  same size and have the same alignment constraints even if`\
`  `` on that platform.`

`* Use ``, ``, etc when you need a certain`\
`  minimum number of bits in a type.  Use `` and `` when`\
`  there's no particular constraint.  ANSI C only guarantees that ints`\
`  are at least 16 bits but within GHC we assume they are 32 bits.`

`* Use `` and `` for floating point values`\
`  which will go on/have come from the stack or heap.  Note that`\
`  `` may occupy more than one ``, but it will`\
`  always be a whole number multiple.`

`* Use ``, `` to read `\
`  and `` values from the stack/heap, and`\
`  `` / `` to assign`\
`  StgFloat/StgDouble values to heap/stack locations.  These macros`\
`  take care of alignment restrictions.`

`* Heap/Stack locations are always `` aligned; the`\
`  alignment requirements of an `` may be more than that`\
`  of ``, but we don't pad misaligned `\
`  because doing so would be too much hassle (see `` & co`\
`  above).`

`*  Avoid conditional code like this:`

` Instead, add an appropriate test to the configure.ac script and use`\
` the result of that test instead.`

` The problem is that things change from one version of an OS to`\
` another - things get added, things get deleted, things get broken,`\
` some things are optional extras.  Using "feature tests" instead of`\
` "system tests" makes things a lot less brittle.  Things also tend to`\
` get documented better.`

Debugging/robustness tricks
---------------------------

Anyone who has tried to debug a garbage collector or code generator will
tell you: "If a program is going to crash, it should crash as soon, as
noisily and as often as possible." There's nothing worse than trying to
find a bug which only shows up when running GHC on itself and doesn't
manifest itself until 10 seconds after the actual cause of the problem.

We put all our debugging code inside . The general policy is we don't
ship code with debugging checks and assertions in it, but we do run with
those checks in place when developing and testing. Anything inside
should not slow down the code by more than a factor of 2.

We also have more expensive "sanity checking" code for hardcore
debugging - this can slow down the code by a large factor, but is only
enabled on demand by a command-line flag. General sanity checking in the
RTS is currently enabled with the RTS flag.

There are a number of RTS flags which control debugging output and
sanity checking in various parts of the system when is defined. For
example, to get the scheduler to be verbose about what it is doing, you
would say . See and for the full set of debugging flags. To check one of
these flags in the code, write: would check the flag before generating
the output (and the code is removed altogether if is not defined).

All debugging output should go to .

Particular guidelines for writing robust code:

`* Use assertions.  Use lots of assertions.  If you write a comment`\
`  that says "takes a +ve number" add an assertion.  If you're casting`\
`  an int to a nat, add an assertion.  If you're casting an int to a`\
`  char, add an assertion.  We use the `` macro for writing`\
`  assertions; it goes away when `` is not defined.`

`* Write special debugging code to check the integrity of your data`\
`  structures.  (Most of the runtime checking code is in`\
`  ``) Add extra assertions which call this code at`\
`  the start and end of any code that operates on your data`\
`  structures.`

`* When you find a hard-to-spot bug, try to think of some assertions,`\
`  sanity checks or whatever that would have made the bug easier to`\
`  find.`

`* When defining an enumeration, it's a good idea not to use 0 for`\
`  normal values.  Instead, make 0 raise an internal error.  The idea`\
`  here is to make it easier to detect pointer-related errors on the`\
`  assumption that random pointers are more likely to point to a 0`\
`  than to anything else.`

`* Use `` or `` whenever you write a piece of`\
`  incomplete/broken code.`

`* When testing, try to make infrequent things happen often.  For`\
`  example, make a context switch/gc/etc happen every time a context`\
`  switch/gc/etc can happen.  The system will run like a pig but it'll`\
`  catch a lot of bugs.`

Syntactic details
-----------------

`* Please keep to 80 columns: the line has to be drawn somewhere, and`\
`  by keeping it to 80 columns we can ensure that code looks OK on`\
`  everyone's screen.  Long lines are hard to read, and a sign that`\
`  the code needs to be restructured anyway.`

`* An indentation width of 4 is preferred (don't use actual tab characters, use spaces).`

`* `**`Important:`**` Put "redundant" braces or parens in your code.`\
`   Omitting braces and parens leads to very hard to spot bugs -`\
`   especially if you use macros (and you might have noticed that GHC`\
`   does this a lot!)`

` In particular, put braces round the body of for loops, while loops,`\
` if statements, etc.  even if they "aren't needed" because it's`\
` really hard to find the resulting bug if you mess up.  Indent them`\
` any way you like but put them in there!`

` * When defining a macro, always put parens round args - just in case.`\
`   For example, write:`

` instead of`

`* Don't declare and initialize variables at the same time.`\
`  Separating the declaration and initialization takes more lines, but`\
`  make the code clearer.`

`* Don't define macros that expand to a list of statements.  You could`\
`  just use braces as in:`

` (but it's usually better to use an inline function instead - see above).`

`* Don't even write macros that expand to 0 statements - they can mess`\
`  you up as well.  Use the `` macro instead.`

`* This code`

` looks like it declares two pointers but, in fact, only p is a pointer.`\
` It's safer to write this:`

` You could also write this:`

` but it is preferrable to split the declarations.`

`* Try to use ANSI C's enum feature when defining lists of constants`\
`  of the same type.  Among other benefits, you'll notice that gdb`\
`  uses the name instead of its (usually inscrutable) number when`\
`  printing values with enum types and gdb will let you use the name`\
`  in expressions you type.`

` Examples:`

` instead of`

` and `

` instead of`

`* When commenting out large chunks of code, use `` `\
`  rather than `` because C doesn't have`\
`  nested comments.`

`* When declaring a typedef for a struct, give the struct a name as`\
`  well, so that other headers can forward-reference the struct name`\
`  and it becomes possible to have opaque pointers to the struct.  Our`\
`  convention is to name the struct the same as the typedef, but add a`\
`  leading underscore.  For example:`

`* Do not use `` instead of explicit comparison against `\
`  or ``; the latter is much clearer.`

`* Please write comments in English.  Especially avoid Klingon.`

Inline functions
----------------

Use inline functions instead of macros if possible - they're a lot less
tricky to get right and don't suffer from the usual problems of side
effects, evaluation order, multiple evaluation, etc.

`* Inline functions get the naming issue right.  E.g. they`\
`  can have local variables which (in an expression context)`\
`  macros can't.`

`* Inline functions have call-by-value semantics whereas macros are`\
`  call-by-name.  You can be bitten by duplicated computation if you`\
`  aren't careful.`

`* You can use inline functions from inside gdb if you compile with`\
`  -O0 or -fkeep-inline-functions.  If you use macros, you'd better know`\
`  what they expand to.`

` However, note that macros can serve as both l-values and r-values and`\
` can be "polymorphic" as these examples show:`

There are three macros to do inline portably. Don't use \`inline\`
directly, use these instead:

\`INLINE\_HEADER\`

` An inline function in a header file.  This is just like a macro.  We never emit`\
` a standalone copy of the function, so it `*`must`*` be inlined everywhere.`

\`STATIC\_INLINE\`

` An inline function in a C source file.  Again, it is always inlined, and we never`\
` emit a standalone copy. `

\`EXTERN\_INLINE\`

` A function which is optionally inlined.  The C compiler is told to inline if possible,`\
` but we also generated a standalone copy of the function just in case (see source:rts/Inlines.c).`

Source-control issues
---------------------

`* Don't be tempted to re-indent or re-organise large chunks of code -`\
`  it generates large diffs in which it's hard to see whether anything`\
`  else was changed, and causes extra conflicts when moving patches to`\
`  another branch.`\
`  `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  If you must re-indent or re-organise, don't include any functional`\
`  changes that commit and give advance warning that you're about to do`\
`  it in case anyone else is changing that file.  For more details on`\
`  source control conventions, see [wiki:WorkingConventions/Git].`

for file in \*; do

`   iconv -f ascii -t utf-8 "$file" -o "${file%.txt}.wiki"`

done

Copying GC
==========

GHC uses copying GC by default, while it requires more memory than
\[wiki:Commentary/Rts/Storage/GC/Compaction mark/compact\], it is
faster.

The basic copying scheme is [Cheney's
Algorithm](http://en.wikipedia.org/wiki/Cheney%27s_algorithm). Starting
from the \[wiki:Commentary/Rts/Storage/GC/Roots roots\], we visit each
live object:

`* The object is `*`evacuated`*``  (copied) to its destination generation.   The destination is given by `bd->dest` pointer in the `bdescr` of the ``\
`  block in which it lives; typically an object is promoted to the next highest generation, but the basic policy is affected by  [wiki:Commentary/Rts/Storage/GC/Aging aging] and [wiki:Commentary/Rts/Storage/GC/EagerPromotion eager promotion].`

`* The header word of the original object is replaced by a `*`forwarding`
`pointer`*`.  The forwarding pointer is just the pointer to the new copy, with the least significant bit set to 1 so that forwarding pointers can be distinguished from info table pointers.`

`* We scan objects that have been evacuated, and `*`scavenge`*` each one.  Scavenging involves evacuating each of the pointers`\
`  in the object, replacing each pointer with a pointer to the evacuated copy.`

`* When there are no more objects to be scavenged, the algorithm is complete.  The memory containing the evacuated objects is retained, all the memory containing the old objects and forwarding pointers is discarded.`

Evacuation is implemented in the file
[GhcFile(rts/sm/Evac.c)](GhcFile(rts/sm/Evac.c) "wikilink").[br](br "wikilink")
Scavenging is implemented in the file
[GhcFile(rts/sm/Scav.c)](GhcFile(rts/sm/Scav.c) "wikilink").[br](br "wikilink")

The principle APIs are

`` `void evacuate (StgClosure **p)`:: ``\
``   which evacuates the object pointed to by the pointer at `p`, and updates `p` to point to the new location. ``

`` `void scavenge_block (bdescr *bd)`:: ``\
``   which scavenges all the objects in the block `bd` (objects between `bd->u.scan` and `bd->free` are assumed to ``\
`  be unscavenged so far).`

= Core-to-Core optimization pipeline

After the source program has been \[wiki:Commentary/Compiler/TypeChecker
typechecked\] it is desugared into GHC's intermediate language
\[wiki:Commentary/Compiler/CoreSynType Core\]. The Core representation
of a program is then optimized by a series of correctness preserving
Core-to-Core passes. This page describes the overall structure of the
Core-to-Core optimization pipeline. Detailed descriptions of
optimizations are available
\[wiki:Commentary/Compiler/Core2CorePipeline\#Furtherreading in the
published papers\]. An overview of the whole compiler pipeline is
available \[wiki:Commentary/Compiler/HscMain here\].

== Optimizations during desugaring

At the end of desugaring we run the \`simpleOptPgm\` function that
performs some simple optimizations: eliminating dead bindings, and
inlining non-recursive bindings that are used only once or where the RHS
is trivial. The rest of Core optimisations is performed by the
Core-to-Core pipeline.

== The pipeline

The structure of the Core-to-Core pipeline is determined in the
\`getCoreToDo\` function in the
[GhcFile(compiler/simplCore/SimplCore.lhs)](GhcFile(compiler/simplCore/SimplCore.lhs) "wikilink")
module. Below is an ordered list of performed optimisations. These are
enabled by default with \`-O1\` and \`-O2\` unless the description says
a specific flag is required. The simplifier, which the pipeline
description below often refers to, is described in detail in
\[wiki:Commentary/Compiler/Core2CorePipeline\#Simplifier the next
section\].

` * `**`Static` `Argument`
`Transformation`**`` : tries to remove redundant arguments to recursive calls, turning them into free variables in those calls.  Only enabled with `-fstatic-argument-transformation`.  If run this pass is preceded with a "gentle" run of the simplifier. ``

` * `**`Vectorisation`**`` : run the [wiki:DataParallel Data Parallel Haskell] [wiki:DataParallel/Vectorisation vectoriser]. Only enabled with `-fvectorise`. TODO: does `-Odph` imply `fvectorise`? ``

` * `**`Simplifier,` `gentle` `run`**

` * `**`Specialisation`**`: specialisation attempts to eliminate overloading. More details can be found in the comments in `[`GhcFile(compiler/specialise/Specialise.lhs)`](GhcFile(compiler/specialise/Specialise.lhs) "wikilink")`.`

` * `**`Full` `laziness,` `1st`
`pass`**`: floats let-bindings outside of lambdas. This pass includes annotating bindings with level information and then running the float-out pass. In this first pass of the full laziness we don't float partial applications and bindings that contain free variables - this will be done by the second pass later in the pipeline. See "Further Reading" section below for pointers where to find the description of the full laziness algorithm.`

` * `**`Float` `in,` `1st`
`pass`**`: the opposite of full laziness, this pass floats let-bindings as close to their use sites as possible. It will not undo the full laziness by sinking bindings inside a lambda, unless the lambda is one-shot. At this stage we have not yet run the demand analysis, so we only have demand information for things that we imported.`

` * `**`Simplifier,` `main`
`run`**`: run the main passes of the simplifier (phases 2, 1 and 0). Phase 0 is run with at least 3 iterations.`

` * `**`Call`
`arity`**`: attempts to eta-expand local functions based on how they are used. If run, this pass is followed by a 0 phase of the simplifier. See Notes in `[`GhcFile(compiler/simplCore/CallArity.hs)`](GhcFile(compiler/simplCore/CallArity.hs) "wikilink")` and the relevant paper.`

` * `**`Demand` `analysis,` `1st`
`pass`**` (a.k.a. strictness analysis): runs the demand analyser followed by worker-wrapper transformation and 0 phase of the simplifier. This pass tries to determine if some expressions are certain to be used and whether they will be used once or many times (cardinality analysis). We currently don't have means of saying that a binding is certain to be used many times. We can only determine that it is certain to be one-shot (ie. used only once) or probable to be one shot. Demand analysis pass only annotates Core with strictness information. This information is later used by worker/wrapper pass to perform transformations. CPR analysis is also done during demand analysis.`

` * `**`Full` `laziness,` `2nd`
`pass`**`: another full-laziness pass. This time partial applications and functions with free variables are floated out.`

` * `**`Common`
`Sub-expression-elimination`**`: eliminates expressions that are identical.`

` * `**`Float` `in,` `2nd` `pass`**

` * `**`Check` `rules,` `1st`
`pass`**`` : this pass is not for optimisation but for troubleshooting the rules. It is only enabled with `-frule-check` flag that accepts a string pattern. This pass looks for rules beginning with that string pattern that could have fired but didn't and prints them to stdout. ``

` * `**`Liberate`
`case`**`` : unrolls recursive functions once in their own RHS, to avoid repeated case analysis of free variables. It's a bit like the call-pattern specialisation but for free variables rather than arguments. Followed by a phase 0 simplifier run. Only enabled with `-fliberate-case` flag. ``

` * `**`Call-pattern`
`specialisation`**`` : Only enabled with `-fspec-constr` flag. TODO: explain what it does. ``

` * `**`Check` `rules,` `2nd` `pass`**

` * `**`Simplifier,` `final`**`: final 0 phase of the simplifier.`

` * `**`Damand` `analysis,` `2nd`
`pass`**``  (a.k.a. late demand analysis): this pass consists of demand analysis followed by worker-wrapper transformation and phase 0 of the simplifier. The reason for this pass is that some opportunities for discovering strictness were not visible earlier; and optimisations like call-pattern specialisation can create functions with unused arguments which are eliminated by late demand analysis. Only run with `-flate-dmd-anal`. FIXME: but the cardinality paper says something else, namely that the late pass is meant to detect single entry thunks. Is it still the case in the current implementation? ``

` * `**`Check` `rules,` `3rd` `pass`**

The plugin mechanism allows to modify the above pipeline dynamically.

== Simplifier

Simplifier is the workhorse of the Core-to-Core optimisation pipeline.
It performs all the local transformations: (TODO: this list is most
likely not comprehensive)

`- constant folding`\
`- applying the rewrite rules`\
`- inlining`\
`- case of case`\
`- case of known constructor`\
`- eta expansion and eta reduction`\
`- combining adjacent casts`\
`- pushing a cast out of the way of an application e.g. `

Video: [GHC Core
language](http://www.youtube.com/watch?v=EQA69dvkQIk&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
(14'04")

The  type
========

The Core language is GHC's central data types. Core is a very small,
explicitly-typed, variant of System F. The exact variant is called
\[wiki:Commentary/Compiler/FC System FC\], which embodies equality
constraints and coercions.

The type, and the functions that operate over it, gets an entire
directory
[GhcFile(compiler/coreSyn)](GhcFile(compiler/coreSyn) "wikilink"):

` * `[`GhcFile(compiler/coreSyn/CoreSyn.hs)`](GhcFile(compiler/coreSyn/CoreSyn.hs) "wikilink")`: the data type itself.`

` * `[`GhcFile(compiler/coreSyn/PprCore.hs)`](GhcFile(compiler/coreSyn/PprCore.hs) "wikilink")`: pretty-printing.`\
` * `[`GhcFile(compiler/coreSyn/CoreFVs.hs)`](GhcFile(compiler/coreSyn/CoreFVs.hs) "wikilink")`: finding free variables.`\
` * `[`GhcFile(compiler/coreSyn/CoreSubst.hs)`](GhcFile(compiler/coreSyn/CoreSubst.hs) "wikilink")`: substitution.`\
` * `[`GhcFile(compiler/coreSyn/CoreUtils.hs)`](GhcFile(compiler/coreSyn/CoreUtils.hs) "wikilink")`: a variety of other useful functions over Core.`

` * `[`GhcFile(compiler/coreSyn/CoreUnfold.hs)`](GhcFile(compiler/coreSyn/CoreUnfold.hs) "wikilink")`: dealing with "unfoldings".`

` * `[`GhcFile(compiler/coreSyn/CoreLint.hs)`](GhcFile(compiler/coreSyn/CoreLint.hs) "wikilink")`: type-check the Core program. This is an incredibly-valuable consistency check, enabled by the flag ``.`

` * `[`GhcFile(compiler/coreSyn/CoreTidy.hs)`](GhcFile(compiler/coreSyn/CoreTidy.hs) "wikilink")`: part of the [wiki:Commentary/Compiler/HscMain the CoreTidy pass] (the rest is in `[`GhcFile(compiler/main/TidyPgm.hs)`](GhcFile(compiler/main/TidyPgm.hs) "wikilink")`).`\
` * `[`GhcFile(compiler/coreSyn/CorePrep.hs)`](GhcFile(compiler/coreSyn/CorePrep.hs) "wikilink")`: [wiki:Commentary/Compiler/HscMain the CorePrep pass]`

Here is the entire Core type
[GhcFile(compiler/coreSyn/CoreSyn.hs)](GhcFile(compiler/coreSyn/CoreSyn.hs) "wikilink"):
That's it. All of Haskell gets compiled through this tiny core.

 is parameterised over the type of its *binders*, . This facility is
used only rarely, and always temporarily; for example, the let-floater
pass attaches a binding level to every binder. By far the most important
type is , which is with binders. If you want to learn more about such
AST-parametrization, I encourage you to read a blog post about it:
<http://blog.ezyang.com/2013/05/the-ast-typing-problem> .

Binder is used (as the name suggest) to bind a variable to an
expression. The data type is parametrized by the binder type. The most
common one is the where comes from
[GhcFile(compiler/basicTypes/Var.hs)](GhcFile(compiler/basicTypes/Var.hs) "wikilink"),
which in fact is a with some extra informations attached (like types).

Here are some notes about the individual constructors of .

`* `` represents variables.  The `` it contains is essentially an [wiki:Commentary/Compiler/RdrNameType#TheOccNametype OccName] plus a ``; however, equality `` on ``s is based only on their ``'s, so `*`two`
`s` `with` `different` `types` `may` `be` `-equal`*`.`

`* `` is used for both term and type abstraction (small and big lambdas).`

`* `` appears only in type-argument positions (e.g. ``).  To emphasise this, the type synonym `` is used as documentation when we expect that a `` constructor may show up.  Anything not called `` should not use a `` constructor. Additional GHC Core uses so called type-lambdas, they are like lambdas, but instead of taking a real argument, they take a type instead. You should not confuse them with TypeFamilies, because type-lambdas are working on a value level, while type families are functions on the type level. The simplies example for a type-lambda usage is a polymorphic one: ``. It will be represented in Core as ``, where `` is a *type argument*, so when specyfying the argument of `` we can refer to ``. This is how polymorphism is represented in Core.`

`* `` handles both recursive and non-recursive let-bindings; see the the two constructors for ``. The Let constructor contains both binders as well as the resulting expression. The resulting expression is the `` in expression ``.`

`* `` expressions need [wiki:Commentary/Compiler/CoreSynType#Caseexpressions more explanation].`

`* `` is used for an [wiki:Commentary/Compiler/FC FC cast expression].  `` is a synonym for ``.`

`* `` is used to represent all the kinds of source annotation we support: profiling SCCs, HPC ticks, and GHCi breakpoints. Was named `` some time ago.`

Case expressions
----------------

Case expressions are the most complicated bit of . In the term :

`* `` is the scrutinee`\
`* `` is the `**`case` `binder`**` (see notes below)`\
`* `` is the type of the entire case expression (redundant once [wiki:Commentary/Compiler/FC FC] is in HEAD -- was for GADTs)`\
`* `` is a list of the case alternatives`

A case expression can scrutinise

`* `**`a` `data` `type`**` (the alternatives are ``s), or `\
`* `**`a` `primitive` `literal`
`type`**` (the alternatives are ``s), or `\
`* `**`a` `value` `of` `any` `type` `at`
`all`**` (if there is one `` alternative).`

A case expression is **always strict**, even if there is only one
alternative, and it is . (This differs from Haskell!) So will call ,
rather then returning .

The field, called the **case binder**, is an unusual feature of GHC's
case expressions. The idea is that *in any right-hand side, the case
binder is bound to the value of the scrutinee*. If the scrutinee was
always atomic nothing would be gained, but real expressiveness is added
when the scrutinee is not atomic. Here is a slightly contrived example:
(Here, "" is the case binder; at least that is the syntax used by the
Core pretty printer.) This expression evaluates ; if the result is , it
returns , otherwise it returns the reversed list appended to itself.
Since the returned value of is present in the implementation, it makes
sense to have a name for it!

The most common application is to model call-by-value, by using instead
of . For example, here is how we might compile the call if we knew that
was strict:

Case expressions have several invariants

`* The `` type is the same as the type of any of the right-hand sides (up to refining unification -- coreRefineTys in `[`GhcFile(compiler/types/Unify.hs)`](GhcFile(compiler/types/Unify.hs) "wikilink")` -- in pre-[wiki:Commentary/Compiler/FC FC]).`\
\
`* If there is a `` alternative, it must appear first.  This makes finding a `` alternative easy, when it exists.`

`* The remaining non-DEFAULT alternatives must appear in order of`\
`   * tag, for ``s`\
`   * lit, for ``s`\
`This makes finding the relevant constructor easy, and makes comparison easier too.`

`* The list of alternatives is `**`always`
`exhaustive`**`, meaning that it covers `**`all` `reachable`
`cases`**`.  Note, however, that an "exhausive" case does not necessarily mention all constructors:`

`The inner case does not need a `` alternative, because x can't be `` at that program point. Furthermore, GADT type-refinement might mean that some alternatives are not reachable, and hence can be discarded.  `

Shadowing
---------

One of the important things when working with Core is that variable
shadowing is allowed. In other words, it is possible to come across a
definition of a variable that has the same name (\`realUnique\`) as some
other one that is already in scope. One of the possible ways to deal
with that is to use \`Subst\` (substitution environment from
[GhcFile(compiler/coreSyn/CoreSubst.hs)](GhcFile(compiler/coreSyn/CoreSubst.hs) "wikilink")),
which maintains the list of variables in scope and makes it possible to
clone (i.e. rename) only the variables that actually capture names of
some earlier ones. For some more explanations about this approach see
[Secrets of the Glasgow Haskell Compiler inliner
(JFP'02)](http://research.microsoft.com/%7Esimonpj/Papers/inlining/index.htm)
(section 4 on name capture).

Human readable Core generation
------------------------------

If you are interested in the way Core is translated into human readable
form, you should check the sources for
[GhcFile(compiler/coreSyn/PprCore.hs)](GhcFile(compiler/coreSyn/PprCore.hs) "wikilink").
It is especially usefull if you want to see how the Core data types are
being build, especially when there is no Show instance defined for them.

CPS Conversion
==============

This part of the compiler is now merged in ghc-HEAD.

Overview
--------

This pass takes Cmm with native proceedure calls and an implicit stack
and produces Cmm with only tail calls implemented as jumps and an
explicit stack. In a word, it does CPS conversion. (All right, so that's
two words.)

Design Aspects
--------------

`* Proc-Point Analysis`\
`* Calling Conventions`\
`* Live Value Analysis`\
`* Stack Layout`

Simple Design
-------------

`* Split blocks into multiple blocks at function calls`\
`  * TODO: eliminate extra jump at block ends when there is already a jump at the end of the call`\
`* Do liveness analysis`\
`* Split every block into a separate function`\
`* Pass all live values as parameters (probably slow)`\
`  * Must arrange for both the caller and callee to know argument order`\
`    * Simple design: callee just chooses some order and all callers must comply`\
`  * Eventually could be passed implicitly but keeping things explicit makes things easier`\
`  * Evantually could use a custom calling convention`\
`  * Actual syntax is probably virtual.  (I.e. in an external table, not in actual syntax because that would require changes to the type for Cmm code)`\
`    * Input code:`\
`      `\
`    * Output code:`\
`      `\
`* Save live values before a call in the continuation`\
`  * Must arrange for both the caller and callee to know field order`\
`    * Simple design: callee just chooses some order and all callers must comply`\
`  * Eventually needs to be optimized to reduce continuation shuffling`\
`    * Can register allocation algorithms be unified with this into one framework?`

To be worked out
----------------

`* The continuations for `` and `` are different.`\
`  `\
`  * Could make a for each that shuffles the arguments into a common format.`\
`  * Could make one branch primary and shuffle the other to match it, but that might entail unnecessary memory writes.`

Pipeline
--------

`* CPS`\
`  * Make closures and stacks manifest`\
`  * Makes all calls are tail calls`\
`* Parameter Elimination`\
`  * Makes calling convention explicit`\
`  * For externally visible functions calling conventions is machine specific, but not backend specific because functions compiled from different backends must be be able to call eachother`\
`  * For local functions calling convention can be left up to the backend because it can take advantage of register allocation.`\
`    * However, the first first draft will specify the standard calling convention for all functions even local ones because:`\
`      * It's simpler`\
`      * The C code generator can't handle function parameters because of the Evil Mangler`\
`      * The NCG doesn't yet understand parameters`

TODO
----

`* Downstream`\
`  * Argument passing convention`\
`  * Stack check`\
`    * Needs some way to synchronize the branch label with the heap check`\
`* Midstream`\
`  * Support `` (needed by rts/Apply.cmm)`\
`  * More factoring and cleanup/documentation`\
`  * Wiki document the designed choosen`\
`  * Better stack slot selection`\
`  * Foreign function calls`\
`  * Garbage collector`\
`  * Proc points`\
`    * May cause new blocks`\
`    * May cause new functions`\
`    * Lives could be passes either on stack or in arguments`\
`  * Proc grouping of blocks`\
`* Upstream`\
`  * Have `` emit C-- with functions.`

Current Pipeline
----------------

### 

The / pipeline and the / pipeline can each independantly use the CPS
pass. However, they currently bypass it untill the CPS code becomes
stablized, but they must both use the pass. This pass converts the
header on each function from a to a .

Non-CPS Changes
---------------

`* Cmm Syntax Changes`\
`  * The returns parameters of a function call must be surrounded by parenthesis.`\
`    For example`

`    This is simply to avoid shift-reduce conflicts with assignment.`\
`    Future revisions to the parser may eliminate the need for this.`

`  * Variable declarations may are annotated to indicate`\
`    whether they are GC followable pointers.`

`  * The bitmap of a `` is now specified using`\
`    a parameter like syntax.`

`    Note that these are not real parameters, they are the stack layout`\
`    of the continuation.  Also, until the CPS algorithm`\
`    gets properly hooked into the `` path the parameter names are not used.`\
`  * The return values of a function call may only be ``.`\
`    This is due to changes in the `` data type.`

`* Cmm Data Type Changes`\
`  * The return parameters of a `` are `` instead of ``.`\
`    This is because a `` doesn't have a well defined pointerhood,`\
`    and the return values will become parameters to continuations where`\
`    their pointerhood will be needed.`\
`  * The type of info tables is now a separate parameter to `\
`    * Before`

`    * After`

`    This is to support using either `` or `\
`    as the header of a ``.`\
`    * Before info table conversion use `

`    * After info table conversion use `

`    Same for `` and ``.`\
`  * New type aliases ``, `` and ``.`\
`    Respectively these are the actual parameters of a function call,`\
`    the formal parameters of a function, and the`\
`    return results of a function call with pointerhood annotation`\
`    (CPS may convert these to formal parameter of the call's continuation).`

Notes
-----

`* Changed the parameter to a `` to be `` instead of `\
`  * `` are `\
`  * This field seems to not have been being used; it only require a type change`\
`* GC can be cleaned up b/c of the CPS`\
`  * Before`

`  * After`

`* We need the NCG to do aliasing analysis.  At present the CPS pass will generate the following, and will assume that the NCG can figure out when the loads and stores can be eliminated.  (The global saves part of a `` is dead b/c of this.)`

`* Simple calls`\
`  * Before`

`  * Output of CPS`

`  * Optimization by the NCG`

Loopholes
---------

There are a number of deviations from what one might expect from a CPS
algorithm due to the need to encode existing optimizations and idioms.

### GC Blocks

For obvious reasons, the stack used by GC blocks does not count tward
the maximum amount of stack used by the function.

This loophole is overloaded by the GC **functions** so they don't create
their own infinite loop. The main block is marked as being the GC block
so its stack usage doesn't get checked.

### Update Frames

Update frame have to be pushed onto the stack at the begining of an
update function. We could do this by wrapping the update function inside
another function that just does the work of calling that other function,
but since updates are so common we don't want to pay the cost of that
extra jump. Thus a function can be annotated with a frame that should be
pushed on entry.

Note that while the frame is equivalent to a tail call at the end of the
function, the frame must be pushed at the beginning of the function
because parts of the blackhole code look for these update frames to
determine what thunks are under evaluation.

### User defined continuations

Pushing an update frame on the stack requires the ability to define a
function that will pull that frame from the stack and have access to any
values within the frame. This is done with user-defined continuations.

### Branches to continuations

A GC block for a heap check after a call should only take one or two
instructions. However the natural code: would generate a trivial
continuation for the call as well as a trivial continuation for the call
that just calls the proc point .

We solve this by changing the syntax to

Now the call has the same return signature as and can use the same
continuation. (A call followed by a thus gets optimized down to just the
call.)

Not in Scope of Current Work
----------------------------

Improvements that could be made but that will not be implemented durring
the curent effort.

### Static Reference Table Handling (SRT)

As it stands, each function and thus each call site must be annotated
with a bitmap and a pointer or offset to the SRT shared by the function.
This does not interact with the stack in any way so it ought to be
outside the scope of the CPS algorithm. However there is some level of
interaction because

`1. the SRT information on each call site needs to be attached to the resulting continuation and`\
`2. functions read from a Cmm file might need to be annotated with that SRT info.`

The first is a concern for correctness but may be handled by treating
the SRT info as opaque data. The second is a concern for ease of use and
thus the likelyhood of mistakes in hand written C-- code. At the moment
it appears that all of the C-- functions in the runtime system (RTS) use
a null SRT so for now we'll just have the CPS algorithm treat the SRT
info as opaque.

In the future it would be nice to have a more satisfactory way to handle
both these issues.

### Cmm Optimization assumed by CPS

In order to simplify the CPS pass, it makes some assumptions about the
optimizer.

`* The CPS pass may generate more blocks than strictly necessary.  In particular,`\
`  it might be possible to join together two blocks when the second block is only`\
`  entered by the first block.  This is a simple optimization that needs to be implemented.`\
`* The CPS pass may generate more loads and stores than strictly necessary.  In particular,`\
`  it may load a local register only to store it back to the same stack location a few`\
`  statements later.  There may be intervening branches.  The optimizer`\
`  needs to be extended to eliminate these load store pairs.`

Notes on future development
---------------------------

### Handling GC

The GHC Commentary: Data types and data constructors
====================================================

This chapter was thoroughly changed Feb 2003. If you are interested in
how a particular data type is implemented take a look at
\[wiki:Commentary/Compiler/CaseStudies/Bool this case study\].

Data types
----------

Consider the following data type declaration: The user's source program
mentions only the constructors \`MkT\` and \`Nil\`. However, these
constructors actually *do* something in addition to building a data
value. For a start, \`MkT\` evaluates its arguments. Secondly, with the
flag \`-funbox-strict-fields\` GHC will flatten (or unbox) the strict
fields. So we may imagine that there's the *source* constructor \`MkT\`
and the *representation* constructor \`MkT\`, and things start to get
pretty confusing.

GHC now generates three unique \`Name\`s for each data constructor:
Recall that each occurrence name (OccName) is a pair of a string and a
name space (see \[wiki:Commentary/Compiler/RdrNameType\#TheOccNametype
RdrNames, Modules, and OccNames\]), and two OccNames are considered the
same only if both components match. That is what distinguishes the name
of the name of the DataCon from the name of its worker Id. To keep
things unambiguous, in what follows we'll write "MkT{d}" for the source
data con, and "MkT{v}" for the worker Id. (Indeed, when you dump stuff
with "-ddumpXXX", if you also add "-dppr-debug" you'll get stuff like
"Foo {- d rMv -}". The "d" part is the name space; the "rMv" is the
unique key.)

Each of these three names gets a distinct unique key in GHC's name
cache.

The life cycle of a data type
=============================

Suppose the Haskell source looks like this: When the parser reads it in,
it decides which name space each lexeme comes from, thus: Notice that in
the Haskell source *all data contructors are named via the "source data
con" MkT{d}*, whether in pattern matching or in expressions.

In the translated source produced by the type checker (-ddump-tc), the
program looks like this:

Notice that the type checker replaces the occurrence of MkT by the
*wrapper*, but the occurrence of Nil by the *worker*. Reason: Nil
doesn't have a wrapper because there is nothing to do in the wrapper
(this is the vastly common case).

Though they are not printed out by "-ddump-tc", behind the scenes, there
are also the following: the data type declaration and the wrapper
function for MkT. Here, the *wrapper* \$WMkT evaluates and takes apart
the argument p, evaluates the argument t, and builds a three-field data
value with the *worker* constructor MkT{v}. (There are more notes below
about the unboxing of strict fields.) The worker \$WMkT is called an
*implicit binding*, because it's introduced implicitly by the data type
declaration (record selectors are also implicit bindings, for example).
Implicit bindings are injected into the code just before emitting code
or External Core.

After desugaring into Core (-ddump-ds), the definition of f looks like
this: Notice the way that pattern matching has been desugared to take
account of the fact that the "real" data constructor MkT has three
fields.

By the time the simplifier has had a go at it, f will be transformed to:
Which is highly cool.

The constructor wrapper functions
---------------------------------

The wrapper functions are automatically generated by GHC, and are really
emitted into the result code (albeit only after CorePre; see
\`CorePrep.mkImplicitBinds\`). The wrapper functions are inlined very
vigorously, so you will not see many occurrences of the wrapper
functions in an optimised program, but you may see some. For example, if
your Haskell source has then \`\$WMkT\` will not be inlined (because it
is not applied to anything). That is why we generate real top-level
bindings for the wrapper functions, and generate code for them.

The constructor worker functions
--------------------------------

Saturated applications of the constructor worker function MkT{v} are
treated specially by the code generator; they really do allocation.
However, we do want a single, shared, top-level definition for top-level
nullary constructors (like True and False). Furthermore, what if the
code generator encounters a non-saturated application of a worker? E.g.
(\`map Just xs\`). We could declare that to be an error (CorePrep should
saturate them). But instead we currently generate a top-level defintion
for each constructor worker, whether nullary or not. It takes the form:
This is a real hack. The occurrence on the RHS is saturated, so the code
generator (both the one that generates abstract C and the byte-code
generator) treats it as a special case and allocates a MkT; it does not
make a recursive call! So now there's a top-level curried version of the
worker which is available to anyone who wants it.

This strange definition is not emitted into External Core. Indeed, you
might argue that we should instead pass the list of \`TyCon\`s to the
code generator and have it generate magic bindings directly. As it
stands, it's a real hack: see the code in CorePrep.mkImplicitBinds.

External Core
-------------

When emitting External Core, we should see this for our running example:
Notice that it makes perfect sense as a program all by itself.
Constructors look like constructors (albeit not identical to the
original Haskell ones).

When reading in External Core, the parser is careful to read it back in
just as it was before it was spat out, namely:

Unboxing strict fields
----------------------

If GHC unboxes strict fields (as in the first argument of MkT above), it
also transforms source-language case expressions. Suppose you write this
in your Haskell source: GHC will desugar this to the following Core
code: The local let-binding reboxes the pair because it may be mentioned
in the case alternative. This may well be a bad idea, which is why
\`-funbox-strict-fields\` is an experimental feature.

It's essential that when importing a type \`T\` defined in some external
module \`M\`, GHC knows what representation was used for that type, and
that in turn depends on whether module M was compiled with
\`-funbox-strict-fields\`. So when writing an interface file, GHC
therefore records with each data type whether its strict fields (if any)
should be unboxed.

Labels and info tables
----------------------

*Quick rough notes: SLPJ March 2003.*

Every data constructor \`C\` has two info tables:

``    * The static info table (label `C_static_info`), used for statically-allocated constructors. ``\
``    * The dynamic info table (label `C_con_info`), used for dynamically-allocated constructors.  ``

Statically-allocated constructors are not moved by the garbage
collector, and therefore have a different closure type from
dynamically-allocated constructors; hence they need a distinct info
table. Both info tables share the same entry code, but since the entry
code is physically juxtaposed with the info table, it must be duplicated
(\`C\_static\_entry\` and \`C\_con\_entry\` respectively).

[PageOutline](PageOutline "wikilink")

Demand analyser in GHC
======================

This page explains basics of the so-called demand analysis in GHC,
comprising strictness and absence analyses. Meanings of demand
signatures are explained and examples are provided. Also, components of
the compiler possibly affected by the results of the demand analysis are
listed with explanations provided.

`* The `[`demand-analyser` `draft`
`paper`](http://research.microsoft.com/en-us/um/people/simonpj/papers/demand-anal/demand.ps)` is as yet unpublished, but gives the most accurate overview of the way GHC's demand analyser works.`

------------------------------------------------------------------------

Demand signatures
-----------------

Let us compile the following program with \`-O2 -ddump-stranal\` flags:

The resulting demand signature for function \`f\` will be the following
one:

This should be read as "\`f\` puts stricts demands on both its arguments
(hence, \`S\`); \`f\` might use its first and second arguments. but in
the second argument (which is a product), the second component is
ignored". The suffix \`m\` in the demand signature indicates that the
function returns **CPR**, a constructed product result (for more
information on CPR see the JFP paper [Constructed Product Result
Analysis for
Haskell](http://research.microsoft.com/en-us/um/people/simonpj/Papers/cpr/index.htm)).

Current implementation of demand analysis in Haskell performs annotation
of all binders with demands, put on them in the context of their use.
For functions, it is assumed, that the result of the function is used
strictly. The analysis infers strictness and usage information
separately, as two components of a cartesian product domain. The same
analysis also performs inference CPR and bottoming properties for
functions, which can be read from the suffix of the signature. Demand
signatures of inner definitions may also include *demand environments*
that indicate demands, which a closure puts to its free variables, once
strictly used, e.g. the signature

indicates that the function has one parameter, which is used lazily
(hence \`<L,U>\`), however, when its result is used strictly, the free
variable \`skY\` in its body is also used strictly.

### Demand descriptions

Strictness demands

``  * `B` -- a  ``*`hyperstrict`*``  demand. The expression `e` puts this demand on its argument `x` if every evaluation of `e` is guaranteed to diverge, regardless of the value of the argument. We call this demand  ``*`hyperstrict`*``  because it is safe to evaluate `x` to arbitrary depth before evaluating `e`. This demand is polymorphic with respect to function calls and can be seen as `B = C(B) = C(C(B)) = ...` for an arbitrary depth. ``\
` `\
``  * `L`  -- a  ``*`lazy`*``  demand. If an expression `e` places demand `L` on a variable  `x`, we can deduce nothing about how `e` uses `x`. `L` is the completely uninformative demand, the top element of the lattice. ``

``  * `S` -- a  ``*`head-strict`*``  demand.  If `e` places demand `S` on `x` then `e` evaluates `x` to at least head-normal form; that is, to the outermost constructor of `x`.  This demand is typically placed by the `seq` function on its first argument. The demand `S(L ... L)` places a lazy demand on all the components, and so is equivalent to `S`; hence the identity `S = S(L ... L)`. Another identity is for functions, which states that `S = C(L)`. Indeed, if a function is certainly called, it is evaluated at lest up to the head normal form, i.e.,  ``*`strictly`*`. However, its result may be used lazily.`

``  * `S(s1 ... sn)` -- a structured strictness demand on a product.  It is at least head-strict, and perhaps more. ``

``  * `C(s)`  -- a  ``*`call-demand`*`` , when placed on a binder `x`, indicates that the value is a function, which is always called and its result is used according to the demand `s`.  ``

Absence/usage demands

``  * `A` -- when placed on a binder `x` it means that `x` is definitely unused. ``

``  * `U` -- the value is used on some execution path.  This demand is a top of usage domain. ``

``  * `H` -- a  ``*`head-used`*``  demand. Indicates that a product value is used itself, however its components are certainly ignored. This demand is typically placed by the `seq` function on its first argument. This demand is polymorphic with respect to products and functions. For a product, the head-used demand is expanded as `U(A, ..., A)` and for functions it can be read as `C(A)`, as the function is called (i.e., evaluated to at least a head-normal form), but its result is ignored. ``

``  * `U(u1 ... un)` -- a structured usage demand on a product. It is at least head-used, and perhaps more. ``

``  * `C(u)` -- a  ``*`call-demand`*``  for usage information. When put on a binder `x`, indicates that `x` in all executions paths where `x` is used, it is  ``*`applied`*``  to some argument, and the result of the application is used with a demand `u`. ``

Additional information (demand signature suffix)

``  * `m`  -- a function returns a  ``[`constructed` `product`
`result`](http://research.microsoft.com/en-us/um/people/simonpj/Papers/cpr/index.htm)

``  * `b` -- the function is a  ``*`bottoming`*``  one, i.e., some decoration of `error` and friends. ``

Worker-Wrapper split
--------------------

Demand analysis in GHC drives the *worker-wrapper transformation*, which
exposes specialised calling conventions to the rest of the compiler. In
particular, the worker-wrapper transformation implements the unboxing
optimisation.

The worker-wrapper transformation splits each function \`f\` into a
*wrapper*, with the ordinary calling convention, and a *worker*, with a
specialised calling convention. The wrapper serves as an
impedance-matcher to the worker; it simply calls the worker using the
specialised calling convention. The transformation can be expressed
directly in GHC's intermediate language. Suppose that \`f\` is defined
thus: and that we know that \`f\` is strict in its argument (the pair,
that is), and uses its components. What worker-wrapper split shall we
make? Here is one possibility: Now the wrapper, \`f\`, can be inlined at
every call site, so that the caller evaluates \`p\`, passing only the
components to the worker \`\$wf\`, thereby implementing the unboxing
transformation.

But what if \`f\` did not use \`a\`, or \`b\`? Then it would be silly to
pass them to the worker \`\$wf\`. Hence the need for absence analysis.
Suppose, then, that we know that \`b\` is not needed. Then we can
transform to: Since \`b\` is not needed, we can avoid passing it from
the wrapper to the worker; while in the worker, we can use \`error
"abs"\` instead of \`b\`.

In short, the worker-wrapper transformation allows the knowledge gained
from strictness and absence analysis to be exposed to the rest of the
compiler simply by performing a local transformation on the function
definition. Then ordinary inlining and case elimination will do the
rest, transformations the compiler does anyway.

Relevant compiler parts
-----------------------

Multiple parts of GHC are sensitive to changes in the nature of demand
signatures and results of the demand analysis, which might cause
unexpected errors when hacking into demands.
\[wiki:Commentary/Compiler/Demand/RelevantParts This list\] enumerates
the parts of the compiler that are sensitive to demand, with brief
summaries of how so.

Support for deriving , , and  instances
======================================

[PageOutline](PageOutline "wikilink")

GHC 6.12.1 introduces an extension to the mechanism allowing for
automatic derivation of , , and instances using the , , and extensions,
respectively. Twan van Laarhoven [first proposed this
feature](https://mail.haskell.org/pipermail/haskell-prime/2007-March/002137.html)
in 2007, and [opened a related GHC Trac
ticket](https://ghc.haskell.org/trac/ghc/ticket/2953) in 2009.

Example
-------

The derived code would look something like this:

Algorithm description
---------------------

, , and all operate using the same underlying mechanism. GHC inspects
the arguments of each constructor and derives some operation to perform
on each argument, which depends of the type of the argument itself. In a
instance, for example would be applied to occurrences of the last type
parameter, but would be applied to other type parameters. Typically,
there are five cases to consider. (Suppose we have a data type .)

1\. Terms whose type does not mention 2. Terms whose type mentions 3.
Occurrences of 4. Tuple values 5. Function values

After this is done, the new terms are combined in some way. For
instance, instances combine terms in a derived definition by applying
the appropriate constructor to all terms, whereas in instances, a
derived definition would the terms together.

### 

A comment in
[TcGenDeriv.hs](http://git.haskell.org/ghc.git/blob/9f968e97a0de9c2509da00f6337b612dd72a0389:/compiler/typecheck/TcGenDeriv.hs#l1476)
lays out the basic structure of , which derives an implementation for .

 is special in that it can recurse into function types, whereas and
cannot (see the section on covariant and contravariant positions).

### 

Another comment in
[TcGenDeriv.hs](http://git.haskell.org/ghc.git/blob/9f968e97a0de9c2509da00f6337b612dd72a0389:/compiler/typecheck/TcGenDeriv.hs#l1725)
reveals the underlying mechanism behind :

In addition to , also generates a definition for as of GHC 7.8.1
(addressing [\#7436](https://ghc.haskell.org/trac/ghc/ticket/7436)). The
pseudo-definition for would look something like this:

### 

From
[TcGenDeriv.hs](http://git.haskell.org/ghc.git/blob/9f968e97a0de9c2509da00f6337b612dd72a0389:/compiler/typecheck/TcGenDeriv.hs#l1800):

### Covariant and contravariant positions

One challenge of deriving instances for arbitrary data types is handling
function types. To illustrate this, note that these all can have derived
instances:

but none of these can:

In , , and , all occurrences of the type variable are in *covariant*
positions (i.e., the values are produced), whereas in , , and , all
occurrences of are in *contravariant* positions (i.e., the values are
consumed). If we have a function , we can't apply to an value in a
contravariant position, which precludes a instance.

Most type variables appear in covariant positions. Functions are special
in that the lefthand side of a function arrow reverses variance. If a
function type appears in a covariant position (e.g., above), then is in
a contravariant position and is in a covariant position. Similarly, if
appears in a contravariant position (e.g., above), then is in a
covariant position and is in a contravariant position.

If we annotate covariant positions with (for positive) and contravariant
positions with (for negative), then we can examine the above examples
with the following pseudo-type signatures:

Since , , and all use the last type parameter in at least one position,
GHC would reject a derived instance for each of them.

Requirements for legal instances
--------------------------------

This mechanism cannot derive , , or instances for all data types.
Currently, GHC checks if a data type meets the following criteria:

1\. The data type has at least one type parameter. (For example, cannot
have a instance.) 2. The data type's last type parameter cannot be used
contravariantly. (see the section on covariant and contravariant
positions.) 3. The data type's last type parameter cannot be used in the
"wrong place" in any constructor's data arguments. For example, in , the
type parameter is only ever used as the last type argument in and , so
both and values can be ped. However, in , the type variable appears in a
position other than the last, so trying to an value would not typecheck.

`  Note that there are two exceptions to this rule: tuple and function types.`

4\. The data type's last type variable cannot used in a constraint. For
example, would be rejected.

In addition, GHC performs checks for certain classes only:

1\. For derived and instances, a data type cannot use function types.
This restriction does not apply to derived instances, however. 2. For
derived and instances, the data type's last type variable must be truly
universally quantified, i.e., it must not have any class or equality
constraints. This means that the following is legal:

`  but the following is not legal:`

`  This restriction does not apply to derived `` instances. See the following section for more details.`

### Relaxed universality check for 

 and cannot be used with data types that use existential constraints,
since the type signatures of and make this impossible. However,
instances are unique in that they do not produce constraints, but only
consume them. Therefore, it is permissible to derive instances for
constrained data types (e.g., GADTs).

For example, consider the following GADT:

In the type signatures for and , the parameter appears both in an
argument and the result type, so pattern-matching on a value of must not
impose any constraints, as neither nor would typecheck.

, however, only mentions in argument types:

Therefore, a derived instance for typechecks:

Deriving instances for GADTs with equality constraints could become
murky, however. Consider this GADT:

All four constructors have the same "shape" in that they all take an
argument of type (or , to which is constrained to be equal). Does that
mean all four constructors would have their arguments folded over? While
it is possible to derive perfectly valid code which would do so:

it is much harder to determine which arguments are equivalent to . Also
consider this case:

For all we know, it may be that . Does this mean that the argument in
should be folded over?

To avoid these thorny edge cases, we only consider constructor arguments
(1) whose types are *syntactically* equivalent to the last type
parameter and (2) in cases when the last type parameter is a truly
universally polymorphic. In the above example, only fits the bill, so
the derived instance is actually:

To expound more on the meaning of criterion (2), we want not only to
avoid cases like , but also something like this:

In this example, the last type variable is instantiated with , which
contains one type variable applied to another type variable . We would
*not* fold over the argument of type in this case, because the last type
variable should be *simple*, i.e., contain only a single variable
without any application.

For the original discussion on this proposal, see
[\#10447](https://ghc.haskell.org/trac/ghc/ticket/10447).

Alternative strategy for deriving \`Foldable\` and \`Traversable\`
------------------------------------------------------------------

We adapt the algorithms for \`-XDeriveFoldable\` and
\`-XDeriveTraversable\` based on that of \`-XDeriveFunctor\`. However,
there is an important difference between deriving the former two
typeclasses and the latter one (as of GHC 8.2, addressing [Trac
\#11174](https://ghc.haskell.org/trac/ghc/ticket/11174)), which is best
illustrated by the following scenario:

The generated code for the \`Functor\` instance is straightforward:

But if we use too similar of a strategy for deriving the \`Foldable\`
and \`Traversable\` instances, we end up with this code:

This is unsatisfying for two reasons:

1\. The \`Traversable\` instance doesn't typecheck! \`Int\#\` is of kind
\`\#\`, but \`pure\` expects an argument whose type is of kind \`\*\`.
This effectively prevents \`Traversable\` from being derived for any
datatype with an unlifted argument type (see [Trac
\#11174](https://ghc.haskell.org/trac/ghc/ticket/11174)).

2\. The generated code contains superfluous expressions. By the
\`Monoid\` laws, we can reduce \`f a &lt;&gt; mempty\` to \`f a\`, and
by the \`Applicative\` laws, we can reduce \`fmap WithInt (f a)
&lt;\*&gt; pure i\` to \`fmap (\\b -&gt; WithInt b i) (f a)\`.

We can fix both of these issues by incorporating a slight twist to the
usual algorithm that we use for \`-XDeriveFunctor\`. The differences can
be summarized as follows:

1\. In the generated expression, we only fold over arguments whose types
mention the last type parameter. Any other argument types will simply
produce useless \`mempty\`s or \`pure\`s, so they can be safely ignored.

2\. In the case of \`-XDeriveTraversable\`, instead of applying
\`ConName\`, we apply \`\\b\_i ... b\_k -&gt; ConName a\_1 ... a\_n\`,
where

-   \`ConName\` has \`n\` arguments
-   \`{b\_i, ..., b\_k}\` is a subset of \`{a\_1, ..., a\_n}\` whose
    indices correspond to the arguments whose types mention the last
    type parameter. As a consequence, taking the difference of \`{a\_1,
    ..., a\_n}\` and \`{b\_i, ..., b\_k}\` yields the all the argument
    values of \`ConName\` whose types do not mention the last
    type parameter. Note that \`\[i, ..., k\]\` is a strictly increasing

[PageOutline](PageOutline "wikilink")

LLVM Back-end Design
====================

The current design tries to fit into GHC's pipeline stages as an
alternative to the C and NCG back-ends as seamlessly as possible. This
allows for quicker development and focus on the core task of LLVM code
generation.

The LLVM pipeline works as follows:

` * New path for LLVM generation, separate from C and NCG. (path forks at compiler/main/CodeOutput.lhs, same place where C and NCG fork).`\
` * LLVM code generation will output LLVM assembly code.`\
` * The LLVM assembly code is translated to an object file as follows`\
`    * The LLVM optimizer is run which is a series of bitcode to bitcode optimization passes (using the `` tool).`\
`    * Finally an object file is created from the LLVM bitcode (using the `` tool)`\
` * This brings the LLVM path back to the other back-ends.`\
` * The final state is the Link stage, which uses the system linker as with the other back-ends.`

Here is a diagram of the pipeline:

This approach was the easiest and thus quickest way to initially
implement the LLVM back-end. Now that it is working, there is some room
for additional optimisations. A potential optimisation would be to add a
new linker phase for LLVM. Instead of each module just being compiled to
native object code ASAP, it would be better to keep them in the LLVM
bitcode format and link all the modules together using the LLVM linker.
This enable all of LLVM's link time optimisations. All the user program
LLVM bitcode will then be compiled to a native object file and linked
with the runtime using the native system linker.

Implementation
==============

Framework
---------

` * New `**`-fllvm`**` code generation pipeline, involved modifying:`\
`   * `` - Selects appropriate back-end for code generation (C, NCG, LLVM).`\
`   * ```  - Stores GHC configuration (command line options, compile time options... ect). Added `HscLlvm` target type. ``\
`   * ```  - Stores modules/files to compile for ghc. Added new LLVM files and directory stored under `llvmGen`, and new CPP flag to enable the LLVM code generator (`-DLLVM`). ``\
`   * ```  - Added new `GhcWithLlvmCodeGen` option which can be set in `build.mk` to `YES` to enable the LLVM code generator. ``\
`   * ```  - Added `LlvmAs` phase to invoke the compilation of LLVM bitcode/IR to an object file. After this phase linking can occur. ``\
`   * ```  - Added code for new `LlvmAs`, `LlvmOpt` and `LlvmLlc` phases. ``\
`     * ```  - Invokes `llvm-as` tool to compile a llvm assembly file ('.ll') to a bitcode file (`.bc`). ``\
`     * ```  - Invokes the llvm `opt` tool to optimise the module. Just use the llvm standard optimisation groups of `O1`, `O2`, `O3`, depending on the optimisation level passed to 'ghc' by the user. ``\
`     * ```  - Invokes the llvm `llc` tool to generate the machine code ('.s' file) from the optimised bitcode. 'As' stage runs next, part of existing 'ghc' pipeline. ``\
`   * ```  - Stores the path and default settings of the system tools needed, so for LLVM back-end this is `llvm-as`, `opt` and `llc`. ``

The LLVM pipeline works as specified above. Code generation phase
occurs, using the option data the appropriate generator is selected
(which is the Llvm back-end is \`-fllvm\` has been specified on the
command line). After code generation, the next phase is determined, this
is done from the \`HscLlvm\` target data constructor which is selected
at ghc startup by . The next phase is \`LlvmAs\` which will compile the
text IR to an LLVM bitcode file (equivalent to \`llvm-as\` tool). After
this the \`LlvmLlc\` phase is run, which produces a native object file
from the llvm bitcode file (equivalanet to the \`llc\` tool). At this
stage, the output from all three back-ends should be 'equivalent'. After
this phase, the \`StopLn\`, or linking phase occurs which should result
in the end result. Compiling some Haskell code with the c-backend and
some with the llvm-backend and linking them together is supported.

LLVM Code Generation
--------------------

For LLVM code generation we need a method for representing and
generating LLVM code. The [LLVM
FAQ](http://llvm.org/docs/FAQ.html#langirgen) suggest the following
possible approaches:

` * Call into LLVM Libraries using FFI (can probably use `[`Haskell`
`LLVM` `Bindings`](http://hackage.haskell.org/package/llvm)`) `\
` * Emit LLVM Assembly (approach taken by `[`EHC's`](http://www.cs.uu.nl/wiki/Ehc/WebHome)` LLVM Back-end, can use the `[`module`](https://subversion.cs.uu.nl/repos/project.UHC.pub/trunk/EHC/src/ehc/LLVM.cag)` developed by them for this) `\
` * Emit LLVM Bitcode (can't see any reason to do this)`

The approach taken was to use the LLVM module from
[EHC](http://www.cs.uu.nl/wiki/Ehc/WebHome). This module contains an
abstract syntax representation of LLVM Assembly and the ability to
pretty print it. It has been heavily modified to increase its language
coverage as it was missing several LLVM constructs which were needed.
Ideally we would like to add a second pretty printer which calls into
the LLVM C++ API to generate LLVM Bitcode. This should hopefully
decrease the compile times and make the back-end more resilient to
future changes to LLVM Assembly. The LLVM Haskell binding (first option)
wasn't used as it represents LLVM at a very high level, which isn't
appropriate for the back-end.

Register Pinning
----------------

The new back-end supports a custom calling convention to place the STG
virtual registers into specific hardware registers. The current approach
taken by the C back-end and NCG of having a fixed assignment of STG
virtual registers to hardware registers for performance gains is not
implemented in the LLVM back-end. Instead, it uses a custom calling
convention to support something semantically equivalent to register
pinning. The custom calling convention passes the first N variables in
specific hardware registers, thus guaranteeing on all function entries
that the STG virtual registers can be found in the expected hardware
registers. This approach is believed to provide better performance than
the register pinning used by NCG/C back-ends as it keeps the STG virtual
registers mostly in hardware registers but allows the register allocator
more flexibility and access to all machine registers.

For some more information about the use of a custom calling convention
see [here (Discussion between Chris Lattner and David
Terei)](http://www.nondot.org/sabre/LLVMNotes/GlobalRegisterVariables.txt)

Code Generation
---------------

Code generation consists of translating a list of \`GenCmmTop\` data
types to LLVM code. \`GenCmmTop\` has the following form:

That is, it consists of two types, static data and functions. Each can
largely be handled separately. Just enough information is needed such
that pointers can be constructed to them and in many cases this
information can be gathered from assumptions and constraints on Cmm.

After all the polymorphic types are bound we get this:

The code generator lives in \`llvmGen\` with the driver being
\`llvmGen/LlvmCodeGen.lhs\`.

A large part of the code generation is keeping track of defined
variables/functions and their type. An \`LlvmEnv\` construct is used for
this. It is simply a dictionary storing function/variable names with
their corresponding type information. This is used to create correct
references/pointers between variables and functions.

### Unregisterised Vs. Registerised

Code generation can take place in two general modes, \`unregisterised\`
and \`registerised\`. There are two major differences from a back-end
code generation point of view. Firstly, in unregisterised mode a
optimisation feature called is disabled. This means that the \`h\` field
of \`CmmProc\` is empty. In registerised mode it instead contains the
\`CmmStatic\` data for the procedures info table which must be placed
just before the procedure in the generated code so that both the info
table and procedure can be accessed through one pointer. This
optimisation can be disabled separately though in \`registerised\` mode.

The other major change is the use of pinned global registers. The
\`Cmm\` language includes a concept called registers. These are used
like machine registers or variables in C to store the result of
expressions. Unlike \`LLVM\` they are mutable. \`Cmm\` includes two
types of registers as you can see below:

A \`LocalReg\` is a temporary general purpose register used in a
procedure with scope of a single procedure. A \`GlobalReg\` on the other
hand has global scope and a specific use. They are used just like
machine registers, with a Stack Pointer and Heap Pointer registers
creating a virtual machine (\`STG\`). \`GlobalReg\` is of the form:

In unregisterised mode these global registers are all just stored in
memory in the heap. A specific pass operating on Cmm that takes place
just before code generation thus transforms code such as:

into the following unregisterised form for code generation:

Where \`MainCapability\` is a label to the start of a RTS defined
structure storing all the global registers.

In registerised mode as many of these global registers are assigned
permanently to fixed hardware registers. This is done as it greatly
improves performance. As these registers are accessed very frequently
needing to load and store to memory for accessing adds a great cost. So
for example on \`x86\` the following map between \`Cmm\` global
registers and \`x86\` hardware registers exists:

These are all the available \`callee save\` registers on x86. \`callee
save\` are used as in ghc generated code now saving and restoring of
these registers are needed due to there new special use and because GHC
uses continuation passing style, so a \`'ret'\` statement is never
actually generated. And since they are \`callee save\`, foreign code can
also be called without any need to handle the \`Cmm\` registers.

!CmmData
--------

\`CmmData\` takes the following form:

Code generation takes place mainly in , driven by the main Llvm compiler
driver, }.

The code generation for data occurs in two phases, firstly the types and
all data is generated except for address values. Then the address values
are resolved. This two step method is used as in the first pass, we
don't know if a address refers to an external address or a
procedure/data structure in the current LLVM module. We also need the
type information in LLVM to create a pointer.

### 1st Pass : Generation

All \`CmmStatic\` is translated to LLVM structures.

!CmmStaticLit
-------------

These are translated when possible as follows:

``  * `CmmInt` -> Reduced to Int and then an appropriate `LMInt` of correct size is created. As LLVM supports any bit size, this is very straight forward. ``\
``  * `CmmFloat` -> Translated to a double, detecting NAN and INFINITY correctly. Then correct LLVM type (`float`, `double`, `float80`, `float128`) is selected. ``\
``  * `CmmLabel` -> Left untranslated at first, later resolved once we have determined types. As pointers are cast to word size ints, we can still determine types. ``\
``  * `CmmLabelOff` -> As above. ``\
``  * `CmmLabelDiffOff` -> As above. ``\
``  * `CmmBlock` -> `BlockId` is changed to a `CLabel` and then treated as a `CmmLabel` static type. ``\
``  * `CmmHighStackMark` -> Panic occurs if this type is encountered. ``

#### !CmmUninitialised

For this, a zeroed array of \`8bit\` values is created of correct size.

#### !CmmAlign & !CmmDataLabel

The LLVM back-end can't handle \`CmmAlign\` or \`CmmDataLabel\`. A panic
occurs if either is encountered. A \`CmmDataLabel\` is expected at the
very start of each list of \`CmmStatic\`. It is removed and used as the
name for the structure and constant instance.

#### !CmmString

This is translated into a LLVM string. Ascii characters are used when
they are printable, escaped hex values otherwise. A null termination is
added.

### 2nd Pass : Resolution

After the first pass, all types have been determined and all data
translated except for address values (CLabel's). All generated llvm data
is added to a Map of string to \`LlvmType\`, string being the data
structure name. All \`CmmProc's\` are added to the map as well, they
don't need to be properly passed though, just their names retrieved as
they have a constant type of void return and no parameters.

Now appropriate pointers can be generated using the type information
from the map and LLVM's \`getelementptr\` instruction. These are then
all passed to int's to allow the types of structures to be determined in
advance. If a pointer doesn't have a match in the Map, it is assumed to
refer to an external (outside of this module) address. An external
reference is declared for this address as:

Where i32 is the pointer size. (i64 if on 64 bit).

!CmmProc
--------

A Cmm procedure is made up of a list of basic blocks, with each basic
block being comprised of a list of CmmStmt

Desugaring instance declarations
================================

These notes compare various ways of desugaring Haskell instance
declarations. The tradeoffs are more complicated than I thought!

Basic stuff
-----------

 These desugar to the following Core: (Notation: I am omitting foralls,
big lambdas, and type arguments. I'm also using \`f x = e\` rather than
\`f = \\x.e\`.)

Points worth noting:

`* The class gives rise to an eponymous data type (in GHC it is actually`\
``   called `:TC`), the dictionary.  ``

`* There is an eponymous top-level selector function for each class method, `\
``   `opF` and `opG` in this case. ``

`` * The default method for `opG` becomes a top-level function `$dmopG`. ``\
``   It takes the `(C a)` dictionary a argument because the RHS is allowed to call ``\
`  other methods of C.`

`` * The instance declaration defines a dictionary `dCInt`.  Notice   ``\
``   that it's recursive, because we must pass `dCInt` to `opGI`. ``

`` * Crucially, the simplifier is careful not to choose `dCInt` as ``\
``   a loop breaker, and hence if it sees `case dCInt of ...` it ``\
``   can simplify the `case`.  ``

`` * If `$dmopG` is inlined, the recursion is broken anyway. ``

Dictionary functions
--------------------

Now consider an instance declaration that has a context: Here is one way
to desugar it. Notice that

`` * If we inline the selector `opF` in `opF d_as`, then ``\
``   we can simplify `opfl` to give a directly-recursive function: ``

`  This is important.`

`` * The BAD THING is that `dCList` is big, and hence won't be inlined. ``\
`  That's bad because it means that if we see`

``   we don't get to call `opfl` directly. Instead we'll call `dCList`, build  ``\
`  the dictionary, do the selection, etc.  So specialiation won't happen,`\
`  even when all the types are fixed.`

The INLINE strategy
-------------------

An obvious suggestion, which GHC implemented for a long time, is to give
\`dCList\` an INLINE pragma. Then it'll inline at every call site, the
dictionary will be visible to the selectors, and good things happen.

But it leads to a huge code blow-up in some cases. We call these
dictionary functions a lot, often in a nested way, and we know programs
for which the INLINE-all-dfuns approach generates gigantic code.
(Example: Serge's !DoCon.)

The out-of-line (A) strategy
----------------------------

The INLINE strategy would make sense if \`dCList\` could be guaranteed
small. Suppose the original instance declaration had been like this:
This is exactly what GHC 6.10 now does, behind the scenes. Desugaring
just as above, we'd get the following: Notice that

`` * `dCList` is guaranteed small, and could reasonably be INLINEd ``\
`  at every call site.  This good because it exposes the dictionary`\
`  structure to selectors.`

`` * `dCList` and `opF_aux` are mutually recursive.  But if we  ``\
``   avoid choosing `dCList` as the loop breaker we can inline ``\
``   `dCList` into `opF_aux`, and then the `opF` selector ``\
``   can "see" the dictionary structure, and `opF_aux` simplifies, thus: ``

``   Good!  Now `opF_aux` is self-recursive as it should be. ``\
`  The same thing happens with two mutually recursive methods`

`` * BUT notice that we reconstruct the `(C [a])` dictionary on ``\
`  each iteration of the loop.  As Ganesh points out in #3073, that`\
`  is sometimes bad.`

The out-of-line (B) strategy
----------------------------

We can avoid reconstructing the dictionary by passing it to
\`opF\_aux\`, by recasting latter thus: Notice the extra \`C \[a\]\` in
the context of \`opF\_aux\`. (Remember this is all internal to GHC.) Now
the same desugaring does this: The two definitions aren't even
recursive. BUT now that \`d\_as\` is an *argument* of \`opF\_aux\`, the
latter can't "see" that it's always a dictionary! Sigh. As a result, the
recursion in \`opF\_aux\` always indirects through the (higher order)
dictionary argument, using a so-called "unknown" call, which is *far*
less efficient than direct recursion.

Note also that

`` * Typechecking `opF_aux` is a bit fragile; see #3018.  Trouble is that ``\
``   when a constraint `(C [a])` arises in its RHS there are two ways ``\
``   of discharging it: by using the argument `d_as` directly, or by ``\
``   calling `(dCList d_a)`.  As #3018 shows, it's hard to guarantee that ``\
`  we'll do the former.`

User INLINE pragmas and out-of-line (A)
---------------------------------------

There is another difficulty with the out-of-line(A) strategy, that is
currently unsolved. Consider something like this: Then we'll desugar to
something like this: The INLINE on \`dCT\` is added by the compiler; the
INLINE on \`opF\_aux\` is just propagated from the users's INLINE
pragma... maybe the RHS is big.

Now the difficulty is that we GHC currently doesn't inline into the RHS
of an INLINE function (else you'd get terrible code blowup). So the
recursion between \`dCT\` and \`opF\_aux\` is not broken. One of the two
must be chosen as loop breaker, and the simplifier chooses \`opF\_aux\`.
Ironcially, therefore the user INLINE pragma has served only to
guarantee that it *won't* be inlined!!

(This issue doesn't arise with out-of-line(B) because (B) doesn't make
\`dCT\` and \`opF\_aux\` mutually recursive.)

Summary
-------

Here are the current (realistic) options:

`* Out-of-line(A): GHC 6.10 does this. `\
`  * Good: recursive methods become directly mutually-recursive`\
`  * Bad: lack of memoisation`\
`  * Bad: difficulty with user INLINE pragmas`

`* Out-of-line(B)`\
`  * Good: memoisation works`\
`  * Very bad: recursive methods iterate only via "unknown" calls.`\
`  * Good: no difficulty with user INLINE pragmas`

My current difficulty is that I see no way to get all the good things at
once.

PS: see also the comments at the start of
\`compiler/typecheck/TcInstDcls.lhs\`, which cover some of the same
ground.

Bugs & Other Problems
=====================

I've moved all known bugs into the trac bug database, the can be found
[here](http://hackage.haskell.org/trac/ghc/query?status=infoneeded&status=merge&status=new&status=patch&component=Compiler+%28LLVM%29&order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component)

Compiling more than one module at once
======================================

When compiling a single module, we can assume that all of our
dependencies have already been compiled, and query the environment as
necessary when we need to do things like look up interfaces to find out
what the types in our dependencies are. When we compile more than module
at once, as in \`--make\`, things get a bit more complicated:

1\. We have to analyze the dependency structure of the program in
question, and come up with a plan for how to compile the various
modules, and

2\. We have an opportunity to cache and reuse information from interface
files which we may load from the environment. This is why, for example,
\`ghc --make\` outperforms parallel one-shot compilation on one core.

This discussion is going to omit concerns related to dynamic code
loading in GHC (as would be the case in GHCi).

The overall driver
------------------

The meat of this logic is in
[GhcFile(compiler/main/GhcMake.hs)](GhcFile(compiler/main/GhcMake.hs) "wikilink"),
with primary entry point the function \`load\` (in the case of
\`--make\`, this function is called with \`LoadAllTargets\`, instructing
all target modules to be compiled, which is stored in \`hsc\_targets\`).

### Dependency analysis

Dependency analysis is carried out by the \`depanal\` function; the
resulting \`ModuleGraph\` is stored into \`hsc\_mod\_graph\`.
Essentially, this pass looks at all of the imports of the target modules
(\`hsc\_targets\`), and recursively pulls in all of their dependencies
(stopping at package boundaries.) The resulting module graph consists of
a list of \`ModSummary\` (defined in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")),
which record various information about modules prior to compilation
(recompilation checking, even), such as their module identity (the
current package name plus the module name), whether or not the file is a
boot file, where the source file lives. Dependency analysis inside GHC
is often referred to as \*\*downsweep\*\*.

ToDo: say something about how hs-boot files are

The dependency analysis is cached (in \`hsc\_mod\_graph\`), so later
calls to \`depanal\` can reuse this information. (This is not germane
for \`--make\`, which only calls \`depanal\` once.) \`discardProg\`
deletes this information entirely, while \`invalidateModSummaryCache\`
simply "touches" the timestamp associated with the file so that we
resummarize it.

The result of dependency analysis is topologically sorted in \`load\` by
\`topSortModuleGraph\`.

### Recompilation checking and stability

See also the page on \[wiki:Commentary/Compiler/RecompilationAvoidance
recompilation avoidance\].

ToDo: say something about stability; it's per SCC

### Compilation

Compilation, also known as \*\*upsweep\*\*, walks the module graph in
topological order and compiles everything. Depending on whether or not
we are doing parallel compilation, this implemented by \`upsweep\` or by
\`parUpsweep\`. In this section, we'll talk about the sequential
upsweep.

The key data structure which we are filling in as we perform compilation
is the \*\*home package table\*\* or HPT (\`hsc\_HPT\`, defined in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")).
As its name suggests, it contains informations from the \*home
package\*, i.e. the package we are currently compiling. Its entries,
\`HomeModInfo\`, contain the sum total knowledge of a module after
compilation: both its pre-linking interface \`ModIface\` as well as the
post-linking details \`ModDetails\`.

We \*clear\* out the home package table in the session (for \`--make\`,
this was empty anyway), but we pass in the old HPT.

ToDo: talk about how we fix up loops after we finish the loop

Finally, when the module is completely done being compiled, it is
registered in the home package table

ToDo: Talk about what happens when we fail while in the middle of
compiling a module cycle

Eager Promotion
===============

Eager promotion is a technique we use in GHC to improve the performance
of generational GC. It is somewhat specific to the characteristics of
lazy evaluation, since it takes advantage of the fact that we have some
objects that are mutated just once (i.e. thunks).

The key observation is this: when an object P contains a pointer to an
object Q in a younger generation, and P is not mutable, then we know
that Q cannot be garbage collected until the generation in which P
resides is collected. Hence, we might as well promote Q to this
generation immediately, rather than
\[wiki:Commentary/Rts/Storage/GC/Aging aging\] it or promoting it to an
intermediate generation. Furthermore, if eager promotion is successful,
then the object containing the old-to-new pointers will no longer need
to be in the \[wiki:Commentary/Rts/Storage/GC/RememberedSets remembered
set\] for the generation it resides in.

We gave some performance results for this technique in [Runtime Support
for Multicore
Haskell](http://www.haskell.org/~simonmar/papers/multicore-ghc.pdf); the
upshot is that it's worth 10% or so.

Eager promotion works like this. To do eager promtion, the scavenger
sets the flag \`gct-&gt;eager\_promotion\` (it can leave the flag set
when scavenging multiple objects, this is the usual way), and
\`gct-&gt;evac\_gen\` is set to the generation to which to eagerly
promote objects. The \`evacuate\` function will try to move each live
object into \`gct-&gt;evac\_gen\` or a higher generation if possible,
and set \`gct-&gt;failed\_to\_evac\` if it fails (see
\[wiki:Commentary/Rts/Storage/GC/RememberedSets\]). It may fail if the
target object has already been moved: we can't move an object twice
during GC, because there may be other pointers already updated to point
to the new location. It may also fail if the object is in a generation
that is not being collected during this cycle.

Objects which are repeatedly mutable should not be subject to eager
promotion, because the object may be mutated again, so eagerly promoting
the objects it points to may lead to retaining garbage unnecessarily.
Hence, when we are scavenging a mutable object (see
[GhcFile(rts/sm/Scav.c)](GhcFile(rts/sm/Scav.c) "wikilink")), we
temporarily turn off \`gct-&gt;eager\_promotion\`.

Eager Version Bumping Strategy
==============================

Versioning of GHC core/boot libraries adheres to Haskell's [Package
Versioning Policy](https://wiki.haskell.org/Package_versioning_policy)
whose scope is considered to apply to \*\*released artifacts\*\* (and
therefore doesn't prescribe when to //actually// perform version
increments during development)

However, in the spirit of continuous integration, GHC releases snapshot
artifacts, and therefore it becomes important for early
testers/evaluators/package-authors to be presented with accurate
PVP-adhering versioning, especially for those who want adapt to upcoming
API changes in new major GHC releases early (rather than being hit
suddenly by a disruptive version-bump-wave occurring at GHC release
time).

So while the usual scheme is to update a package version in the VCS
right before a release (and reviewing at that point whether a
patchlevel, minor or major version bump is mandated by the PVP), for GHC
bundled core/boot packages, the \*\*eager version bumping\*\* scheme is
preferred, which basically means:

This becomes particularly easy when also maintaining a \`changelog\`
file during development highlighting the changes for releases, as then
one easily keeps track of the last released version, as well as becoming
aware more easily of minor/major version increment-worthy API changes.

Video: [Types and
Classes](http://www.youtube.com/watch?v=pN9rhQHcfCo&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
(23'53")

Data types for Haskell entities: , , , , and 
=============================================

For each kind of Haskell entity (identifier, type variable, type
constructor, data constructor, class) GHC has a data type to represent
it. Here they are:

`* `**`Type`
`constructors`**` are represented by the `` type (`[`GhcFile(compiler/types/TyCon.hs)`](GhcFile(compiler/types/TyCon.hs) "wikilink")`).`\
`* `**`Classes`**` are represented by the `` type (`[`GhcFile(compiler/types/Class.hs)`](GhcFile(compiler/types/Class.hs) "wikilink")`).`\
`* `**`Data`
`constructors`**` are represented by the `` type (`[`GhcFile(compiler/basicTypes/DataCon.hs)`](GhcFile(compiler/basicTypes/DataCon.hs) "wikilink")`).`\
`* `**`Pattern`
`synonyms`**` are represented by the `` type (`[`GhcFile(compiler/basicTypes/PatSyn.hs)`](GhcFile(compiler/basicTypes/PatSyn.hs) "wikilink")`).`\
`* `**`Term` `variables`**` `` and `**`type`
`variables`**` `` are both represented by the `` type (`[`GhcFile(compiler/basicTypes/Var.hs)`](GhcFile(compiler/basicTypes/Var.hs) "wikilink")`).`

All of these entities have a , but that's about all they have in common.
However they are sometimes treated uniformly:

`* A `**`` `TyThing` ``**` (`[`GhcFile(compiler/types/TypeRep.hs)`](GhcFile(compiler/types/TypeRep.hs) "wikilink")`) is simply the sum of all four:`

`For example, a type environment is a map from `` to ``.  (The fact that a `` tells what name space it belongs to allow, for example, identically named values and types to  sit in a single map.)`

All these data types are implemented as a big record of information that
tells you everything about the entity. For example, a contains a list of
its data constructors; a contains its type (which mentions its ); a
contains the s of all its method selectors; and an contains its type
(which mentions type constructors and classes).

So you can see that the GHC data structures for entities is a *graph*
not tree: everything points to everything else. This makes it very
convenient for the consumer, because there are accessor functions with
simple types, such as . But it means that there has to be some tricky
almost-circular programming ("knot-tying") in the type checker, which
constructs the entities.

Type variables and term variables
---------------------------------

Type variables and term variables are represented by a single data type,
, thus
([GhcFile(compiler/basicTypes/Var.hs)](GhcFile(compiler/basicTypes/Var.hs) "wikilink")):
It's incredibly convenient to use a single data type for both, rather
than using one data type for term variables and one for type variables.
For example:

`* Finding the free variables of a term gives a set of variables (both type and term variables): ``.`\
`* We only need one lambda constructor in Core: ``.`

The type distinguishes the two sorts of variable; indeed, it makes
somewhat finer distinctions
([GhcFile(compiler/basicTypes/Var.hs)](GhcFile(compiler/basicTypes/Var.hs) "wikilink")):
Every has fields and a . The latter is identical to the in the former,
but is cached in the for fast comparison.

Here are some per-flavour notes:

`:: is self explanatory.`

`:: is used during type-checking only.  Once type checking is finished, there are no more ``s.`

`:: is used for term variables bound `*`in` `the` `module` `being`
`compiled`*`.   More specifically, a `` is bound either `*`within`*` an expression (lambda, case, local let), or at the top level of the module being compiled.`\
`* The `` of a `` may change as the simplifier repeatedly bashes on it.`\
`* A `` carries a flag saying whether it's exported. This is useful for knowing whether we can discard it if it is not used.`

`:: is used for fixed, immutable, top-level term variables, notably ones that are imported from other modules.  This means that, for example, the optimizer won't change its properties.`\
`* Always has an `` or `` [wiki:Commentary/Compiler/NameType Name], and hence has a `` that is globally unique across the whole of a GHC invocation.`\
`* Always bound at top level. `\
`* The `` of a `` is completely fixed.`\
`* All implicit Ids (data constructors, class method selectors, record selectors and the like) are are ``s from birth, even the ones defined in the module being compiled.`\
`* When finding the free variables of an expression (``), we only collect `` and ignore ``.`

All the value bindings in the module being compiled (whether top level
or not) are s until the !CoreTidy phase. In the !CoreTidy phase, all
top-level bindings are made into s. This is the point when a becomes
"frozen" and becomes a fixed, immutable .

 and implict Ids
----------------

s are further classified by their . This type is defined in
[GhcFile(compiler/basicTypes/IdInfo.hs)](GhcFile(compiler/basicTypes/IdInfo.hs) "wikilink"),
because it mentions other structured types such as . Unfortunately it is
*used* in Var.hs so there's a hi-boot knot to get it there. Anyway,
here's the declaration (elided a little): Some s are called **implicit
s**. These are s that are defined by a declaration of some other entity
(not just an ordinary variable binding). For example:

`* The selectors of a record type`\
`* The method selectors of a class`\
`* The worker and wrapper Id for a data constructor`

It's easy to distinguish these Ids, because the field says what kind of
thing it is: .

HC files and the Evil Mangler
=============================

GHC no longer has an evil mangler.

Strictness analysis: examples
=============================

Consider:

We want to make sure to figure out that f's argument is demanded with
type L1X(L1X(LMX)) -- that is, it may or may not be demanded, but if it
is, it's always applied to two arguments. This shows why shouldn't just
throw away the argument info: in this case, the expression has a
nonstrict demand placed on it, yet we still care about the arguments.

On the other hand, in: we want to say that if the result of has demand
placed on it (i.e., not a call demand), the body of has demand placed on
it, not . So this case needs to be treated differently from the one
above.

System FC: equality constraints and coercions
=============================================

For many years, GHC's intermediate language was essentially:

`* System Fw, plus`\
`* algebraic data types (including existentials)`

But that is inadequate to describe GADTs and associated types. So in
2006 we extended GHC to support System FC, which adds

`* equality constraints and coercions`

You can find a full description of FC in the paper
[3](http://research.microsoft.com/~simonpj/papers/ext-f); note that GHC
uses the system described in post-publication Appendix C, not the system
in the main body of the paper. The notes that follow sketch the
implementation of FC in GHC, but without duplicating the contents of the
paper.

A coercion \`c\`, is a type-level term, with a kind of the form \`T1 :=:
T2\`. (\`c :: T1 :=: T2\`) is a proof that a term of type \`T1\` can be
coerced to type \`T2\`. Coercions are classified by a new sort of kind
(with the form ). Most of the coercion construction and manipulation
functions are found in the module,
[GhcFile(compiler/types/Coercion.hs)](GhcFile(compiler/types/Coercion.hs) "wikilink").

Coercions appear in Core in the form of expressions: if \`t :: T1\` and
\`c :: T1:=:T2\`, then . See \[wiki:Commentary/Compiler/CoreSynType\].

Coercions and Coercion Kinds
----------------------------

The syntax of coercions extends the syntax of types (and the type
\`Coercion\` is just a synonym for \`Type\`). By representing coercion
evidence on the type level, we can take advantage of the existing
erasure mechanism and keep non-termination out of coercion proofs (which
is necessary to keep the system sound). The syntax of coercions and
types also overlaps a lot. A normal type is evidence for the reflexive
coercion, i.e., Coercion variables are used to abstract over evidence of
type equality, as in

There are also coercion constants that are introduced by the compiler to
implement some source language features (newtypes for now, associated
types soon and probably more in the future). Coercion constants are
represented as \`TyCon\`s made with the constructor \`CoercionTyCon\`.

Coercions are type level terms and can have normal type constructors
applied to them. The action of type constructors on coercions is much
like in a logical relation. So if \`c1 :: T1 :=: T2\` then

and if \`c2 :: S1 :=: S2\` then The sharing of syntax means that a
normal type can be looked at as either a type or as coercion evidence,
so we use two different kinding relations, one to find type-kinds
(implemented in Type as \`typeKind :: Type -&gt; Kind\`) and one to find
coercion-kinds (implemented in Coercion as \`coercionKind :: Coercion
-&gt; Kind\`).

Coercion variables are distinguished from type variables, and
non-coercion type variables (just like any normal type) can be used as
the reflexive coercion, while coercion variables have a particular
coercion kind which need not be reflexive.

GADTs
-----

The internal representation of GADTs is as regular algebraic datatypes
that carry coercion evidence as arguments. A declaration like would
result in a data constructor with type This means that (unlike in the
previous intermediate language) all data constructor return types have
the form \`T a1 ... an\` where \`a1\` through \`an\` are the parameters
of the datatype.

However, we also generate wrappers for GADT data constructors which have
the expected user-defined type, in this case Where the 4th and 5th
arguments given to \`T1\` are the reflexive coercions

Representation of coercion assumptions
--------------------------------------

In most of the compiler, as in the FC paper, coercions are abstracted
using \`ForAllTy cv ty\` where \`cv\` is a coercion variable, with a
kind of the form \`PredTy (EqPred T1 T2)\`. However, during type
inference it is convenient to treat such coercion qualifiers in the same
way other class membership or implicit parameter qualifiers are treated.
So functions like \`tcSplitForAllTy\` and \`tcSplitPhiTy\` and
\`tcSplitSigmaTy\`, treat \`ForAllTy cv ty\` as if it were \`FunTy
(PredTy (EqPred T1 T2)) ty\` (where \`PredTy (EqPred T1 T2)\` is the
kind of \`cv\`). Also, several of the \`dataCon\`XXX functions treat
coercion members of the data constructor as if they were dictionary
predicates (i.e. they return the \`PredTy (EqPred T1 T2)\` with the
theta).

Newtypes are coerced types
--------------------------

The implementation of newtypes has changed to include explicit type
coercions in the place of the previously used ad-hoc mechanism. For a
newtype declared by the \`NewTyCon\` for \`T\` will contain n\`t\_co =
CoT\` where: This \`TyCon\` is a \`CoercionTyCon\`, so it does not have
a kind on its own; it basically has its own typing rule for the
fully-applied version. If the newtype \`T\` has k type variables, then
\`CoT\` has arity at most k. In the case that the right hand side is a
type application ending with the same type variables as the left hand
side, we "eta-contract" the coercion. So if we had then we would
generate the arity 0 coercion \`CoS : S :=: \[\]\`. The primary reason
we do this is to make newtype deriving cleaner. If the coercion cannot
be reduced in this fashion, then it has the same arity as the tycon.

In the paper we'd write and then when we used \`CoT\` at a particular
type, \`s\`, we'd say which encodes as \`(TyConApp instCoercionTyCon
\[TyConApp CoT \[\], s\])\`

But in GHC we instead make \`CoT\` into a new piece of type syntax (like
\`instCoercionTyCon\`, \`symCoercionTyCon\` etc), which must always be
saturated, but which encodes as In the vocabulary of the paper it's as
if we had axiom declarations like The newtype coercion is used to wrap
and unwrap newtypes whenever the constructor or case is used in the
Haskell source code.

Such coercions are always used when the newtype is recursive and are
optional for non-recursive newtypes. Whether or not they are used can be
easily changed by altering the function mkNewTyConRhs in
iface/BuildTyCl.lhs.

Roles
-----

Roles specify what nature of equality a coercion is proving. See
\[wiki:Roles\] and RolesImplementation.

Simplification
--------------

`* exprIsConApp_maybe`

`* simplExpr`

GHC Commentary: Runtime aspects of the FFI
==========================================

Foreign Import "wrapper"
------------------------

Files [GhcFile(rts/Adjustor.c)](GhcFile(rts/Adjustor.c) "wikilink")
[GhcFile(rts/AdjustorAsm.S)](GhcFile(rts/AdjustorAsm.S) "wikilink").

Occasionally, it is convenient to treat Haskell closures as C function
pointers. This is useful, for example, if we want to install Haskell
callbacks in an existing C library. This functionality is implemented
with the aid of adjustor thunks.

An adjustor thunk is a dynamically allocated code snippet that allows
Haskell closures to be viewed as C function pointers.

Stable pointers provide a way for the outside world to get access to,
and evaluate, Haskell heap objects, with the RTS providing a small range
of ops for doing so. So, assuming we've got a stable pointer in our hand
in C, we can jump into the Haskell world and evaluate a callback
procedure, say. This works OK in some cases where callbacks are used,
but does require the external code to know about stable pointers and how
to deal with them. We'd like to hide the Haskell-nature of a callback
and have it be invoked just like any other C function pointer.

Enter adjustor thunks. An adjustor thunk is a little piece of code
that's generated on-the-fly (one per Haskell closure being exported)
that, when entered using some 'universal' calling convention (e.g., the
C calling convention on platform X), pushes an implicit stable pointer
(to the Haskell callback) before calling another (static) C function
stub which takes care of entering the Haskell code via its stable
pointer.

An adjustor thunk is allocated on the C heap, and is called from within
Haskell just before handing out the function pointer to the Haskell (IO)
action. User code should never have to invoke it explicitly.

An adjustor thunk differs from a C function pointer in one respect: when
the code is through with it, it has to be freed in order to release
Haskell and C resources. Failure to do so will result in memory leaks on
both the C and Haskell side.

------------------------------------------------------------------------

CategoryStub

Function Calls
==============

Source files: [GhcFile(rts/Apply.h)](GhcFile(rts/Apply.h) "wikilink"),
[GhcFile(rts/Apply.cmm)](GhcFile(rts/Apply.cmm) "wikilink")

Dealing with calls is by far the most complicated bit of the execution
model, and hence of the code generator. GHC uses an *eval/apply*
strategy for compiling function calls; all the details of the design are
in the paper [Making a fast curry: push/enter vs. eval/apply for
higher-order
languages](http://www.haskell.org/~simonmar/papers/eval-apply.pdf).

First, we need some terminology:

` * The `**`arity`**` of a function is the number of lambdas statically used in [wiki:Commentary/Compiler/StgSynType the lambda-form of its definition].  Note that arity is not deducible from the type.  Example:`

``    Here, `f` has arity 1, even though its type suggests it takes two arguments.  The point is that the compiled code for `f` will expect to be passed just one argument, `x`. ``

` * The `**`entry` `point`**` (sometimes called the `**`fast` `entry`
`point`**`) of a function of arity N expects its first N  arguments to be passed in accordance with the standard [wiki:Commentary/Rts/HaskellExecution/CallingConvention calling conventions].`

` * A `**`known`
`call`**` is a call of a function whose binding site is statically visible:`\
`   * The function is bound at top level in this module; or,`\
`   * The function is bound at top level in another module, and optimistion is on, so we can see the details (notably arity) of the function in the module's interface file; or,`\
``    * The function is bound by an `let` binding that encloses the call. ``

When compiling a call, there are several cases to consider, which are
treated separately.

` * `**`Unknown`
`function`**`;  a call in which we do not statically know what the function is.  In that case we must do a "generic apply".  This is so exciting that it deserves its [wiki:Commentary/Rts/HaskellExecution/FunctionCalls#Genericapply own section].`

` * `**`Known` `function,` `saturated`
`call`**`.   The function is applied to exactly the right number of arguments to satisfy its arity.  In that case, we simply load the arguments according to the standard entry convention, and tail-call (jump to) the function's entry point.  On average, about 80% of all calls fall into this category (see the eval/apply paper for measurements).`

` * `**`Known` `function,` `too` `few`
`arguments`**`.  In this case, we want to build a partial application (PAP), and return with a pointer to the PAP in the return register.  Since building a PAP is a complicated business, instead we just behave as for an unknown function call, which will end up calling into the `[`ref(Generic`
`apply)`](ref(Generic_apply) "wikilink")` code, which will build the PAP for us.`

` * `**`Known` `function,` `too` `many`
`arguments`**`.  We want to save the extra arguments on the stack, push a return address, and then behave just like a saturated call.  When the result comes back, we should behave like "unknown call".  However, to avoid needing to generate code for a new continuation here, the return address that we push on the stack is that of an appropriate `[`ref(Generic`
`apply)`](ref(Generic_apply) "wikilink")` function, which will perform the application of the extra arguments to the (unknown) function returned by the saturated call.`

Generic apply
-------------

Files: [GhcFile(utils/genapply)](GhcFile(utils/genapply) "wikilink")

When compiling a call that has an unknown function, we must generate
code to

` * Evaluate the function`\
` * Scrutinise the function value returned to see its arity, and dispatch into the same three cases as in the case of known calls:`\
`   * Exactly the right number of arguments: load them into the standard locations and tail-call the function's entry point`\
`   * Too few arguments: build a PAP`\
`   * Too many arguments: save the excess arguments, and tail call the function as for a saturated cal.`

All of this takes quite a lot of code, so we pre-generate a whole bunch
of generic-apply code sequencues, one for each combination of arguments.
This code is generated by the tool
[GhcFile(utils/genapply)](GhcFile(utils/genapply) "wikilink"), and the
generated code appears in \`rts/AutoApply.cmm\`.

For example, if we find a call to an unknown function applied to two
(boxed) \`Int\` arguments, load the function and its two arguments as
for the standard entry convention and jump to \`stg\_ap\_pp\_fast\`.
This latter code is in \`rts/AutoApply.cmm\`, generated by the
\`genapply\` tool. The "\`pp\`" part is the bit that says the code is
specialised for two pointer arguments.

In addition to the family of \`stg\_ap\_<pattern>\_fast\` functions for
making calls to unknown functions with various argument patterns, there
is a corresponding family of return addresses
\`stg\_ap\_<pattern>\_info\`. The idea is that you can push a
continuation that will make a call to the function that is returned to
it. For example, to push a continuation that will apply a single pointer
argument, we would push the following words on the stack:

|| arg || || \`stg\_ap\_p\_info\` ||

The Garbage Collector
=====================

GC concepts:

`* [wiki:Commentary/Rts/Storage/GC/Aging Aging]`\
`* [wiki:Commentary/Rts/Storage/GC/Pinned Pinned objects]`\
`* [wiki:Commentary/Rts/Storage/GC/Roots Roots]`\
`* [wiki:Commentary/Rts/Storage/GC/EagerPromotion Eager promotion]`\
`* [wiki:Commentary/Rts/Storage/GC/RememberedSets Remembered sets]`\
`* [wiki:Commentary/Rts/Storage/GC/Weak Weak pointers and finalizers]`\
`* [wiki:Commentary/Rts/Storage/GC/CAFs CAFs]`

GC algorithms supported:

`* [wiki:Commentary/Rts/Storage/GC/Copying Copying GC]`\
`* [wiki:Commentary/Rts/Storage/GC/Parallel Parallel GC]`\
`* [wiki:Commentary/Rts/Storage/GC/Marking Marking] (for compaction or sweeping)`\
`* [wiki:Commentary/Rts/Storage/GC/Compaction Compaction]`\
`* [wiki:Commentary/Rts/Storage/GC/Sweeping Sweeping] (for mark-region GC)`\
`* [wiki:Commentary/Rts/Storage/GC/Immix Immix] (not supported yet)`

GC overview
-----------

The GC is designed to be flexible, supporting lots of ways to tune its
behaviour. Here's an overview of the techniques we use:

`` * Generational GC, with a runtime-selectable number of generations (`+RTS -G ``<n>``  -RTS`, where `n >= 1`).  Currently it is a ``\
`  traditional generational collector where each collection collects a particular generation and all younger generations.`\
`  Generalizing this such that any subset of generations can be collected is a possible future extension.`

`* The heap grows on demand.  This is straightforwardly implemented by basing the whole storage manager on a [wiki:Commentary/Rts/Storage/BlockAlloc block allocator].`

`* Aging: objects can be aged within a generation, to avoid premature promotion.  See [wiki:Commentary/Rts/Storage/GC/Aging].`

`` * The heap collection policy is runtime-tunable.  You select how large a generation gets before it is collected using the `+RTS -F ``<n>``  -RTS` option, where ` ``<n>`` ` is a factor of the generation's size the last time it was collected.  The default value is 2, that is a generation is allowed to double in size before being collected. ``

GC data structures
------------------

[GhcFile(includes/rts/storage/GC.h)](GhcFile(includes/rts/storage/GC.h) "wikilink")

### generation

The main data structure is \`generation\`, which contains:

`` `blocks`:: ``\
`  a pointer to a list of blocks`

`` `large_objects`:: ``\
`  a pointer to a list of blocks containing large objects`

`` `threads`:: ``\
`  a list of threads in this generation`

`` `mut_list`:: ``\
`  the [wiki:Commentary/Rts/Storage/GC/RememberedSets remembered set], a list of blocks containing pointers to objects in `*`this`*` generation that point to objects in `*`younger`*` generations`

and various other administrative fields (see
[GhcFile(includes/rts/storage/GC.h)](GhcFile(includes/rts/storage/GC.h) "wikilink")
for the details).

Generations are kept in the array \`generations\[\]\`, indexed by the
generation number.

### nursery

A \`nursery\` is a list of blocks into which the mutator allocates new
(small) objects. For reasons of locality, we want to re-use the list of
blocks for the nursery after each GC, so we keep the nursery blocks
rather than freeing and re-allocating a new nursery after GC.

The struct \`nursery\` contains only two fields

`` `blocks`:: ``\
`  the list of blocks in this nursery`\
`` `n_blocks`:: ``\
`  the number of blocks in the above list`

In the threaded RTS, there is one nursery per Capability, as each
Capability allocates independently into its own allocation area.
Nurseries are therefore stored in an array \`nurseries\[\]\`, indexed by
Capability number.

The blocks of the nursery notionally logically to generation 0, although
they are not kept on the list \`generations\[0\].blocks\`. The reason is
that we want to keep the actual nursery blocks separate from any blocks
containing live data in generation 0. Generation 0 may contain live data
for two reasons:

`* objects live in the nursery are not promoted to generation 1 immediately, instead they are [wiki:Commentary/Rts/Storage/GC/Aging aged], first being copied to generation 0, and then being promoted to generation 1 in the next GC cycle if they are still alive.`

`* If there is only one generation (generation 0), then live objects in generation 0 are retained in generation 0 after a GC.`

I know kung fu: learning STG by example
=======================================

The STG machine is an essential part of GHC, the world's leading Haskell
compiler. It defines how the Haskell evaluation model should be
efficiently implemented on standard hardware. Despite this key role, it
is generally poorly understood amongst GHC users. This document aims to
provide an overview of the STG machine in its modern, eval/apply-based,
pointer-tagged incarnation by a series of simple examples showing how
Haskell source code is compiled.

What is STG, exactly?
---------------------

Haskell code being sucked through GHC has a complex lifecycle. Broadly
speaking, it transitions between five representations:

The path from C-- to assembly varies: the three possible backends are C
(\`-fvia-c\`), LLVM (\`-fllvm\`), and the default backend -- the native
code genarator (or NCG), which generates assembly directly from the
GHC-internal C-- data type.

STG is a simple functional language, rather like the more famous Core
language. It differs in the following main respects:

`1. In its current incarnation, it isn't typed in the Haskell sense,`\
`   though it does know about `*`representation`*` types`\
`2. It is in administrative normal form (ANF), which is where every`\
`   subexpression is given a name`\
`3. Every $\lambda$, constructor application, and primitive operator`\
`   is $\eta$-expanded`\
`4. It is annotated with a ton of information that the code`\
`   generator is interested in knowing`

STG expressions can be one of the following:

`1. Atoms (i.e. literals and variables)`\
`` 2. `let`-bindings (both recursive and non-recursive) over another ``\
`   expression, where let-bound things are one of:`\
`    * A function value with explicit lambdas`\
`    * An unsaturated application`\
`    * A constructor applied to atoms`\
`    * A thunk (i.e. any expression not fitting into one of the above`\
`      categories)`

`3. Saturated primitive application of a primitive to variables`\
`4. Application of a variable to one or more atoms`\
`5. Case deconstruction of an expression, where each branch may also`\
`   be an expression`

The job of the *STG machine* is to evaluate these expressions in a way
which is efficiently implementable on standard hardware. This document
will look at how exactly this is achieved by looking at real examples of
the C-- code GHC generates for various Haskell expressions.

This document will take a very low-level view of the machine, so if you
want to get comfortable with how the STG machine executes at a more
abstract level before reading this document, you might want to read the
paper ["How to make a fast curry: push/enter vs.
eval/apply"](http://research.microsoft.com/en-us/um/people/simonpj/papers/eval-apply/).
It presents the STG machine without reference to an explicit stack or
registers, but instead as a transition system. This transition system
has also been implemented as a Haskell program called
[ministg](http://hackage.haskell.org/package/ministg) by [Bernie
Pope](http://ww2.cs.mu.oz.au/~bjpop/), for those who wish to see it in
action on some simple examples.

An overview of the STG machine
------------------------------

Before we dive in, a note: this document will describe the STG machine
as it is implemented on x86-style architectures. I will use the terms
"the STG machine" and "the STG machine as implemented on x86 by GHC"
interchangeably. The implementation is somewhat different on x64, not
least due to the greater number of available registers.

This overview section is rather bare. Readers might be able to fill in
any gaps in my explanation by using some of the following sources:

`* `[`The` `Haskell` `Execution`
`Model`](http://hackage.haskell.org/trac/ghc/wiki/Commentary/Rts/HaskellExecution)\
`* `[`Storage`](http://hackage.haskell.org/trac/ghc/wiki/Commentary/Rts/Storage)\
`* `[`The` `Spineless` `Tagless`
`G-machine`](http://research.microsoft.com/en-us/um/people/simonpj/Papers/spineless-tagless-gmachine.ps.gz)\
`  - now sadly rather out of date`\
`* `[`Faster` `laziness` `through` `dynamic` `pointer`
`tagging`](http://research.microsoft.com/en-us/um/people/simonpj/papers/ptr-tag/ptr-tagging.pdf)

### Components of the machine

In its bare essentials, the STG machine consists of three parts:

`1. The STG registers:`\
`    * There are rather a lot of registers here: more than can be`\
`      practicably stored in actual available processor registers on most`\
`      architectures.`\
`    * To deal with the lack of processor registers, most of the STG `\
`      registers are actually kept on the stack in a block of memory`\
`      pointed to by a special STG register called the "base register" (or `\
``       `BaseReg`). To get or set values of registers which are not kept in ``\
`      processor registers, the STG machine generates an instruction to`\
``       load or store from an address relative to the `BaseReg`. ``\
``     * The most important four registers are the `BaseReg`, the stack ``\
``       pointer (`Sp`), the heap pointer (`Hp`), and the general purpose ``\
``       register `R1` which is used for intermediate values, as well as for  ``\
`      returning evaluated values when unwinding the stack. These are the `\
`      four registers which are assigned actual processor registers when`\
`      implementing the STG machine on x86.`\
`2. The STG stack:`\
`    * Stores function arguments and continuations (i.e. the stack`\
`      frames which are executed when a function returns)`\
`    * Grows downwards in memory`\
``     * The top of the stack is pointed to by the STG register `Sp`, and  ``\
``       the maximum available stack pointer is stored in `SpLim`. There is ``\
`      no frame pointer.`

`3. The heap:`\
`   * Used to store many different sorts of heap object: notably`\
`     functions, thunks and data constructors`\
`   * Grows upwards in memory, towards the stack`\
`   * All allocation occurs using a bump-allocator: the heap pointer is`\
`     simply incremented by the number of bytes desired (subject to to a`\
`     check that this does not exhaust available memory). The garbage`\
`     collector is responsible for moving objects out of the area of the `\
`     heap managed by the bump allocator and into the care of its `\
`     generational collector.`\
`   * The last address in the bump-allocated part of the heap that has `\
``      been used is pointed to by the STG register `Hp`, with `HpLim` ``\
`     holding the maximum address available for bump-allocation.`

### Important concepts in the machine

Some of the key concepts in the STG machine include *closures*, *info
tables* and *entry code*. We tackle them in reverse order:

`Entry code::`\
`    The actual machine code that the STG machine will execute upon`\
`    "entry". Entry means different things for different heap objects.`

`     * For `*`thunks`*`, entry is when the thunk is forced by some demand`\
``        for its value, such as a `case` expression scrutinising it ``\
`     * For `*`functions`*`, entry is when the function is applied to as`\
`       many arguments as are demanded by the arity recorded in its info`\
`       table`\
`     * For `*`continuations`*`, entry occurs when a value is returned from`\
`       a nested call, and hence the need arises to consume the value and`\
`       continue evaluation`

`Info table::`\
`    A block of memory allocated statically, which contains metadata`\
`    about a closure. The most important fields for our purposes are the`\
`    entry code pointer and the arity information (if this is the info`\
`    table for a thunk, function or partial application)`

`Closure::`\
`    Essentially a heap-allocated pair of the free variables of some`\
`    code, and a pointer to its info table (i.e. its info pointer).`

For an example of how these parts work together, consider the following
code

The nested lambda will give rise to all of the above objects.

The closure will store a pointer to \`x\`'s closure (as it is a free
variable of the lambda), along with a pointer to an info table. That
info table will contain information relevant to a function value,
recording information such as the fact that it has an arity of 1 (i.e.
the binding for \`y\`), and the pointer to the entry code for the
function \`\\y -&gt; y + x\` itself. This entry code will implement the
addition by combining the closure for the free variable \`x\` (taken
from the closure) with the stack-passed \`y\` variable's closure.

Upon entry to some code, pointers to closures are made available in
\`R1\`. That is to say, before entry code is jumped to, \`R1\` is set up
to point to the associated closure, so that the entry code can access
free variables (if any).

Closures for code which contain no free variables (such as the closure
for \`True\` and \`False\`, and functions applied to no arguments such
as \`(:)\` and \`id\`) are allocated statically by the compiler in the
same manner as info tables are.

### Overview of execution model of the machine

This will be covered in more detail in the examples below, so I will use
this section to make some general points.

The goal of the STG machine is to reduce the current expression to a
value. When it has done so, it:

`1. Stores a tagged pointer to evaluated closure in the STG register`\
``    `R1` ``\
`2. Jumps to the entry code of the info table pointed to by the`\
`   value at the top of the STG stack`\
`    * This may also be called the info table of the `*`continuation`*` of`\
`      the expression`

The continuation code is responsible for popping its info pointer (and
stack-allocated free variables, if any) from the stack before returning.

Arguments are passed on the stack, and are popped by the callee. Upon a
jump to the entry code for a function, there are always precisely as
many arguments on the stack as the (statically known) arity of that
function, and those arguments will be followed by the info pointer of a
continuation.

Saturated application to known functions
----------------------------------------

Handling application in the STG machine is a big topic, and so in this
first section we only look at the case of *saturated* applications to
*known* functions - i.e. those functions that the compiler statically
knows information such as the entry code pointer and arity for.

### Example 1: function application with sufficient stack space

Application of functions is the bread and butter of the STG machine.
Correspondingly, this first Haskell program

compiles to very simple C-- code

The STG machine passes arguments to functions on the STG stack, and a
pointer to the stack top is stored in the STG register \`Sp\`.
Furthermore, because GHC currently uses the eval/apply variant of the
STG machine, exactly as many arguments as the function expects to
receive are guaranteed to present on the stack.

Therefore, upon entry to the \`known\_app\` function, we are guaranteed
that the STG stack has a pointer to a closure of type \`()\` on top of
it. In order to call \`known\_fun\`, we just modify the top of the stack
to replace that pointer with a pointer to the statically allocated
closure for the literal \`10\`, and then tail-call into the entry code
of \`known\_fun\`.

### Example 2: function application that needs to grow the stack

This Haskell code is apparently little more complicated than the
previous example

however, it generates radically different C-- code:

As before, upon entry the STG stack is guaranteed to have a single
closure pointer at its top. However, in order to call into known\_fun\_2
we need at least two free stack slots at the top for arguments, which
means that we have to grow the stack by one word before we can make the
call.

#### Checking for sufficient stack space

First, we check to see if growing the stack would overflow allocated
stack space, by comparing the STG stack pointer register \`Sp\` with the
stack limit register \`SpLim\`:

(The stack grows downwards, hence the *subtraction* of 4 from the
current \`Sp\`). If the stack check fails, we branch to \`clH\`:

This stores the closure of the current function in \`R1\`, and then
jumps into the hand-written garbage collector code to force it to grow
the stack. After the stack has been grown, the collector will call back
into \`Main\_knownzuappzu2\_entry\` by using the information stored in
the (statically-allocated) \`Main\_knownzuappzu2\_closure\` closure
pointed to by \`R1\`, and the stack check will be run again - hopefully
succeeding this time!

#### Making the known call

Given that the stack check succeeds, it is easy to make the actual call
we are after. We simply grow the stack by the required amount, and write
the two arguments to \`known\_fun\_2\` into the top two stack slots
(overwriting our own first argument in the process, of course):

A simple tail call to the new function finishes us off:

Example 3: Unsaturated applications to known functions
------------------------------------------------------

Despite describing an undersaturated call, this Haskell code

compiles to straightforward C-- as follows

The reason that there is no special magic to deal with undersaturated
applications to known functions is simple: GHC simply gives
\`known\_undersaturated\_app\` an arity of 2, so by the time we jump to
the entry code the stack must already contain any arguments required by
\`known\_fun\_2\`.

Example 4: Applications to unknown functions
--------------------------------------------

We aren't going to tackle oversaturated calls to known functions until
we've considered happens to calls to statically-unknown functions. To
see what these look like, we are going to use the following Haskell code

Which compiles to this C-- function

Unlike the previous cases we have looked at, we are compiling an
application where we don't statically know either the arity or the info
pointer of the function being applied. To deal with such cases, the STG
machine uses several pre-compiled "generic apply" functions which
inspect the info-table for the function in question and decide how the
available arguments should be applied to it.

### Dealing with generic application

There are three cases the generic apply functions have to deal with:

`1. The function's arity (recorder in the function closure's info`\
`   table) exactly matches the number of arguments available on the`\
`   stack`\
`    * This is the best case. In this case, the generic apply function`\
`      simply makes a tail call into the function's entry code`

`2. The function's arity is greater than the number of arguments`\
`   available on the stack`\
`    * In this case, the generic apply code allocates a PAP (partial`\
`      application) closure which closes over both the new arguments and`\
`      the function pointer, and returns that value, in the normal STGish`\
`      way, to the continuation on the top of the stack`

`3. The function's arity is less than the number of arguments`\
`   available on the stack`\
`    * In this case, a number of arguments matching the arity are pushed`\
`      on top of the stack, followed by a continuation which uses another`\
`      of the generic apply functions to apply the remaining arguments.`\
`      The code for the original function is then entered`\
`    * Eventually the code for the continuation is entered and another`\
`      generic apply function will be tail-called to deal with the`\
`      result`

Potentially, one generic apply function is required for every "argument
pattern". Some example argument patterns are:

Because the number of patterns is large (actually unbounded, because
functions might be of any arity), GHC only generates generic apply
functions for enough patterns so that 99.9% of all calls observed in
practice have a generic apply function. Generic apply functions for
calls of larger arity can be simulated by chaining together several
smaller generic apply functions, in a similar manner as when dealing
with oversaturated function applications.

### Making the call to the generic application code

Let's remind ourselves of the original code:

Knowing about generic apply functions, the call itself is easy to
understand. We pop the top of the stack (the function argument) into
\`R1\` and then jump into the generic application code for the case
where the stack contains a single pointer argument, which deals with all
the cases for \`f\` described above.

Example 5: oversaturated applications to known functions
--------------------------------------------------------

This Haskell code

compiles to the following C-- function

As you might see, despite being a call to a known function, this code
makes use of the generic apply functions we discussed in the last
section. Let's pick the function apart and see how it works.

First, we do the usual stack check. What differs from the last time we
saw this check is that we are not only allocating space for arguments on
the stack, but also for a *continuation*. We set up these new stack
entries as follows:

i.e. the final stack looks as follows (note that the code overwrites the
old pointer to a closure of type ()):

Because \`known\_fun\_2\` is of arity 2, when we jump to its entry code,
it will only consume the top two arguments from the stack: i.e. the two
pointers to \`base\_GHCziBase\_id\_closure\`. It will then evaluate to
some sort of value and transfer control to the entry code for
\`stg\_ap\_p\_info\`.

This is where the magic happens: the entry code for \`stg\_ap\_p\_info\`
will apply the function value that was returned from \`known\_fun\_2\`
to the (pointer) argument in the "free variable" of its (stack
allocated) closure -- and we have arranged that that is
\`stg\_INTLIKE\_closure+209\`, i.e. the closure for the \`Int\` literal
\`10\`. This code is shared with the generic application functions for
calls to unknown functions, so this will make use of the
\`stg\_ap\_p\_fast\` function we saw before.

Finally, control will be transferred back to the caller for
\`known\_oversat\_app\`, and all will be well.

Example 6: allocation of thunks and data
----------------------------------------

Something that happens all the time in Haskell is allocation. There are
three principal types of thing that get allocated: function closures,
thunks, and data. These are all treated pretty much the same in the STG
machine for the simple reason that they share many common
characteristics:

`* Entry code which the STG machine jumps to, in order to evaluate`\
`  them`\
`   * Note that for constructors, the entry code is trivial, as they`\
`     are always already evaluated! In this case, control will be`\
`     transferred directly back to the caller's continuation.`

`* Free variables stored in a closure`\
`   * For data, these "free variables" will be the values in the fields`\
`     of the particular data constructor`

`* Info-tables containing various miscellaneous metadata about the`\
`  heap object, such as function arity`

Let us look at how a thunk and a data constructor get allocated in a
simple setting:

This compiles into the following C--:

Let's break this function down slowly.

### Checking for sufficient heap space

Any function that needs to allocate memory might find that the heap has
been exhausted. If that happens, it needs to call into the garbage
collector in order to get the heap cleaned up and (possibly) enlarged.

Hence, the first thing any such function does is check to see if enough
memory is available for its purposes:

This is simple enough. The function needs to allocate 20 bytes (the data
constructor takes up 2 words, and the thunk will take up 3), so it
speculatively increments Hp and then checks the STG registers \`Hp\` and
\`HpLim\` (the pointer to the top of the available heap space) against
each other.

If memory is insufficient (i.e. we have moved \`Hp\` past the top of the
available heap), the code deals with it by setting the \`HpAlloc\`
register to the number of bytes needed and \`R1\` to the closure for the
function in which the heap check failed, before jumping into the
hand-written garbage collector code for the cleanup. The garbage
collector will resume execution of the code by using the information
from \`R1\`, after it has freed up enough memory.

Side note: I believe that the line setting \`R1\` is unnecessary here,
because \`R1\` should anyway always be set to the address of the closure
when executing the closure entry code. I could be wrong, though.

### Performing the actual allocation

Once the heap check succeeds, we will be able to enter the body of the
function proper. Since the \`Hp\` has already been incremented, we can
just construct the new heap objects directly:

So we get something like this:

The bottom two words are the allocated \`Just\` value, and the three
above that correspond to the \`x + 1\` closure.

### Returning an allocated value to the caller

Now that we have allocated the data we entered the function in order to
construct, we need to return it to the caller. This is achieved by the
following code:

To return, the STG machine:

`` 1. Sets `R1` to the pointer to the result of evaluation ``\
`2. Pops all the arguments to the function from the stack`\
`3. Jumps to the entry code for the continuation. This is always`\
`   found at the top of the STG stack, logically below any arguments`\
`   that were pushed to make the call.`

This is indeed exactly what happens here, with two interesting points:
pointer tagging, and the double-deference of the stack pointer. These
will be discussed in the next two subsections.

#### Pointer tagging

One exciting feature is that the code setting \`R1\`, i.e. \`R1 = Hp -
2\`. This is setting \`R1\` to point to the \`Just\`, we just allocated,
but simultaneously tagging that pointer with the value 2. The fact that
the tag is non-zero indicates to users of the pointer that the thing
pointed to is already evaluated. Furthermore, because \`Maybe\` has only
two constructors, we are able to use the pointer tags to record which
constructor it evaluated to: in this case, the 2 indicates the \`Just\`
constructor.

It is compulsory to tag pointers before jumping to the address of the
continuation entry code: the entry code can and will rely on those tags
being present!

#### \`TABLES\_NEXT\_TO\_CODE\`

Because I have compiled GHC without \`TABLES\_NEXT\_TO\_CODE\`, the
entry code for the continuation is found by dereferencing the pointer to
the info table we found at the top of the STG stack - i.e. a
double-dereference.

The layout of heap objects without \`TABLES\_NEXT\_TO\_CODE\` is as
follows:

With \`TABLES\_NEXT\_TO\_CODE\` on, the situation looks more like this:

The \`TABLES\_NEXT\_TO\_CODE\` optimisation removes the need for that
second dereference during the return, because the entry code is always
right next to the info table. However, it requires special support from
the backend for ensuring that data (i.e. the info table) and code are
contiguous in memory, so it cannot always be used.

Example 7: \`case\` expressions
-------------------------------

Let us now examine how \`case\` expressions are handled. Compiling the
following Haskell

Produces this C-- code

Notice that GHC has generated *two* functions:
\`Main\_casezuscrut\_entry\` and \`scj\_ret\` correspond to the code for
forcing the argument to the \`case\`, and for the *continuation* of the
\`case\` respectively. Let's pick them apart and see how they work!

### Forcing the scrutinee of the \`case\`

When we first call the \`case\_scrut\` function, its entry code begins
executing:

This is a function of arity 1 (i.e. with a single argument), so upon
entry the machine state looks like this:

Because this is a top level function, the closure is statically
allocated and contains no free variables. However, as discussed
previously, the single argument to the function is guaranteed to be
present at the top of the stack.

The code starts off by saving this argument (the \`x\`) temporarily into
\`R1\`:

The next thing the code does is overwrites this argument on the stack
with a pointer to the info-table of the continuation code. This is the
code that will be invoked after \`x\` has been evaluated into WHNF, and
which will do the test to decide whether to continue as the \`Nothing\`
or as the \`Just\` branch of the case:

As we saw earlier, any time that the STG machine decides that it has a
value in its hand, it will continue evaluation by tail-calling the entry
code found by dereferencing the info-table pointer at the top of the
stack. So by putting the address of our continuation in here, we ensure
that the entry code for \`scj\_info\` is executed after \`x\` becomes a
value.

Now, what we need to do is to start the evaluation of \`x\`. We could
just jump into \`x\`'s entry code and hope for the best, but thanks to
GHC's pointer tagging we can sometimes avoid doing this indirect branch.

So, instead, we test to see if the \`x\` pointer has a tag. If it is
tagged, then we know that it is already evaluated and hence jump
directly to the code for the continuation. If it is not tagged, we are
forced to make the jump into the entry code for \`x\`. This choice is
embodied by the following code:

Note the test \`R1 & 3 != 0\`: this reflects the fact that pointer tags
are stored in the lower 2 bits of the pointer on 32 bit machines.
Another interesting feature is how the \`jump\` instructions find the
entry code: again, we see a deference of the info pointer because
\`TABLES\_NEXT\_TO\_CODE\` is turned off.

As we saw, the \`case\` scrutinisation code ended with one of two things
happening: 1. A direct call into the continuation code \`scj\_ret\` if
the scrutinee was already evaluated 2. A call into the entry code for
the scrutinee, if the scrutinee was not evaluated (or it *was*
evaluated, but the pointer was somehow not tagged with that information)
- Because we pushed \`scj\_info\` onto the STG stack, control will
eventually return to \`scj\_ret\` after the evaluation of \`x\` has
finished

It is now time to examine the continuation code to see what happens
after \`x\` becomes a value.

### Dealing with the forced scrutinee

The continuation code is a little more complicated:

Whenever the STG machine evaluates to a value it will return the value
by jumping to the entry point at the top of the stack. In this case,
\`R1\` is guaranteed to be a (tagged) pointer to the thing that was just
evaluated. Because we are scrutinising a \`Maybe\` type (which has fewer
than 4 constructors) the code for the \`case\` continuation is able to
use the tag bits on the returned pointer to decide which of the two
branches to take:

If we were scrutinising a data type with more constructors, the tag bits
would only tell us that the thing was evaluated, not which constructor
it was evaluated to. In this case, we would have to read the constructor
tag by dereferencing \`R1\` and testing the resulting info table pointer
against all possibilities.

If the tag was greater than or equal to 2, we go to the \`ccv\` branch,
which deals with what happens if we had a \`Just\`. In this case, we
need to continue by forcing the thunk inside the \`Just\` and returning
that value to our caller, which is what these lines are doing:

To access the thing inside the \`Just\`, the code assumes that the
\`R1\` pointer is tagged with the 2 that indicates a \`Just\`
constructor, and hence finds the first free variable (stored 4 bytes
into the closure) using \`I32\[R1 + 2\]\`, which is then saved into
\`R1\`. It pops the address of \`scj\_info\` that was pushed onto the
stack in \`Main\_casezuscrut\_entry\` by moving \`Sp\` up 4 bytes
(remember that the STG stack grows downwards) and then untags and jumps
into the entry code for the \`R1\` thunk, using the same
double-dereference pattern discussed earlier.

There seems to be a small missed opportunity here: the code could check
the pointer tag on \`R1\`, and then return directly if it is set. I
imagine that this isn't being done in order to reduce possible code
bloat.

Example 8: thunks and thunk update
----------------------------------

You might be wondering how the \`x + 1\` thunk we saw allocated in a
previous section will behave when it is actually forced. To remind you,
the thunk we saw was constructed by the following Haskell code:

So how does the \`x + 1\` thunk work? An excellent question! Let's take
a look at the C-- for its entry code and find out:

The original Haskell code read \`x + 1\`, but GHC has inlined the actual
code for the addition operation on \`Int\`s, which looks something like:

The second pattern match (to get \`b\`) has been performed statically by
GHC, obtaining the machine literal 1, which shows up directly in the
generated code. Therefore, the code only need to evaluate and
case-decompose the unknown free variable \`x\` of our closure, to get
the \`a\` argument to \`plusInt\`.

### Thunk entry point

This evaluation is what is being done by the thunk entry code
\`slk\_entry\`. Ignoring the stack check, the C-- begins thusly:

Remembering that upon entry to the thunk entry code, \`R1\` points to
the thunk's closure, the new stack looks as follows:

The C-- statement \`R1 = I32\[R1 + 8\]\` is pulling out the pointer to
the free variable of the thunk (which was set up in
\`Main\_buildzudata\_entry\`) into \`R1\`.

Finally, the entry code evaluates that free variable (checking the tag
bits of the pointer first, as usual):

Because we put \`soN\_info\` at the top of the stack, when evaluation of
\`x\` is complete the STG machine will continue by executing the
\`soN\_ret\` code.

The most interesting feature of this code is the extra stuff that has
been pushed onto the stack below \`soN\_ret\`: an info pointer called
\`stg\_upd\_frame\_info\`, and a pointer to the thunk currently being
evaluated.

This is all part of the STG machine's thunk update mechanism. When the
\`soN\_ret\` continuation returns, it will transfer control *not* to the
code forcing the thunk, but to some code which overwrites the contents
of the current thunk closure with a closure representing an
"indirection". The entry code for such an indirection closure is
trivial: it immediately returns a pointer to the thing that was returned
from the \`soN\_ret\` continuation in \`R1\`.

These indirections are the mechanism which ensures that the STG machine
never repeats the work of evaluating a thunk more than once: after the
first evaluation, any code forcing the thunk jumps into the indirection
entry code rather than \`slk\_entry\`.

That being said, let us look at how the continuation responsible for
actually finding the value of \`x + 1\` works:

### Continuation of the thunk

Upon entry to the continuation code, we have the evaluated \`x\` in
\`R1\`: it now needs to do the addition and allocate a \`I\#\`
constructor to hold the result of the addition. Because of the
allocation, \`soN\_ret\` begins with a heap check. Ignoring that check,
we have the following code:

This is mostly standard stuff. Because the \`R1\` pointer is guaranteed
tagged, and there is only one possible constructor, the tag must be 1
and so the \`Int\#\` value inside the \`Int\` is pulled out using
\`I32\[R1 + 3\]\`. This is then put into a newly heap-allocated \`I\#\`
constructor, which is returned in \`R1\` after we pop the \`soN\_info\`
pointer from the stack.

The only interesting point is where we return to: rather than
dereference \`Sp\` to find the info pointer at the top of the STG stack,
GHC has generated code that takes advantage of the fact that the \`Sp\`
is guaranteed to point to \`stg\_upd\_frame\_info\`. This avoids one
pointer dereference.

Conclusion
----------

This document has left much of the detail of how STG is implemented out:
notable omissions include CAFs, and the precise behaviour of the garbage
collector. Nonetheless, my hope is that it has helped you to gain some
more insight into the weird and wonderful way the Haskell evaluation
model is implemented.

Support for generic programming
===============================

[PageOutline](PageOutline "wikilink")

GHC includes a new (in 2010) mechanism to let you write generic
functions. It is described in paper [A generic deriving mechanism for
Haskell](http://www.dreixel.net/research/pdf/gdmh_nocolor.pdf). This
page sketches the specifics of the implementation; we assume you have
read the paper. The [HaskellWiki
page](http://www.haskell.org/haskellwiki/Generics) gives a more general
overview.

This mechanism replaces the [previous generic classes
implementation](http://www.haskell.org/ghc/docs/6.12.2/html/users_guide/generic-classes.html).
What we describe until the "Kind polymorphic overhaul" section is
implemented and released in GHC 7.2.1.

Status
------

Use **Keyword** = \`Generics\` to ensure that a ticket ends up on this
auto-generated list

Open Tickets:
[patch|infoneeded,keywords=\~Generics)](TicketQuery(status=infoneeded,status=new "wikilink")

Closed Tickets:
[TicketQuery(status=infoneeded,status=closed,keywords=\~Generics)](TicketQuery(status=infoneeded,status=closed,keywords=~Generics) "wikilink")

Main components
---------------

`` * `TcDeriv.tcDeriving` now allows deriving `Generic` instances. ``

`` * The representation types and core functionality of the library live on `GHC.Generics` (on the `ghc-prim` package). ``

`` * Many names have been added as known in `prelude/PrelNames` ``

`` * Most of the code generation is handled by `types/Generics` ``

Things that have been removed
-----------------------------

`* All of the `[`generic` `classes`
`stuff`](http://www.haskell.org/ghc/docs/6.12.2/html/users_guide/generic-classes.html)`. In particular, the following have been removed:`\
``   * `hasGenerics` field from `TyCon`; ``\
``   * `HsNumTy` constructor from `HsType`; ``\
``   * `TypePat` constructor from `Pat`. ``

`` * The `-XGenerics` flag is now deprecated. ``

What already works
------------------

`` * `Generic` and `Generic1` instances can be derived when `-XDeriveGeneric` is enabled. ``

`` * The `default` keyword can used for generic default method signatures when `-XDefaultSignatures` is enabled. ``

`* Generic defaults are properly instantiated when giving an instance without defining the generic default method.`

`` * Base types like `[]`, `Maybe`, tuples, come with Generic instances. ``

Testing
-------

`` * Tests are available under the `generics` directory of the testsuite. ``

Kind polymorphic overhaul
=========================

With the new \`-XPolyKinds\` functionality we can make the support for
generic programming better typed. The basic idea is to define the
universe codes (\`M1\`, \`:+:\`, etc.) as constructors of a datatype.
Promotion then lifts these constructors to types, which we can use as
before, only that now we have them all classified under a new kind. The
overhaul of the main module is explained below; for easier comparison
with the current approach, names are kept the same whenever possible.

Generic representation universe
-------------------------------

\`m\` is the only real parameter here. \`f\` and \`x\` are there because
we can't write kinds directly, since \`Universe\` is also a datatype
(even if we're only interested in its promoted version). So we pass
\`f\` and \`x\` only to set them to \`\* -&gt; \*\` and \`\*\`,
respectively, in \`Interprt\`. \`m\` is different: it stands for the
kind of metadata representation types, and we really want to be
polymorphic over that, since each user datatype will introduce a new
metadata kind.

Universe interpretation
-----------------------

As promised, we set \`f\` to \`\* -&gt; \*\` and \`x\` to \`\*\`.
Unfortunately we don't have \[GhcKinds\#Explicitkindvariables explicit
kind variable annotations\] yet, so we cannot leave \`m\` polymorphic!
So this code doesn't compile:

### Names

As an aside, note that we have to come up with names like \`UU\` and
\`KK\` for the \`Universe\` even though we really just wanted to use
\`U1\` and \`K1\`, like before. Then we would have a type and a
constructor with the same name, but that's ok. However, \`Universe\`
defines both a type (with constructors) and a kind (with types). So if
we were to use \`U1\` in the \`Universe\` constructors, then we could no
longer use that name in the \`Interprt\` constructors. It's a bit
annoying, because we are never really interested in the type
\`Universe\` and its constructors: we're only interested in its promoted
variant. This is a slight annoyance of automatic promotion: when you
define a "singleton type" (like our GADT \`Interprt\` for \`Universe\`)
you cannot reuse the constructor names.

Metadata representation
-----------------------

 There's more of these, but they don't add any new concerns.

Conversion between user datatypes and generic representation
------------------------------------------------------------

We now get a more precise kind for \`Rep\`:

Example generic function: \`fmap\` (kind \`\* -&gt; \*\`)
---------------------------------------------------------

User-visible class, exported:

Defined by the generic programmer, not exported:

Note that previously \`Functor\` and \`GFunctor\` had exactly the same
types. Now we can make clear what the difference between them is.

Example generic function: \`show\` (kind \`\*\`, uses metadata)
---------------------------------------------------------------

User-visible class, exported:

Defined by the generic programmer, not exported:

The other cases do not add any further complexity.

Example datatype encoding: lists (derived by the compiler)
----------------------------------------------------------

Note that we use only one datatype; more correct would be to use 3, one
for \`DList\`, another for the constructors, and yet another for the
selectors (or maybe even n datatypes for the selectors, one for each
constructor?) But we don't do that because \`Universe\` is polymorphic
only over \`m\`, so a single metadata representation type. If we want a
more fine-grained distinction then we would need more parameters in
\`Universe\`, and also to split the \`MM\` case.

### Digression

Even better would be to index the metadata representation types over the
type they refer to. Something like: But now we are basically asking for
promotion of data families, since we want to use promoted \`DList\`.
Also, the case for \`MM\` in \`Universe\` would then be something like:
But I'm not entirely sure about this.

GHC 8.0 and later
-----------------

### Type-level metadata encoding

Because what we've described so far is rather backwards-incompatible, we
wanted to at least try to improve the encoding of metadata, which was
currently rather clunky prior to GHC 8.0 (giving rise to lots of empty,
compiler-generated datatypes and respective instances). We can
accomplished that by changing \`M1\` to keep the meta-information *at
the type level*:

Why did we need to add \`FixityI\`? Because \`Fixity\` does not promote.
Yet, we wanted to expose \`Fixity\` to the user, not \`FixityI\`. Note
that the meta-data classes remained mostly unchanged (aside from some
enhancements to
[Datatype](https://ghc.haskell.org/trac/ghc/ticket/10030) and
[Selector](https://ghc.haskell.org/trac/ghc/ticket/10716)):

But now, using the magic of singletons, we give *one single instance*
for each of these classes, instead of having to instantiate them each
time a user derives \`Generic\`:

Naturally, we require singletons for \`Bool\`, \`Maybe\`, \`FixityI\`,
\`Associativity\`, \`SourceUnpackedness\`, \`SourceStrictness\`, and
\`DecidedStrictness\`, but that is one time boilerplate code, and is not
visible for the user. (In particular, this is where we encode that the
demotion of (the kind) \`FixityI\` is (the type) \`Fixity\`.)

I believe this change is almost fully backwards-compatible, and lets us
simplify the code for \`deriving Generic\` in GHC. Furthermore, I
suspect it will be useful to writers of generic functions, who can now
match at the type-level on things such as whether a constructor is a
record or not.

I say "almost fully backwards-compatible" because handwritten
\`Generic\` instances might break with this change. But we've never
recommended doing this, and I think users who do this are more than
aware that they shouldn't rely on it working across different versions
of GHC.

#### Example

Before GHC 8.0, the following declaration:

Would have generated all of this:

But on GHC 8.0 and later, this is all that is generated (assuming it was
compiled with no strictness optimizations):

Not bad!

### Strictness

The \`Selector\` class now looks like this:

This design draws much inspiration from the way Template Haskell handles
strictness as of GHC 8.0 (see
[here](https://ghc.haskell.org/trac/ghc/ticket/10697) for what motivated
the change). We make a distinction between the *source* strictness
annotations and the strictness GHC actually *decides* during
compilation. To illustrate the difference, consider the following data
type:

If we were to encode the source unpackedness and strictness of each of
\`T\`'s fields, they were be \`SourceUnpack\`/\`SourceStrict\`,
\`NoSourceUnpackedness\`/\`SourceStrict\`, and
\`NoSourceUnpackedness\`/\`NoSourceStrictness\`, no matter what. Source
unpackedness/strictness is a purely syntactic property.

The strictness that the user writes, however, may be different from the
strictness that GHC decides during compilation. For instance, if we were
to compile \`T\` with no optimizations, the decided strictness of each
field would be \`DecidedStrict\`, \`DecidedStrict\`, and
\`DecidedLazy\`. If we enabled \`-O2\`, however, they would be
\`DecidedUnpack\`, \`DecidedStrict\`, and \`DecidedLazy\`.

Things become even more interesting when \`-XStrict\` and \`-O2\` are
enabled. Then the strictness that GHC would decided is
\`DecidedUnpack\`, \`DecidedStrict\`, and \`DecidedStrict\`. And if you
enable \`-XStrict\`, \`-O2\`, *and* \`-funbox-strict-fields\`, then the
decided strictness is \`DecidedUnpack\`, \`DecidedUnpack\`, and
\`DecidedUnpack\`.

The variety of possible \`DecidedStrictness\` combinations demonstrates
that strictness is more just annotation

Source Tree Layout
------------------

An overview of the source tree may be found \[wiki:Commentary/SourceTree
here\].

Build System Basics
-------------------

Detailed information about the build system may be found \[wiki:Building
here\]; what follows is a quick overview, highlighting the areas where
GHC's build system diverges substantially from the way is used in most
other projects.

Most projects keep the parts of their build machinery in files called
found in many/most subdirectories of the source tree. GHC uses the
filename instead; you'll find a file with this name in quite a number of
subdirectories.

Other build system files are in and .

Coding Style
------------

The \[wiki:WorkingConventions Coding style guidelines\] may be found on
the wiki.

The GHC Commentary: GHCi
========================

This isn't a coherent description of how GHCi works, sorry. What it is
(currently) is a dumping ground for various bits of info pertaining to
GHCi, which ought to be recorded somewhere.

Debugging the interpreter
-------------------------

The usual symptom is that some expression / program crashes when running
on the interpreter (commonly), or gets wierd results (rarely).
Unfortunately, finding out what the problem really is has proven to be
extremely difficult. In retrospect it may be argued a design flaw that
GHC's implementation of the STG execution mechanism provides only the
weakest of support for automated internal consistency checks. This makes
it hard to debug.

Execution failures in the interactive system can be due to problems with
the bytecode interpreter, problems with the bytecode generator, or
problems elsewhere. From the bugs seen so far, the bytecode generator is
often the culprit, with the interpreter usually being correct.

Here are some tips for tracking down interactive nonsense:

`* Find the smallest source fragment which causes the problem.`

`` * Using an RTS compiled with `-DDEBUG`, run with `+RTS -Di` to get a listing in great detail from the interpreter. Note that the listing is so voluminous that this is impractical unless you have been diligent in the previous step. ``

`* At least in principle, using the trace and a bit of GDB poking around at the time of death (See also [wiki:Debugging]), you can figure out what the problem is. In practice you quickly get depressed at the hopelessness of ever making sense of the mass of details. Well, I do, anyway.`

`` * `+RTS -Di` tries hard to print useful descriptions of what's on the stack, and often succeeds. However, it has no way to map addresses to names in code/data loaded by our runtime linker. So the C function `ghci_enquire` is provided. Given an address, it searches the loaded symbol tables for symbols close to that address. You can run it from inside GDB: ``

`` In this case the enquired-about address is `PrelBase_ZMZN_static_entry`. If no symbols are close to the given addr, nothing is printed. Not a great mechanism, but better than nothing. ``

`` * We have had various problems in the past due to the bytecode generator (compiler/ghci/ByteCodeGen.lhs) being confused about the true set of free variables of an expression. The compilation scheme for `let`s applies the BCO for the RHS of the `let` to its free variables, so if the free-var annotation is wrong or misleading, you end up with code which has wrong stack offsets, which is usually fatal. ``

`* Following the traces is often problematic because execution hops back and forth between the interpreter, which is traced, and compiled code, which you can't see. Particularly annoying is when the stack looks OK in the interpreter, then compiled code runs for a while, and later we arrive back in the interpreter, with the stack corrupted, and usually in a completely different place from where we left off.`

`If this is biting you baaaad, it may be worth copying sources for the compiled functions causing the problem, into your interpreted module, in the hope that you stay in the interpreter more of the time.`

`` * There are various commented-out pieces of code in Interpreter.c which can be used to get the stack sanity-checked after every entry, and even after after every bytecode instruction executed. Note that some bytecodes (`PUSH_UBX`) leave the stack in an unwalkable state, so the `do_print_stack` local variable is used to suppress the stack walk after them.  ``

Useful stuff to know about the interpreter
------------------------------------------

The code generation scheme is straightforward (naive, in fact).
\`-ddump-bcos\` prints each BCO along with the Core it was generated
from, which is very handy.

`` * Simple `let`s are compiled in-line. For the general case, `let v = E in ...`, the expression `E` is compiled into a new BCO which takes as args its free variables, and `v` is bound to `AP(the new BCO, free vars of E)`. ``

`` * `case`s as usual, become: push the return continuation, enter the scrutinee. There is some magic to make all combinations of compiled/interpreted calls and returns work, described below. In the interpreted case, all `case` alts are compiled into a single big return BCO, which commences with instructions implementing a switch tree.  ``

### Stack management

There isn't any attempt to stub the stack, minimise its growth, or
generally remove unused pointers ahead of time. This is really due to
laziness on my part, although it does have the minor advantage that
doing something cleverer would almost certainly increase the number of
bytecodes that would have to be executed. Of course we \`SLIDE\` out
redundant stuff, to get the stack back to the sequel depth, before
returning a HNF, but that's all. As usual this is probably a cause of
major space leaks.

### Building constructors

Constructors are built on the stack and then dumped into the heap with a
single \`PACK\` instruction, which simply copies the top N words of the
stack verbatim into the heap, adds an info table, and zaps N words from
the stack. The constructor args are pushed onto the stack one at a time.
One upshot of this is that unboxed values get pushed untaggedly onto the
stack (via \`PUSH\_UBX\`), because that's how they will be in the heap.
That in turn means that the stack is not always walkable at arbitrary
points in BCO execution, although naturally it is whenever GC might
occur.

Function closures created by the interpreter use the AP-node (tagged)
format, so although their fields are similarly constructed on the stack,
there is never a stack walkability problem.

### Perspective

I designed the bytecode mechanism with the experience of both STG hugs
and Classic Hugs in mind. The latter has an small set of bytecodes, a
small interpreter loop, and runs amazingly fast considering the cruddy
code it has to interpret. The former had a large interpretative loop
with many different opcodes, including multiple minor variants of the
same thing, which made it difficult to optimise and maintain, yet it
performed more or less comparably with Classic Hugs.

My design aims were therefore to minimise the interpreter's complexity
whilst maximising performance. This means reducing the number of opcodes
implemented, whilst reducing the number of insns despatched. In
particular, very few (TODO: How many? Which?) opcodes which deal with
tags. STG Hugs had dozens of opcodes for dealing with tagged data.
Finally, the number of insns executed is reduced a little by merging
multiple pushes, giving \`PUSH\_LL\` and \`PUSH\_LLL\`. These opcode
pairings were determined by using the opcode-pair frequency profiling
stuff which is ifdef-d out in Interpreter.c. These significantly improve
performance without having much effect on the ugliness or complexity of
the interpreter.

Overall, the interpreter design is something which turned out well, and
I was pleased with it. Unfortunately I cannot say the same of the
bytecode generator.

case returns between interpreted and compiled code
--------------------------------------------------

Variants of the following scheme have been drifting around in GHC RTS
documentation for several years. Since what follows is actually what is
implemented, I guess it supersedes all other documentation. Beware; the
following may make your brain melt. In all the pictures below, the stack
grows downwards.

### Returning to interpreted code.

Interpreted returns employ a set of polymorphic return infotables. Each
element in the set corresponds to one of the possible return registers
(R1, D1, F1) that compiled code will place the returned value in. In
fact this is a bit misleading, since R1 can be used to return either a
pointer or an int, and we need to distinguish these cases. So, supposing
the set of return registers is {R1p, R1n, D1, F1}, there would be four
corresponding infotables, stg\_ctoi\_ret\_R1p\_info, etc. In the
pictures below we call them stg\_ctoi\_ret\_REP\_info.

These return itbls are polymorphic, meaning that all 8 vectored return
codes and the direct return code are identical.

Before the scrutinee is entered, the stack is arranged like this:

On entry, the interpreted contination BCO expects the stack to look like
this:

A machine code return will park the returned value in R1/F1/D1, and
enter the itbl on the top of the stack. Since it's our magic itbl, this
pushes the returned value onto the stack, which is where the interpreter
expects to find it. It then pushes the BCO (again) and yields. The
scheduler removes the BCO from the top, and enters it, so that the
continuation is interpreted with the stack as shown above.

An interpreted return will create the value to return at the top of the
stack. It then examines the return itbl, which must be immediately
underneath the return value, to see if it is one of the magic
stg\_ctoi\_ret\_REP\_info set. Since this is so, it knows it is
returning to an interpreted contination. It therefore simply enters the
BCO which it assumes it immediately underneath the itbl on the stack.

### Returning to compiled code.

Before the scrutinee is entered, the stack is arranged like this:

The scrutinee value is then entered. The case continuation(s) expect the
stack to look the same, with the returned HNF in a suitable return
register, R1, D1, F1 etc.

A machine code return knows whether it is doing a vectored or direct
return, and, if the former, which vector element it is. So, for a direct
return we jump to \`Sp\[0\]\`, and for a vectored return, jump to
\`((CodePtr\*)(Sp\[0\]))\[ - ITBL\_LENGTH - vector number \]\`. This is
(of course) the scheme that compiled code has been using all along.

An interpreted return will, as described just above, have examined the
itbl immediately beneath the return value it has just pushed, and found
it not to be one of the ret\_REP\_ctoi\_info set, so it knows this must
be a return to machine code. It needs to pop the return value, currently
on the stack, into R1/F1/D1, and jump through the info table.
Unfortunately the first part cannot be accomplished directly since we
are not in Haskellised-C world.

We therefore employ a second family of magic infotables, indexed, like
the first, on the return representation, and therefore with names of the
form stg\_itoc\_ret\_REP\_info. (Note: itoc; the previous bunch were
ctoi). This is pushed onto the stack (note, tagged values have their tag
zapped), giving:

We then return to the scheduler, asking it to enter the itbl at t.o.s.
When entered, stg\_itoc\_ret\_REP\_info removes itself from the stack,
pops the return value into the relevant return register, and returns to
the itbl to which we were trying to return in the first place.

Amazingly enough, this stuff all actually works! Well, mostly ...

Unboxed tuples: a Right Royal Spanner In The Works
--------------------------------------------------

The above scheme depends crucially on having magic infotables
stg\_{itoc,ctoi}\_ret\_REP\_info for each return representation REP. It
unfortunately fails miserably in the face of unboxed tuple returns,
because the set of required tables would be infinite; this despite the
fact that for any given unboxed tuple return type, the scheme could be
made to work fine.

This is a serious problem, because it prevents interpreted code from
doing IO-typed returns, since IO t is implemented as \`(\# t,
RealWorld\# \#)\` or thereabouts. This restriction in turn rules out FFI
stuff in the interpreter. Not good.

Although we have no way to make general unboxed tuples work, we can at
least make IO-types work using the following ultra-kludgey observation:
\`RealWorld\#\` doesn't really exist and so has zero size, in compiled
code. In turn this means that a type of the form \`(\# t, RealWorld\#
\#)\` has the same representation as plain t does. So the bytecode
generator, whilst rejecting code with general unboxed tuple returns,
recognises and accepts this special case. Which means that IO-typed
stuff works in the interpreter. Just.

If anyone asks, I will claim I was out of radio contact, on a 6-month
walking holiday to the south pole, at the time this was ... er ...
dreamt up.

Porting GHC using LLVM backend
==============================

This document is kind of short porting roadmap which serves as a
high-level overview for porters of GHC who decided to use LLVM instead
of implementing new NCG for their target platform. Please have
\[wiki:Commentary/Compiler/Backends/LLVM/Design Design &
Implementation\] at hand since this contains more in-depth information.
The list of steps needed for new GHC/LLVM port is:

**(1)** Make sure GHC unregisterised build is working on your target
platform (using the C backend). This guide isn't intended for porting
GHC to a completely unsupported platform. If the platform in question
doesn't have a GHC unregisterised build then follow the
\[wiki:Building/Porting GHC Porting Guide\] first.

**(2)** Now try to compile some very simple programs such as 'hello
world' or simpler using the GHC you just built. Try with the C backend
First to make sure everything is working. Then try with the LLVM
backend. If the llvm backend built programs are failing find out why.
This is done using a combination of things such as the error message you
get when the program fails, \[wiki:Debugging/CompiledCode tracing the
execution with GDB\] and also just comparing the assembly code produced
by the C backend to what LLVM produces. This last method is often the
easiest and you can occasionally use techniques like doing doing a
'binary search' for the bug by merging the assembly produced by the C
backend and LLVM backend.

**(3)** When the programs you throw at the LLVM backend are running, try
running the GHC testsuite. First run it against the C backend to get a
baseline, then run it against the LLVM backend. Fix any failures that
are LLVM backend specific.

**(4)** If the testsuite is passing, now try to build GHC itself using
the LLVM backend. This is a very tough test. When working though its a
good proof that the LLVM backend is working well on your platform.

**(5)** Now you have LLVM working in unregistered mode, so the next
thing is to implement the GHC calling convention in LLVM that is used by
GHC's LLVM backend. This should then allow you to get the LLVM backend
working in registered mode but with (TABLES\_NEXT\_TO\_CODE = NO in your
build.mk). Majority of this step involves hacking inside the LLVM code.
Usually lib/Target/<your target platform name> is the best way to start.
Also you might study what David Terei did for [x86
support](http://lists.cs.uiuc.edu/pipermail/llvmdev/2010-March/030031.html)
and his [patch
itself](http://lists.cs.uiuc.edu/pipermail/llvmdev/attachments/20100307/714e5c37/attachment-0001.obj)
to get an idea what's really needed.

**(6)** Once **(5)** is working you have it all running except
TABLES\_NEXT\_TO\_CODE. So change that to Yes in your build.mk and get
that working. This will probably involve changing the mangler used by
LLVM to work on the platform you are targeting.

Registerised Mode
-----------------

Here is an expanded version of what needs to be done in step 5 and 6 to
get a registerised port of LLVM working:

1\. GHC in registerised mode stores some of its virtual registers in real
hardware registers for performance. You will need to decide on a mapping
of GHC's virtual registers to hardware registers. So how many registers
you want to map and which virtual registers to store and where. GHC's
design for this on X86 is basically to use as many hardware registers as
it can and to store the more frequently cessed virtual registers like
the stack pointer in callee saved registers rather than caller saved
registers. You can find the mappings that GHC currently uses for
supported architectures in 'includes/stg/MachRegs.h'.

2\. You will need to implement a custom calling convention for LLVM for
your platform that supports passing arguments using the register map you
decided on. You can see the calling convention I have created for X86 in
the llvm source file 'lib/Target/X86/X86CallingConvention.td'.

3\. Get GHC's build system running on your platform in registerised mode.

4\. Add new inline assembly code for your platform to ghc's RTS. See
files like 'rts/StgCRun.c' that include assembly code for the
architectures GHC supports. This is the main place as its where the
boundary between the RTS and haskell code is but I'm sure there are
definitely other places that will need to be changed. Just grep the
source code to find existing assembly and add code for your platform
appropriately.

5\. Will need to change a few things in LLVM code gen.

5.1 'compiler/llvmGen/LlvmCodeGen/Ppr.hs' defines a platform specific
string that is included in all generated llvm code. Add one for your
platform. This string specifies the datalayout parameters for the
platform (e.g pointer size, word size..). If you don't include one llvm
should still work but wont optimise as aggressively.

5.2 'compiler/llvmGen/LlvmCodeGen/CodeGen.hs' has some platform specific
code on how write barriers should be handled.

6\. Probably some stuff elsewhere in ghc that needs to be changed (most
likely in the main/ subfolder which is where most the compiler driver
lives or in codegen/ which is the Cmm code generator).

7\. This is just what I know needs to be done, I'm sure there is many
small pieces missing although they should all fall into one of the above
categories. In the end just trial and error your way to success.

[PageOutline](PageOutline "wikilink")

Packages in GHC
===============

This page summarises our current proposal for packages in GHC. (See also
\[wiki:Commentary/Packages/PackageNamespacesProposal an extended
proposal\] to make namespaces first-class. The two proposals are
mutually exclusive.)

The problem
-----------

A vexed question in the current design of Haskell is the issue of
whether a single program can contain two modules with the same name. In
Haskell 98 that is absolutely ruled out. As a result, packages are
fundamentally non-modular: to avoid collisions *every* module in *every*
package written by *anyone* must have different module names. That's
like saying that every function must have different local variables, and
is a serious loss of modularity.

GHC 6.6 makes a significant step forward by lifting this restriction.
However it leaves an open question, which is what this page is about.

Assumptions
-----------

Before we start, note that we take for granted the following

`* `**`Each` `package` `has` `a` `globally-unique`
`name`**`, organised by some social process.  This assumption is deeply built into Cabal, and lots of things would need to change if it wasn't met.`

`* `**`Module` `names` `describe` *`purpose`* `(what` `it's` `for,`
`e.g.` `),` `whereas` `package` `names` `describe` *`provenance`*
`(where` `it` `comes` `from,` `e.g.`
`)`**`.  We should not mix these two up, and that is a good reason for not combining package and module names into a single grand name.  One quite frequently wants to globally change provenance but not purpose (e.g. compile my program with a new version of package "foo"), without running through all the source files to change the import statements.`

`* `**`New:` `a` `module` `name` `must` `be` `unique` `within` `its`
`package`
`(only)`**`.   That is, a single program can use two modules with the same module name, provided they come from different packages.  This is new in GHC 6.6.  `

For all this to work, GHC must incorporate the package name (and
version) into the names of entities the package defines. That means that
when compiling a module M you must say what package it is part of: Then
C.o will contain symbols like "" etc. In effect, the "original name" of
a function in module of package is .

The open question
-----------------

The remaining question is this: **When you say , from what package does
A.B.C come?**. Three alternatives are under consideration:

` * Plan A (GHC's current story)`\
` * Plan B: grafting.  An enhancement of plan A; see [wiki:Commentary/Packages/PackageMountingProposal Frederik Eaton's proposal]`\
` * Plan C: optionally specify the package in the import.  An alternative to (B), described in a [wiki:Commentary/Packages/PackageImportsProposal separate page].`

------------------------------------------------------------------------

Plan A: GHC's current story
---------------------------

GHC already has a fairly elaborate scheme (perhaps too elaborate;
[documentation
here](http://www.haskell.org/ghc/dist/current/docs/users_guide/packages.html))
for deciding what package you mean when you say "import A.B.C":

`* For a start, it only looks in `*`installed`*` packages.  `\
`* Even for installed packages, the package may or may not be `*`exposed`*` by default (reasoning: you may want old versions of package X to be installed, but not in scope by default).  `\
`* Then, you can use the `` flag to hide an otherwise-exposed package, and the `` flag to expose an otherwise-hidden package.`

So, you can expose package P1 when compiling module M (say), and expose
P2 when compiling module N by manipulating these flags. Then M and N
could both import module A.B.C, which would come from P1 and P2
respectively. But:

`* What if you wanted to import A.B.C from P1 and A.B.C from P2 into the `*`same`*` module?`\
`* What if you want to only replace `*`parts`*` of P1 (e.g., you want to use an updated version of a module in ``)?`\
`* Compiling different modules with different flags in a way that affects the `*`semantics`*` (rather than, say, the optimisation level) seems undesirable.`\
`* To support `` in this situation we'd need to allow `` flags in the per-module `` pragmas, which isn't currently supported.  (`` already gathers those options together for the link step.)  `*`This`
`is` `not` `yet` `implemented,` `but` `it` `is` `close` `to` `being`
`implemented.`*

If we did implement the "\`-package\` in \`OPTIONS\` pragma" fix, then
is is not clear how pressing the need is for anything more. It's still
impossible to import M from P1, and M from P2, into the same module. But
how often will that happen?

------------------------------------------------------------------------

Plan B: package mounting
------------------------

This proposal is described by a
\[wiki:Commentary/Packages/PackageMountingProposal separate page\].

------------------------------------------------------------------------

Plan C: mention the package in the import
-----------------------------------------

This proposal is described by a
\[wiki:Commentary/Packages/PackageImportsProposal separate page\].

This wiki discusses how bringing [Nix](https://nixos.org/nix/)-style
package management facilities to cabal can solve various cabal problems
and help in effective mitigation of cabal hell. It also contains the
goals and implementation plan for the GSoC project. It is based on a
[blog post by Duncan
Coutts](http://www.well-typed.com/blog/2015/01/how-we-might-abolish-cabal-hell-part-2/).

Problems
========

Breaking re-installations
-------------------------

[Image(http://www.well-typed.com/blog/aux/images/cabal-hell/install-example1.png)](Image(http://www.well-typed.com/blog/aux/images/cabal-hell/install-example1.png) "wikilink")

There are situations where Cabal's chosen solution would involve
reinstalling an existing version of a package but built with different
dependencies. In this example, after installing app-1.1, app-1.0 and
other-0.1 will be broken. The root of the problem is having to delete or
mutate package instances when installing new packages. This is due to
the limitation of only being able to have one instance of a package
version installed at once.

Type errors when using packages together
----------------------------------------

[Image(http://www.well-typed.com/blog/aux/images/cabal-hell/install-example2.png)](Image(http://www.well-typed.com/blog/aux/images/cabal-hell/install-example2.png) "wikilink")

The second, orthogonal, problem is that it is possible to install two
packages and then load them both in GHCi and find that you get type
errors when composing things defined in the two different packages.
Effectively you cannot use these two particular installed packages
together. The fundamental problem is that developers expect to be able
to use combinations of their installed packages together, but the
package tools do not enforce consistency of the developer's environment.

Goals
=====

-   Fix breaking re-installs (Persistent package store)
-   Implement garbage collection to free unreachable packages
-   Enable sharing of packages between sandbox
-   Enforce development environment consistency (Giving error earlier
    and better)
-   Implement package manager tools in cabal-install(cabal upgrade and
    cabal remove)

Implementation Plan
===================

Persistent package store
------------------------

A
[patch](https://github.com/ghc/ghc/commit/dd3a7245d4d557b9e19bfa53b0fb2733c6fd4f88)
has been pushed for ghc-7.11 that allows multiple instance of the same
package to be installed. So the remaining work is in cabal tool for
never modifying installed packages. I have written a [patch to make
cabal
(almost)non-destructive](https://github.com/fugyk/cabal/commit/45ec5edbaada1fd063c67d6109e69efa0e732e6a).
This patch makes all the changes to Package database non-destructive if
Installed Package ID is different. To make it fully non-mutable, Thomas
Tuegel suggested to

-   change installed package IDs to be computed by hash of the
    sdist tarball.
-   Enforce that a package is never overwritten by taking out a lock
    when updating the database.(before building the package)

It will have additional benefit that package will not be built again if
same source has already been built earlier, thus saving time.

Views
-----

Views will the subset of packages of package store whose modules can be
imported. Views will be present as various \*.view file in
<Package DB location>/views like default.view. The view file contains
list of installed package IDs. There will exist a default view which
contains packages installed by cabal install outside sandbox. If a
package name is installed two times, default view will contain the
instance of package which is installed at last. Views' packages will
also act like GC roots.

To facilitate views, ghc-pkg will need some new commands:

-   Create a view / Symlink a view
-   Delete a view
-   List all views
-   Modify a view
-   Add a package
-   Remove a package

Sandbox will be a view. Cabal needs to set view when using sandbox. It
also needs the ability to make a view and also add a package to the
view. Packages can be shared between views. View path will be passed to
ghc using -package-env. The view file that sandbox creates lies in the
same directory and is symlinked from the package database view file for
allowing GC. It will have a benefit that when we just delete the sandbox
directory without deleting the view, GC can free that sandbox package.

It looks similar to nix development environment but has some
differences. nix environments are like everything that is visible. It is
kind of like imported packages with dependency closure. nix needs to
make directories visible, while here we already have one more layer.
Here we only need exposed package and ghc can make complete environment
already. Views are just exposed packages of the environment. So,
dependency of the package need not be in the view that the package is
in. The problem that we are trying to solve with views is consistent way
of managing packages and sandboxes, allowing packages to be shared
between sandboxes and its packages being used as GC root.

Summary of design details

When installing a package outside sandbox

-   Package is added to default view / modified in default view

Making a sandbox

-   A view is made in the directory
-   The new view is symlinked from the database
-   Packages that are installed are added to that view. Sandboxes cannot
    affect any other things outside sandbox.

Within sandbox

-   All the cabal commands pass view name to ghc and ghc will use
    relevant package

Consistent developer environment
--------------------------------

It will require additional constraint to check that there is no other
instance of the same package or its dependencies is in the
environment(packages from which we have imported the modules with their
dependency closure) when we are importing the module from a package. It
also needs to be checked when cabal is configuring the package, that a
package do not directly or indirectly depends on two version of same
package. If it is violated it needs to give out an error.

Garbage collection
------------------

This will firstly involve determining the root packages and package
list. Root packages are the packages which are in some view. Then we
find list of all packages in the database. As there will be single
database after implementing views, we don't need to call it for every
sandbox database. Then we need to do mark-sweep and find which package
are not in the reachable package list and select it for garbage
collection. Then the selected packages will be deleted from the package
store and also unregistered from database with ghc-pkg.

cabal remove
------------

With everything implemented above, it is just removing a package from
default view. If package is unreachable it can be freed from disk by GC.
It is guaranteed to not break any package except the package that is
removed.

cabal upgrade
-------------

cabal upgrade is just installing every package that is present in
default view that has update available.

Current Status
--------------

It is possible to install multiple instances of the same package version
with my forks of cabal and ghc. Quite a few problems remain.

See also \[wiki:Commentary/Packages/MultiInstances\]

### Unique Install Location

When specifying the install location there is a new variable \$unique
available. It is resolved to a random number by cabal-install during
configuring. The default libsubdir for cabal-install should be
"\$packageid-\$unique" for example "mtl-2.1.2-1222131559". Cabal the
library does not understand \$unique so multiple instances of the same
package version installed via "runhaskell Setup.hs install" are still
problematic.

### ghc-pkg

ghc-pkg never removes registered packages when registering a new one.
Even if a new package with the same \`InstalledPackageId\` as an
existing package is registered. Or if a new package that points to the
same install directory is registered. \`ghc-pkg\` should probably check
this and issue a warning.

### Adhoc dependency resolution

A new field \`timestamp\` was added to \`InstalledPackageInfo\`. It is
set by Cabal the library when registering a package. It is used by Cabal
the library, GHC and cabal-install to choose between different instances
of the same package version.

### Detect whether an overwrite happens and warn about it

Currently cabal-install still warns about dangerous reinstalls and
requires \`--force-reinstalls\` when it is sure a reinstall would
happen. The correct behaviour here would be to detect if a reinstall
causes overwriting (because of a version of ghc-pkg that does this) and
warn only in this case. In this implementation reinstalls are not
dangerous anymore.

### Communicate the \`InstalledPackageId\` back to cabal-install

An \`InstallPlan\` contains installed packages as well as packages to be
installed and dependencies between those. We want to specify all of
these dependencies with an \`InstalledPackageId\`. Unfortunately the
\`InstalledPackageId\` is determined after installation and therefore
not available for not yet installed packages. After installation it
would have to be somehow communicated back to cabal-install. The current
workaround is to only specify those packages that were previously
installed with an \`InstalledPackageId\` and trust on Cabal picking the
instance that was most recently (during execution of this install plan)
installed for the other ones.

### Garbage Collection

A garbage collection should offer the removal of a certain package
specified by \`InstalledPackageId\`, the removal of broken packages and
the removal of probably unnecessary packages. A package is unnecessary
if all packages that depend on it are unnecessary (this includes the
case that no package depends on it) and it is not the most recently
installed instance for its version. All of this should be accompanied by
a lot of "are you sure" questioning.

### About Shadowing

GHC has the concept of shadowing. It was introduced as far as i
understand (correct me please) because when combining the global and the
user package databases you could end up with two instances of the same
package version. The instance in the user database was supposed to
shadow the one in the global database. Now that there are multiple
instances of the same package version even in one package database this
concepts needs to be rethought. This is non-trivial because flags asking
for a package version as well as flags requiring a certain instance need
to be taken into account.

### About Unique Identifier

Currently a big random number is created by cabal-install during
configuration and passed to Cabal to be appended to the
\`InstalledPackageId\` before registering. The reason is that the
\`InstalledPackageId\` still contains the ABI hash which is only known
after compilation. I personally would like the \`InstalledPackageId\` to
be the name of the package, the version and a big random number. This
could be determined before compilation, used as the \`libsubdir\` and
baked into \`package\_Paths.hs\`. Since it would be determined by
cabal-install it would also make communicating the InstalledPackageId
back to cabal-install after an installation unnecessary. The problem is
that the \`InstalledPackageId\` would not be deterministic anymore.

Original Plan
-------------

Cabal and GHC do not support multiple instances of the same package
version installed at the same time. If a second instance of a package
version is installed it is overwritten on the file system as well as in
the \`PackageDB\`. This causes packages that depended upon the
overwritten instance to break. The idea is to never overwrite an
installed package. As already discussed in
[4](http://hackage.haskell.org/trac/ghc/wiki/Commentary/Packages/MultiInstances)
the following changes need to be made:

`* Cabal should install packages to a location that does not just depend on name and version,`\
`` * `ghc-pkg` should always add instances to the `PackageDB` and never overwrite them, ``\
`` * `ghc --make`, `ghci`, and the configure phase of Cabal should select suitable instances according to some rule of thumb (similar to the current resolution technique), ``\
`* we want to be able to make more fine-grained distinctions between package instances than currently possible, for example by distinguishing different build flavours or "ways" (profiling, etc.)`\
`` * `cabal-install` should still find an `InstallPlan`, and still avoid unnecessarily rebuilding packages whenever it makes sense ``\
`* some form of garbage collection should be offered to have a chance to reduce the amount of installed packages`

Hashes and identifiers
----------------------

There are three identifiers:

`` * `XXXX`: the identifier appended to the installation directory so that installed packages do not clash with each other ``\
`` * `YYYY`: the `InstalledPackageId`, which is an identifier used to uniquely identify a package in the package database. ``\
`` * `ZZZZ`: the ABI hash derived by GHC after compiling the package ``

The current situation:

`` * `XXXX`: is empty, which is bad (two instances of a package install in the same place) ``\
`` * `YYYY`: is currently equal to `ZZZZ`, which is bad because we need to make more distinctions: ``\
`  * we need to distinguish between two packages that have identical ABIs but different behaviour (e.g. a bug was fixed)`\
`  * we need to distinguish between two instances of a package that are compiled against different dependencies, or with different options, or compiled in a different way (profiling, dynamic)  `

Some notes:

`` * `XXXX` must be decided  ``*`before`*``  we begin compiling, because we have to generate the `Paths_P.hs` file that is compiled along with the package, whereas `ZZZZ` is only available  ``*`after`*` we have compiled the package.`\
`` * `ZZZZ` is not uniquely determined by the compilation inputs (see #4012), although in the future we hope it will be ``\
`` * It is desirable that when two packages have identical `YYYY` values, then they are compatible, even if they were built on separate systems.  Note that this is not guaranteed even if `YYYY` is a deterministic function of the compilation inputs, because `ZZZZ` is non-deterministic (previous point).  Hence `YYYY` must be dependent on `ZZZZ`.  ``\
`` * It is desirable that `YYYY` be as deterministic as possible, i.e. we would rather not use a GUID, but `YYYY` should be determined by the compilation inputs and `ZZZZ`.  We know that `ZZZZ` is currently not deterministic, but in the future it will be, and at that point `YYYY` will become deterministic too, in the meantime `YYYY` should be no less deterministic than `ZZZZ`. ``

Our proposal:

`* We define a new `*`Cabal`
`Hash`*``  that hashes the compilation inputs (the `LocalBuildInfo` and the contents of the source files) ``\
`` * `XXXX` is a GUID. ``\
`  * Why not use the `*`Cabal`
`Hash`*`?  We could, but then there could conceivably be a clash. (Andres - please expand this point, I have forgotten the full rationale).`\
`` * `YYYY` is the combination of the  ``*`Cabal`
`Hash`*``  and `ZZZZ` (concatenated) ``\
`` * `ZZZZ` is recorded in the package database as a new field `abi-hash`. ``\
``   * When two packages have identical `ZZZZ`s then they are interface-compatible, and the user might in the future want to change a particular dependency to use a different package but the the same `ZZZZ`.  We do not want to make this change automatically, because even when two packages have identical `ZZZZ`s, they may have different behaviour (e.g. bugfixes). ``

Install location of installed Cabal packages
--------------------------------------------

Currently the library part of packages is installed to
\`\$prefix/lib/\$pkgid/\$compiler\`. For example the \`GLUT\` package of
version 2.3.0.0 when compiled with GHC 7.4.1 when installed globally
lands in \`/usr/local/lib/GLUT-2.3.0.0/ghc-7.4.1/\`. This is the default
path. It is completely customizable by the user. In order to allow
multiple instances of this package to coexist we need to change the
install location to a path that is unique for each instance. Several
ways to accomplish this have been discussed:

### Hash

Use a hash to uniquely identify package instances and make the hash part
of both the InstalledPackageId and the installation path.

The ABI hash currently being used by GHC is not suitable for unique
identification of a package, because it is nondeterministic and not
necessarily unique. In contrast, the proposed Cabal hash should be based
on all the information needed to build a package.

This approach requires that we know the hash prior to building the
package, because there is a data directory (per default under
\$prefix/share/\$pkgid/) that is baked into Paths\_foo.hs in preparation
of the build process.

### Unique number

Use a unique number as part of the installation path.

A unique number could be the number of packages installed, or the number
of instances of this package version already installed, or a random
number. It is important that the numbers are guaranteed to be unique
system-wide, so the counter-based approaches are somewhat tricky.

The advantage over using a hash is that this approach should be very
simple to implement. On the other hand, identifying installed packages
(see below) could possibly become more difficult, and migrating packages
to other systems is only possible if the chance of collisions is
reasonably low (for example, if random numbers are being used).

` 1. The unique number is also part of the installed package id.`

` 2. We can use another unique identifier (for example, a Cabal hash) to identify installed packages. In this case, that identifier would be allowed to depend on the output of a package build.`

\`ghc-pkg\`
-----------

\`ghc-pkg\` currently identifies each package by means of an
\`InstalledPackageId\`. At the moment, this id has to be unique per
package DB and is thereby limiting the amount of package instances that
can be installed in a single package DB at one point in time.

In the future, we want the \`InstalledPackageId\` to still uniquely
identify installed packages, but in addition to be unique among all
package instances that could possibly be installed on a system. There's
still the option that one InstalledPackageId occurs in several package
DBs at the same time, but in this case, the associated packages should
really be completely interchangeable. \[If we want to be strict about
this, we'd have to include the ABI hash in the \`InstalledPackageId\`.\]

Even though, as discussed above, the ABI hash is not suitable for use as
the \`InstalledPackageId\` given these changed requirements, we will
need to keep the ABI hash as an essential piece of information for ghc
itself.

\`ghc-pkg\` is responsible for storing all information we have about
installed packages. Depending on design decisions about the solver and
the Cabal hash, further information may be required in \`ghc-pkg\`'s
description format (see below).

The following fields will be added to the description format:

A field *Way* of type \`\[String\]\`. It tracks the way in which the
package was compiled. It is a subset of \`{v,d,p}\`. "v" means vanilla,
"d" means dynamic linking and "p" means profiling. Other ways may be
added later.

A \`timestamp\` of the time when the package was installed (or built?).
It is used by GHC and Cabal to put a preference on the latest package of
a certain version.

A currently empty but extensible set of fields starting with
"x-cabal-...". \`ghc-pkg\` ignores them when parsing. During the
resolution phase \`cabal-install\` might use them to decide
compatibility between packages.

A field abi-hash that contains the ABI hash because it is no longer
stored implicitly as part of the \`InstalledPackageId\`.

Simplistic dependency resolution
--------------------------------

The best tool for determining suitable package instances to use as build
inputs is \`cabal-install\`. However, in practice there will be many
situations where users will probably not have the full \`cabal-install\`
functionality available:

` 1. invoking GHCi from the command line,`\
` 2. invoking GHC directly from the command line,`\
``  3. invoking the configure phase of Cabal (without using `cabal-install`). ``

In these cases, we have to come up with a suitable selection of package
instances, and the only info we have available are the package DBs plus
potential command line flags. Cabal will additionally take into account
the local constraints of the package it is being invoked for, whereas
GHC will only consider command-line flags, but not modules it has been
invoked with.

Currently if GHC is invoked by the user it does some adhoc form of
dependency resolution. The most common case of this is using ghci. If
there are multiple instances of the same package in the
\`PackageDBStack\` the policy used to select a single one prefers DBs
higher in the stack. It then prefers packages with a higher version.
Once we allow package instances with the same version within a single
package DB, we need to refine the algorithm. Options are:

`* pick a random / unspecified instances`\
`* use the time of installation`\
`* user-specified priorities`\
`` * use the order in the `PackageDB` ``\
`* look at the transitive closure of dependencies and their versions`\
`* build a complex solver into GHC`

Picking a random version is a last resort. A combination of installation
time and priorities seems rather feasible. It makes conflicts unlikely,
and allows to persistently change the priorities of installed packages.
Using the order in the package DB is difficult if directories are being
used as DBs. Looking at the transitive closure of dependencies makes it
hard to define a total ordering of package instances. Adding a complex
solver is unattractive unless we find a way to reuse \`cabal-install\`'s
functionality within GHC, but probably we do not want to tie the two
projects together in this way.

Build flavours
--------------

Once we distinguish several package instances with the same version, we
have a design decision how precise we want that distinction to be.

The minimal approach would be to just take the transitive dependencies
into account. However, we might also want to include additional
information about builds such as Cabal flag settings, compiler options,
profiling, documentation, build tool versions, external (OS)
dependencies, and more.

These differences have to be tracked. The two options we discuss are to
store information in the \`ghc-pkg\` format, or to incorporate them in a
Cabal hash (which is then stored). Both options can be combined.

### The Cabal hash

\[A few notes about where to find suitable information in the source
code:\]

A build configuration consists of the following:

The Cabal hashes of all the package instances that are actually used for
compilation. This is the environment. It is available in the
\`installedPkgs\` field of \`LocalBuildInfo\` which is available in
every step after configuration. It can also be extracted from an
\`InstallPlan\` after dependency resolution.

The compiler, its version and its arguments and the tools and their
version and their arguments. Available from LocalBuildInfo also. More
specifically: \`compiler\`, \`withPrograms\`, \`withVanillaLib\`,
\`withProfLib\`, \`withSharedLib\`, \`withDynExe\`, \`withProfExe\`,
\`withOptimization\`, \`withGHCiLib\`, \`splitObjs\`, \`stripExes\`. And
a lot more. \[Like what?\]

The source code. This is necessary because if the source code changes
the result of compilation changes. For released packages I would assume
that the version number uniquely identifies the source code. A hash of
the source code should be available from hackage to avoid downloading
the source code. For an unreleased package we need to find all the
source files that are needed for building it. Including non-haskell
source files. One way is to ask a source tarball to be built as if the
package was released and then hash all the sources included in that.

OS dependencies are not taken into account because i think it would be
very hard.

### Released and Unreleased packages

If we cabal install a package that is released on hackage we call this a
**clean install**. If we cabal install an unreleased package we call
this a **dirty install**. Clean installs are mainly used to bring a
package into scope for ghci and to install applications. While they can
be used to satisfy dependencies this is discouraged. For released
packages the set of source files needed for compilation is known. For
unreleased packages this is currently not the case.

Dependency resolution in cabal-install
--------------------------------------

There are two general options for communicating knowledge about build
flavors to the solver:

` 1. `**`the` `direct`
`way`**`: i.e., all info is available to ghc-pkg and can be communicated back to Cabal and therefore the solver can figure out if a particular package is suitable to use or not, in advance;`

` 2. `**`the` `agnostic`
`way`**`: this is based on the idea that the solver at first doesn't consider installed packages at all. It'll just do resolution on the source packages available. Then, taking all build parameters into account, Cabal hashes will be computed, which can then be compared to hashes of installed packages.`

Reusing installed packages instead of rebuilding them is then an
optimization of the install plan.

The agnostic way does not require \`ghc-pkg\` to be directly aware of
all the build parameters, as long as the hash computation is robust

The options are to support either both by putting all info into
\`InstalledPackageInfo\` or to support only the second option by just
putting a hash into \`InstalledPackageInfo\`. The disadvantage of
supporting both is that \`InstalledPackageInfo\` would have to change
more often. This could be fixed by explicitly making the
\`InstalledPackageInfo\` format extensible in a backwards-compatible
way.

The advantages of having all info available, independently of the solver
algorihm, are that the info might be useful for other tools and user
feedback.

Possible disadvantages of the agnostic approach could be that is is a
rather significant change and can probably not be supported in a similar
way for other Haskell implementation. Also, in the direct approach, we
could in principle allow more complex compatibility rules, such as
allowing non-profiling libraries to depend on profiling libraries.

Also, even if we go for the agnostic approach, we still have to be able
to handle packages such as base or ghc-prim which are in general not
even available in source form.

On the other hand, the agnostic approach might lead to more predictable
and reproducible solver results across many different systems.

Garbage Collection
------------------

The proposed changes will likely lead to a dramatic increase of the
number of installed package instances on most systems. This is
particularly relevant for package developers who will conduct lots of
dirty builds that lead to new instances being installed all the time.

It should therefore be possible to have a garbage collection to remove
unneeded packages. However, it is not possible for Cabal to see all
potential reverse dependencies of a package, so automatic garbage
collection would be extremely unsafe.

Options are to either offer an interactive process where packages that
look unused are suggested for removal, or to integrate with a sandbox
mechanism. If, for example, dirty builds are usually installed into a
separate package DB, that package DB could just be removed completely by
a user from time to time.

The garbage collection functionality is part of cabal-install not of
ghc-pkg. As a first approximation gc does not remove files only
unregisters packages from the \`PackageDB\`.

Currently open design decisions
-------------------------------

### \`InstalledPackageId\` and install path

Options for uniquely identifying \`InstalledPackageId\`:

`  * Cabal hash only`\
`  * Cabal + ABI hash (truly unique)`\
`  * random number`

Options for identifying install path:

`  * Cabal hash`\
`  * random number`

ABI hash cannot be in install path because it's only available after
build.

### Handling of dirty builds

How should hash computation work for dirty builds?

`  * Use a random number even if we otherwise use hashes`\
`  * Hash the complete build directory`\
`  * Attempt to make a clean (sdist-like) copy or linked copy of the sources and hash and build from that.`\
`  * Use the Cabal file to determine the files that would end up in an sdist and hash those directly without copying.`

The third option has the advantage(?) that the build is more guaranteed
to use only files actually mentioned in the Cabal file.

### Build flavours

To what degree should we distinguish package instances?

`  * Only package versions transitively`\
`  * Ways and Cabal flags`\
`  * Everything Haskell-specific info that we can query`\
`  * Even non-Haskell-specific inputs such as OS dependencies`

### \`InstalledPackageInfo\` and solver algorithm

Options for \`InstalledPackageInfo\`:

`  * Only add Cabal hash.`\
`  * Add (nearly) all information, but in an extensible format.`\
``   * Add all information in a way that `ghc-pkg` itself can use it. ``

\[These aren't necessarily mutually exclusive.\]

Options for the solver:

``   * Direct (see above): requires a certain amount of info in the `InstalledPackageInfo`. ``

``   * Agnostic (except for builtin packages): could be done with only the Cabal hash in `InstalledPackageInfo`. ``

### Simplistic dependency resolution

Options (in order of preference):

`* use the time of installation`\
`* user-specified priorities`\
`* pick a random / unspecified instances`\
`* (build a complex solver into GHC)`

A combination of the first two seems possible and useful.

Related topics
--------------

In the following, we discuss some other issues which are related to the
multi-instance problem, but not necessarily directly relevant in order
to produce an implementation.

### Separating storage and selection of packages

Currently the two concepts of storing package instances (cabal store)
and selecting package instances for building (environment) are conflated
into a \`PackageDB\`. Sandboxes are used as a workaround to create
multiple different environments. But they also create multiple places to
store installed packages. The disadvantages of this are disk usage,
compilation time and one might lose the overview. Also if the
multi-instance restriction is not lifted sandboxes will eventually
suffer from the same unintended breakage of packages as non-sandboxed
\`PackageDB\`s. There should be a separation between the set of all
installed packages called the cabal store and a subset of these called
an environment. While the cabal store can contain multiple instances of
the same package version an environment needs to be consistent. An
environment is consistent if for every package version it contains only
one instance of that package version.

### First class environments

It would be nice if we had some explicit notion of an environment.

Questions to remember
---------------------

Should the cabal version be part of the hash?

Does the hash contain characters conflicting under windows?

What about builtin packages like ghc-prim, base, rts and so on?

Inplace Registration?

Who has assumptions about the directory layout of installed packages?

Executables?

Haddock?

Installation Planner?

Custom Builds and BuildHooks?

Other Compilers, backwards compatibility?

What is ComponentLocalBuildInfo for?

The Haskell Execution Model
===========================

The \[wiki:Commentary/Compiler/StgSynType STG language\] has a clear
*operational* model, as well as having a declarative lambda-calculus
reading. The business of the \[wiki:Commentary/Compiler/CodeGen code
generator\] is to translate the STG program into \`C--\`, and thence to
machine code, but that is mere detail. From the STG program you should
be able to understand:

` * What functions are in the compiled program, and what their entry and return conventions are`\
` * What heap objects are allocated, when, and what their layout is`

GHC uses an eval/apply execution model, described in the paper [How to
make a fast curry: push/enter vs
eval/apply](http://research.microsoft.com/%7Esimonpj/papers/eval-apply).
This paper is well worth reading if you are interested in this section.

Contents:

`* [wiki:Commentary/Rts/HaskellExecution/Registers Registers]`\
`* [wiki:Commentary/Rts/HaskellExecution/FunctionCalls Function Calls]`\
`* [wiki:Commentary/Rts/HaskellExecution/CallingConvention Call and Return Conventions]`\
`* [wiki:Commentary/Rts/HaskellExecution/HeapChecks Heap and Stack checks]`\
`* [wiki:Commentary/Rts/HaskellExecution/Updates Updates]`\
`* [wiki:Commentary/Rts/HaskellExecution/PointerTagging Pointer Tagging]`

HEAP\_ALLOCED
=============

This page is about the \`HEAP\_ALLOCED()\` macro/function in the runtime
system. See \#8199 which is about getting rid of \`HEAP\_ALLOCED\`.

It is defined in \`rts/sm/MBlock.h\`. The purpose of \`HEAP\_ALLOCED()\`
is to return true if the given address is part of the
dynamically-allocated heap, and false otherwise. Its primary use is in
the Garbage Collector: when examining a pointer, we need to get to the
block descriptor for that object. Static objects don't have block
descriptors, because they live in static code space, so we need to
establish whether the pointer is into the dynamic heap first, hence
\`HEAP\_ALLOCED()\`.

On a 32-bit machine, \`HEAP\_ALLOCED()\` is implemented with a
4096-entry byte-map, one byte per megabyte of the address space (the
dynamic heap is allocated in units of aligned megabytes).

On a 64-bit machine, it's a bit more difficult. The current method (GHC
6.10.1 and earlier) uses a cache, with a 4096-entry map and a 32-bit
tag. If the upper 32 bits of the pointer match the tag, we look up in
the map, otherwise we back off to a slow method that searches a list of
mappings (bug \#2934 is about the lack of thread-safety in the slow path
here). This arrangement works fine for small heaps, but is pessimal for
large (multi-GB) heaps, or heaps that are scattered around the address
space.

Speeding up \`HEAP\_ALLOCED()\`
-------------------------------

We should consider how to speed up \`HEAP\_ALLOCED()\` for large heaps
on 64-bit machines. This involves some kind of cache arrangement - the
memory map is like a page table, and we want a cache that gives us quick
access to commonly accessed parts of that map.

[5](attachment:faster-heap-alloced.patch.gz) implements one such scheme.
Measurements show that it slows down GC by about 20% for small heaps
(hence it wasn't committed), though it would probably speed up GC on
large heaps.

Eliminating \`HEAP\_ALLOCED\` completely
----------------------------------------

Can we eliminate \`HEAP\_ALLOCED\` altogether? We must arrange that all
closure pointers have a valid block descriptor.

### Method 1: put static closures in an aligned section

ELF sections can be arbitrarily aligned. So we could put all our static
closures in a special section, align the section to 1MB, and arrange
that there is space at the beginning of the section for the block
descriptors.

This almost works (see [6](attachment:eliminate-heap-alloced.patch.gz)),
but sadly fails for shared libraries: the system dynamic linker doesn't
honour section-alignment requests larger than a page, it seems. Here is
a simple test program which shows the problem on Linux:

Compare static linking and dynamic linking:

### Method 2: copy static closures into a special area at startup

We could arrange that we access all static closures via indirections,
and then at startup time we copy all the static closures into a special
area with block descriptors.

Disadvantages:

`* references to static objects go through another indirection. (This includes all of the RTS code!)`\
`  * when doing dynamic linking, references to static objects in another package`\
`    already go through an indirection and we could arrange that only one indirection is required.`\
`  * References to static closures from the the fields of a static constructor would not incur the extra indirection,`\
`    only direct references to static closures from code.`\
`  * we currently reference the static closure of a function from the heap-check-fail code, but in fact`\
`    we only really need to pass the info pointer.`

Advantages

`* we get to fix up all the tag bits in static closure pointers`\
`* we get to eliminate HEAP_ALLOCED, speeding up GC and removing complexity`\
`* CAFs might get a bit simpler, since they are already indirections into the heap`

Heap and Stack checks
=====================

Source files:
[GhcFile(rts/HeapStackCheck.cmm)](GhcFile(rts/HeapStackCheck.cmm) "wikilink")

When allocating a heap object, we bump \`Hp\` and compare to \`HpLim\`.
If the test fails we branch to ???. Usually this code tests an interrupt
flag (to see if execution should be brought tidily to a halt); grabs the
next block of allocation space; makes \`Hp\` point to it and \`HpLim\`
to its end; and returns. If there are no more allocation-space blocks,
garbage collection is triggered.

------------------------------------------------------------------------

CategoryStub

[PageOutline](PageOutline "wikilink")

GHC Commentary: The Layout of Heap Objects
==========================================

Terminology
-----------

`* A `*`lifted`*` type is one that contains bottom (_|_), conversely an `*`unlifted`*` type does not contain _|_.`\
`  For example, `` is lifted, but `` is unlifted.`

`* A `*`boxed`*` type is represented by a pointer to an object in the heap, an `*`unboxed`*` object is represented by a value.`\
`  For example, `` is boxed, but `` is unboxed.`

The representation of \_|\_ must be a pointer: it is an object that when
evaluated throws an exception or enters an infinite loop. Therefore,
only boxed types may be lifted.

There are boxed unlifted types: eg. . If you have a value of type , it
definitely points to a heap object with type (see below), rather than an
unevaluated thunk.

Unboxed tuples are both unlifted and unboxed. They are represented by
multiple values passed in registers or on the stack, according to the
\[wiki:Commentary/Rts/HaskellExecution return convention\].

Unlifted types cannot currently be used to represent terminating
functions: an unlifted type on the right of an arrow is implicitly
lifted to include \`\_|\_\`.

------------------------------------------------------------------------

Heap Objects
------------

All heap objects have the same basic layout, embodied by the type in
\[source:includes/rts/storage/Closures.h Closures.h\]. The diagram below
shows the layout of a heap object:

[Image(heap-object.png)](Image(heap-object.png) "wikilink")

A heap object always begins with a *header*, defined by in
\[source:includes/rts/storage/Closures.h Closures.h\]:

The most important part of the header is the *info pointer*, which
points to the info table for the closure. In the default build, this is
all the header contains, so a header is normally just one word. In other
builds, the header may contain extra information: eg. in a profiling
build it also contains information about who built the closure.

Most of the runtime is insensitive to the size of ; that is, we are
careful not to hardcode the offset to the payload anywhere, instead we
use C struct indexing or . This makes it easy to extend with new fields
if we need to.

The compiler also needs to know the layout of heap objects, and the way
this information is plumbed into the compiler from the C headers in the
runtime is described here:
\[wiki:Commentary/Compiler/CodeGen\#Storagemanagerrepresentations\].

------------------------------------------------------------------------

Info Tables
-----------

The info table contains all the information that the runtime needs to
know about the closure. The layout of info tables is defined by in
\[source:includes/rts/storage/InfoTables.h InfoTables.h\]. The basic
info table layout looks like this:

[Image(basic-itbl.png)](Image(basic-itbl.png) "wikilink")

Where:

`* The `*`closure`
`type`*` is a constant describing the kind of closure this is (function, thunk, constructor etc.).  All`\
`  the closure types are defined in [source:includes/rts/storage/ClosureTypes.h ClosureTypes.h], and many of them have corresponding C struct`\
`  definitions in [source:includes/rts/storage/Closures.h Closures.h].`

`* The `*`SRT`
`bitmap`*` field is used to support [wiki:Commentary/Rts/Storage/GC/CAFs garbage collection of CAFs].`

`* The `*`layout`*` field describes the layout of the payload for the garbage collector, and is described in more`\
`  detail in `[`ref(Types` `of` `Payload`
`Layout)`](ref(Types_of_Payload_Layout) "wikilink")` below.`

`* The `*`entry`
`code`*` for the closure is usually the code that will `*`evaluate`*` the closure.  There is one exception:`\
`  for functions, the entry code will apply the function to the arguments given in registers or on the stack, according`\
`  to the calling convention.  The entry code assumes all the arguments are present - to apply a function to fewer arguments`\
`  or to apply an unknown function, the [wiki:Commentary/Rts/HaskellExecution/FunctionCalls#Genericapply generic apply functions] must`\
`  be used.`

Some types of object add more fields to the end of the info table,
notably functions, return addresses, and thunks.

Space in info tables is a premium: adding a word to the standard info
table structure increases binary sizes by 5-10%.

### 

Note that the info table is followed immediately by the entry code,
rather than the code being at the end of an indirect pointer. This both
reduces the size of the info table and eliminates one indirection when
jumping to the entry code.

GHC can generate code that uses the indirect pointer instead; the turns
on the optimised layout. Generally is turned off when compiling
unregisterised.

When is off, info tables get another field, , which points to the entry
code. In a generated object file, each symbol representing an info table
will have an associated symbol pointing to the entry code (in , the
entry symbol is omitted to keep the size of symbol tables down).

------------------------------------------------------------------------

Types of Payload Layout
-----------------------

The GC needs to know two things about the payload of a heap object: how
many words it contains, and which of those words are pointers. There are
two basic kinds of layout for the payload: *pointers-first* and
*bitmap*. Which of these kinds of layout is being used is a property of
the *closure type*, so the GC first checks the closure type to determine
how to interpret the layout field of the info table.

### Pointers-first layout

The payload consists of zero or more pointers followed by zero or more
non-pointers. This is the most common layout: constructors, functions
and thunks use this layout. The layout field contains two
half-word-sized fields:

` * Number of pointers`\
` * Number of non-pointers`

### Bitmap layout

The payload consists of a mixture of pointers and non-pointers,
described by a bitmap. There are two kinds of bitmap:

**Small bitmaps.** A small bitmap fits into a single word (the layout
word of the info table), and looks like this:

|| Size (bits 0-4) || Bitmap (bits 5-31) ||

(for a 64-bit word size, the size is given 6 bits instead of 5).

The size field gives the size of the payload, and each bit of the bitmap
is 1 if the corresponding word of payload contains a pointer to a live
object.

The macros , , and in \[source:includes/rts/storage/InfoTables.h
InfoTables.h\] provide ways to conveniently operate on small bitmaps.

**Large bitmaps.** If the size of the stack frame is larger than the 27
words that a small bitmap can describe, then the fallback mechanism is
the large bitmap. A large bitmap is a separate structure, containing a
single word size and a multi-word bitmap: see in
\[source:includes/rts/storage/InfoTables.h InfoTables.h\].

------------------------------------------------------------------------

Dynamic vs. Static objects
--------------------------

Objects fall into two categories:

`* `*`dynamic`*` objects reside in the heap, and may be moved by the garbage collector.`

`* `*`static`*` objects reside in the compiled object code.  They are never moved, because pointers to such objects are`\
`  scattered through the object code, and only the linker knows where.`

To find out whether a particular object is dynamic or static, use the
\[wiki:Commentary/Rts/Storage/HeapAlloced HEAP\_ALLOCED()\] macro, from
\[source:rts/sm/HeapAlloc.h\]. This macro works by consulting a bitmap
(or structured bitmap) that tells for each
\[wiki:Commentary/Rts/Storage\#Structureofblocks megablock\] of memory
whether it is part of the dynamic heap or not.

### Dynamic objects

Dynamic objects have a minimum size, because every object must be big
enough to be overwritten by a forwarding pointer ([ref(Forwarding
Pointers)](ref(Forwarding_Pointers) "wikilink")) during GC. The minimum
size of the payload is given by in \[source:includes/rts/Constants.h\].

### Static objects

All static objects have closure types ending in , eg. for static data
constructors.

Static objects have an additional field, called the *static link field*.
The static link field is used by the GC to link all the static objects
in a list, and so that it can tell whether it has visited a particular
static object or not - the GC needs to traverse all the static objects
in order to \[wiki:Commentary/Rts/CAFs garbage collect CAFs\].

The static link field resides after the normal payload, so that the
static variant of an object has compatible layout with the dynamic
variant. To access the static link field of a closure, use the macro
from \[source:includes/rts/storage/ClosureMacros.h\].

------------------------------------------------------------------------

Types of object
---------------

### Data Constructors

All data constructors have pointers-first layout:

|| Header || Pointers... || Non-pointers... ||

Data constructor closure types:

`* ``: a vanilla, dynamically allocated constructor`\
`* ``: a constructor whose layout is encoded in the closure type (eg. `` has one pointer`\
`  and zero non-pointers.  Having these closure types speeds up GC a little for common layouts.`\
`* ``: a statically allocated constructor.`\
`* ``: TODO: Needs documentation`

The entry code for a constructor returns immediately to the topmost
stack frame, because the data constructor is already in WHNF. The return
convention may be vectored or non-vectored, depending on the type (see
\[wiki:Commentary/Rts/HaskellExecution/CallingConvention\]).

Symbols related to a data constructor X:

`* X_``: info table for a dynamic instance of X`\
`* X_``: info table for a static instance of X`\
`* X_``: the `*`wrapper`*` for X (a function, equivalent to the`\
`  curried function `` in Haskell, see`\
`  [wiki:Commentary/Compiler/EntityTypes]).  `\
`* X_``: static closure for X's wrapper`

### Function Closures

A function closure represents a Haskell function. For example: Here,
would be represented by a static function closure (see below), and a
dynamic function closure. Every function in the Haskell program
generates a new info table and entry code, and top-level functions
additionally generate a static closure.

All function closures have pointers-first layout:

|| Header || Pointers... || Non-pointers... ||

The payload of the function closure contains the free variables of the
function: in the example above, a closure for would have a payload
containing a pointer to .

Function closure types:

`* ``: a vanilla, dynamically allocated function`\
`* ``: same, specialised for layout (see constructors above)`\
`* ``: a static (top-level) function closure`

Symbols related to a function :

`* ``: f's info table and code`\
`* ``: f's static closure, if f is a top-level function.`\
`  The static closure has no payload, because there are no free`\
`  variables of a top-level function.  It does have a static link`\
`  field, though.`

### Thunks

A thunk represents an expression that is not obviously in head normal
form. For example, consider the following top-level definitions: Here
the right-hand sides of and are both thunks; the former is static while
the latter is dynamic.

Thunks have pointers-first layout:

|| Header || (empty) || Pointers... || Non-pointers... ||

As for function closures, the payload contains the free variables of the
expression. A thunk differs from a function closure in that it can be
\[wiki:Commentary/Rts/HaskellExecution\#Updates updated\].

There are several forms of thunk:

`* ``, ``: vanilla, dynamically allocated`\
`  thunks.  Dynamic thunks are overwritten with normal indirections`\
`  `` when evaluated.`

`* ``: a static thunk is also known as a ''constant`\
`  applicative form'', or `*`CAF`*`.  Static thunks are overwritten with`\
`  static indirections (``).`

The only label associated with a thunk is its info table:

`* `` is f's info table.`

The empty padding is to allow thunk update code to overwrite the target
of an indirection without clobbering any of the saved free variables.
This means we can do thunk update without synchronization, which is a
big deal.

### Selector thunks

 is a (dynamically allocated) thunk whose entry code performs a simple
selection operation from a data constructor drawn from a
single-constructor type. For example, the thunk is a selector thunk. A
selector thunk is laid out like this:

|| Header || Selectee pointer ||

The \`layout\` word contains the byte offset of the desired word in the
selectee. Note that this is different from all other thunks.

The garbage collector "peeks" at the selectee's tag (in its info table).
If it is evaluated, then it goes ahead and does the selection, and then
behaves just as if the selector thunk was an indirection to the selected
field. If it is not evaluated, it treats the selector thunk like any
other thunk of that shape.

This technique comes from the Phil Wadler paper [Fixing some space leaks
with a garbage
collector](http://homepages.inf.ed.ac.uk/wadler/topics/garbage-collection.html),
and later Christina von Dorrien who called it "Stingy Evaluation".

There is a fixed set of pre-compiled selector thunks built into the RTS,
representing offsets from 0 to , see \[source:rts/StgStdThunks.cmm\].
The info tables are labelled where is the offset. Non-updating versions
are also built in, with info tables labelled .

These thunks exist in order to prevent a space leak. For example, if y
is a thunk that has been evaluated, and y is unreachable, but x is
reachable, the risk is that x keeps both the a and b components of y
live. By making the selector thunk a special case, we make it possible
to reclaim the memory associated with b. (The situation is further
complicated when selector thunks point to other selector thunks; the
garbage collector sees all, knows all.)

### Partial applications

Partial applications are tricky beasts.

A partial application, closure type , represents a function applied to
too few arguments. Partial applications are only built by the
\[wiki:Commentary/Rts/HaskellExecution/FunctionCalls\#Genericapply
generic apply functions\] in \[source:rts/Apply.cmm\].

|| Header || Arity || No. of words || Function closure || Payload... ||

Where:

`* `*`Arity`*` is the arity of the PAP.  For example, a function with`\
`  arity 3 applied to 1 argument would leave a PAP with arity 2.`

`* `*`No.` `of` `words`*` refers to the size of the payload in words.`

`* `*`Function` `closure`*` is the function to which the arguments are`\
`  applied.  Note that this is always a pointer to one of the`\
`  `` family, never a ``.  If a `` is applied`\
`  to more arguments to give a new ``, the arguments from`\
`  the original `` are copied to the new one.`

`* The payload is the sequence of arguments already applied to`\
`  this function.  The pointerhood of these words are described`\
`  by the function's bitmap (see `` in `\
`  [source:rts/sm/Scav.c] for an example of traversing a PAP).`

There is just one standard form of PAP. There is just one info table
too, called . A PAP should never be entered, so its entry code causes a
failure. PAPs are applied by the generic apply functions in .

### Generic application

An object is very similar to a , and has identical layout:

|| Header || Arity || No. of words || Function closure || Payload... ||

The difference is that an is not necessarily in WHNF. It is a thunk that
represents the application of the specified function to the given
arguments.

The arity field is always zero (it wouldn't help to omit this field,
because it is only half a word anyway).

 closures are used mostly by the byte-code interpreter, so that it only
needs a single form of thunk object. Interpreted thunks are always
represented by the application of a to its free variables.

### Stack application

An is a special kind of object:

|| Header || Size || Closure || Payload... ||

It represents computation of a thunk that was suspended midway through
evaluation. In order to continue the computation, copy the payload onto
the stack (the payload was originally the stack of the suspended
computation), and enter the closure.

Since the payload is a chunk of stack, the GC can use its normal
stack-walking code to traverse it.

 closures are built by in \[source:rts/RaiseAsync.c\] when an
\[wiki:Commentary/Rts/AsyncExceptions asynchronous exception\] is
raised. It's fairly typical for the end of an AP\_STACK's payload to
have another AP\_STACK: you'll get one per update frame.

### Indirections

Indirection closures just point to other closures. They are introduced
when a thunk is updated to point to its value. The entry code for all
indirections simply enters the closure it points to.

The basic layout of an indirection is simply

|| Header || Target closure ||

There are several variants of indirection:

`* ``: is the vanilla, dynamically-allocated indirection.`\
`  It is removed by the garbage collector.  An `` only exists in the youngest generation.  `\
`  The update code (`` and friends) checks whether the updatee is in the youngest`\
`  generation before deciding which kind of indirection to use.`\
`* ``: a static indirection, arises when we update a ``.  A new `\
`  is placed on the mutable list when it is created (see `` in [source:rts/sm/Storage.c]).`

### Byte-code objects

### Black holes

,

Black holes represent thunks which are under evaluation by another
thread (that thread is said to have claimed the thunk). Attempting to
evaluate a black hole causes a thread to block until the thread who
claimed the thunk either finishes evaluating the thunk or dies. You can
read more about black holes in the paper 'Haskell on a Shared-Memory
Multiprocessor'. Black holes have the same layout as indirections.

|| Header || Target closure ||

Sometimes black holes are just ordinary indirection. Check
\`stg\_BLACKHOLE\_info\` for the final word: if the indirectee has no
tag, then we assume that it is the TSO that has claimed the thunk; if
the indirectee is tagged, then it is just a normal indirection. (EZY: I
think this optimization is to avoid having to do two memory writes on
thunk update; we don't bother updating the header, only the target.)

When eager blackholing is enabled, the black hole that is written is not
a true black hole, but an eager black hole. True black holes are
synchronized, and guarantee that only one black hole is claimed (this
property is used to implement non-dupable unsafePerformIO). Eager black
holes are not synchronized; eager black hole are converted into true
black holes in ThreadPaused.c. Incidentally, this facility is also used
to convert update frames to black holes; this is important for
eliminating a space leak caused by the thunk under evaluation retaining
too much data (overwriting it with a black hole frees up variable.)

### Arrays

, , , ,

Non-pointer arrays are straightforward:

||| Header ||| Bytes ||| Array payload |||

Arrays with pointers are a little more complicated, they include a card
table, which is used by the GC to know what segments of the array to
traverse as roots (the card table is modified by the GC write barrier):

||| Header ||| Ptrs ||| Size ||| Array payload + card table |||

You can access the card table by using \`mutArrPtrsCard(array, element
index)\`, which gives you the address of the card for that index.

### MVars

MVars have a queue of the TSOs blocking on them along with their value:

|| Header || Head of queue || Tail of queue || Value ||

An MVar can be in several states. It can be empty (in which case the
value is actually just a \`stg\_END\_TSO\_QUEUE\_closure\`) or it can be
full. When it is full, the queue of TSOs are those waiting to put; when
it is empty, the queue of TSOs are those waiting to read and take (with
readers first). Like many mutable objects, MVars have CLEAN and DIRTY
headers to avoid reapplying a write barrier when an MVar is already
dirty.

### Weak pointers

### Stable Names

### Thread State Objects

Closure type is a Thread State Object. It represents the complete state
of a thread, including its stack.

TSOs are ordinary objects that live in the heap, so we can use the
existing allocation and garbage collection machinery to manage them.
This gives us one important benefit: the garbage collector can detect
when a blocked thread is unreachable, and hence can never become
runnable again. When this happens, we can notify the thread by sending
it the exception.

GHC keeps divides stacks into stack chunks, with logic to handle stack
underflow and overflow:
<http://hackage.haskell.org/trac/ghc/blog/stack-chunks>

The TSO structure contains several fields. For full details see
\[source:includes/rts/storage/TSO.h\]. Some of the more important fields
are:

`* `*`link`*`: field for linking TSOs together in a list.  For example, the threads blocked on an `` are kept in`\
`  a queue threaded through the link field of each TSO.`\
`* `*`global_link`*`: links all TSOs together; the head of this list is `` in [source:rts/Schedule.c].`\
`* `*`what_next`*`: how to resume execution of this thread.  The valid values are:`\
`  * ``: continue by returning to the top stack frame.`\
`  * ``: continue by interpreting the BCO on top of the stack.`\
`  * ``: this thread has received an exception which was not caught.`\
`  * ``: this thread ran out of stack and has been relocated to a larger TSO; the link field points`\
`    to its new location.`\
`  * ``: this thread has finished and can be garbage collected when it is unreachable.`\
`* `*`why_blocked`*`: for a blocked thread, indicates why the thread is blocked.  See [source:includes/rts/Constants.h] for`\
`  the list of possible values.`\
`* `*`block_info`*`: for a blocked thread, gives more information about the reason for blockage, eg. when blocked on an`\
`   MVar, block_info will point to the MVar.`\
`* `*`bound`*`: pointer to a [wiki:Commentary/Rts/Scheduler#Task Task] if this thread is bound`\
`* `*`cap`*`: the [wiki:Commentary/Rts/Scheduler#Capabilities Capability] on which this thread resides.`

### STM objects

These object types are used by \[wiki:Commentary/Rts/STM STM\]: , , , .

### Forwarding Pointers

Forwarding pointers appear temporarily during
\[wiki:Commentary/Rts/Storage/GC garbage collection\]. A forwarding
pointer points to the new location for an object that has been moved by
the garbage collector. It is represented by replacing the info pointer
for the closure with a pointer to the new location, with the least
significant bit set to 1 to distinguish a forwarding pointer from an
info pointer.

How to add new heap objects
---------------------------

There are two This page is a stub.

Change History
--------------

`* `*`History` `of` `when` `Hoopl` `was` `integrated` `into` `a` `GHC`
`back` `end`*

`* After the publication of the Hoopl paper, a contributor (sorry I have forgotten who) did quite a bit to integrate the supply of ``s into Hoopl.  (Time? Person?)`

`* `*`Note` `that` `the` `new` `code` `generator` `appears` `about`
`10x` `slower` `than` `the` `old.` `Slowdown` `attributed` `to` `Hoopl`
`dataflow.`*`   See `[`Google` `Plus` `post` `by` `Simon`
`Marlow`](https://plus.google.com/107890464054636586545/posts/dBbewpRfw6R)`.`

`* Fixed-point algorithm rewritten to reduce duplicate computation.  (Simon Marlow in late 2011.  Also Edward Yang in spring 2011.) Is there any more? I suggest looking at traces in the simple cases.`

`* Change in representation of blocks, Simon Marlow, late 2011.  (Details?)  Performance difference almost too small to be measurable, but Simon M likes the new rep anyway.`

Speculation and Commentary
--------------------------

`* Simon PJ had questions about "optimization fuel" from the beginning.  Norman maintains that optimization fuel is an invaluable debugging aid, but that in a production compiler, one would like it to be turned off.   At some point we had abstracted over the `` so that we could make a "zero" fuel monad that did nothing and cost nothing.  As of January 2012, Norman doesn't know what the state of that plan is or whether GHC's optimiser can actually eliminate the overheads.`

`* Unlike Fuel, a supply of ``s was believed to be an absolute necessity: an optimiser must be able to rewrite blocks, and in the general case, it must be able to introduce new blocks.  It was believed that the only way to do this consistent with GHC was to plumb in a Uniq supply.   `*`Query`*`: was this integrated with Fuel somehow?`

`* The published version of Hoopl passes an explicit dictionary that contains all the dataflow facts for all the labels.   Earlier versions of Hoopl kept this information in a monad.  It's not known whether the change has implications for performance, but it is probably easier to manage the speculative rewriting without a monad.`

`* Norman has always been uneasy about the dictionaries passed to the `` function.  He conjectures that most blocks have a small number of outedges, and probably not that many inedges either (case expressions and the Adams optimisation notwithstanding).  He wonders if instead of some kind of trie structure with worst-case logarithmic performance, we might not be better off with a simple association list---especially because it is common to simply join `*`all`*` facts flowing into a block.   `**`Query:`
`Is` `there` `a` `way` `to` `measure` `the` `costs` `of` `using`
`dictionaries` `in` `this` `fashion?` `Cost` `centers,` `perhaps?`**

`* There was a Google Plus thread in which CPS was criticized (by Jan Maessen, I think).  The original authors had many big fights, and one of them was about CPS.  At some point Norman drafted a dataflow analyser that was very aggressively CPS.  Simon PJ found the extensive CPS difficult to read.  Norman doesn't remember the eventual outcome.   Is it possible that the CPS is causing the allocation of too many function closures?   Could the CPS be rewritten, perhaps by a different way of nesting functions, to eliminate the need to allocate closures in the inner loop?  Johan Tibell tried optimizing postorder_dfs, but was put off by the CPS style of code. (We speculate that caching the result of toposort may help.)`

`* Another important thing to keep in mind is that some of the existing passes used by GHC may be implemented inefficiently (of no fault of Hoopl itself.) For example, the rewrite assignments pass takes around 15% of the entire compilation time; we believe this is because it has to rewrite the entire graph into a new representation before doing any transformations, and then rewrite it back to the original. Optimizations here (for example, storing the information in an external map as opposed to the AST itself) would probably would help a lot.`

Record of performance improvements made to the Hoopl library starting January 2012
----------------------------------------------------------------------------------

Haskell Program Coverage
========================

This page describes the Haskell Program Coverage implementation inside
GHC. Background information can be found in the paper [Haskell Program
Coverage](http://www.ittc.ku.edu/~andygill/papers/Hpc07.pdf) by Andy
Gill and Colin Runciman, and the Haskell wiki page [Haskell program
coverage](https://wiki.haskell.org/Haskell_program_coverage).

The basic idea is this

`* For each (sub)expression in the Haskell Syntax, write the (sub)expression in a    `\
``   `HsTick` ``\
`` * Each `HsTick` has a module local index number. ``\
`* There is a table (The Mix data structure) that maps this index number to original source location.`\
`` * Each `HsTick` is mapped in the Desugar pass with:  ``

`` * This tick is a special type of `Id`, a `TickOpId` which takes no core-level argument, but has two pre-applied arguments; the module name and the module-local tick number. ``\
`  * We store both module name and tick number to allow this Id to be passed (inlined) inside other modules.`\
``   * This `Id` has type  ``**`State#` `World#`**\
`* The core simplifier must not remove this case, but it can move it.`\
`  * The do-not-remove is enforced via the ... function in ....`\
``   * The semantics are tick if-and-when-and-as you enter the `DEFAULT` case. But a chain of consecutive ticks can be executed in any order. ``\
`` * The !CoreToStg Pass translates the ticks into `StgTick` ``

`` * The `Cmm` code generator translates `StgTick` to a 64 bit increment. ``

Other details

`* A executable startup time, we perform a depth first traversal some module`\
`  specific code, gathering a list of all Hpc registered modules, and the`\
`  module specific tick table. `\
`* There is one table per module, so we can link the increment statically,`\
`  without needing to know the global tick number.`\
`* The module Hpc.c in the RTS handles all the reading of these table.`\
`* At startup, if a .tix file is found, Hpc.c checks that this is the same`\
`  binary as generated the .tix file, and if so, pre-loads all the tick counts`\
`  in the module specific locations.`\
`* (I am looking for a good way of checking the binaries for sameness)`\
`* At shutdown, we write back out the .tix files, from the module-local tables.`

### Binary Tick Boxes

There is also the concept of a binary tick box. This is a syntactical
boolean, like a guard or conditional for an if. We use tick boxes to
record the result of the boolean, to check for coverage over True and
False.

`` * Each `HsBinaryTick` is mapped in the Desugar pass with:  ``

-   After desugaring, there is no longer any special code for binary
    tick box.

Machine Generated Haskell
-------------------------

Sometimes, Haskell is the target language - for example, Happy and Alex.
In this case, you want to be able to check for coverage of your
**original** program. So we have a new pragma.

This means that the expression was obtained from the given file and
locations. This might be code included verbatim (for example the actions
in Happy), or be generated from a specification from this location.

Compiling one module: !HscMain
==============================

Here we are going to look at the compilation of a single module. There
is a picture that goes with this description, which appears at the
bottom of this page, but you'll probably find it easier to open
\[wiki:Commentary/Compiler/HscPipe this link\] in another window, so you
can see it at the same time as reading the text.

You can also watch a **video** of Simon Peyton-Jones explaining the
compilation pipeline here: [Compiler Pipeline
II](http://www.youtube.com/watch?v=Upm_kYMgI_c&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
(10'16")

Look at the picture first. The yellow boxes are compiler passes, while
the blue stuff on the left gives the data type that moves from one phase
to the next. The entire pipeline for a single module is run by a module
called !HscMain
([GhcFile(compiler/main/HscMain.hs)](GhcFile(compiler/main/HscMain.hs) "wikilink")).
Each data type's representation can be dumped for further inspection
using a \`-ddump-\*\` flag. (Consider also using \`-ddump-to-file\`:
some of the dump outputs can be large!) Here are the steps it goes
through:

`* The `**`Front`
`End`**` processes the program in the [wiki:Commentary/Compiler/HsSynType big HsSyn type]. `` is parameterised over the types of the term variables it contains.  The first three passes (the front end) of the compiler work like this:`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  * The `**`[wiki:Commentary/Compiler/Parser`
`Parser]`**` produces `` parameterised by `**`[wiki:Commentary/Compiler/RdrNameType`
`RdrName]`**`.  To a first approximation, a ```  is just a string. (`-ddump-parsed`)  ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  * The `**`[wiki:Commentary/Compiler/Renamer`
`Renamer]`**` transforms this to `` parameterised by `**`[wiki:Commentary/Compiler/NameType`
`Name]`**`.  To a first appoximation, a `` is a string plus a `` (number) that uniquely identifies it.  In particular, the renamer associates each identifier with its binding instance and ensures that all occurrences which associate to the same binding instance share a single ``` . (`-ddump-rn`)   ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  * The `**`[wiki:Commentary/Compiler/TypeChecker`
`Typechecker]`**` transforms this further, to `` parameterised by `**`[wiki:Commentary/Compiler/EntityTypes`
`Id]`**`.  To a first approximation, an `` is a `` plus a type. In addition, the type-checker converts class declarations to ``es, and type declarations to ``s and ``s.  And of course, the type-checker deals in ``s and ``s. The [wiki:Commentary/Compiler/EntityTypes data types for these entities] (``, ``, ``, ``, ``` ) are pervasive throughout the rest of the compiler. (`-ddump-tc`) ``

`These three passes can all discover programmer errors, which are sorted and reported to the user.`\
\
`* The `**`Desugarer`**` (`[`GhcFile(compiler/deSugar/Desugar.hs)`](GhcFile(compiler/deSugar/Desugar.hs) "wikilink")`) converts from the massive ```  type to [wiki:Commentary/Compiler/CoreSynType GHC's intermediate language, CoreSyn].  This Core-language data type is unusually tiny: just eight constructors.) (`-ddump-ds`) ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  Generally speaking, the desugarer produces few user errors or warnings. But it does produce `*`some`*`` .  In particular, (a) pattern-match overlap warnings are produced here; and (b) when desugaring Template Haskell code quotations, the desugarer may find that `THSyntax` is not expressive enough.  In that case, we must produce an error ( ``[`GhcFile(compiler/deSugar/DsMeta.hs)`](GhcFile(compiler/deSugar/DsMeta.hs) "wikilink")`).`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  This late desugaring is somewhat unusual.  It is much more common to desugar the program before typechecking, or renaming, because that presents the renamer and typechecker with a much smaller language to deal with.  However, GHC's organisation means that`\
`   * error messages can display precisely the syntax that the user wrote; and `\
`   * desugaring is not required to preserve type-inference properties.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")

`* The `**`!SimplCore`**` pass (`[`GhcFile(compiler/simplCore/SimplCore.hs)`](GhcFile(compiler/simplCore/SimplCore.hs) "wikilink")`) is a bunch of Core-to-Core passes that optimise the program; see `[`A`
`transformation-based` `optimiser` `for` `Haskell`
`(SCP'98)`](http://research.microsoft.com/%7Esimonpj/Papers/comp-by-trans-scp.ps.gz)` for a more-or-less accurate overview.  See [wiki:Commentary/Compiler/Core2CorePipeline] for an overview of the Core-to-Core optimisation pipeline. The main passes are:`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`Simplifier`**`, which applies lots of small, local optimisations to the program.  The simplifier is big and complicated, because it implements a `*`lot`*` of transformations; and tries to make them cascade nicely.  The transformation-based optimiser paper gives lots of details, but two other papers are particularly relevant: `[`Secrets`
`of` `the` `Glasgow` `Haskell` `Compiler` `inliner`
`(JFP'02)`](http://research.microsoft.com/%7Esimonpj/Papers/inlining/index.htm)` and `[`Playing`
`by` `the` `rules:` `rewriting` `as` `a` `practical` `optimisation`
`technique` `in` `GHC` `(Haskell` `workshop`
`2001)`](http://research.microsoft.com/%7Esimonpj/Papers/rules.htm)`` .  (`-ddump-simpl`) ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`float-out`**` and `**`float-in`**` transformations, which move let-bindings outwards and inwards respectively.  See `[`Let-floating:`
`moving` `bindings` `to` `give` `faster` `programs` `(ICFP`
`'96)`](http://research.microsoft.com/%7Esimonpj/papers/float.ps.gz)`.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`strictness`
`analyser`**`.  This actually comprises two passes: the `**`analyser`**` itself and the `**`worker/wrapper`**` transformation that uses the results of the analysis to transform the program. (Further described in [wiki:Commentary/Compiler/Demand Demand analysis].) The same analyser also does `[`Constructed`
`Product` `Result`
`analysis`](http://research.microsoft.com/%7Esimonpj/Papers/cpr/index.htm)` and `[`Cardinality`
`analysis`](http://research.microsoft.com/en-us/um/people/simonpj/papers/usage-types/cardinality-extended.pdf)`` . (`-ddump-stranal`) ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`liberate-case`**` transformation.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`constructor-specialialisation`**` transformation.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`   * The `**`common` `sub-expression`
`eliminiation`**``  (CSE) transformation. (`-ddump-cse`) ``

`* Then the `**`!CoreTidy`
`pass`**` gets the code into a form in which it can be imported into subsequent modules (when using ``) and/or put into an interface file.  `\
\
`` It makes a difference whether or not you are using `-O` at this stage.  With `-O` (or rather, with `-fomit-interface-pragmas` which is a consequence of `-O`), the tidied program (produced by `tidyProgram`) has unfoldings for Ids, and RULES.  Without `-O` the unfoldings and RULES are omitted from the tidied program.  And that, in turn, affects the interface file generated subsequently. ``

`There are good notes at the top of the file `[`GhcFile(compiler/main/TidyPgm.hs)`](GhcFile(compiler/main/TidyPgm.hs) "wikilink")`; the main function is ``, documented as "Plan B" ("Plan A" is a simplified tidy pass that is run when we have only typechecked, but haven't run the desugarer or simplifier).`

` * At this point, the data flow forks.  First, the tidied program is dumped into an interface file.  This part happens in two stages:`\
`   * It is `**`converted` `to`
**` (defined in `[`GhcFile(compiler/iface/IfaceSyn.hs)`](GhcFile(compiler/iface/IfaceSyn.hs) "wikilink")` and `[`GhcFile(compiler/iface/IfaceType.hs)`](GhcFile(compiler/iface/IfaceType.hs) "wikilink")`).`\
`   * The `` is `**`serialised` `into` `a` `binary` `output`
`file`**` (`[`GhcFile(compiler/iface/BinIface.hs)`](GhcFile(compiler/iface/BinIface.hs) "wikilink")`).`\
``  The serialisation does (pretty much) nothing except serialise.  All the intelligence is in the `Core`-to-`IfaceSyn` conversion; or, rather, in the reverse of that step. ``

` * The same, tidied Core program is now fed to the Back End.  First there is a two-stage conversion from `` to [wiki:Commentary/Compiler/StgSynType GHC's intermediate language, StgSyn].`\
`   * The first step is called `**`!CorePrep`**`` , a Core-to-Core pass that puts the program into A-normal form (ANF).  In ANF, the argument of every application is a variable or literal; more complicated arguments are let-bound.  Actually `CorePrep` does quite a bit more: there is a detailed list at the top of the file  ``[`GhcFile(compiler/coreSyn/CorePrep.hs)`](GhcFile(compiler/coreSyn/CorePrep.hs) "wikilink")`.`\
`   * The second step, `**`!CoreToStg`**`, moves to the `` data type (`[`GhcFile(compiler/stgSyn/CoreToStg.hs)`](GhcFile(compiler/stgSyn/CoreToStg.hs) "wikilink")`).  The output of !CorePrep is carefully arranged to exactly match what `` allows (notably ANF), so there is very little work to do. However, `` is decorated with lots of redundant information (free variables, let-no-escape indicators), which is generated on-the-fly by ``.`

` * Next, the `**`[wiki:Commentary/Compiler/CodeGen` `Code`
`Generator]`**` converts the STG program to a `` program.  The code generator is a Big Mother, and lives in directory `[`GhcFile(compiler/codeGen)`](GhcFile(compiler/codeGen) "wikilink")`  `

` * Now the path forks again:`\
`   * If we are generating GHC's stylised C code, we can just pretty-print the `` code as stylised C (`[`GhcFile(compiler/cmm/PprC.hs)`](GhcFile(compiler/cmm/PprC.hs) "wikilink")`)`\
`   * If we are generating native code, we invoke the native code generator.  This is another Big Mother (`[`GhcFile(compiler/nativeGen)`](GhcFile(compiler/nativeGen) "wikilink")`).`\
`   * If we are generating LLVM code, we invoke the LLVM code generator. This is a reasonably simple code generator (`[`GhcFile(compiler/llvmGen)`](GhcFile(compiler/llvmGen) "wikilink")`).`

The Diagram
===========

This diagram is also located \[wiki:Commentary/Compiler/HscPipe here\],
so that you can open it in a separate window.

[Image(Commentary/Compiler/HscPipe:HscPipe2.png)](Image(Commentary/Compiler/HscPipe:HscPipe2.png) "wikilink")

Picture of the main compiler pipeline
=====================================

See \[wiki:Commentary/Compiler compiling one module\] for the commentary
on this diagram.

[Image(HscPipe2.png)](Image(HscPipe2.png) "wikilink")

[PageOutline](PageOutline "wikilink")

Video: [Abstract Syntax
Types](http://www.youtube.com/watch?v=lw7kbUvAmK4&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
(1hr03')

The  types
=========

The program is initially parsed into "****", a collection of data types
that describe the full abstract syntax of Haskell. is a pretty big
collection of types: there are 52 data types at last count. Many are
pretty trivial, but a few have a lot of constructors ( has 40).
represents Haskell in its full glory, complete with all syntactic sugar.

The modules live in the
[GhcFile(compiler/hsSyn)](GhcFile(compiler/hsSyn) "wikilink") directory.
Each module declares a related group of declarations, *and* gives their
pretty-printer.

`* `[`GhcFile(compiler/hsSyn/HsSyn.hs)`](GhcFile(compiler/hsSyn/HsSyn.hs) "wikilink")`: the root module.  It exports everything you need, and it's generally what you should import.`\
`* `[`GhcFile(compiler/hsSyn/HsBinds.hs)`](GhcFile(compiler/hsSyn/HsBinds.hs) "wikilink")`: bindings.`\
`* `[`GhcFile(compiler/hsSyn/HsImpExp.hs)`](GhcFile(compiler/hsSyn/HsImpExp.hs) "wikilink")`: imports and exports.`\
`* `[`GhcFile(compiler/hsSyn/HsDecls.hs)`](GhcFile(compiler/hsSyn/HsDecls.hs) "wikilink")`: top-level declarations.`\
`* `[`GhcFile(compiler/hsSyn/HsExpr.hs)`](GhcFile(compiler/hsSyn/HsExpr.hs) "wikilink")`: expressions, match expressions, comprehensions.`\
`* `[`GhcFile(compiler/hsSyn/HsLit.hs)`](GhcFile(compiler/hsSyn/HsLit.hs) "wikilink")`: literals.`\
`* `[`GhcFile(compiler/hsSyn/HsPat.hs)`](GhcFile(compiler/hsSyn/HsPat.hs) "wikilink")`: patterns.`\
`* `[`GhcFile(compiler/hsSyn/HsTypes.hs)`](GhcFile(compiler/hsSyn/HsTypes.hs) "wikilink")`: types.`\
`* `[`GhcFile(compiler/hsSyn/HsUtils.hs)`](GhcFile(compiler/hsSyn/HsUtils.hs) "wikilink")`: utility functions (no data types).`

There is significant mutual recursion between modules, and hence a
couple of files. Look at \[wiki:ModuleDependencies\] to see the
dependencies.

Decorating \`HsSyn\` with type information
------------------------------------------

The type checker adds type information to the syntax tree, otherwise
leaving it as undisturbed as possible. This is done in two ways:

` * Some constructors have a field of type ``, which is just a synonym for ``. For example:`

` An `` represents the explicit list construct in Haskell (e.g. "``"). The parser fills the `` field with an error thunk ``; and the renamer does not touch it.  The typechecker figures out the type, and fills in the value.  So until the type checker, we cannot examine or print the `` fields.`

``  The error thunks mean that we can't conveniently pretty-print the `PostTcType` fields, because the pretty-printer would poke the error thunks when run on pre-typchecked code.  We could have defined `PostTcType` to be `Maybe Type`, but that would have meant unwrapping lots of `Just` constructors, which is messy.  It would be nicer to parameterise `HsSyn` over the `PostTcType` fields.  Thus: ``

` This would be a Good Thing to do.`

` * In a few cases, the typechecker moves from one constructor to another.  Example:`

` The parser and renamer use ``; the typechecker generates a ``. This naming convention is used consistently.`

` * There are a few constructors added by type checker (rather than replacing an input constructor), particularly:`\
`   * ``, in the `` type.`\
`   * ``, in the `` type.`\
` These are invariably to do with type abstraction and application, since Haskell source is implicitly generalized and instantiated, whereas GHC's intermediate form is explicitly generalized and instantiated.`

Source Locations
----------------

\`HsSyn\` makes heavy use of the \`Located\` type
([GhcFile(compiler/basicTypes/SrcLoc.hs)](GhcFile(compiler/basicTypes/SrcLoc.hs) "wikilink")):
A \`Located t\` is just a pair of a \`SrcSpan\` (which describes the
source location of \`t\`) and a syntax tree \`t\`. The module \`SrcLoc\`
defines two other types:

``  * `SrcLoc` specifies a particular source location: (filename, line number, character position) ``\
``  * `SrcSpan` specifes a range of source locations: (filename, start line number and character position, end line number and character position) ``

More details in
[GhcFile(compiler/basicTypes/SrcLoc.hs)](GhcFile(compiler/basicTypes/SrcLoc.hs) "wikilink").

Naming convention within the code: "\`LHs\`" means located Haskell, e.g.

Interface files
===============

An **interface file** supports separate compilation by recording the
information gained by compiling in its interface file . Morally
speaking, the interface file is part of the object file ; it's like a
super symbol-table for .

Interface files are kept in binary, GHC-specific format. The format of
these files changes with each GHC release, but not with patch-level
releases. The contents of the interface file is, however, completely
independent of the back end you are using (\`-fviaC\`, \`-fasm\`,
\`-fcmm\` etc).

Although interface files are kept in binary format, you can print them
in human-readable form using the command: This textual format is not
particularly designed for machine parsing. Doing so might be possible,
but if you want to read GHC interface files you are almost certainly
better off using the \[wiki:Commentary/Compiler/API GHC API\] to do so.
If you are wondering how some particular language feature is represented
in the interface file, this command is really useful! Cross-reference
its output with the \`Outputable\` instance defined in
[GhcFile(compiler/iface/LoadIface.hs)](GhcFile(compiler/iface/LoadIface.hs) "wikilink")

Here are some of the things stored in an interface file

`* The version of GHC used to compile the module, as well as the compilation way and other knick-knacks`\
`* A list of what `` exports.`\
`* The types of exported functions, definition of exported types, and so on.`\
`* Version information, used to drive the [wiki:Commentary/Compiler/RecompilationAvoidance recompilation checker].`\
`* The strictness, arity, and unfolding of exported functions.  This is crucial for cross-module optimisation; but it is only included when you compile with ``.`

The contents of an interface file is the result of serialising the ****
family of data types. The data types are in
[GhcFile(compiler/iface/IfaceSyn.lhs)](GhcFile(compiler/iface/IfaceSyn.lhs) "wikilink")
and
[GhcFile(compiler/iface/IfaceType.lhs)](GhcFile(compiler/iface/IfaceType.lhs) "wikilink");
the binary serialisation code is in
[GhcFile(compiler/iface/BinIface.hs)](GhcFile(compiler/iface/BinIface.hs) "wikilink").
The definition of a module interface is the **** data type in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink").

Details of some of the types involved in GHC's representation of Modules
and Interface files can be found \[wiki:Commentary/Compiler/ModuleTypes
here\].

When is an interface file loaded?
---------------------------------

The act of loading an interface file can cause various parts of the
compiler to behave differently; for instance, a type class instance will
only be used if the interface file which defines it was loaded.
Additionally, GHC tries to avoid loading interface files if it can avoid
it, since every loaded interface file requires going to the file system
and parsing the result.

The big situations when we load an interface file:

-   When you import it (either explicitly using an \`import\`, or
    implicitly, e.g. through \`-fimplicit-import-qualified\` in
    GHCi; \`loadSrcInterface\`)
-   When we need to get the type for an identifier (\`loadInterface\`
    in \`importDecl\`)
-   When it is listed as an orphan of an imported module
    (\`loadModuleInterfaces "Loading orphan modules"\`)

We also load interface files in some more obscure situations:

-   When it is used as the backing implementation of a signature
    (\`loadSysInterface\` in \`tcRnSignature\`)
-   When we look up its family instances (\`loadSysInterface\`
    in \`getFamInsts\`)
-   When its information or safety (\`getModuleInterface\`
    in \`hscGetSafe\`)
-   When we an identifier is explicitly used (including a use from
    Template Haskell), we load the interface to check if the identifier
    is deprecated (\`loadInterfaceForName\` in
    \`warnIfDeprecated\`/\`loadInterfaceforName\` in \`rn\_bracket\`)
-   Recompilation checking (\`needInterface\` in \`checkModUsage\`)
-   When we need the fixity for an identifier (\`loadInterfaceForName\`
    in \`lookupFixityRn\`)
-   When we reify a module for Template Haskell
    (\`loadInterfaceForModule\` in \`reifyModule\`)
-   When we use a wired-in type constructor, since otherwise the
    interface file would not be loaded because the compiler already has
    the type for the identifier. (\`Loading instances for
    wired-in things\`)
-   When \`-XParallelArrays\` or \`-fvectorise\` are specified for DPH
    (\`loadModule\` in \`initDs\`)
-   When we load a plugin (\`DynamicLoading\`)
-   To check consistency against the \`hi-boot\` of a module
-   To check the old interface file for recompilation avoidance

Immix Garbage Collector
=======================

In a [Google Summer of Code
project](http://socghop.appspot.com/gsoc/student_project/show/google/gsoc2010/haskell/t127230760695),
[marcot](http://wiki.debian.org/MarcoSilva) started an implementation of
the Immix Garbage Collector in GHC. It's not in a state where it can be
included in GHC yet, but it's functional, don't have known bugs and gets
better results than the default GC in the
[nofib](http://www.dcs.gla.ac.uk/fp/software/ghc/nofib.html) suite. On
the other hand, it gets worse results than the default GC for the
nofib/gc suite. The implementation was reported on these blog posts:
[1](http://marcotmarcot.wordpress.com/2010/05/17/google-summer-of-code-weekly-report-1/)
[3](http://marcotmarcot.wordpress.com/2010/05/31/summer-of-code-weekly-report-3/)
[4](http://marcotmarcot.wordpress.com/2010/06/04/summer-of-code-weekly-report-4/)
[5](http://marcotmarcot.wordpress.com/2010/06/15/summer-of-code-weekly-report-5/)
[6](http://marcotmarcot.wordpress.com/2010/06/18/immix-on-ghc-summer-of-code-weekly-report-6/)
[7](http://marcotmarcot.wordpress.com/2010/06/29/immix-on-ghc-summer-of-code-weekly-report-7/)
[8](http://marcotmarcot.wordpress.com/2010/07/05/immix-on-ghc-summer-of-code-weekly-report-8/)
[9](http://marcotmarcot.wordpress.com/2010/07/07/immix-on-ghc-summer-of-code-weekly-report-9/)
[10](http://marcotmarcot.wordpress.com/2010/07/21/immix-on-ghc-summer-of-code-weekly-report-10/)
[11](http://marcotmarcot.wordpress.com/2010/08/10/immix-on-ghc-summer-of-code-report-11/)
[12](http://marcotmarcot.wordpress.com/2010/08/13/immix-on-ghc-summer-of-code-report-12-debconf-debian-day-bh/)

The patches
===========

There are [some patches
available](http://people.debian.org/~marcot/immix/).

The main patch
--------------

`* `[`Generated` `with` `darcs` `diff`
`-u`](http://people.debian.org/~marcot/immix/immix.patch)\
`* `[`Darcs`
`bundle`](http://people.debian.org/~marcot/immix/immix.dpatch)

This patch includes the basic implementation of Immix. It's tested, and
has no known bugs. In [the
measurements](http://people.debian.org/~marcot/immix/log.tar.gz), it has
shown these results:

|| || **Runtime** || **Memory used** || || **nofib** || -2.9% || -1.7%
|| || **nofib/gc** || +4.3% || +1.2% ||

Currently, it overwrites the \[wiki:Commentary/Rts/Storage/GC/Sweeping
mark/sweep algorithm\]. It uses the same mark bits as
\[wiki:Commentary/Rts/Storage/GC/Marking mark/compact and mark/sweep\],
but consider these bits in groups of 32 or 64, depending on the
architecture used, which are called lines. It creates a list of free
lines for each
[generation](http://hackage.haskell.org/trac/ghc/wiki/Commentary/Rts/Storage/GC/Aging),
and allocates on them when possible.

As only the first part of each object in memory is marked in the
\[wiki:Commentary/Rts/Storage/GC/Marking bitmap\], it skips the first
free line for each group of subsequent lines, because it's possible that
an object that starts in the previous line is using part of it. Also, it
doesn't deal with \[wiki:Commentary/Rts/Storage/BlockAlloc blocks\] that
objects bigger than the size of a line, called medium sized objects,
marked with \`BF\_MEDIUM\`.

The mark stack is used to ensure that the objects allocated on lines get
scavenged.

Line before inscreasing block size
----------------------------------

`* `[`Generated` `with` `darcs` `diff`
`-u`](http://people.debian.org/~marcot/immix/order.patch)\
`* `[`Darcs`
`bundle`](http://people.debian.org/~marcot/immix/order.dpatch)

Before the implementation of Immix, the code in todo\_block\_full did
the following:

`1. Try to increase the block size.`\
`2. If it could not be increased, get a new block.`

With Immix, it turned to:

`1. If we were allocating in a block, try to increase the block size.`\
`2. If it could not be increased, search for a line.`\
`3. If there're no free lines, get a new block.`

Another possibility for it is:

`1. Search for a line.`\
`2. If there are no free lines `**`and`**` we were allocating in a block, try to increase the block.`\
`3. If it could not be increased, get a new block.`

Basically, this swaps 1 and 2, making it prefer allocating on lines than
increasing the block size. In the measurements done so far, it has not
shown significative improvements over the way the code is now, so I'll
keep it here to benchmark again when another thing changes, like:

Allocate in lines in minor GCs
------------------------------

`* `[`Generated` `with` `darcs` `diff`
`-u`](http://people.debian.org/~marcot/immix/minor.patch)\
`* `[`Darcs`
`bundle`](http://people.debian.org/~marcot/immix/minor.dpatch)

This small patch makes it possible to allocate on lines during minor
GCs, removing the check about being in a major GC for the search for
lines and for the creating of the mark stack. Maybe it shouldn't be so
small, because it's not working. The code is being debugged, and
possibly there will be a fix soon.

Remove partial list
-------------------

With the allocation on lines, it's possible not to allocate on partially
full blocks. By making all blocks full (with possibly free lines),
there'll be no need to use the list of partial blocks. This is not done
yet.

To do
=====

`* Make it faster and use less memory than the default GC for all benchmarks`\
`* Correct "Allocate in lines in minor GCs"`\
`* Implement and bechmark "Remove partial lists"`

[PageOutline](PageOutline "wikilink")

GHC Source Tree Roadmap: includes/
==================================

This directory contains C header files that are included in a GHC
distribution. The headers fall into several categories.

External APIs
-------------

These are header files that define an external API to the RTS that can
be used by client code. These interfaces are intended to be relatively
stable:

`[source:includes/HsFFI.h HsFFI.h]::`\
` The external FFI api, as required by the FFI spec`

`[source:includes/RtsAPI.h RtsAPI.h]::`\
` The API for calling into the RTS.  Used by the implementation`\
``  of `foreign export` calls, but may also be used by external ``\
` clients.`

`[source:includes/Rts.h Rts.h]::`\
` This header file defines everything that is visible`\
``  externally to the RTS.  It includes `Stg.h` and everything ``\
``  in the `rts` subdirectory. ``

Derived Constants
-----------------

The canonical definition of certain structures are in C header files.
For example, the layout of closures and info tables are defined in the
headers \[source:includes/rts/storage/Closures.h Closures.h\] and
\[source:includes/rts/storage/InfoTables.h InfoTables.h\] respectivesly.
How do we get the information about the layout of these structures to
the parts of the system that are not written in C, such as the compiler
itself, or the C-- code in the RTS?

Our solution is the Haskell program in
\[source:utils/deriveConstants/DeriveConstants.hs\]. It determines the
sizes and fields offsets from the C header files by invoking the C
compiler for the target platform, and then looking at the resulting
object file (we can't *run* the code generated by the target C compiler,
because this is the host platform).

The !DeriveConstants program generates a few header files, notably
\`includes/dist-derivedconstants/header/DerivedConstants.h\`, which
contains C \`\#define\`s for each of the derived constants; this file is
used by C-- code in the RTS. It also generates a few files of Haskell
code which are included into GHC itself, in the \`DynFlags\` module.

Used when compiling via C
-------------------------

These header files are \`\#included\` into the \`.hc\` file generated by
GHC when it compiles Haskell code to C. They are also \`\#included\` by
\`Rts.h\`, so the definitions from these files are shared by the RTS
code.

These days the amount of stuff included this way is kept to a minimum.
In particular, there are no function prototypes: all calls to C
functions from \`.hc\` files are given types at the call site.

`[source:includes/Stg.h Stg.h]::`\
``  The top of the hierarchy is `Stg.h`, which includes everything ``\
``  required by `.hc` code.  Most files `#included` by `Stg.h` are in the ``\
``  `stg` subdirectory. ``

`[source:includes/ghcconfig.h ghcconfig.h]::`\
``  Configuration info derived by the `configure` script. ``\
`[source:includes/MachDeps.h MachDeps.h]::`\
``  Sizes of various basic types (should be in the `stg` subdirectory, ``\
` but left here for backwards-compatibility reasons).`\
`[source:includes/stg/DLL.h stg/DLL.h]::`\
` Stuff related to Windows DLLs.`\
`[source:includes/stg/MachRegs.h stg/MachRegs.h]::`\
` Global register assignments for this processor.`\
`[source:includes/stg/MiscClosures.h stg/MiscClosures.h]::`\
` Declarations for closures & info tables built-in to the RTS`\
`[source:includes/stg/Regs.h stg/Regs.h]::`\
` "registers" in the virtual machine.`\
`[source:includes/stg/SMP.h stg/SMP.h]::`\
` Atomic memory operations for SMP support`\
`[source:includes/stg/Ticky.h stg/Ticky.h]::`\
` Declarations for ticky-ticky counters`\
`[source:includes/stg/Types.h stg/Types.h]::`\
``  Basic types specific to the virtual machine (eg. `StgWord`). ``

The RTS external APIs
---------------------

The header \[source:includes/Rts.h Rts.h\] includes all the headers
below the \`rts\` subdirectory, which together define the RTS external
API. Virtually all RTS code \`\#includes\` \`Rts.h\`.

The rts header files are divided into a few directories:

`* [source:includes/rts includes/rts]: Most of`\
`  the external RTS APIs, in separate header files per-subsystem`

`* [source:includes/rts/storage includes/rts/storage]: Definitions of the layout of heap and stack`\
`  objects, info tables, structures that define memory areas managed`\
`  by the GC, and memory management APIs.`

`* [source:includes/rts/prof includes/rts/prof]:`\
`  Interfaces and definitions for profiling.`

Included into C-- (\`.cmm\`) code
---------------------------------

`[source:includes/Cmm.h Cmm.h]::`\
``  included into `.cmm` source only; provides useful macros for writing ``\
` low-level C-- code for GHC.`

[PageOutline](PageOutline "wikilink")

Installing & Using the LLVM Back-end
====================================

Installing
----------

The LLVM backend is now included in GHC HEAD. Just grab the git HEAD
version of GHC and build it. The backend now also supports all modes
that GHC can be built in so you shouldn't need to change your build.mk
file either.

For instructions on building GHC go
[here](http://hackage.haskell.org/trac/ghc/wiki/Building)

LLVM Support
------------

The LLVM backend only supports LLVM version **2.7** or later. Problems
with LLVM &gt;= 2.9 and GHC 7.0.3 currently exist (see bug \#5103). GHC
7.2 and later works fine with LLVM &gt;= 2.9.

Simply install GHC and make sure the various llvm tools (opt, llc) are
available on your path.

Using
-----

Once built you can check that you have the LLVM backend GHC will support
these extra options:

` * `*`-fllvm`*` - Compile code using the llvm backend`\
` * `*`-pgmlo`*` - The program to use as the llvm optimiser`\
` * `*`-pgmlc`*` - The program to use as the llvm compiler`\
` * `*`-optlo`*` - Extra options to pass to the llvm optimiser`\
` * `*`-optlc`*` - Extra options to pass to the llvm compiler`\
` * `*`-ddump-llvm`*` - Dumps the llvm IR while compiling`\
` * `*`-keep-llvm-files`*` - Keep a copy of the llvm intermediate file around`

Supported Platforms & Correctness
---------------------------------

`* Linux x86-32/x86-64: Currently well supported. The back-end can pass the test suite and build a working version of GHC (bootstrap test).`\
`* Windows x86-32: Currently well supported. The back-end can pass the test suite and build a working version of GHC (bootstrap test).`\
`* Mac OS X 10.5/10.6 (x86-32/x86-64): Currently well supported. The back-end can pass the test suite and bootstrap GHC. OS X has caused a lot more problems then Linux or Windows and does a few things slightly differently then them. It is quite stable these days though.`\
`* ARM: Work is currently progressing to fully support GHC using the LLVM backend on ARM. You can see a blog with info about this `[`here`](http://ghcarm.wordpress.com/)`.`\
`* Other platforms haven't been tested at all.`

Shared Libraries
----------------

Shared libraries are supported on Linux x64 and Mac OSX x64. Other
platforms aren't supported.

Performance
-----------

(All done on linux/x86-32)

A quick summary of the results are that for the 'nofib' benchmark suite,
the LLVM code generator was 3.8% slower than the NCG (the C code
generator was 6.9% slower than the NCG). The DPH project includes a
benchmark suite which I (David Terei) also ran and for this type of code
using the LLVM back-end shortened the runtime by an average of 25%
compared to the NCG. Also, while not included in my thesis paper as I
ran out of time, I did do some benchmarking with the 'nobench' benchmark
suite. It gave performance ratios for the back-ends of around:

||NCG || 1.11|| ||C || 1.05|| ||LLVM || 1.14||

A nice demonstration of the improvements the LLVM back-end can bring to
some code though can be see at
<http://donsbot.wordpress.com/2010/02/21/smoking-fast-haskell-code-using-ghcs-new-llvm-codegen/>

[PageOutline](PageOutline "wikilink")

GHC Commentary: Libraries/Integer
=================================

GHC is set up to allow different implementations of the \`Integer\` type
to be chosen at build time.

Selecting an Integer implementation
-----------------------------------

You can select which implementation of Integer is used by defining
\`INTEGER\_LIBRARY\` in \`mk/build.mk\`. This tells the build system to
build the library in \`libraries/\$(INTEGER\_LIBRARY)\`, and the
\`cIntegerLibrary\` and \`cIntegerLibraryType\` values in \`Config.hs\`
are defined accordingly.

The default value is \`integer-gmp\`, which uses the [GNU Multiple
Precision Arithmetic Library (GMP)](http://gmplib.org/) to define the
Integer type and its operations.

The other implementation currently available is \`integer-simple\`,
which uses a simple (but slow, for larger Integers) pure Haskell
implementation.

The Integer interface
---------------------

All Integer implementations should export the same set of types and
functions from \`GHC.Integer\` (within whatever \`integer\` package you
are using). These exports are used by the \`base\` package However, all
of these types and functions must actually be defined in
\`GHC.Integer.Type\`, so that GHC knows where to find them.
Specifically, the interface is this:

How Integer is handled inside GHC
---------------------------------

`* `**`Front`
`end`**`` .  Integers are represented using the `HsInteger` constructor of `HsLit` for the early phases of compilation (e.g. type checking) ``

`* `**`Core`**`` .  In `Core` representation, an integer literal is represented by the `LitInteger` constructor of the `Literal` type.  ``

`` While `Integer`s aren't "machine literals" like the other `Core` `Literal` constructors, it is more convenient when writing constant folding RULES to pretend that they are literals rather than having to understand their concrete representation. (Especially as the concrete representation varies from package to package.) We also carry around a `Type`, representing the `Integer` type, in the constructor, as we need access to it in a few functions (e.g. `literalType`). ``

`* `**`Constant`
`folding`**`` .  There are many constant-folding optimisations for `Integer` expressed as built-in rules in  ``[`GhcFile(compiler/prelude/PrelRules.lhs)`](GhcFile(compiler/prelude/PrelRules.lhs) "wikilink")`` ; look at `builtinIntegerRules`.  All of the types and functions in the `Integer` interface have built-in names, e.g. `plusIntegerName`, defined in  ``[`GhcFile(compiler/prelude/PrelNames.lhs)`](GhcFile(compiler/prelude/PrelNames.lhs) "wikilink")``  and included in `basicKnownKeyNames`. This allows us to match on all of the functions in `builtinIntegerRules` in  ``[`GhcFile(compiler/prelude/PrelRules.lhs)`](GhcFile(compiler/prelude/PrelRules.lhs) "wikilink")`` , so we can constant-fold Integer expressions. An important thing about constant folding of Integer divisions is that they depend on inlining. Here's a fragment of `Integral Integer` instance definition from `libraries/base/GHC/Real.lhs`: ``

`` Constant folding rules for divisions are defined for `quotInteger` and other division functions from `integer-gmp` library. If `quot` was not inlined constant folding rules would not fire. The rules would also not fire if call to `quotInteger` was inlined, but this does not happen because it is marked with NOINLINE pragma - see below. ``

`* `**`Converting` `between` `Int` `and`
`Integer`**`` .  It's quite commonly the case that, after some inlining, we get something like `integerToInt (intToInteger i)`, which converts an `Int` to an `Integer` and back.  This  ``*`must`*``  optimise away (see #5767).  We do this by requiring that the `integer` package exposes ``

`` Now we can define `intToInteger` (or, more precisely, the `toInteger` method of the `Integral Int` instance in `GHC.Real` ) thus ``

`` And we have a RULE for `integerToInt (smallInteger i)`. ``

`* `**`Representing`
`integers`**`` .  We stick to the `LitInteger` representation (which hides the concrete representation) as late as possible in the compiler.   In particular, it's important that the `LitInteger` representation is used in unfoldings in interface files, so that constant folding can happen on expressions that get inlined.   ``

`` We finally convert `LitInteger` to a proper core representation of Integer in  ``[`GhcFile(compiler/coreSyn/CorePrep.lhs)`](GhcFile(compiler/coreSyn/CorePrep.lhs) "wikilink")`` , which looks up the Id for `mkInteger` and uses it to build an expression like `mkInteger True [123, 456]` (where the `Bool` represents the sign, and the list of `Int`s are 31 bit chunks of the absolute value from lowest to highest). ``

`` However, there is a special case for `Integer`s that are within the range of `Int` when the `integer-gmp` implementation is being used; in that case, we use the `S#` constructor (via `integerGmpSDataCon` in  ``[`GhcFile(compiler/prelude/TysWiredIn.lhs)`](GhcFile(compiler/prelude/TysWiredIn.lhs) "wikilink")`) to break the abstraction and directly create the datastructure.`

`* `**`Don't` `inline` `integer`
`functions`**`` .  Most of the functions in the Integer implementation in the `integer` package are marked `NOINLINE`. For example in `integer-gmp` we have ``

`` Not only is this a big function to inline, but inlining it typically does no good because the representation of literals is abstact, so no pattern-matching cancellation happens.  And even if you have `(a+b+c)`, the conditionals mean that no cancellation happens, or you get an exponential code explosion! ``

An Integrated Code Generator for GHC
====================================

We propose reworking GHC's back end into an **Integrated Code
Generator**, which will widen the interface between machine-independent
and machine-dependent parts of the back end. We wish to **dissolve the
barrier** between the current machine-independent transformations (CPS
conversion, stack layout, etc) and the native-code generators
(instruction selection, calling conventions, register allocation --
including spilling to the C stack, etc). The goal is instead to have a
code generator that **integrates both machine-independent and
machine-dependent components**, which will interact through wide but
well-specified interfaces. From this refactoring we expect the following
benefits:

`* `**`The` `back` `end` `will` `be` `simpler`
`overall`**`, primarily because the`\
`  refactoring will reduce or eliminate duplication of code`

`* `**`Complexity` `will` `be`
`isolated`**` in two modules with well-defined`\
`  interfaces: a dataflow engine and a register allocator`

`* `**`GHC` `will` `generate` `better` `machine`
`code`**`, primarily because`\
`  important decisions about register usage will be made at a later`\
`  stage of translation and will exploit knowledge of the actual`\
`  target machine. `

Design elements
---------------

The important elements of our design are as follows:

` 0. Build two big hammers, and hit as many nails as possible.  (The big hammers are the `**`dataflow`
`optimization` `engine`**` and a `**`coalescing` `register`
`allocator.`**` For more on their uses, see our [wiki:Commentary/Compiler/IntegratedCodeGen#Designphilosophy design philosophy].)  The hammer itself may be big and complicated, but `**`using`
`a` `big` `hammer` `should` `be`
`easy`**` and should give easily predictable results.`\
` 0. Load all back ends into every instance of the compiler, and `**`treat`
`every` `compilation` `as` `a`
`cross-compilation.`**`  Despite having been used in production compilers for at least twenty years, this technique is still seen as somewhat unorthodox, but it removes many ``s and saves significant complexity at compiler-configuration time. Removing ``s also mitigates problems with  validating the compiler under different build configurations.`

Design philosophy
-----------------

State-of-the art dataflow optimization and register allocation both
require complex implementations. We live with this complexity because
**creating new clients is easy.**

`* `**`Dataflow` `optimization:`**` We can define a new`\
`  optimization simply by defining a lattice of dataflow facts (akin`\
`  to a specialized logic) and then writing the dataflow-transfer`\
`  functions found in compiler textbooks.   Handing these functions to`\
`  the dataflow engine produces a new optimization that is not only`\
`  useful on its own, but that can easily be composed with other`\
`  optimizations to create an integrated "superoptimization" that is`\
`  strictly more powerful than any sequence of individual optimizations,`\
`  no matter how many times they are re-run.`\
`  The dataflow engine is based on `\
`  `[`(Lerner,` `Grove,` `and` `Chambers`
`2002)`](http://citeseer.ist.psu.edu/old/lerner01composing.html)`;`\
`  you can find a functional implementation of the dataflow engine presented in`\
`  `[`(Ramsey` `and` `Dias`
`2005)`](http://www.cs.tufts.edu/~nr/pubs/zipcfg-abstract.html)`.`

`* `**`Coalescing` `register`
`allocator:`**` The back end can use fresh temporaries and register-register moves`\
`  with abandon, knowing that a state-of-the-art register allocator`\
`  will eliminate almost all move instructions.`

`* `**`Back`
`ends:`**` Our ultimate goal is to make adding a new back end easy as well.`\
`  In the long run, we wish to apply John Dias's dissertation work to GHC.`\
`  In the short run, however, we`\
`  think it more sensible to represent each target-machine instruction`\
`  set with an algebraic datatype.  We propose to use type classes to`\
`  define common functions such as identifying the registers read and`\
`  written by each instruction.`

Proposed compilation pipeline
-----------------------------

`0. Convert from `` to an control flow graph ``:`\
`0. Instruction selection:`\
`0. Optimise:`\
`0. Proc-point analysis, and transformation`\
`0. Register allocation`\
`0. Stack layout`\
`0. Tidy up`

### Convert from STG to control flow graph

Convert from to an control flow graph
([GhcFile(compiler/cmm/ZipCfg.hs)](GhcFile(compiler/cmm/ZipCfg.hs) "wikilink"),
[GhcFile(compiler/cmm/ZipCfgCmmRep.hs)](GhcFile(compiler/cmm/ZipCfgCmmRep.hs) "wikilink")).
This step is Simon PJ's "new code generator" from September 2007. This
conversion may introduce new variables, stack slots, and compile-time
constants.

`  * Implements calling conventions for call, jump, and return instructions: all parameter passing is turned into data-movement instructions (register-to-register move, load, or store), and stack-pointer adjustments are inserted. After this point, calls, returns, and jumps are just control-transfer instructions -- the parameter passing has been compiled away.  `\
`  * How do we refer to locations on the stack when we haven't laid it out yet? The compiler names a stack slot using the idea of a "late compile-time constant," which is just a symbolic constant that will be replaced with an actual stack offset when the stack layout is chosen.One departure from the old code generator is that `**`we`
`do` `not` `build` `a` `abstract-syntax`
`tree;`**` instead we go straight to a control-flow graph.`

In practice, we first generate an "abstract control flow graph",
\`CmmAGraph\`, which makes the business of generating fresh \`BlockId\`s
more convenient, and convert that to a \`CmmGraph\`. The former is
convenient for *construction* but cannot be analysed; the latter is
concrete, and can be analyzed, transformed, and optimized.

### Instruction selection

Instruction selection: each and node in the control-flow graph is
replaced with a new graph in which the nodes are machine instructions.
The type represents computational machine instructions; the type
represents control-transfer instructions. The choice of representation
is up to the author of the back end, but for continuity with the
existing native code generators, we expect to begin by using algebraic
data types inspired by the existing definitions in
[GhcFile(compiler/nativeGen/MachInstrs.hs)](GhcFile(compiler/nativeGen/MachInstrs.hs) "wikilink").

Note that the graph still contains:

`* `**`Variables`**` (ie local register that are not yet mapped to particular machine registers)`\
`* `**`Stack-slot` `addressing`
`modes`**`, which include late-bound compile-time constants, such as the offset in the frame of the a variable spill location, or !BlockId stack-top-on-entry.`

The invariant is that each node could be done by one machine
instruction, provided each \`LocalReg\` maps to a (suitable) physical
register; and an instruction involving a stack-slot can cope with
(Sp+n).

An **extremely important distinction** from the existing code is that we
plan to eliminate and instead provide multiple datatypes, e.g., in , , ,
and so on.

Similarly, we expect a an instruction selector for *each* back end, so
for example, we might have a transformation that maps (with variables,
stack slots, and compile-time constants) (with variables, stack slots,
and compile-time constants).

We expect to **abstract away from the details of these representations**
by borrowing some abstractions from [Machine
SUIF](http://www.eecs.harvard.edu/hube/software/nci/overview.html). In
the longer term we would like to support RTL-based representations such
as are used in gcc, vpo and Quick C--. What this means is that
\`I386.Middle\` (etc) is an abstract type, an instance of type class
that supports the functions that the rest of the pipeline needs. For
example: This allows us to **make code improvements
machine-independent**, by using machine-dependent functions to capture
the semantics of instructions. Figuring out precisely what the interface
should be is a key step. For example, to support copy propagation we
might want an operation Similarly, to support peephole optimsation (eg
transform \`x = y+2; p = bits32\[x\]\` to \`p = bits32\[y+2\]\`) we
might want something like The \`substExprs\` operation returns a
\`Just\` iff a substitution took place.

Interfaces like these would require the machine-specific abstract type
\`i\` to contain enough information to reconstruct a \`LocalReg\` or
\`CmmExpr\`. Later one, we'll need to construct SRTs too, so we must
continue to track pointer-hood.

One possible implementation for \`I386\` or \`Sparc\` would be to use a
generic RTL representation, together with a recogniser to maintain the
machine invariant. Our initial idea, though, is that is an
implementation choice. It's still possible that a machine-independent
optimisation could take advantage of the representation being an RTL.
For example, we could provide a function in the \`Instr\` class which is
particularly cheap for architectures that do use \`RTL\` as the
representation type.

### Optimisation

Optimise the code. (with variables, stack slots, and compile-time
constants) (with variables, stack slots, and compile-time constants),
such as

`  * Branch chain elimination.`\
`  * Remove unreachable blocks (dead code).`\
`  * Constant propagation.`\
`  * Copy propagation.`\
`  * Lazy code motion (hoisting, sinking, partial redundancy elimination).`\
`  * Block concatenation.  branch to K; and this is the only use of K.  `\
`  * Common Block Elimination (like CSE). This essentially implements the Adams optimisation, we believe.`\
`  * Consider (sometime): block duplication.  branch to K; and K is a short block.  Branch chain elimination is just a special case of this.`\
`  * Peephole optimisation.  The difficulty of implementing a good peephole optimizer varies greatly with the representation of instructions.  We propose to postpone serious work on peephole optimization until we have a back end capable of representing machine instructions as RTLs, which makes peephole optimization trivial.`

### Proc-point analysis

 Both input and output still have variables and stack-slot addressing
modes.

` * Proc points are found, and the appropriate control-transfer instructions are inserted.`\
` * Why so early(before register allocation, stack layout)? Depending on the back end (think of C as the worst case), the proc-point analysis might have to satisfy some horrible calling convention. We want to make these requirements explicit before we get to the register allocator.  We also want to `**`exploit`
`the` `register`
`allocator`**` to make the best possible decisions about `*`which`
`live` `variables` `(if` `any)` `should` `be` `in` `registers` `at` `a`
`proc` `point`*`.`

### Register allocation

Register allocation replaces variable references with machine register
and stack slots. This may introduce spills and reloads (to account for
register shortage), which which is why we may get new stack-slot
references.

That is, register allocation takes (with variables, stack slots) (with
stack slots only). No more variables!

We no longer need to spill to the C stack, because we have fully
allocated everything to machine registers.

### Stack layout

Stack Layout: (with stack slots, and compile-time constants)

` * Choose a stack layout.`\
` * Replace references to stack slots with addresses on the stack.`\
` * Replace compile-time constants with offsets into the stack.`

No more stack-slot references.

### Tidy up

`0. Proc-point splitting: `` `\
` * Each proc point gets its own procedure.`\
`0. Code layout: `\
` * A reverse postorder depth-first traversal simultaneously converts the graph to sequential code and converts each instruction into an assembly-code string: `**`Assembly`
`code` `ahoy`**`!`

Machine-dependence
------------------

A key property of the design is that the scopes of machine-dependent
code and machine-dependent static types are limited as much as possible:

` 0. The representation of machine instructions may be machine-dependent (algebraic data type), or we may use a machine-independent representation that satisfies a machine-dependent dynamic invariant (RTLs).   The back end should be designed in such a way that most passes don't know the difference; we intend to borrow heavily from Machine SUIF.  To define the interface used to conceal the difference, Machine SUIF uses C++ classes; we will use Haskell's type classes.`\
` 0. Instruction selection is necessarily machine-dependent, and moreover, it must know the representation of machine instructions`\
` 0. Most of the optimizer need not know the representation of machine instructions.`\
` 0. Other passes, including register allocation, stack layout, and so on, should be completely machine-independent.`\
` 0. RTLs are not a new representation; they are a trivial extension of existing `` representations.`

GHC Commentary: The byte-code interpreter and dynamic linker
============================================================

Linker
------

The linker lives in \`rts/Linker.c\` and is responsible for handling
runtime loading of code into a Haskell process. This is something of a
big blob of unpleasant code, and see DynamicGhcPrograms for information
about efforts to reduce our dependence on this linker.

Nevertheless, GHC's linker certainly adds functionality, and this has
been enough to earn its keep (for now). In particular, the linker knows
how to \*\*relocate static libraries\*\* (e.g. \`.o\` and \`.a\`
libraries). This is a pretty rare feature to find: ordinarily, libraries
that are to be loaded at runtime are compiled as position independent
code (-fPIC), which allows the same physical code pages to be shared
between processes, reducing physical memory usage. At runtime, GHC
rewrites the relocations, meaning that the resulting page cannot be
shared across processes, but that the result is just as efficient as if
the code had been statically linked to begin with.

Implementation of the linker cuts three axes: object file format (ELF,
Mach-O, PEi386), operating system (Linux, MingW, Darwin, etc), and
architecture (i386, x86\_64, powerpc, arm), and there are corresponding
sets of macros for fiddling with each (\`OBJFORMAT\_\*\`,
\`\*\_HOST\_OS\` and \`\*\_HOST\_ARCH\`). Are large part of the
unpleasantness of the current linker is the fact that all of these
different concerns are jumbled in one file; refactoring these out to
separate files would be a very nice service.

(write more here)

Bytecode Interpreter
--------------------

------------------------------------------------------------------------

CategoryStub

The I/O Manager
===============

This page describes the internals of the I/O manager, the latest version
of which can be found in
[GHC.Event](http://hackage.haskell.org/packages/archive/base/latest/doc/html/GHC-Event.html).
The I/O manager's job is to to provide a blocking I/O API to the user
without forcing the RTS to create one operating system thread per
Haskell thread. We here focus on the *threaded* RTS on non-Windows
platforms.

ezyang: **WARNING: some of this information may be out of date**

The RTS keeps a global list of pending events, unsuprising called
\`pendingEvents\`, containing a elements of the following data type:

When a thread wants to read from a file descriptor \`fd\` it calls
\`threadWaitRead\` which in turn calls \`waitForReadEvent\`.

\`waitForReadEvent\` creates a new \`MVar\`, adds it to
\`pendingEvents\` and finally blocks on it. \`pendingEvents\` gets read
by the I/O manager thread which runs the event loop, in GHC called
\`service\_loop\`. It roughly performs these steps:

`` 1. Pick up new I/O requests from `pendingRequests` and set the variable to the empty list. ``\
`` 2. Create data structures appropriate for calling `select`. ``\
`` 3. For each `Read` request in `pendingEvents` check if the file descriptor is in the ready set returned by `select`. If so perform a `putMVar` on the `MVar` associated with that request to wake up the blocked thread. ``\
`4. Repeat from step 1.`

Key data types
==============

The key to understanding GHC is to understand its key data types. There
are pages describing many of them here (please add new pages!). The
diagram below shows their inter-dependencies.

`* [wiki:Commentary/Compiler/HsSynType The source language: HsSyn] `\
`* [wiki:Commentary/Compiler/RdrNameType RdrNames, Modules, and OccNames]`\
`* [wiki:Commentary/Compiler/ModuleTypes ModIface, ModDetails, ModGuts]`\
`* [wiki:Commentary/Compiler/Unique Uniques]: Not drawn in the diagram, because nearly everything depends on Uniques.`\
`* [wiki:Commentary/Compiler/NameType Names]`\
`* [wiki:Commentary/Compiler/EntityTypes Entities]: variables, type constructors, data constructors, and classes.`\
`* Types: [wiki:Commentary/Compiler/TypeType Type and Kind], [wiki:Commentary/Compiler/FC equality types and coercions]`\
`* [wiki:Commentary/Compiler/CoreSynType The core language]`\
`* [wiki:Commentary/Compiler/StgSynType The STG language]`\
`* [wiki:Commentary/Compiler/CmmType The Cmm language]`\
`* [wiki:Commentary/Compiler/BackEndTypes Back end types]`

[Image(types.png)](Image(types.png) "wikilink")

Kinds
=====

Kinds classify types. So for example: The base kinds are these:

`` * "`*`" is the kind of boxed values. Things like `Int` and `Maybe Float` have kind `*`. ``\
`` * "`#`" is the kind of unboxed values. Things like `Int#` have kind `#`. ``\
`* With the advent of [wiki:GhcKinds data type promotion and kind polymorphism] we can have a lot more kinds.`

(Unboxed tuples used to have a distinct kind, but in 2012 we combined
unboxed tuples with other unboxed values in a single kind "\`\#\`".)

Representing kinds
------------------

Kinds are represented by the data type \`Type\` (see
\[wiki:Commentary/Compiler/TypeType\]): Basic kinds are represented
using type constructors, e.g. the kind \`\*\` is represented as where
\`liftedTypeKindTyCon\` is a built-in \`PrimTyCon\`. The arrow type
constructor is used as the arrow kind constructor, e.g. the kind \`\*
-&gt; \*\` is represented internally as It's easy to extract the kind of
a type, or the sort of a kind: The "sort" of a kind is always one of the
sorts: \`TY\` (for kinds that classify normal types) or \`CO\` (for
kinds that classify coercion evidence). The coercion kind, \`T1 :=:
T2\`, is represented by \`PredTy (EqPred T1 T2)\`.

Kind subtyping
--------------

There is a small amount of sub-typing in kinds. Suppose you see \`(t1
-&gt; t2)\`. What kind must \`t1\` and \`t2\` have? It could be \`\*\`
or \`\#\`. So we have a single kind \`OpenKind\`, which is a super-kind
of both, with this simple lattice:

[Image(https://docs.google.com/drawings/pub?id=1M5yBP8iAWTgqdI3oG1UNnYihVlipnvvk2vLInAFxtNM&w=359&h=229)](Image(https://docs.google.com/drawings/pub?id=1M5yBP8iAWTgqdI3oG1UNnYihVlipnvvk2vLInAFxtNM&w=359&h=229) "wikilink")

(You can edit this picture
[here](https://docs.google.com/drawings/d/1M5yBP8iAWTgqdI3oG1UNnYihVlipnvvk2vLInAFxtNM/edit?hl=en_GB).)

Linearity
=========

The solution is to distinguish call demands from product demands.
Consider again: The demands placed on by the first and second call get
bothed together to yield . But this is incorrect. Consider: Here, the
demands placed on by the body of and by the call to in the -body get
bothed together: . Note that this is the same as the demand placed on
above, yet we want to distinguish between the two situations, because in
the first example, the inner lambda in 's rhs is only called once.

The solution is to treat call demands and product demands differently,
and to define the function for call demands to have the same behavior as
. Then in the first example, has demand placed on it, and in the second,
. This is what we want; now, if has demand placed on it, that implies is
always called with two arguments.

Why does this make sense? Consider what it means if we see an example
like: (where is lazy in , and is strict in and ). is used both with
demand (in the call to and with demand (in the call to ). This means
it's perfectly same to strictly evaluate , so when we both together the
two demands, we should get . On the other hand, if a function is
*called* once with one argument and once with two, we don't want to
treat it as a function that's always called with two arguments; we're
only interested in functions that are *always* called with *n* arguments
for a given *n*. Hence, both should behave the same way as lub for call
demands.

Ticky
=====

(NB out-of-date, but maybe historically useful; cf
\[wiki:Debugging/TickyTicky\])

The following code inserts extra fields into closures when ticky is
enabled (and so had to be commented out): in
[GhcFile(compiler/codeGen/CgTicky.hs)](GhcFile(compiler/codeGen/CgTicky.hs) "wikilink").

Other relevant functions: in
[GhcFile(compiler/codeGen/CgTicky.hs)](GhcFile(compiler/codeGen/CgTicky.hs) "wikilink")
(called by in
[GhcFile(compiler/codeGen/CgClosure.lhs)](GhcFile(compiler/codeGen/CgClosure.lhs) "wikilink")).

Argh! I spent days tracking down this bug: in
[GhcFile(compiler/cmm/CLabel.hs)](GhcFile(compiler/cmm/CLabel.hs) "wikilink")
needs to return for labels of type (i.e., labels for ticky counters.) By
default, it was returning , which caused the ticky counter labels to get
declared with the wrong type in the generated C, which caused C compiler
errors.

Declarations for ticky counters
-------------------------------

 spits out C declarations that look like this: Here, is actually an
(this type is declared in
[GhcFile(includes/StgTicky.h)](GhcFile(includes/StgTicky.h) "wikilink")).
The counters get used by in
[GhcFile(rts/Ticky.c)](GhcFile(rts/Ticky.c) "wikilink"), which prints
out the ticky reports. The counter fields are accessed using offsets
defined in
[GhcFile(includes/GHCConstants.h)](GhcFile(includes/GHCConstants.h) "wikilink")
(), which in turn get generated from
[GhcFile(includes/mkDerivedConstants.c)](GhcFile(includes/mkDerivedConstants.c) "wikilink")
(change it and then run in .

<s>Note that the first 3 fields of the counters are 16-bit ints and so
the generated ticky-counter registration code has to reflect that (I
fixed a bug where the first field was getting treated as a 32-bit
int.)</s> I modified the type so that all fields are s, because it seems
that the code generator can't cope with anything else anyway (i.e., in
the declaration above, is an array of s, even though the C type
declaration implies that some fields are halfwords.)

In in
[GhcFile(compiler/codeGen/CgClosure.lhs)](GhcFile(compiler/codeGen/CgClosure.lhs) "wikilink"),
"eager blackholing" was getting employed in the case where ticky was
turned on; this was causing programs to when they wouldn't with ticky
disabled, so I turned that off.

Strictness and let-floating
===========================

We run into the following problem in the nofib benchmark: suppose we
have: where doesn't depend on . Demand analysis says that has a strict
demand placed on it. Later, gets floated to the top level because it
doesn't depend on (in reality it's more complicated because in this case
probably would have gotten floated out before demand analysis, but bear
with me). still has a strict demand signature, which a top-level binding
isn't allowed to have. Currently this manifests itself as an assertion
failure in
[GhcFile(compiler/simplCore/SimplEnv.lhs)](GhcFile(compiler/simplCore/SimplEnv.lhs) "wikilink").

There are two possible easy solutions: don't float out bindings for
strict things, or "both" the demand for a binder with Lazy when its
binding gets floated out. The question is, is it better to do the
let-floating and lose the strictness into or to evaluate something
strictly but lose sharing?

Coercions
=========

When we run into an expression like that we're placing demand on, we
analyze to get , then check whether the depth of is equal to the depth
of or not. This is necessary because we might be casting a function to a
non-function type. So, if and have equal depth, we return as is; if 's
arity is less, we drop the appropriate number of args from ; if 's arity
is less, we add the appropriate number of dummy argument demands to it.

WARN: arity /
=============

dmdTypeDepth rhs\_dmd\_ty && not (exprIsTrivial rhs) =

This warning was happening for (at least) two reasons: - lambdas with a
strict non-call demand placed on them were being handled wrong (see the
first two examples in
\[wiki:Commentary/Compiler/StrictnessAnalysis/Examples\]) - coercions
were being handled wrong, resulting in a demand type with depth 0 being
assigned to an rhs consisting of a cast from/to a function type

Explaining demand transformers
==============================

For those who, like me, are a little slow, this example might go in
section 5.1 of the paper:

(a): (b):

In both (a) and (b), 's rhs places a strict demand on . So if we see:
with a strict demand placed on it, it wouldn't be sound to look at 's
demand signature and say that places a strict demand on under -- because
we don't know whether is like (a) or like (b). This is why when we see a
partial application of , we discard all of the argument information in
's demand type.

Nofib stuff
===========

I've had weird problems with the and commands under MSYS but I think
it's just when running nofib. At some point I wrote down:

TIME needs to be not

and

MSYS does not work, use cygwin

but of \*course\* I no longer remember what I meant.
[PageOutline](PageOutline "wikilink")

GHC Commentary: Libraries
=========================

All GHC build trees contain a set of libraries, called the **Boot
Packages**. These are the libraries that GHC's source code imports.
Obviously you need the boot packages to build GHC at all. The boot
packages are those packages in the file \[source:packages\] that have a
\`-\` in the "tag" column.

The repository structure of a GHC source tree is described in
\[wiki:Repositories\].

You can see exactly which versions of what packages GHC depends on by
looking in \[source:compiler/ghc.cabal.in\]. The versions of the boot
packages (including the \`base\` library) associated with each GHC
release are tabulated in [GHC Boot Library Version
History](wiki:Commentary/Libraries/VersionHistory "wikilink").

Building packages that GHC doesn't depend on
============================================

You can make the build system build extra packages, on which GHC doesn't
strictly depend, by adding them to the \`\$(TOP)/packages\` file, with
an \`extra\` tag. Then set \`BUILD\_EXTRA\_PKGS=YES\` in your
\`mk/build.mk\` file.

It should be exceptional, but you can make the build system provide
per-package compiler flags, by adding some definitions in
\`\$(TOP)/ghc.mk\`, just below the comment

------------------------------------------------------------------------

Classifying boot packages
=========================

A **boot package** is, by definition, a package that can be built by
GHC's build system.

Boot packages can be classified in four different ways:

` * Required vs optional`\
` * Wired-in vs independent`\
` * Zero-boot vs not zero-boot`\
` * Installed vs not installed`

These distinctions are described in the following sub-sections.

Required or optional
--------------------

Most boot packages **required** to build \`ghc-stage2\`, or one of the
supporting utilities such as \`ghc-pkg\`, \`hsc2hs\`, etc.

However a few are **optional**, and are built only

`` * To ensure that they do indeed build cleanly; they are stress tests of GHC.  E.g. `dph` ``\
`* Because they are used in regression tests`

Coupling to GHC
---------------

An important classification of the boot packages is as follows:

`* `**`Wired` `in`
`packages`**``  are totally specific to GHC.  See the list in `compiler/main/Packages.lhs` function `findWiredInPackages`, and c.f. [wiki:Commentary/Compiler/Packages]. At the moment these are: ``\
``   * `ghc-prim` ``\
``   * `integer-gmp`, `integer-simple` ``\
``   * `base` ``\
``   * `template-haskell` ``\
``   * `dph` ``

`* `**`Independent`**``  packages are loosely coupled to GHC, and often maintained by others.  Most boot packages are independent; e.g. `containers`, `binary`, `haskeline` and so on.   ``

Independent libraries may have a master repository somewhere separate
from the GHC repositories. Whenever we release GHC, we ensure that the
installed boot libraries (i.e. that come with GHC) that are also
independent are precisely sync'd with a particular released version of
that library.

Zero-boot packages
------------------

Since GHC's source code imports the boot packages, *even the bootstrap
compiler must have the boot packages available*. (Or, more precisely,
all the types and values that are imported must be available from some
package in the bootstrap compiler; the exact set of packages does not
need to be identical.)

For the most part we simply assume that the bootstrap compiler already
has the boot packages installed. The **Zero-boot Packages** are a set of
packages for which this assumption does not hold. Two reasons dominate:

`` * For certain fast-moving boot packages (notably `Cabal`), we don't want to rely on the user having installed a bang-up-to-date version of the package. ``\
`` * The only packages that we can "assume that the bootstrap compiler already has" are those packages that come with GHC itself; i.e. the installed boot packages.  So non-installed boot packages are also zero-boot packages.  Example: `bin-package-db` or `hoopl`. ``

So we begin the entire build process by installing the zero-boot
packages in the bootstrap compiler. (This installation is purely local
to the build tree.) This is done in \`ghc.mk\` by setting
\`PACKAGES\_STAGE0\` to the list of zero-boot packages; indeed this is
the only way in which zero-boot packages are identified in the build
system.

As time goes on, a Zero-boot package may become an ordinary boot
package, because the bootstrap compiler is expected to have (a
sufficiently up to date) version of the package already. Remember that
we support bootstrapping with two previous versions of GHC.

To find out which packages are currently zero-boot packages, do the
following in a GHC build:

Some Zero-boot packages are **maintained by other people**. In order to
avoid GHC being exposed to day-by-day changes in these packages, we
maintain a "lagging" Git repository for each that we occasionally sync
with the master repository. We never push patches to lagging repository;
rather we push to the master (in discussion with the package
maintainer), and pull the patches into the lagging repo. The current
Zero-boot packages of this kind are:

`` * `Cabal`: we frequently update Cabal and GHC in sync ``\
`` * `binary` (renamed to `ghc-binary` in the 6.12 branch): required by `bin-package-db`. ``

Other Zero-boot packages are **maintained by us**. There is just one Git
repo for each, the master. When we make a GHC release, we simultaneously
tag and release each of these packages. They are:

`` * `hpc` ``\
`` * `extensible-exceptions`: this is a shim that provides an API to older versions of GHC that is compatible with what the current `base` package now exports.  So, unusually, `extensible-exceptions` is a zero-boot package, but not a boot package. ``\
`` * `bin-package-db`: a GHC-specific package that provides binary serialisation of the package database, use by `ghc-pkg` and GHC itself. ``

Installation
------------

When we build a distribution of GHC, it includes at least some
libraries, otherwise it would be utterly useless. Since GHC is part of
the Haskell Platform, any library that is installed with GHC is
necessarily part of the Haskell Platform, so we have to be a bit careful
what we include.

Alas, since the \`ghc\` package (implementing the GHC API) is certainly
an installed package, all the packages on which it depends must also be
installed, and hence willy-nilly become part of the Haskell Platform. In
practice that means that almost all the Boot Packages are installed. In
some cases that is unfortunate. For example, we currently have a special
version of the \`binary\` library, which we don't really expect Haskell
users to use; in this case, we call it \`ghc-binary\`, and informally
discourage its use.

Currently the Boot Packages that are not installed are \`haskeline\`,
\`mtl\`, and \`terminfo\`; these are needed to build the GHC front-end,
but not to build the \`ghc\` *package*.

**QUESTION**: where in the build system is the list of installed
packages defined?

------------------------------------------------------------------------

Boot packages dependencies
==========================

`* At the root of the hierarchy we have `**`` `ghc-prim` ``**`` . As the name implies, this package contains the most primitive types and functions. It only contains a handful of modules, including `GHC.Prim` (which contains `Int#`, `+#`, etc) and `GHC.Bool`, containing the `Bool` datatype.  See "WARNING: pattern matching" below. ``

`` * Above `ghc-prim` are the packages ``\
``   * `integer-gmp` ``\
``   * `integer-simple` ``\
`` The two have the same interface, and only one of the two is used. (When we want to be vague about which one, we call it `integer-impl`.)  They provide a definition of the `Integer` type (on top of the C `gmp` library, or in plain Haskell, respectively). Which functionality is provided in `ghc-prim` is mostly driven by what functionality the `integer-impl` packages need. By default `integer-gmp` is used; to use `integer-simple` define `INTEGER_LIBRARY=integer-simple` in `mk/build.mk`. ``

`  See "WARNING: pattern matching" below.`

`* Next is the `**`` `base` ``**``  package. This contains a large number of modules, many of which are in one big cyclic import knot, mostly due to the `Exception` type. ``

`* On top of base are a number of other, more specialised packages, whose purpose is generally clear from their name. If not, you can get more detail from the descriptions in their Cabal files.  The up-to-date list of packages can be found in the file [source:packages].`

The \`haskell98\`, \`old-time\`, \`old-locale\` and \`random\` packages
are mostly only needed for Haskell 98 support, although \`dph\`
currently uses \`random\` too.

WARNING: Pattern matching in \`ghc-prim\`, \`integer-simple\`, and \`integer-gmp\`
----------------------------------------------------------------------------------

Note that \`ghc-prim\` and \`integer-impl\` are below the dependency
chain from Exception (in \`base\`), which means they must not raise
generate code to raise an exception (it's not enough that this code will
never run). One particularly subtle case of GHC exception-raising code
is in the case of (complete!) pattern matches. Consider the unboxed form
of Integers, which has the constructor S\# or J\#.

GHC will incorrectly generate core that pattern matches against the
second argument twice, the second match being a partial one with (dead)
exception raising code. When compiled with optimizations, the dead code
is eliminated. However, this breaks with -O0, thus: The fix is to
explicitly spell out the constructor in the second and third line, so
that GHC does not generate calls to \`patError\`:

Repositories
============

The list of repository locations has moved to \[wiki:Repositories\].

The LLVM backend
================

David Terei wrote a new code generator for GHC which targets the LLVM
compiler infrastructure. Most of the work was done as part of an honours
thesis at the University of New South Wales under the supervision of
Manuel Chakravarty. It was merged into GHC Head around May of 2010 and
has been included in GHC since the 7.0 release.

Documentation:

`* [wiki:Commentary/Compiler/Backends/LLVM/Installing Installing & Using]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/Design Design & Implementation]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/Mangler LLVM Mangler]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/DevelopmentNotes Bugs & Other Problems]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/GHC_LLVMPorting Porting GHC/LLVM to another platform]`

Work in Progress:

`* [wiki:SIMD SIMD instructions and LLVM]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/Alias Improving Alias Analysis]`

Future Ideas:

`* [wiki:Commentary/Compiler/Backends/LLVM/WIP ToDo List of Sorts]`\
`* [wiki:Commentary/Compiler/Backends/LLVM/ReplacingNCG Replacing the Native Code Generator]`\
`* `[`David` `Terei` `blog` `post` `of` `LLVM-related`
`projects`](http://dterei.blogspot.com/2011/09/ghc-project-for-all.html)

Other information:

`* The `[`thesis`
`paper`](http://www.cse.unsw.edu.au/~pls/thesis/davidt-thesis.pdf)` which offers a detailed performance evaluation, as well as the motivation and design of the back-end.`\
`* `[`Blog`
`post`](http://blog.llvm.org/2010/05/glasgow-haskell-compiler-and-llvm.html)` on the LLVM blog about the backend.`\
`* A more recent `[`paper`](http://www.cse.unsw.edu.au/~chak/papers/TC10.html)` submitted to the Haskell Symposium '10, gives updated design overview and performance numbers.`

Loopification
=============

Loopification is a C-- optimisation pass that turns tail recursion into
proper loops.

Here is a summary of relevant links and tickets

-   [Krzysztof Wos's
    project](http://research.microsoft.com/en-us/um/people/simonpj/tmp/wos-diss-draft.pdf)
    in which he reports great performance improvements by turning tail
    recursion into loops in C--.

<!-- -->

-   Tickets:

` * #8285`\
` * #8793, #11372; see comment 15 of #8793) etc, where it seems that we are missing loopification for a simple IO function`\
` * #8585 concerned getting the loop to start `*`after`*` the stack check`

LLVM Mangler
============

The LLVM backend sadly includes a 'mangler'. This is a Haskell written
program (well pass of GHC) that runs on the assembly code generated by
the LLVM compiler. We do this as there are a few issues with
communicating to LLVM exactly what we want generated as object code and
so, for now, it is easiest to post-process the assembly.

Long term we ideally would submit patches to LLVM and get rid of the
mangler. The work required to do that may be quite high and the patches
needed potentially fairly specific to GHC. So no one has done that yet.

Below are the issues that the LLVM Mangler addresses in the assembly
code.

TABLES\_NEXT\_TO\_CODE (TNTC)
-----------------------------

TODO

Stack Alignment
---------------

LLVM requires that the C stack be properly aligned for spills. One Win32
the stack is 4-byte aligned, which is not enough for SSE spills, and
even on x64 platforms the stack is only 16-byte aligned, which is not
enough for AVX spills. When the stack is not properly aligned for
spills, LLVM generates prologue/epilogue code that fiddles with the base
pointer, which GHC uses as its stack pointer, and disables tail call
optimization. Both are very bad. Therefore we currently tell LLVM to
always assume the stack is properly aligned and then rewrite all aligned
SSE/AVX move instructions to their unaligned counterparts inside the
mangler.

SIMD / AVX
----------

Migrating Old Commentary
========================

Below you will find a table with a line for each section of the [old
commentary](http://darcs.haskell.org/ghc/docs/comm/). Please replace
*unknown* with **done** if you believe that the wiki commentary
completely captures *all* of the information in that section of the old
commentary, and that there is no longer any reason for people to read
that section of the commentary.

Before the Show Begins
----------------------

||Feedback||**done**|| ||Other Sources of Wisdom||**done**||

Genesis
-------

||Outline of the Genesis||**done**|| ||Mindboggling
Makefiles||**done**|| ||GHC's Marvellous Module Structure||**done**||

The Beast Dissected
-------------------

||Coding style used in the compiler||**done**|| ||The Glorious
Driver||Sections 1 & 2 **done**, *Other sections mostly outdated*||
||Primitives and the Prelude||*unknown*|| ||Just Syntax||*unknown*||
||The Basics||*unknown*|| ||Modules, !ModuleNames and
Packages||*unknown*|| ||The truth about names: Names and
!OccNames||*unknown*|| ||The Real Story about Variables, Ids, !TyVars,
and the like||*unknown*|| ||Data types and constructors||*unknown*||
||The Glorious Renamer||*unknown*|| ||Hybrid Types||*unknown*||
||Checking Types||*unknown*|| ||Sugar Free: From Haskell To
Core||*unknown*|| ||The Mighty Simplifier||*unknown*|| ||The Evil
Mangler||**done**|| ||Alien Functions||*unknown*|| ||You Got Control:
The STG-language||*unknown*|| ||The Native Code Generator||*unknown*||
||GHCi||*unknown*|| ||Implementation of foreign export||*unknown*||
||Compiling and running the Main module||*unknown*||

RTS & Libraries
---------------

||Coding Style Guidelines||**done**|| ||Spineless Tagless C||*unknown*||
||Primitives||*unknown*|| ||Prelude Foundations||*unknown*|| ||Cunning
Prelude Code||*unknown*|| ||On why we have !ForeignPtr||*unknown*||
||Non-blocking I/O for Win32||*unknown*|| ||Supporting multi-threaded
interoperation||*unknown*||

Extensions, or Making a Complicated System More Complicated
-----------------------------------------------------------

||Template Haskell||*unknown*|| ||Parallel Arrays||*unknown*||

The Marvellous Module Structure of GHC
======================================

`* `**`See` `also:` `[ModuleDependencies/Hierarchical` `Proposal` `for`
`hierarchical` `module` `structure]`**

`* `**`NOTE:`**` Possibly outdated.`

GHC is built out of about 245 Haskell modules. It can be quite tricky to
figure out what the module dependency graph looks like. It can be
important, too, because loops in the module dependency graph need to be
broken carefully using .hi-boot interface files.

This section of the commentary documents the subtlest part of the module
dependency graph, namely the part near the bottom.

`* The list is given in compilation order: that is, module near the top are more primitive, and are compiled earlier.`\
`* Each module is listed together with its most critical dependencies in parentheses; that is, the dependencies that prevent it being compiled earlier.`\
`* Modules in the same bullet don't depend on each other.`\
`* Loops are documented by a dependency such as "loop Type.Type". This means tha the module imports Type.Type, but module Type has not yet been compiled, so the import comes from Type.hi-boot. `

Compilation order is as follows:
--------------------------------

`* First comes a layer of modules that have few interdependencies, and which implement very basic data types:`\
`  * Util`\
`  * !OccName`\
`  * Pretty`\
`  * Outputable`\
`  * !StringBuffer`\
`  * !ListSetOps`\
`  * Maybes`\
`  * etc `

`* Now comes the main subtle layer, involving types, classes, type constructors identifiers, expressions, rules, and their operations.`\
`  * Name, !PrimRep`\
`  * !PrelNames`\
`  * Var (Name, loop !IdInfo.!IdInfo, loop Type.Type, loop Type.Kind)`\
`  * !VarEnv, !VarSet, !ThinAir`\
`  * Class (loop !TyCon.!TyCon, loop Type.Type)`\
`  * !TyCon (loop Type.Type, loop !DataCon.!DataCon, loop Generics.!GenInfo)`\
`  * !TypeRep (loop !DataCon.!DataCon, loop Subst.substTyWith)`\
`  * Type (loop !PprType.pprType, loop Subst.substTyWith)`\
`  * !FieldLabel (Type), !TysPrim (Type)`\
`  * Literal (!TysPrim, !PprType), !DataCon (loop !PprType, loop Subst.substTyWith, !FieldLabel.!FieldLabel)`\
`  * !TysWiredIn (loop !MkId.mkDataConIds)`\
`  * !TcType ( lots of !TysWiredIn stuff)`\
`  * !PprType ( lots of !TcType stuff )`\
`  * !PrimOp (!PprType, !TysWiredIn)`\
`  * !CoreSyn [does not import Id]`\
`  * !IdInfo (!CoreSyn.Unfolding, !CoreSyn.!CoreRules)`\
`  * Id (lots from !IdInfo)`\
`  * CoreFVs, !PprCore`\
`  * !CoreUtils (!PprCore.pprCoreExpr, CoreFVs.exprFreeVars, !CoreSyn.isEvaldUnfolding !CoreSyn.maybeUnfoldingTemplate)`\
`  * !CoreLint ( !CoreUtils ), !OccurAnal (!CoreUtils.exprIsTrivial), !CoreTidy (!CoreUtils.exprArity )`\
`  * !CoreUnfold (!OccurAnal.occurAnalyseGlobalExpr)`\
`  * Subst (!CoreUnfold.Unfolding, CoreFVs), Generics (!CoreUnfold.mkTopUnfolding), Rules (!CoreUnfold.Unfolding, !PprCore.pprTidyIdRules)`\
`  * !MkId (!CoreUnfold.mkUnfolding, Subst, Rules.addRule)`\
`  * !PrelInfo (!MkId), !HscTypes ( Rules.!RuleBase ) `

`* That is the end of the infrastructure. Now we get the main layer of modules that perform useful work.`\
`  * !CoreTidy (!HscTypes.!PersistentCompilerState) `

Typechecker stuff
-----------------

`* !TcType`\
`* !TcEvidence( !TcType )`\
`* TcMType( !TcEvidence )`\
`* !TcUnify( TcMType )`\
`* TcSMonad( TcMType )`\
`* !TcSimplify( TcSMonad )`\
`* !TcValidity( !TcSimplify.simplifyTop, !TcUnify.tcSubType )`\
`* !TcHsType( !TcValidity.checkValidType, !TcValidity.checkValidInstance )`

!HsSyn stuff
------------

`* !HsPat.hs-boot`\
`* !HsExpr.hs-boot (loop !HsPat.LPat)`\
`* !HsTypes (loop !HsExpr.!HsSplice)`\
`* !HsBinds (!HsTypes.LHsType, loop !HsPat.LPat, !HsExpr.pprFunBind and others) !HsLit (!HsTypes.!SyntaxName)`\
`* !HsPat (!HsBinds, !HsLit) !HsDecls (!HsBinds)`\
`* !HsExpr (!HsDecls, !HsPat) `

Library stuff: base package
---------------------------

`* GHC.Base`\
`* Data.Tuple (GHC.Base), GHC.Ptr (GHC.Base)`\
`* GHC.Enum (Data.Tuple)`\
`* GHC.Show (GHC.Enum)`\
`* GHC.Num (GHC.Show)`\
`* GHC.ST (GHC.Num), GHC.Real (GHC.Num)`\
`* GHC.Arr (GHC.ST) GHC.STRef (GHC.ST)`\
`* GHC.!IOBase (GHC.Arr)`\
`* Data.Bits (GHC.Real)`\
`* Data.!HashTable (Data.Bits, Control.Monad)`\
`* Data.Typeable (GHC.IOBase, Data.!HashTable)`\
`* GHC.Weak (Data.Typeable, GHC.IOBase) `

High-level Dependency Graph
---------------------------

Dark red edges indicate that only one module in one group depends on a
module in the other group. Dark green means 11 or more dependencies.
Arrows point from the importing module to the imported module.

[Image(dep5.png)](Image(dep5.png) "wikilink")

Module Types
============

Here we attempt to describe some of the main data structures involved in
GHC's representation and handling of Haksell modules. GHC uses a number
of different data types to represent modules, for efficiency (some types
load less information) and categorising how other modules relate to the
one being compiled. Most these types are defined in
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink").

Module
------

Location:
[GhcFile(compiler/basicTypes/Module.lhs)](GhcFile(compiler/basicTypes/Module.lhs) "wikilink")

The **Module** data type is simply an identifier of a module; its fully
qualified name.

!ModIface
---------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

The **!ModIface** data type is one of the fullest representations of a
module. It is a complete representation of a modules interface file
(**.hi**). It is this data structure that is serialised to produce a
modules **.hi** file.

!ModDetails
-----------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

**!ModDetails** is essentially a cache for information in the
**!ModIface** for home modules only. It stores information about a
module after linking has taken place. **!ModIface** stores information
about a module before linking. Information stored in a **!ModDetails**
is created from a **!ModIface**, typically during type checking.

### !ModGuts

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

A **!ModGuts** is carried through the compiler, accumulating stuff as it
goes. There is only one **!ModGuts** at any time, the one for the module
being compiled right now. Once it is compiled, a **!ModIface** and
**!ModDetails** are extracted and the **!ModGuts** is discarded.

!ModSummary
-----------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

A **!ModSummary** stores a summary of a module that is suitable for
recompilation checking. A **!ModSummary** is a node in the compilation
manager's dependency graph.

!HomeModInfo
------------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

A **!HomeModInfo** stores information about a module in the package
being compiled. It simply stores for the **!ModIface**, **!ModDetails**
and linkage information about a single module.

!HomePackageTable
-----------------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

The home package table describes already-compiled home-package modules,
/excluding/ the module we are compiling right now.

!ExternalPackageState
---------------------

Location:
[GhcFile(compiler/main/HscTypes.lhs)](GhcFile(compiler/main/HscTypes.lhs) "wikilink")

Stores information about other packages that we have pulled in while
compiling the current module.

Multi-instance packages
=======================

This page is about how to change the package system to allow multiple
instances of a package to be installed at the same time. There are two
reasons we want to be able to do this:

`` * To be able to track the different "ways" in which a package is available: e.g. profiling, dynamic.  At the moment, the package database doesn't track this information, with the result that the user has to reinstall packages with `--enable-profiling` on a trial-and-error basis in order to get profiling support for packages they have already installed. ``\
`  The same holds, in principle, for different flag settings or other configuration variations of a package.`

`* To make installing new packages more robust.  When installing a new package, we sometimes need to upgrade packages that are already installed to new versions, which may require recompiling other packages against the new version.  For example, if we have P1 installed, Q1 depends on P (any version), and we need to install R that depends on both P2 and Q1.  We need to build P2, rebuild Q1 against P2, and finally build R against P2 and the new Q1.  We would like to do this without removing P1 or the old Q1 from the package database, because other packages may be depending on the old Q1, and we don't want to break those packages (which is what currently happens with GHC 7.0).`

See also

`* [wiki:Commentary/Packages Commentary pages about packages]`\
`* Philipp Schuster's GSoC project `[`proposal`
`(DEAD)`](http://www.google-melange.com/gsoc/proposal/review/google/gsoc2012/phischu/1)`, `[`GSoC`
`project` `page`
`(DEAD)`](http://www.google-melange.com/gsoc/project/google/gsoc2012/phischu/19001)`,  [wiki:Commentary/GSoCMultipleInstances Trac wiki page], `[`git`
`repo`](https://github.com/phischu/cabal)`, and `[`video`](https://www.youtube.com/watch?v=h4QmkyN28Qs)`.`\
`* `[`Mikhail's`
`post`](http://coldwa.st/e/blog/2013-08-20-Cabal-sandbox.html)` about Cabal sandboxes. `\
`* Mailing list stuff `[`here`](http://comments.gmane.org/gmane.comp.lang.haskell.ghc.devel/443)` and `[`here`](http://markmail.org/message/4qvegvx32lhlo66g#query:+page:1+mid:bwdgykv4g2hzqg5t+state:results)`.`

!ToDo list
----------

`* ghc-pkg: do not overwrite previous instances in the package DB`\
`  * but we need to think about the case where we overwrite an existing package on the file system and re-register. This will happen with local (or in-place) package registration that occurs when building a bunch of related components. In this case the tool should know it's doing that and unregister the old instance first (though reliably tracking that state may be tricky, since users can make clean etc). We should check make it a checked error to re-register in the same filesystem location with new package id, without unregistering the old one first. Perhaps we can identify some key file.`

`* GHC: discard conflicting instances during its shadowing phase`\
`  * SDM: GHC will currently do *something* here, but it might end up with a result that the user didn't want/expect.  One way to improve things is to prioritise packages that were installed more recently.`\
``   * Andres suggests that GHC should be much cleverer, and look at the actual dependencies of the modules being compiled before deciding which packages to enable.  This would almost certainly result in more things working and possibly less surprising behaviour sometimes, but Simon thinks that (a) it is too hard, (b) if users need this, they should use Cabal and its dependency resolver, which will do a good job, (c) you can often resolve problems by adding `-package X`, and (d) eventually we will want a system where users manage separate sessions, so they can set up an environment in which the packages they want are available.  This has a lot in common with `cabal-dev` and sandboxes, so the mechanisms (and concepts) should be shared. (kosmikus: perhaps an alternative is to force the user to make an active decision in case of conflicts, i.e., to create a sandbox that exposes a consistent package set). ``

`* GHC: allow specifying a package instance in the -package flags`\
`  * SDM: already done (-package-id flag)`\
`  * DC: already used by Cabal`

`* Cabal: allow specifying a package instance when doing Setup.hs configure`\
`  * DC: currently only == version constraints can be used, not installed package id. Shouldn't be too hard to add however.`\
`  * JT: Done according to DC.`

`* instances of packages must install in a different location`\
`  * install directory includes hash?`\
``   * SDM: not done yet.  One problem is that we don't know the hash until the package is built, but we need to know the install locations earlier because we bake them into `Paths_foo.hs`. ``\
`  * Simon and Andres discussed that one option is to let Cabal compute its own hash. However, then we'd have two hashes to deal with. Only using the Cabal-computed hash isn't an option either according to Simon, because apparently GHC's ABI hash computation is non-deterministic, so we might end up with situations where Cabal's hash is stable, but GHC computes an ABI-incompatible version. This is somewhat worrying ... `\
`  * Duncan thinks that we should store both a package identity and a package ABI hash. Currently we form the package id from the name, version and ABI hash. We should store the ABI hash separately anyway because eventually we will want to know it, to know which packages are ABI compatible. So Cabal can compute a package Id in advance, however is sensible, and the ABI hash is calculated as now, after the build. The installation directory follows the package Id.`

`* Cabal: will the dependency solver work correctly in the presence of multiple package instances?`\
`  * Andres claims it will using the new solver. (There is now no point in updating the old solver, though it'd be technically possible.) A little bit more detail: the modular solver has no concept of shadowing, only of preference. So if several instances are provided by one or more package DBs, they'll all be valid choices.`

`* ghc-pkg cleanup: remove old/unused instances of packages`\
`  * how can we tell when something is unnecessary? This is actually rather hard because unlike Nix we do not track every random executable that the user compiles.`

Next step: dealing with ways
----------------------------

`* Add the "way" to InstalledPackageInfo, include the way in the hash`

`* GHC: slice the package DB during startup according to the correct way`

`* Cabal: fix up the dep resolver (kosmikus: anything still needed there?)`

`* Cabal: ways? (this would be really easy, if we could get more information about installed packages back from ghc-pkg)`

`` * To handle flags and other config, add two new fields to InstalledPackageInfo: `install-agent: {agent-id}` which identifies cabal/rpm/etc and then `configuration: {free text}`. The interpretation of the configuration string depends on the installation agent, and need be known only to that agent. This way, agents can see if it was them that installed a package, and so they should know how to interpret the config string. For cabal this would include config flags etc. It should make it possible to reproduce a package, e.g. if we have to rebuild for some reason, or to get the profiling equiv of a normal instance. ``

The  type
========

Every entity (type constructor, class, identifier, type variable) has a
. The Name type is pervasive in GHC, and is defined in
[GhcFile(compiler/basicTypes/Name.hs)](GhcFile(compiler/basicTypes/Name.hs) "wikilink").
Here is what a looks like, though it is private to the Name module:

`* The `` field says what sort of name this is: see `**`[wiki:Commentary/Compiler/NameType#TheNameSortofaName`
`NameSort]`**` below. `\
`* The `` field gives the "occurrence name", or `**`[wiki:Commentary/Compiler/RdrNameType#TheOccNametype`
`OccName]`**`, of the Name.`\
`* The `` field allows fast tests for equality of Names. `\
`* The `` field gives some indication of where the name was bound. `

The  of a Name
-------------

There are four flavours of Name:

`, ``::     `\
`   An `` `` has only an occurrence name. Distinct `` `` may have the same occurrence name; the `` distinguishes them.  `

`There is only a tiny difference between `` and ``; the former simply remembers that the name was originally written by the programmer, which helps when generating error messages.`

`:: `\
`   An `` `` has a globally-unique (module, occurrence name) pair, namely the original name of the entity, that describes where the thing was originally defined. So for example, if we have `

`   then in module ``, the function `` has an External Name ``.`

` During any invocation of GHC, each (module, occurrence-name) gets one, and only one, ``, stored in the `` field of the ``.  This association remains fixed even when GHC finishes one module and starts to compile another.  This association between (module, occurrence-name) pairs and the corresponding `` (with its `` field) is maintained by the Name Cache.`

` ``::`\
`   A `` `` is a special sort of `` ``, one that is completely known to the compiler (e.g. the `` type constructor).  See [wiki:Commentary/Compiler/WiredIn].`

` The `` field is just a boolean yes/no flag that identifies entities that are denoted by built-in syntax, such as `` for the empty list.  These `` aren't "in scope" as such, and we occasionally need to know that.`

Entities and 
-------------

Here are the sorts of Name an entity can have:

`* Class: always has an `` Name. `

`* !TyCon: always has an `` or `` Name. `

`* !TyVar: can have ``, or `` Names; the former are ones arise from instantiating programmer-written type signatures.`

`* Ids: can have ``, ``, or `` Names. `\
`   * Before !CoreTidy, the Ids that were defined at top level in the original source program get `` Names, whereas extra top-level bindings generated (say) by the type checker get `` Names. This distinction is occasionally useful for filtering diagnostic output; e.g. for ``. `\
`   * After !CoreTidy: An Id with an `` Name will generate symbols that appear as external symbols in the object file. An Id with an `` Name cannot be referenced from outside the module, and so generates a local symbol in the object file. The !CoreTidy pass makes the decision about which names should be External and which Internal. `

Native Code Generator (NCG)
===========================

For other information related to this page, see:

`* [wiki:BackEndNotes] for optimisation ideas regarding the current NCG`\
`* [wiki:Commentary/Compiler/CmmType The Cmm language] (the NCG code works from Haskell's implementation of C-- and many optimisations in the NCG relate to Cmm)`\
`* [wiki:Commentary/Compiler/Backends/NCG/RegisterAllocator The register allocator].`

On some platforms (currently x86 and x86\_64, with possibly bitrotted
support for PowerPC and Sparc), GHC can generate assembly code directly.
The NCG is enabled by default on supported platforms.

The NCG has always been something of a second-class citizen inside GHC,
an unloved child, rather. This means that its integration into the
compiler as a whole is rather clumsy, which brings some problems
described below. That apart, the NCG proper is fairly cleanly designed,
as target-independent as it reasonably can be, and so should not be
difficult to retarget.

NOTE! The native code generator was largely rewritten as part of the C--
backend changes, around May 2004. Unfortunately the rest of this
document still refers to the old version, and was written with relation
to the CVS head as of end-Jan 2002. Some of it is relevant, some of it
isn't.

### Files, Parts

After GHC has produced \[wiki:Commentary/Compiler/CmmType Cmm\] (use
-ddump-cmm or -ddump-opt-cmm to view), the Native Code Generator (NCG)
transforms Cmm into architecture-specific assembly code. The NCG is
located in
[GhcFile(compiler/nativeGen)](GhcFile(compiler/nativeGen) "wikilink")
and is separated into eight modules:

`* `[`GhcFile(compiler/nativeGen/AsmCodeGen.lhs)`](GhcFile(compiler/nativeGen/AsmCodeGen.lhs) "wikilink")[`BR`](BR "wikilink")\
`  top-level module for the NCG, imported by `[`GhcFile(compiler/main/CodeOutput.lhs)`](GhcFile(compiler/main/CodeOutput.lhs) "wikilink")`; also defines the Monad for optimising generic Cmm code, `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/MachCodeGen.hs)`](GhcFile(compiler/nativeGen/MachCodeGen.hs) "wikilink")[`BR`](BR "wikilink")\
`  generates architecture-specific instructions (a Haskell-representation of assembler) from Cmm code`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/MachInstrs.hs)`](GhcFile(compiler/nativeGen/MachInstrs.hs) "wikilink")[`BR`](BR "wikilink")\
`  contains data definitions and some functions (comparison, size, simple conversions) for machine instructions, mostly carried out through the `` data type, defined here`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/NCGMonad.hs)`](GhcFile(compiler/nativeGen/NCGMonad.hs) "wikilink")[`BR`](BR "wikilink")\
`  defines the the main monad in the NCG: the Native code Machine instruction Monad, ``, and related functions.  `*`Note:`
`the` `NCG` `switches` `between` `two` `monads` `at` `times,`
`especially` `in` `:` `and` `the` `Monad` `used` `throughout` `the`
`compiler.`*[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/PIC.hs)`](GhcFile(compiler/nativeGen/PIC.hs) "wikilink")[`BR`](BR "wikilink")\
`  handles generation of position independent code and issues related to dynamic linking in the NCG; related to many other modules outside the NCG that handle symbol import, export and references, including ``, ``, `` and the RTS, and the Mangler`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/PprMach.hs)`](GhcFile(compiler/nativeGen/PprMach.hs) "wikilink")[`BR`](BR "wikilink")\
`  Pretty prints machine instructions (``) to assembler code (currently readable by GNU's ``), with some small modifications, especially for comparing and adding floating point numbers on x86 architectures`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/RegAllocInfo.hs)`](GhcFile(compiler/nativeGen/RegAllocInfo.hs) "wikilink")[`BR`](BR "wikilink")\
`  defines the main register information function, ``, which takes a set of real and virtual registers and returns the actual registers used by a particular ``; register allocation is in AT&T syntax order (source, destination), in an internal function, ``; defines the `` data type`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `[`GhcFile(compiler/nativeGen/RegisterAlloc.hs)`](GhcFile(compiler/nativeGen/RegisterAlloc.hs) "wikilink")[`BR`](BR "wikilink")\
`  one of the most complicated modules in the NCG, `` manages the allocation of registers for each `*`basic`
`block`*` of Haskell-abstracted assembler code: management involves `*`liveness`*` analysis, allocation or deletion of temporary registers, `*`spilling`*` temporary values to the `*`spill`
`stack`*` (memory) and many optimisations.  ''See [wiki:Commentary/Compiler/CmmType The Cmm language] for the definition of a `*`basic`
`block`*` (in Haskell, `**`).''`

and one header file:

`* `[`GhcFile(compiler/nativeGen/NCG.h)`](GhcFile(compiler/nativeGen/NCG.h) "wikilink")[`BR`](BR "wikilink")\
`  defines macros used to separate architecture-specific code in the Haskell NCG files; since GHC currently only generates machine code for the architecture on which it was compiled (GHC is not currently a cross-compiler), the Haskell NCG files become considerably smaller after preprocessing; ideally all architecture-specific code would reside in separate files and GHC would have them available to support cross-compiler capabilities.`

The NCG has **machine-independent** and **machine-dependent** parts.

The **machine-independent** parts relate to generic operations,
especially optimisations, on Cmm code. The main machine-independent
parts begin with *Cmm blocks.* (A *Cmm block* is a compilation unit of
Cmm code, a file. See \[wiki:Commentary/Compiler/CmmType The Cmm
language\] for a discussion of what a *Cmm block* is but note that *Cmm*
is a type synonym for .) A machine-specific (assembler) instruction is
represented as a . The machine-independent NCG parts:

`1. optimise each Cmm block by reordering its basic blocks from the original order (the `` order from the ``) to minimise the number of branches between basic blocks, in other words, by maximising fallthrough of execution from one basic block to the next.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`1. lazily convert each Cmm block to abstract machine instructions (``) operating on an infinite number of registers--since the NCG Haskell files only contain instructions for the host computer on which GHC was compiled, these `` are machine-specific; and,`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`1. lazily allocate real registers for each basic block, based on the number of available registers on the target (currently, only the host) machine; for example, 32 integer and 32 floating-point registers on the PowerPC architecture.  The NCG does not currently have support for SIMD registers such as the vector registers for Altivec or any variation of SSE.`[`BR`](BR "wikilink")*`Note`*`: if a basic block simultaneously requires more registers than are available on the target machine and the temporary variable needs to be used (would sill be `*`live`*`) after the current instruction, it will be moved (`*`spilled`*`) into memory.`

The **machine-dependent** parts:

`1. define the abstract (Haskell) assembler `` for the target (host) machine and convert every Cmm block into it;`\
`1. define, manage and allocate the real registers available on the target system;`\
`1. pretty-print the Haskell-assembler to GNU AS (GAS) assembler code`

Overview
--------

The top-level code generator function is The returned \`SDoc\` is for
debugging, so is empty unless you specify \`-ddump-stix\`. The
\`Pretty.Doc\` bit is the final assembly code. Translation involves
three main phases, the first and third of which are target-independent.

#### Translation into the Stix representation

Stix is a simple tree-like RTL-style language, in which you can mention:

`* An infinite number of temporary, virtual registers.`\
`` * The STG "magic" registers (`MagicId`), such as the heap and stack pointers. ``\
`` * Literals and low-level machine ops (`MachOp`). ``\
`* Simple address computations.`\
`* Reads and writes of: memory, virtual regs, and various STG regs.`\
`` * Labels and `if ... goto ...` style control-flow.  ``

Stix has two main associated types:

`` * `StixStmt` -- trees executed for their side effects: assignments, control transfers, and auxiliary junk such as segment changes and literal data. ``\
`` * `StixExpr` -- trees which denote a value.  ``

Translation into Stix is almost completely target-independent. Needed
dependencies are knowledge of word size and endianness, used when
generating code to do deal with half-word fields in info tables. This
could be abstracted out easily enough. Also, the Stix translation needs
to know which \`MagicId\`s map to registers on the given target, and
which are stored in offsets from \`BaseReg\`.

After initial Stix generation, the trees are cleaned up with
constant-folding and a little copy-propagation ("Stix inlining", as the
code misleadingly calls it). We take the opportunity to translate
\`MagicId\`s which are stored in memory on the given target, into
suitable memory references. Those which are stored in registers are left
alone. There is also a half-hearted attempt to lift literal strings to
the top level in cases where nested strings have been observed to give
incorrect code in the past.

Primitive machine-level operations will already be phrased in terms of
\`MachOp\`s in the presented Abstract C, and these are passed through
unchanged. We comment only that the \`MachOp\`s have been chosen so as
to be easy to implement on all targets, and their meaning is intended to
be unambiguous, and the same on all targets, regardless of word size or
endianness.

**A note on \`MagicId\`s**. Those which are assigned to registers on the
current target are left unmodified. Those which are not are stored in
memory as offsets from \`BaseReg\` (which is assumed to permanently have
the value (\`&MainCapability.r\`)), so the constant folder calculates
the offsets and inserts suitable loads/stores. One complication is that
not all archs have \`BaseReg\` itself in a register, so for those
(sparc), we instead generate the address as an offset from the static
symbol \`MainCapability\`, since the register table lives in there.

Finally, \`BaseReg\` does occasionally itself get mentioned in Stix
expression trees, and in this case what is denoted is precisely
(\`&MainCapability.r\`), not, as in all other cases, the value of memory
at some offset from the start of the register table. Since what it
denotes is an r-value and not an l-value, assigning \`BaseReg\` is
meaningless, so the machinery checks to ensure this never happens. All
these details are taken into account by the constant folder.

#### Instruction selection

This is the only majorly target-specific phase. It turns Stix statements
and expressions into sequences of \`Instr\`, a data type which is
different for each architecture. Instr, unsurprisingly, has various
supporting types, such as \`Reg\`, \`Operand\`, \`Imm\`, etc. The
generated instructions may refer to specific machine registers, or to
arbitrary virtual registers, either those created within the instruction
selector, or those mentioned in the Stix passed to it.

The instruction selectors live in \`MachCode.lhs\`. The core functions,
for each target, are:

The insn selectors use the "maximal munch" algorithm. The
bizarrely-misnamed \`getRegister\` translates expressions. A simplified
version of its type is: That is: it (monadically) turns a StixExpr into
a sequence of instructions, and a register, with the meaning that after
executing the (possibly empty) sequence of instructions, the (possibly
virtual) register will hold the resulting value. The real situation is
complicated by the presence of fixed registers, and is detailed below.

Maximal munch is a greedy algorithm and is known not to give globally
optimal code sequences, but it is good enough, and fast and simple.
Early incarnations of the NCG used something more sophisticated, but
that is long gone now.

Similarly, \`getAmode\` translates a value, intended to denote an
address, into a sequence of insns leading up to a (processor-specific)
addressing mode. This stuff could be done using the general
\`getRegister\` selector, but would necessarily generate poorer code,
because the calculated address would be forced into a register, which
might be unnecessary if it could partially or wholly be calculated using
an addressing mode.

Finally, \`assignMem\_IntCode\` and \`assignReg\_IntCode\` create
instruction sequences to calculate a value and store it in the given
register, or at the given address. Because these guys translate a
statement, not a value, they just return a sequence of insns and no
associated register. Floating-point and 64-bit integer assignments have
analogous selectors.

Apart from the complexities of fixed vs floating registers, discussed
below, the instruction selector is as simple as it can be. It looks long
and scary but detailed examination reveals it to be fairly
straightforward.

#### Register allocation

The register allocator, \`AsmRegAlloc.lhs\` takes sequences of Instrs
which mention a mixture of real and virtual registers, and returns a
modified sequence referring only to real ones. It is gloriously and
entirely target-independent. Well, not exactly true. Instead it regards
\`Instr\` (instructions) and \`Reg\` (virtual and real registers) as
abstract types, to which it has the following interface: \`insnFuture\`
is used to (re)construct the graph of all possible control transfers
between the insns to be allocated. \`regUsage\` returns the sets of
registers read and written by an instruction. And \`patchRegs\` is used
to apply the allocator's final decision on virtual-to-real reg mapping
to an instruction.

Clearly these 3 fns have to be written anew for each architecture. They
are defined in \`RegAllocInfo.lhs\`. Think twice, no, thrice, before
modifying them: making false claims about insn behaviour will lead to
hard-to-find register allocation errors.

\`AsmRegAlloc.lhs\` contains detailed comments about how the allocator
works. Here is a summary. The head honcho takes a list of instructions
and a list of real registers available for allocation, and maps as many
of the virtual regs in the input into real ones as it can. The returned
\`Bool\` indicates whether or not it was successful. If so, that's the
end of it. If not, the caller of \`allocUsingTheseRegs\` will attempt
spilling. More of that later. What \`allocUsingTheseRegs\` does is:

`* Implicitly number each instruction by its position in the input list.`\
`` * Using `insnFuture`, create the set of all flow edges -- possible control transfers -- within this set of insns. ``\
`` * Using `regUsage` and iterating around the flow graph from the previous step, calculate, for each virtual register, the set of flow edges on which it is live. ``\
`* Make a real-register committment map, which gives the set of edges for which each real register is committed (in use). These sets are initially empty. For each virtual register, attempt to find a real register whose current committment does not intersect that of the virtual register -- ie, is uncommitted on all edges that the virtual reg is live. If successful, this means the vreg can be assigned to the realreg, so add the vreg's set to the realreg's committment.`\
`` * If all the vregs were assigned to a realreg, use `patchInstr` to apply the mapping to the insns themselves.  ``

### Spilling

If \`allocUsingTheseRegs\` fails, a baroque mechanism comes into play.
We now know that much simpler schemes are available to do the same thing
and give better results. Anyways:

The logic above \`allocUsingTheseRegs\`, in \`doGeneralAlloc\` and
\`runRegAllocate\`, observe that allocation has failed with some set R
of real registers. So they apply \`runRegAllocate\` a second time to the
code, but remove (typically) two registers from R before doing so. This
naturally fails too, but returns a partially-allocated sequence.
\`doGeneralAlloc\` then inserts spill code into the sequence, and
finally re-runs \`allocUsingTheseRegs\`, but supplying the original,
unadulterated R. This is guaranteed to succeed since the two registers
previously removed from R are sufficient to allocate all the
spill/restore instructions added.

Because x86 is very short of registers, and in the worst case needs
three removed from R, a softly-softly approach is used.
\`doGeneralAlloc\` first tries with zero regs removed from R, then if
that fails one, then two, etc. This means \`allocUsingTheseRegs\` may
get run several times before a successful arrangement is arrived at.
\`findReservedRegs\` cooks up the sets of spill registers to try with.

The resulting machinery is complicated and the generated spill code is
appalling. The saving grace is that spills are very rare so it doesn't
matter much. I did not invent this -- I inherited it.

### Dealing with common cases fast

The entire reg-alloc mechanism described so far is general and correct,
but expensive overkill for many simple code blocks. So to begin with we
use \`doSimpleAlloc\`, which attempts to do something simple. It
exploits the observation that if the total number of virtual registers
does not exceed the number of real ones available, we can simply dole
out a new realreg each time we see mention of a new vreg, with no regard
for control flow. \`doSimpleAlloc\` therefore attempts this in a single
pass over the code. It gives up if it runs out of real regs or sees any
condition which renders the above observation invalid (fixed reg uses,
for example).

This clever hack handles the majority of code blocks quickly. It was
copied from the previous reg-allocator (the Mattson/Partain/Marlow/Gill
one).

Complications, observations, and possible improvements
------------------------------------------------------

### Real vs virtual registers in the instruction selectors

The instruction selectors for expression trees, namely \`getRegister\`,
are complicated by the fact that some expressions can only be computed
into a specific register, whereas the majority can be computed into any
register. We take x86 as an example, but the problem applies to all
archs.

Terminology: \`rreg\` means real register, a real machine register.
\`vreg\` means one of an infinite set of virtual registers. The type
\`Reg\` is the sum of \`rreg\` and \`vreg\`. The instruction selector
generates sequences with unconstrained use of vregs, leaving the
register allocator to map them all into rregs.

Now, where was I ? Oh yes. We return to the type of \`getRegister\`,
which despite its name, selects instructions to compute the value of an
expression tree.

At first this looks eminently reasonable (apart from the stupid name).
\`getRegister\`, and nobody else, knows whether or not a given
expression has to be computed into a fixed rreg or can be computed into
any rreg or vreg. In the first case, it returns \`Fixed\` and indicates
which rreg the result is in. In the second case it defers committing to
any specific target register by returning a function from \`Reg\` to
\`InstrBlock\`, and the caller can specify the target reg as it sees
fit.

Unfortunately, that forces \`getRegister\`'s callers (usually itself) to
use a clumsy and confusing idiom in the common case where they do not
care what register the result winds up in. The reason is that although a
value might be computed into a fixed rreg, we are forbidden (on pain of
segmentation fault :) from subsequently modifying the fixed reg. This
and other rules are record in "Rules of the game" inside
\`MachCode.lhs\`.

Why can't fixed registers be modified post-hoc? Consider a simple
expression like \`Hp+1\`. Since the heap pointer \`Hp\` is definitely in
a fixed register, call it R, \`getRegister\` on subterm \`Hp\` will
simply return Fixed with an empty sequence and R. But we can't just emit
an increment instruction for R, because that trashes \`Hp\`; instead we
first have to copy it into a fresh vreg and increment that.

With all that in mind, consider now writing a \`getRegister\` clause for
terms of the form \`(1 + E)\`. Contrived, yes, but illustrates the
matter. First we do \`getRegister\` on \`E\`. Now we are forced to
examine what comes back. This seems unreasonably cumbersome, yet the
instruction selector is full of such idioms. A good example of the
complexities induced by this scheme is shown by \`trivialCode\` for x86
in \`MachCode.lhs\`. This deals with general integer dyadic operations
on x86 and has numerous cases. It was difficult to get right.

An alternative suggestion is to simplify the type of \`getRegister\` to
this: and then we could safely write which is about as straightforward
as you could hope for. Unfortunately, it requires \`getRegister\` to
insert moves of values which naturally compute into an rreg, into a
vreg. Consider: On x86 the ccall result is returned in rreg \`%eax\`.
The resulting sequence, prior to register allocation, would be: If, as
is likely, \`%eax\` is not held live beyond this point for any other
purpose, the move into a fresh register is pointless; we'd have been
better off leaving the value in \`%eax\` as long as possible.

The simplified \`getRegister\` story is attractive. It would clean up
the instruction selectors significantly and make it simpler to write new
ones. The only drawback is that it generates redundant register moves. I
suggest that eliminating these should be the job of the register
allocator. Indeed:

`* There has been some work on this already ("Iterated register coalescing" ?), so this isn't a new idea.`

`* You could argue that the existing scheme inappropriately blurs the boundary between the instruction selector and the register allocator. The instruction selector should .. well .. just select instructions, without having to futz around worrying about what kind of registers subtrees get generated into. Register allocation should be `*`entirely`*` the domain of the register allocator, with the proviso that it should endeavour to allocate registers so as to minimise the number of non-redundant reg-reg moves in the final output. `

Selecting insns for 64-bit values/loads/stores on 32-bit platforms
------------------------------------------------------------------

Note that this stuff doesn't apply on 64-bit archs, since the
\`getRegister\` mechanism applies there. The relevant functions are:

\`iselExpr64\` is the 64-bit, plausibly-named analogue of
\`getRegister\`, and \`ChildCode64\` is the analogue of \`Register\`.
The aim here was to generate working 64 bit code as simply as possible.
To this end, I used the simplified \`getRegister\` scheme described
above, in which iselExpr64generates its results into two vregs which can
always safely be modified afterwards.

Virtual registers are, unsurprisingly, distinguished by their
\`Unique\`s. There is a small difficulty in how to know what the vreg
for the upper 32 bits of a value is, given the vreg for the lower 32
bits. The simple solution adopted is to say that any low-32 vreg may
also have a hi-32 counterpart which shares the same unique, but is
otherwise regarded as a separate entity. \`getHiVRegFromLo\` gets one
from the other. Apart from that, 64-bit code generation is really
simple. The sparc and x86 versions are almost copy-n-pastes of each
other, with minor adjustments for endianness. The generated code isn't
wonderful but is certainly acceptable, and it works.

Shortcomings and inefficiencies in the register allocator
---------------------------------------------------------

### Redundant reconstruction of the control flow graph

The allocator goes to considerable computational expense to construct
all the flow edges in the group of instructions it's allocating for, by
using the \`insnFuture\` function in the \`Instr\` pseudo-abstract type.

This is really silly, because all that information is present at the
abstract C stage, but is thrown away in the translation to Stix. So a
good thing to do is to modify that translation to produce a directed
graph of Stix straight-line code blocks, and to preserve that structure
through the insn selector, so the allocator can see it.

This would eliminate the fragile, hacky, arch-specific \`insnFuture\`
mechanism, and probably make the whole compiler run measurably faster.
Register allocation is a fair chunk of the time of non-optimising
compilation (10% or more), and reconstructing the flow graph is an
expensive part of reg-alloc. It would probably accelerate the vreg
liveness computation too.

### Really ridiculous method for doing spilling

This is a more ambitious suggestion, but ... reg-alloc should be
reimplemented, using the scheme described in "Quality and speed in
linear-scan register allocation." (Traub?) For straight-line code
blocks, this gives an elegant one-pass algorithm for assigning registers
and creating the minimal necessary spill code, without the need for
reserving spill registers ahead of time.

I tried it in Rigr, replacing the previous spiller which used the
current GHC scheme described above, and it cut the number of spill loads
and stores by a factor of eight. Not to mention being simpler, easier to
understand and very fast.

The Traub paper also describes how to extend their method to multiple
basic blocks, which will be needed for GHC. It comes down to reconciling
multiple vreg-to-rreg mappings at points where control flow merges.

### Redundant-move support for revised instruction selector suggestion

As mentioned above, simplifying the instruction selector will require
the register allocator to try and allocate source and destination vregs
to the same rreg in reg-reg moves, so as to make as many as possible go
away. Without that, the revised insn selector would generate worse code
than at present. I know this stuff has been done but know nothing about
it. The Linear-scan reg-alloc paper mentioned above does indeed mention
a bit about it in the context of single basic blocks, but I don't know
if that's sufficient.

x86 arcana that you should know about
-------------------------------------

The main difficulty with x86 is that many instructions have fixed
register constraints, which can occasionally make reg-alloc fail
completely. And the FPU doesn't have the flat register model which the
reg-alloc abstraction (implicitly) assumes.

Our strategy is: do a good job for the common small subset, that is
integer loads, stores, address calculations, basic ALU ops (+, -, and,
or, xor), and jumps. That covers the vast majority of executed insns.
And indeed we do do a good job, with a loss of less than 2% compared
with gcc.

Initially we tried to handle integer instructions with awkward register
constraints (mul, div, shifts by non-constant amounts) via various
jigglings of the spiller et al. This never worked robustly, and putting
platform-specific tweaks in the generic infrastructure is a big No-No.
(Not quite true; shifts by a non-constant amount are still done by a
giant kludge, and should be moved into this new framework.)

Fortunately, all such insns are rare. So the current scheme is to
pretend that they don't have any such constraints. This fiction is
carried all the way through the register allocator. When the insn
finally comes to be printed, we emit a sequence which copies the
operands through memory (\`%esp\`-relative), satisfying the constraints
of the real instruction. This localises the gruesomeness to just one
place. Here, for example, is the code generated for integer divison of
\`%esi\` by \`%ecx\`: This is not quite as appalling as it seems, if you
consider that the division itself typically takes 16+ cycles, whereas
the rest of the insns probably go through in about 1 cycle each.

This trick is taken to extremes for FP operations.

All notions of the x86 FP stack and its insns have been removed.
Instead, we pretend, to the instruction selector and register allocator,
that x86 has six floating point registers, \`%fake0\` .. \`%fake5\`,
which can be used in the usual flat manner. We further claim that x86
has floating point instructions very similar to SPARC and Alpha, that
is, a simple 3-operand register-register arrangement. Code generation
and register allocation proceed on this basis.

When we come to print out the final assembly, our convenient fiction is
converted to dismal reality. Each fake instruction is independently
converted to a series of real x86 instructions. \`%fake0\` .. \`%fake5\`
are mapped to \`%st(0)\` .. \`%st(5)\`. To do reg-reg arithmetic
operations, the two operands are pushed onto the top of the FP stack,
the operation done, and the result copied back into the relevant
register. When one of the operands is also the destination, we emit a
slightly less scummy translation. There are only six \`%fake\` registers
because 2 are needed for the translation, and x86 has 8 in total.

The translation is inefficient but is simple and it works. A cleverer
translation would handle a sequence of insns, simulating the FP stack
contents, would not impose a fixed mapping from \`%fake\` to \`%st\`
regs, and hopefully could avoid most of the redundant reg-reg moves of
the current translation.

There are, however, two unforeseen bad side effects:

`* This doesn't work properly, because it doesn't observe the normal conventions for x86 FP code generation. It turns out that each of the 8 elements in the x86 FP register stack has a tag bit which indicates whether or not that register is notionally in use or not. If you do a FPU operation which happens to read a tagged-as-empty register, you get an x87 FPU (stack invalid) exception, which is normally handled by the FPU without passing it to the OS: the program keeps going, but the resulting FP values are garbage. The OS can ask for the FPU to pass it FP stack-invalid exceptions, but it usually doesn't.`

`Anyways: inside NCG created x86 FP code this all works fine. However, the NCG's fiction of a flat register set does not operate the x87 register stack in the required stack-like way. When control returns to a gcc-generated world, the stack tag bits soon cause stack exceptions, and thus garbage results.`

`` The only fix I could think of -- and it is horrible -- is to clear all the tag bits just before the next STG-level entry, in chunks of code which use FP insns. `i386_insert_ffrees` inserts the relevant `ffree` insns into such code blocks. It depends critically on `is_G_instr` to detect such blocks. ``

`* It's very difficult to read the generated assembly and reason about it when debugging, because there's so much clutter. We print the fake insns as comments in the output, and that helps a bit. `

Generating code for ccalls
--------------------------

For reasons I don't really understand, the instruction selectors for
generating calls to C (genCCall) have proven surprisingly difficult to
get right, and soaked up a lot of debugging time. As a result, I have
once again opted for schemes which are simple and not too difficult to
argue as correct, even if they don't generate excellent code.

The sparc ccall generator in particular forces all arguments into
temporary virtual registers before moving them to the final
out-registers (\`%o0\` .. \`%o5\`). This creates some unnecessary
reg-reg moves. The reason is explained in a comment in the code.

Duplicate implementation for many STG macros
--------------------------------------------

This has been discussed at length already. It has caused a couple of
nasty bugs due to subtle untracked divergence in the macro translations.
The macro-expander really should be pushed up into the Abstract C phase,
so the problem can't happen.

Doing so would have the added benefit that the NCG could be used to
compile more "ways" -- well, at least the 'p' profiling way.

How to debug the NCG without losing your sanity/hair/cool
---------------------------------------------------------

Last, but definitely not least ...

The usual syndrome is that some program, when compiled via C, works, but
not when compiled via the NCG. Usually the problem is fairly simple to
fix, once you find the specific code block which has been mistranslated.
But the latter can be nearly impossible, since most modules generate at
least hundreds and often thousands of them.

My solution: cheat.

Because the via-C and native routes diverge only late in the day, it is
not difficult to construct a 1-1 correspondence between basic blocks on
the two routes. So, if the program works via C but not on the NCG, do
the following:

`` * Recompile `AsmCodeGen.lhs` in the afflicted compiler with `-DDEBUG_NCG`, so that it inserts `___ncg_debug_markers` into the assembly it emits. ``\
`* Using a binary search on modules, find the module which is causing the problem.`\
`` * Compile that module to assembly code, with identical flags, twice, once via C and once via NCG. Call the outputs `ModuleName.s-gcc` and `ModuleName.s-nat`. Check that the latter does indeed have `___ncg_debug_markers` in it; otherwise the next steps fail. ``\
`` * Build (with a working compiler) the program `utils/debugNCG/diff_gcc_nat`. ``\
`` * Run: `diff_gcc_nat ModuleName.s`. This will construct the 1-1 correspondence, and emits on stdout a cppable assembly output. Place this in a file -- I always call it synth.S. Note, the capital S is important; otherwise it won't get cpp'd. You can feed this file directly to ghc and it will automatically get cpp'd; you don't have to do so yourself. ``\
`` * By messing with the `#define`s at the top of `synth.S`, do a binary search to find the incorrect block. Keep a careful record of where you are in the search; it is easy to get confused. Remember also that multiple blocks may be wrong, which also confuses matters. Finally, I usually start off by re-checking that I can build the executable with all the `#define`s set to 0 and then all to 1. This ensures you won't get halfway through the search and then get stuck due to some snafu with gcc-specific literals. Usually I set `UNMATCHED_GCC` to 1 all the time, and this bit should contain only literal data. `UNMATCHED_NAT` should be empty.  ``

\`diff\_gcc\_nat\` was known to work correctly last time I used it, in
December 01, for both x86 and sparc. If it doesn't work, due to changes
in assembly syntax, or whatever, make it work. The investment is well
worth it. Searching for the incorrect block(s) any other way is a total
time waster.

Historical page
---------------

This page describes state of the new code generator sometime back in
2008. It is completely outdated and is here only for historical reasons.
See \[wiki:Commentary/Compiler/CodeGen Code Generator\] page for a
description of current code generator.

Overview of modules in the new code generator
=============================================

This page gives an overview of the new code generator, including
discussion of:

`* the [wiki:Commentary/Compiler/NewCodeGenModules#ThenewCmmdatatype new Cmm type]`\
`* the [wiki:Commentary/Compiler/NewCodeGenModules#Modulestructureofthenewcodegenerator module structure of the new code generator]`

See also \[wiki:Commentary/Compiler/NewCodeGenPipeline the description
of the new code generation pipeline\].

The new Cmm data type
---------------------

There is a new Cmm data type:

`* `[`GhcFile(compiler/cmm/ZipCfg.hs)`](GhcFile(compiler/cmm/ZipCfg.hs) "wikilink")` contains a generic zipper-based control-flow graph data type.  It is generic in the sense that it's polymorphic in the type of `**`middle`
`nodes`**` and `**`last`
`nodes`**` of a block.  (Middle nodes don't do control transfers; last nodes only do control transfers.)  There are extensive notes at the start of the module.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`The key types it defines are:`\
``   * Block identifiers: `BlockId`, `BlockEnv`, `BlockSet` ``\
``   * Control-flow blocks: `Block` ``\
``   * Control-flow graphs: `Graph` ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `**`` `ZipDataFlow` ``**``  contains a generic framework for solving dataflow problems over `ZipCfg`. It allows you to define a new optimization simply by defining a lattice of dataflow facts (akin to a specialized logic) and then writing the dataflow-transfer functions found in compiler textbooks. Handing these functions to the dataflow engine produces a new optimization that is not only useful on its own, but that can easily be composed with other optimizations to create an integrated "superoptimization" that is strictly more powerful than any sequence of individual optimizations, no matter how many times they are re-run.  The dataflow engine is based on  ``[`(Lerner,`
`Grove,` `and` `Chambers`
`2002)`](http://citeseer.ist.psu.edu/old/lerner01composing.html)`; you can find a functional implementation of the dataflow engine presented in `[`(Ramsey`
`and` `Dias`
`2005)`](http://www.cs.tufts.edu/~nr/pubs/zipcfg-abstract.html)`.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `**[`GhcFile(compiler/cmm/ZipCfgCmmRep.hs)`](GhcFile(compiler/cmm/ZipCfgCmmRep.hs) "wikilink")**``  instantiates `ZipCfg` for Cmm, by defining types `Middle` and `Last` and using these to instantiate the polymorphic fields of `ZipCfg`.  It also defines a bunch of smart constructor (`mkJump`, `mkAssign`, `mkCmmIfThenElse` etc) which make it easy to build `CmmGraph`. ``[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`* `**`` `CmmExpr` ``**` contains the data types for Cmm expressions, registers, and the like. Here is a fuller description of these types is at [wiki:Commentary/Compiler/BackEndTypes]. It does not depend on the dataflow framework at all.  `

Module structure of the new code generator
------------------------------------------

The new code generator has a fair number of modules, which can be split
into three groups:

`* basic datatypes and infrastructure`\
`* analyses and transformations`\
`* linking the pipeline`

All the modules mentioned are in the \`cmm/\` directory, unless
otherwise indicated.

### Basic datatypes and infrastructure

Ubiquitous types:

`` * `CLabel` (`CLabel`): All sorts of goo for making and manipulating labels. ``

`` * `BlockId` (`BlockId`, `BlockEnv`, `BlockSet`): ``\
`  The type of a basic-block id, along with sets and finite maps.`

`` * `CmmExpr` (`CmmType`, `LocalReg`, `GlobalReg`, `Area`, `CmmExpr`): ``\
`  Lots of type definitions: for Cmm types (bit width, GC ptr, float, etc),`\
`  registers, stack areas, and Cmm expressions.`

`` * `Cmm` (`GenCmm`, `CmmInfo`, `CmmInfoTable`): ``\
``   More type definitions: the parameterized top-level Cmm type (`GenCmm`), ``\
`  along with the type definitions for info tables.`

Control-flow graphs:

`` * `ZipCfg` (`Graph`, `LGraph`, `Block`): ``\
`  Describes a zipper-like representation for true basic-block`\
`  control-flow graphs.  A block has a single entry point,`\
`  which is a always a label, followed by zero or mode 'middle`\
`  nodes', each of which represents an uninterruptible`\
`  single-entry, single-exit computation, then finally a 'last`\
`  node', which may have zero or more successors.`\
``   `ZipCFG` is polymorphic in the type of middle and last nodes. ``\
`` * `ZipCfgCmmRep` (`Middle`, `Last`, `CmmGraph`) ``\
``   Types to instantiate `ZipCfg` for C--: middle and last nodes, ``\
``   and a bunch of abbreviations of types in `ZipCfg` and `Cmm`. ``

`` * `MkZipCfg` (`AGraph`, `mkLabel`, `mkMiddle`, `mkBranch`) ``\
`  Smart constructors for control-flow graphs (and the constructors have`\
`  non-monadic types).`\
``   Like `ZipCfg`, `MkZipCfg` is polymorphic in the types of middle and last nodes. ``\
`` * `MkZipCfgCmm` (`mkNop`, `mkAssign`, `mkStore`, `mkCall`, ...) ``\
`  Smart constructors for creating middle and last nodes in`\
`  control-flow graphs (and the constructors have non-monadic types).`

Calling conventions:

`` * `CmmInfo` (`cmmToRawCmm`, `mkBareInfoTable`): ``\
``   Converts Cmm code to "raw" Cmm.  What this means is: convert a `CmmInfo` data structure describing the info table for each `CmmProc` to a `[CmmStatic]`.  ``\
``   `mkBareInfoTable` is the workhorse that produces the `[CmmStatic]`.  It is also used to produce the info table required for safe foreign calls (a middle node). ``\
`` * `CmmCallConv` (`ArgumentFormat`, `assignArgumentsPos`): ``\
`  Implements Cmm calling conventions: given arguments and a calling convention,`\
`  this module decides where to put the arguments.`\
`  (JD: Crufty. Lots of old code in here, needs cleanup.)`

Dataflow analysis:

`` * `CmmTx` (`Tx`, `TxRes`): ``\
`  A simple monad for tracking when a transformation has`\
`  occurred (something has changed).`\
`  Used by the dataflow analysis to keep track of when the graph is rewritten.`

`` * `OptimizationFuel` (`OptimizationFuel`, `FuelMonad`, `maybeRewriteWithFuel`) ``\
`  We can use a measure of "fuel" to limit the number of rewrites performed`\
`  by a transformation. This module defines a monad for tracking (and limiting)`\
`  fuel use.`\
`  (JD: Largely untested.)`

`` * `DFMonad` (`DataflowLattice`, `DataflowAnalysis`, `runDFM`): ``\
`  Defines the type of a dataflow lattice and an analysis.`\
`  Defines the monad used by the dataflow framework.`\
`  The monad keeps track of dataflow facts, along with fuel,`\
`  and it can provide unique id's.`\
`  All in support of the dataflow module.`

`` * `ZipDataflow` (`ForwardTransfers`, `BackwardTransfers`, `ForwardRewrites`, `BackwardRewrites`, ``\
``   `zdfSolveFrom`, `zdfRewriteFrom`, etc) ``\
`  This module implements the Lerner/Grove/Chambers dataflow analysis frameword.`\
`  Given the definitions of a lattice and dataflow transfer/rewrite functions,`\
`  this module provides all the work of running the dataflow analysis and transformation.`\
`  A number of the phases of the back end rely on this code,`\
`  and hopefully more optimizations will target it in the future.`

And a few basic utilities:

`` * `CmmZipUtil`: (JD: Unused, I believe, but probably should be used in a few places.) ``\
`  A few utility functions for manipulating a zipcfg.`\
`` * `PprC`:   Prettyprinting to generate C code. ``\
`` * `PprCmm`: Prettyprinting the C-- code. ``\
`` * `PprCmmZ`: (JD: Unused, I believe.) ``\
``   Prettyprinting functions related to `ZipCfg` and `ZipCfgCmm`. ``

### Analyses and transformations

`` * `CmmLint` (`cmmLint`, `cmmLintTop`): ``\
`  Some sanity checking on the old Cmm graphs.`\
`  Not sure how effective this is.`\
`` * `CmmLiveZ` (`CmmLive`, `livelattice`, `cmmLivenessZ`): ``\
`  Liveness analysis for registers (uses dataflow framework).`\
`` * `CmmProcPointZ` (`ProcPointSet`, `callProcPoints`, `minimalProcPointSet`, ``\
``   `procPointAnalysis`, `splitAtProcPoints`) ``\
`  A proc point is a block in a control-flow graph that must be the`\
`  entry point of a new procedure when we generate C code.`\
`  For example, successors of calls and joinpoints that follow calls`\
`  are procpoints.`\
`  This module provides the analyses to find procpoints, as well as`\
`  the transformation to split the procedure into pieces.`\
`  The procpoint analysis doesn't use the dataflow framework,`\
`  but it really should - dominators are the way forward.`\
`` * `CmmSpillReload` (`DualLive`, `dualLiveLattice`, `dualLiveness`, ``\
``   `dualLivenessWithInsertion`, `insertLateReloads`, ``\
``   `removeDeadAssignmentsAndReloads`): ``\
`  Inserts spills and reloads to establish the invariant that`\
`  at a safe call, there are no live variables in registers.`\
`` * `CmmCommonBlockElimZ` (`elimCommonBlocks`): ``\
`  Find blocks in the CFG that are identical; merge them.`\
`` * `CmmContFlowOpt` (`branchChainElimZ`, `removeUnreachableBlocksZ`, ``\
``   `runCmmOpts`): ``\
`  Branch-chain elimination and elimination of unreachable code.`\
`` * `CmmStackLayout` (`SlotEnv`, `liveSlotAnal`, `manifestSP`, `stubSlotsOnDeath`): ``\
`  The live-slot analysis discovers which stack slots are live`\
`  at each basic block.`\
`  We use the results for two purposes:`\
`  stack layout (manifestSP) and info tables (in !CmmBuildInfoTables).`\
``   The function `stubSlotsOnDeath' is used as a debugging pass: ``\
`  it stubs each stack slot when it dies, hopefully causing bad`\
`  programs to fail faster.`\
`` * `CmmBuildInfoTables` (`CAFEnv`, `cafAnal`, `lowerSafeForeignCalls`, ``\
``   `setInfoTableSRT`, `setInfoTableStackMap`): ``\
`  This module is responsible for building info tables.`\
`  Specifically, it builds the maps of live variables (stack maps)`\
`  and SRTs.`\
`  It also has code to lower safe foreign calls into a sequence`\
`  that makes them safe (but suspending and resuming threads very carefully).`\
`  (JD: The latter function probably shouldn't be here.)`

### Linking the pipeline

`` * `CmmCvt`: Converts between `Cmm` and `ZipCfgCmm` representations. ``\
`  (JD: The Zip -> Cmm path definitely works; haven't tried the`\
`  other in a long time -- there's no reason to use it with`\
`  the new Stg -> Cmm path).`\
`` * `CmmCPSZ`: Links the phases of the back end in sequence, along with ``\
`  some possible debugging output.`

### Dead code

`` * `CmmCPSGen`, `CmmCPS` (Michael Adams), `CmmBrokenBlock`, `CmmLive`, `CmmPprCmmZ`, `StackColor`, `StackPlacements` ``

Historical page
---------------

This page stores historical information about Cmm Pipeline in the new
code generator. This description has been updated and is maintained on
the \[wiki:Commentary/Compiler/CodeGen Code Generator\] page. This page
has also historical notes about Adams optimisation. That optimisation is
also described in Note \[sharing continuations\] in
[GhcFile(compiler/codeGen/StgCmmMonad.hs)](GhcFile(compiler/codeGen/StgCmmMonad.hs) "wikilink")
and probably deserves its own wiki page.

Design of the new code generator
================================

This page contains notes about the design of the new code generator. See
also: \[wiki:Commentary/Compiler/NewCodeGenModules overview of the
module structure in the new code generator\].

Overview
--------

Code generation now has three stages:

` 1. Convert STG to Cmm, with implicit stack implicit, and native Cmm calls.`\
` 2. Optimise the Cmm, and CPS-convert it to have an explicit stack, and no native calls.`\
``     This part of the pipeline is stitched together in `cmm/CmmPipeline.hs`. ``\
` 3. Feed the CPS-converted Cmm to the existing, unmodified native code generators.`

Ultimately our plan is to expand the capability of the new pipeline so
that it does native code generation too, and we can ultimately discard
the existing code generators. The design of this stage is here:
\[wiki:Commentary/Compiler/IntegratedCodeGen\]

The Cmm pipeline
----------------

The first two steps are described in more detail here:

`* `**`Code`
`generator`**``  converts STG to `CmmGraph`.  Implemented in `StgCmm*` modules (in directory `codeGen`).  ``\
``   * `Cmm.CmmGraph` is pretty much a Hoopl graph of `CmmNode.CmmNode` nodes. Control transfer instructions are always the last node of a basic block. ``\
``   * Parameter passing is made explicit; the calling convention depends on the target architecture.  The key function is `CmmCallConv.assignArgumentsPos`.  ``\
`    * Parameters are passed in virtual registers R1, R2 etc. [These map 1-1 to real registers.] `\
`    * Overflow parameters are passed on the stack using explicit memory stores, to locations described abstractly using the [wiki:Commentary/Compiler/StackAreas `*`Stack`
`Area`*` abstraction.].   `\
``     * Making the calling convention explicit includes an explicit store instruction of the return address, which is stored explicitly on the stack in the same way as overflow parameters. This is done (obscurely) in `MkGraph.mkCall`. ``

`* `**`Simple` `control` `flow`
`optimisation`**`` , implemented in `CmmContFlowOpt`.  It's called both at the beginning and end of the pipeline. ``\
`  * Branch chain elimination.`\
`  * Remove unreachable blocks.`\
`  * Block concatenation.  branch to K; and this is the only use of K.  `

`* `**`More` `control` `flow` `optimisations`**`.`\
`  * Common Block Elimination (like CSE). This essentially implements the Adams optimisation, we believe.`\
`  * Consider (sometime): block duplication.  branch to K; and K is a short block.  Branch chain elimination is just a special case of this.`

`* `**`Proc-point`
`analysis`**` and `**`transformation`**`` , implemented in `CmmProcPoint`. The transformation part adds a function prologue to the front of each proc-point, following a standard entry convention. ``\
``    * The analysis produces a set of `BlockId` that should become proc-points ``\
`   * The transformation inserts a function prologue at the start of each proc-point, and a function epilogue just before each branch to a proc-point.`

`* `**`(OUTDATED` `-` `!CmmSpillReload` `does` `not` `exist` `any`
`more)`**` `**`Add`
`spill/reload`**`` , implemented in `CmmSpillReload`, to spill live C-- variables before a call and reload them afterwards.  The spill and reload instructions are simply memory stores and loads respectively, using symbolic stack offsets (see [wiki:Commentary/Compiler/StackAreas#Layingoutthestack stack layout]).  For example, a spill of variable 'x' would look like `Ptr32[SS(x)] = x`. ``\
``   * `dualLivenessWithInsertion` does two things: ``\
`    * Spills at the definition of any variable that is subequently live across a call (uses a backward analysis)`\
`    * Adds a reload at each return (or proc) point`\
``   At this point, no (`LocalReg`) variables are live across a call. ``\
``   * TODO: avoid  `f();g()` turning into `spill x; f(); reload x; spill x; g(); reload x`. ``

`* `**`(OUTDATED` `-` `!CmmRewriteAssignments` `is` `not` `used` `any`
`more)`**` `**`Rewrite`
`assignments`**` (assignments to local regs, that is, not stores). `\
``   * Convert graph to annotated graph whose nodes are `CmmRewriteAssignments.WithRegUsage`.  Specifically, `CmmAssign` is decorated with a flag `RegUsage` saying whether it is used once or many times. ``\
`  * Sink or inline assignments nearer their use points`\
`  * Do constant mach-op folding. This is done in this phase, because folded mach-ops can be inlined, and inlining exposes opportunities for mach-op folding.`

`* `**`Remove` `dead` `assignments` `and`
`stores`**``` , implemented in `CmmLive`, removes assignments to dead variables and things like ``a = a`` or ``I32[Hp] = I32[Hp]``. The latter may more appropriately be done in a general optimization pass, as it doesn't take advantage of liveness information. ```

`* `**`Figure` `out` `the` `stack`
`layout`**`` , implemented in `CmmStackLayout`. ``\
`  * Each variable 'x', and each proc-point label 'K', has an associated `*`Area`*`, written SS(x) and SS(k) resp, that names a contiguous portion of the stack frame.  `\
`  * The stack layout pass produces a mapping of: `*`` (`Area` `` `->`
`` `StackOffset`) ``*`. For more detail, see [wiki:Commentary/Compiler/StackAreas#Layingoutthestack the description of stack layout.]`\
``   * A `StackOffset` is the byte offset of a stack slot from the old end (high address) of the frame.  It doesn't vary as the physical stack pointer moves. ``

`* `**`Manifest` `the` `stack`
`pointer`**`` , implemented in `CmmStackLayout`.  Once the stack layout mapping has been determined, a second pass walks over the graph, making the stack pointer, `Sp` explicit. Before this pass, there is no `Sp` at all.  After this, `Sp` is completely manifest. ``\
``   * replacing references to `Areas` with offsets from `Sp`. ``\
``   * adding adjustments to `Sp`. ``\
\
`* `**`Split` `into` `multiple`
`!CmmProcs`**`` , implemented in `CmmProcPointZ`.  At this point we build an info-table for each of the !CmmProcs, including SRTs.  Done on the basis of the live local variables (by now mapped to stack slots) and live CAF statics. ``\
``   * `LastCall` and `LastReturn` nodes are replaced by `Jump`s. ``

`* `**`Build` `info`
`tables`**`` , implemented in `CmmBuildInfoTables`..   ``\
``   * Find each safe `MidForeignCall` node, "lowers" it into the suspend/call/resume sequence (see `Note [Foreign calls]` in `CmmNode.hs`.), and build an info table for them. ``\
``   * Convert the `CmmInfo` for each `CmmProc` into a `[CmmStatic]`, using the live variable information computed just before "Figure out stack layout".   ``

### Branches to continuations and the "Adams optimisation"

A GC block for a heap check after a call should only take one or two
instructions. However the natural code: The label M is the head of the
call-gc-and-try-again loop. If we do this, we'll generate two info
tables, one for L and one for K.

We can do better like this:

Now the call has the same return signature as and can use the same
continuation, thus: Now we can coalesce the uniquely-used block M into
L, thus: (A call followed by a thus gets optimized down to just the
call.)

Now things are good. Simple common block elimination (CBE) will common
up K and L, so both calls share the same info table.

Runtime system
--------------

`* `**`Garbage` `collector` `entry`
`points`**`` : see `Note [Heap checks]` in `StgCmmHeapery`. ``

`* `**`PAPs`**\
\
`* `**`Update` `frames`**` and `**`exception`
`handling`**`.  Also STM frames.`

`* `**`Primitives`**` can be rewritten:`\
`  * Use parameters`\
`  * In a few cases, use native calls (notably eval)`

NOTE: Historical page
=====================

This page is here for historical reasons. Most of the issues described
here are now fixed (2 Aug 2012), and the new code generator produces
code approximately as good as the old code generator. Any remaining
issues will be made into tickets as necessary. See
\[wiki:Commentary/Compiler/CodeGen Code Generator\] page for an
up-to-date description of the current code generator.

Stupidity in the New Code Generator
===================================

Presently compiling using the new code generator results in a fairly
sizable performance hit, because the new code generator produces
sub-optimal (and sometimes absolutely terrible code.) There are [a lot
of ideas for how to make things
better](http://darcs.haskell.org/ghc/compiler/cmm/cmm-notes); the idea
for this wiki page is to document all of the stupid things the new code
generator is doing, to later be correlated with specific refactorings
and fixes that will hopefully eliminate classes of these stupid things.
The hope here is to develop a sense for what the most endemic problems
with the newly generated code is.

Cantankerous Comparisons
------------------------

FIXED in newcg branch, 15/2/2012

In \`cgrun065\` we have

Which compiles to the nice STG code

But the comparison is compiled into stupid code:

etc.

We're actually converting to a \`Bool\` and then doing an algebraic
case! This is a StgCmm issue, not a pipeline issue.

Dead stack/heap checks
----------------------

FIXED in newcg branch, but in an ad-hoc way (the stack allocator does
it). We probably want to do this as part of a more general optimisation
pass.

See in \`cgrun065\`

Instruction reordering
----------------------

NEW. We should be able to reorder instructions in order to decrease
register pressure. Here's an example from 3586.hs

R1 and Sp probably don't clobber each other, so we ought to use \_cPY
twice in quick succession. Fortunately stg\_IND\_STATIC\_info is a
constant so in this case the optimization doesn't help to much, but in
other cases it might make sense. TODO Find better example

Stack space overuse
-------------------

FIXED in the newcg branch. (stack layout algorithm redesigned)

CONFIRMED. \`T1969.hs\` demonstrates this:

The call area for the jump in cbG is using an extra word on the stack,
but in fact Sp + 0 at the entry of the function immediately becomes dead
after the assignment, so we ought to be able to save some space in our
layout. Simon Marlow suggests we distinguish between the return address
and the old call area; however, since this can also happen for the
return parameters from call areas, we need a more general scheme.

After I discussed this with SPJ, we've decided that we need to teach the
stack layout how to handle partial conflicts. There is a complication
here, in that if we do this naively, the interference graph will blow up
(since, rather than conflicting call areas, we now have conflicting
words of call areas.) Simon suggested that we bound the amount of
conflicts we track: either up to 3 or conflict with everything (in which
case we just place the area as far down as necessary rather than try to
be clever.) I plan on doing this once I understand the current layout
code...

Double temp-use means no inlinining?
------------------------------------

CONFIRMED. Here's a curious piece of code that fails to get inlined
(from \`cc004\`):

Why is that? Because the temp gets reused later on:

In this case, we want more aggressive inlining because there are too
many temps and they're going to have to get spilled to the stack anyway.
IS THAT TRUE? For comparison's sake, the old codegen doesn't appear to
do any rewriting, because it just reuses the call area.

Stupid spills
-------------

CONFIRMED. If something is already in memory, why do we have to spill it
again?

Well, it's because the spiller isn't clever enough:

Ick! The old codegen was much better...

The trouble is that the spiller doesn't know that the old call area is
also valid game for locations that variables can live in. So, the
solution is to rewrite the spiller to know about existing incoming
memory locations. Make sure that this information gets to the stack
layout engine when we do partial layouts (it should automatically
notice, but double check!)

Noppy proc-points
-----------------

CONFIRMED. Consider

We generate an extra proc-point for \`\`cmM\`\`, where in theory we
ought to be able to stick the subsequent \`\`stg\_ap\_pp\_fast\`\` onto
the stack as another return point.

Lots of temporary variables
---------------------------

WONTFIX. Lots of temporary variables (these can tickle other issues when
the temporaries are long-lived, but otherwise would be optimized away).
You can at least eliminate some of them by looking at the output of
\`-ddump-opt-cmm\`, which utilizes some basic temporary inlining when
used with the native backend \`-fasm\`, but this doesn't currently apply
to the GCC or LLVM backends.

\~\~At least one major culprit for this is \`allocDynClosure\`,
described in Note \`Return a LocalReg\`; this pins down the value of the
\`CmmExpr\` to be something for one particular time, but for a vast
majority of use-cases the expression is used immediately afterwards.
Actually, this is mostly my patches fault, because the extra rewrite
means that the inline pass is broken.\~\~ Fixed in latest version of the
pass; we don't quite manage to inline enough but there's only one extra
temporary.

Another cause of all of these temporary variables is that the new code
generator immediately assigns any variables that were on the stack to
temporaries immediately upon entry to a function. This is on purpose.
The idea is we optimize these temporary variables away.

Double proc points
------------------

FIXED in newcg branch.

Given a simple case expression

we generate \*two\* proc points, not one.

Both \`cbE\` and \`cbW\` are going to become proc points.

To avoid it we should generate code that re-uses \`cbE\` as the
destination for the first \`if\`; that is, we need to load up the
registers as if we were returning from the call. This needs some
refactoring in the code generator.

Rewriting stacks
----------------

FIXED. \`3586.hs\` emits the following code:

We see that these temporary variables are being repeatedly rewritten to
the stack, even when there are no changes.

Since these areas on the stack are all old call areas, one way to fix
this is to inline all of the memory references. However, this has
certain undesirable properties for other code, so we need to be a little
more clever. The key thing to notice is that these accesses are only
used once per control flow path, in which case sinking the loads down
and then inlining them should be OK (it will increase code size but not
execution time.) However, the other difficulty is that the CmmOpt
inliner, as it stands, won't inline things that look like this because
although the variable is only used once in different branches, the same
name is used, so it can't distinguish between the temporaries with
mutually exclusive live ranges. Building a more clever inliner with
Hoopl is also a bit tricky, because inlining is a forward
analysis/transformation, but usage counting is a backwards analysis.

This looks fixed with the patch from April 14.

Spilling Hp/Sp
--------------

FIXED. \`3586.hs\` emits the following code:

We see \`Hp - 4\` being allocated to a temp, and then consequently being
spilled to the stack even though \`newCAF\` definitely will not change
\`Hp\`, so we could have floated the expression down.

This seems to happen whenever there's a \`newCAF\` ccall.

We also seem to reload these values multiple times.

\~\~We need to not spill across certain foreign calls, but for which
calls this is OK for is unclear.\~\~ Variables stay live across all
unsafe foreign calls (foreign calls in the middle), except for the
obvious cases (the return registers), so no spilling should happen at
all. The liveness analysis is too conservative.

This is not fixed in the April 14 version of the patch... we still need
to fix the liveness analysis? I thought I fixed that... that's because
the transform did extra spilling for CmmUnsafeForeignCalls. Removed that
code, and now it's fixed.

Up and Down
-----------

FIXED. A frequent pattern is the stack pointer being bumped up and then
back down again, for no particular reason.

This is mentioned at the very top of \`cmm-notes\`. This was a bug in
the stack layout code that I have fixed.

Sp is generally stupid
----------------------

FIXED. Here is an optimized C-- sample from \`arr016.hs\`.

Compare with the old code:

You can see the up and down behavior here, but that's been fixed, so
ignore it for now. (Update the C--!) The unfixed problem is this (some
of the other problems were already addressed): we do an unnecessary
stack check on entry to this function. We should eliminate the stack
check (and by dead code analysis, the GC call) in such cases.

This pattern essentially happens for every function, since we always
assign incoming parameters to temporary variables before doing anything.

Heap and R1 aliasing
--------------------

FIXED. Values on the heap and values from R1 don't necessarily clobber
each other. allocDynClosure seems like a pretty safe bet they don't. But
is this true in general? ANSWER: Memory writes with Hp are always new
allocations, so they don't clobber anything.

Historical page
---------------

This page stores notes about progress of work on the "new" code
generator. This page is here for historical reasons. See
\[wiki:Commentary/Compiler/CodeGen Code Generator\] page for an
up-to-date description of the current code generator.

GHC's glorious new code generator
=================================

This page summarises work that Norman Ramsey, Simon M, Simon PJ, and
John Dias are doing on re-architecting GHC's back end. Here is the state
of play; see also \[wiki:Commentary/Compiler/Backends/LLVM work on the
LLVM back end\].

`* Bug list (code-gen related bugs that we may be able to fix):`\
`  * #1498 (avoid redundant heap check on the fast path)`\
`  * #3552 (unreachable code)`\
`  * #3462 (a feature)`\
`  * #2249`\
`  * #2253`\
`  * #2289`\
`  * #7219 (reinstate constant-prop)`\
`  * #7213 (massive array)`

`* (Sept 12) New code generator is live.  Here's the [wiki:Commentary/Compiler/NewCodeGen/Cleanup page listing clean-up tasks] that we can now do.`

`* Simon M added a [blog:newcg-update Blog Post] about the new code generator status`

`* Link to `[`Krzysztof` `Wos's`
`project`](http://research.microsoft.com/en-us/um/people/simonpj/tmp/wos-diss-draft.pdf)`, in which he reports great performance improvements by turning tail recursion into loops in C--.`

`* Norman added a [wiki:Commentary/Compiler/HooplPerformance Hoopl performance page]`

`* Edward Yang has a wiki page that describes shortcomings of the code generated by the new pipeline: [wiki:Commentary/Compiler/NewCodeGenStupidity]`

`` * John D has built a complete new codegen pipeline, running alongside the old one, enabled by `-fuse-new-codegen`. It is described here: [wiki:Commentary/Compiler/NewCodeGenPipeline].  It uses a new representation for `Cmm`, mostly with "Z" in the name.  (Let's call the original Cmm `OldCmm` and this new one `CmmZ`.)  It has a new conversion STG->CmmZ, and then sequence of passes that optimise and cps-convert the Cmm.  Finally, it is converted back to the old Cmm so that it can flow to the old code generators. ``

`* Compiling through the new pipeline passes all tests and GHC is bootstrappable.`

`` * Separately, we have developed yet another, and still better, Cmm representation, the subject of an upcoming ICFP 2010 submission.  It uses phantom types and GADTs to add very useful open/closed invariants.  This isn't in GHC at all yet.  I'll call it `CmmGADT` for easy reference. ``

Generally we want to keep old and new pipelines working simultaneously,
so that we can switch only when we are sure the new stuff works. Next
steps in this grand plan are:

`* Check the impact on compilation time of the new route.`

`` * Finalise `CmmGADT` and make the new pipeline use it. ``

`` * Make the Cmm parser (which parses `.cmm` files from the RTS) produce `CmmGADT`, and push that down the new pipeline. ``

`* Implement the many refactorings and improvements to the new pipeline described in `[`http://darcs.haskell.org/ghc/compiler/cmm/cmm-notes`](http://darcs.haskell.org/ghc/compiler/cmm/cmm-notes)`. See also: [wiki:Commentary/Compiler/NewCodeGenStupidity]`

`` * Instead of converting new Cmm to old Cmm, make the downstream code generators consume `CmmGADT`, and convert old Cmm to `CmmGADT`. ``

Longer term

`* Expand the capability of the new pipeline so that it does native code generation too, and we can ultimately discard the existing code generators.  The design of this stage is here: [wiki:Commentary/Compiler/IntegratedCodeGen]`

Workflow for the new code generator and Hoopl
---------------------------------------------

We have the following repositories:

`` * HEAD: the main GHC git repo. `http://darcs.haskell.org/ghc.git` ``

`* !HooplMaster: the master Hoopl Git repository.`\
`  `[`BR`](BR "wikilink")` `**`Location`**`` : `http://ghc.cs.tufts.edu/hoopl/hoopl.git/` ``\
`  `[`BR`](BR "wikilink")``  (Physical location: `linux.cs.tufts.edu:/r/ghc/www/hoopl/hoopl.git`) ``

`* !HooplLag: a Git repo that is guaranteed to work with GHC HEAD.    It is`\
`  not automatically updated by pushes to !HooplMaster.  Instead a manual`\
`  process (below) updates it; hence "lag".`\
`  `[`BR`](BR "wikilink")` `**`Location`**`` : `http://darcs.haskell.org/packages/hoopl.git`. ``

Normal GHC developers, who are uninterested in Hoopl, ignore all this.
If they download HEAD including all submodules, they'll get !HooplLag,
which is always guaranteed to work with HEAD.

Developers who work on GHC and also need to modify Hoopl need to ensure
their changes end up in both repositories.

`* In your hoopl directory in your development tree, add !HooplMaster as a remote and update your reference there. `\
`* Hack away in the development tree.`\
`* Record Hoopl commits.`\
`* Run validate in the development tree`\
`* Push the commits in hoopl to the !HooplMaster Git repo`\
`` * Wait for the mirrors to update (the impatient can run `/srv/darcs/do_mirrors` on darcs.haskell.org) ``\
`* Push the commits in hoopl to the !HooplLag Git repo (probably the origin remote)`

Status report April 2011
------------------------

Term

Old Code Generator (prior to GHC 7.8)
=====================================

Material below describes old code generator that was used up to GHC 7.6
and was retired in 2012. This page is not maintained and is here only
for historical purposes. See \[wiki:Commentary/Compiler/CodeGen Code
generator\] page for an up to date description of the current code
generator.

Storage manager representations
-------------------------------

See \[wiki:Commentary/Rts/Storage The Storage Manager\] for the
\[wiki:Commentary/Rts/Storage/Stack Layout of the stack\].

The code generator needs to know the layout of heap objects, because it
generates code that accesses and constructs those heap objects. The
runtime also needs to know about the layout of heap objects, because it
contains the garbage collector. How can we share the definition of
storage layout such that the code generator and the runtime both have
access to it, and so that we don't have to keep two independent
definitions in sync?

Currently we solve the problem this way:

`* C types representing heap objects are defined in the C header files, see for example `[`GhcFile(includes/rts/storage/Closures.h)`](GhcFile(includes/rts/storage/Closures.h) "wikilink")`.`

`* A C program, `[`GhcFile(includes/mkDerivedConstants.c)`](GhcFile(includes/mkDerivedConstants.c) "wikilink")`` ,  `#includes` the runtime headers. ``\
``   This program is built and run when you type `make` or `make boot` in `includes/`.  It is ``\
``   run twice: once to generate `includes/DerivedConstants.h`, and again to generate  ``\
``   `includes/GHCConstants.h`. ``

`` * The file `DerivedConstants.h` contains lots of `#defines` like this: ``

``   which says that the offset to the why_blocked field of an `StgTSO` is 18 bytes.  This file ``\
``   is `#included` into  ``[`GhcFile(includes/Cmm.h)`](GhcFile(includes/Cmm.h) "wikilink")`, so these offests are available to the`\
`  [wiki:Commentary/Rts/Cmm hand-written .cmm files].`

`` * The file `GHCConstants.h` contains similar definitions: ``

``  This time the definitions are in Haskell syntax, and this file is `#included` directly into ``\
` `[`GhcFile(compiler/main/Constants.lhs)`](GhcFile(compiler/main/Constants.lhs) "wikilink")`.  This is the way that these offsets are made`\
` available to GHC's code generator.`

Generated Cmm Naming Convention
-------------------------------

See
[GhcFile(compiler/cmm/CLabel.hs)](GhcFile(compiler/cmm/CLabel.hs) "wikilink")

Labels generated by the code generator are of the form where is for
external names and for internal names. is one of the following:

` info::                   Info table`\
` srt::                    Static reference table`\
` srtd::                   Static reference table descriptor`\
` entry::                  Entry code (function, closure)`\
` slow::                   Slow entry code (if any)`\
` ret::                    Direct return address    `\
` vtbl::                   Vector table`\
` `*`n`*`_alt::              Case alternative (tag `*`n`*`)`\
` dflt::                   Default case alternative`\
` btm::                    Large bitmap vector`\
` closure::                Static closure`\
` con_entry::              Dynamic Constructor entry code`\
` con_info::               Dynamic Constructor info table`\
` static_entry::           Static Constructor entry code`\
` static_info::            Static Constructor info table`\
` sel_info::               Selector info table`\
` sel_entry::              Selector entry code`\
` cc::                     Cost centre`\
` ccs::                    Cost centre stack`

Many of these distinctions are only for documentation reasons. For
example, \_ret is only distinguished from \_entry to make it easy to
tell whether a code fragment is a return point or a closure/function
entry.

Modules
-------

### 

Top level, only exports .

Called from for each module that needs to be converted from Stg to Cmm.

For each such module does three things:

`* `` for the `\
`* `` for the `` (These are constructors not constructor calls).`\
`* `` for the module`

 generates several boilerplate initialization functions that:

`* regiser the module,`\
`* creates an Hpc table,`\
`* setup its profiling info (``, code coverage info ``), and`\
`* calls the initialization functions of the modules it imports.`

If neither SCC profiling or HPC are used, then the initialization code
short circuits to return.

If the module has already been initialized, the initialization function
just returns.

The and modules get special treatment.

 is a small wrapper around which in turn disptaches to:

`* `` for `\
`  (these are bindings of constructor applications not constructors themselves) and`\
`* `` for ``.`

 and are located in and which are the primary modules called by .

### 

TODO

### 

TODO

### 

The monad that most of codeGen operates inside

`* Reader`\
`* State`\
`* (could be Writer?)`\
`* fork`\
`* flatten`

### 

Called by and .

Since everything in STG is an expression, almost everything branches off
from here.

This module exports only one function , which for the most part just
dispatches to other functions to handle each specific constructor in .

Here are the core functions that each constructor is disptached to
(though some may have little helper functions called in addition to the
core function):

`:: Calls to `` in `\
`:: Calls to `` in `\
`::`\
`  Calls to `` in `\
`   and `` in `\
`::`\
`  Is a bit more complicated see below.`\
`:: Calls to `` in `\
`:: Calls to `` in `\
`::`\
`  Calls to `` in ``, but with a little bit of wrapping`\
`  by `` and ``.`\
`:: Calls to  `` in `\
`:: Calls to `` in `\
`::`\
`  Does not have a case because it is only for ``'s work.`

Some of these cases call to functions defined in . This is because they
need a little bit of wrapping and processing before calling out to their
main worker function.

`::`\
`* For `` calls out to `` in ``.`\
`* For `` calls out to ``.`\
`  In turn, `` calls out to `` for selectors and thunks,`\
`  and calls out to `` in the default case.`\
`  Both these are defined in ``.`

`::`\
`* Wraps a call to `` with `\
`  depending on whether it is called on a recursive or a non-recursive binding.`\
`  In turn `` wraps `\
`  defined in ``.`

 has a number of sub-cases.

`* `\
`* `` of a !TagToEnumOp`\
`* `` that is primOpOutOfLine`\
`* `` that returns Void`\
`* `` that returns a single primitive`\
`* `` that returns an unboxed tuple`\
`* `` that returns an enumeration type`

(It appears that non-foreign-call, inline \[wiki:Commentary/PrimOps
PrimOps\] are not allowed to return complex data types (e.g. a |Maybe|),
but this fact needs to be verified.)

Each of these cases centers around one of these three core calls:

`* `` in `\
`* `` in `\
`* `` in `

There is also a little bit of argument and return marshelling with the
following functions

`Argument marshelling::`\
`  ``, `\
`Return marshelling::`\
`  ``, ``, `\
`Performing the return::`\
`  ``, ``,`\
`  ``, `

In summary the modules that get called in order to handle a specific
expression case are:

#### Also called for top level bindings by 

`:: for `` and the `` part of `\
`:: for the `` part of `

#### Core code generation

`:: for ``, ``, and `\
`:: for `\
`:: for `\
`:: for `

#### Profiling and Code coverage related

`:: for `\
`:: for `

#### Utility modules that happen to have the functions for code generation

`:: for `\
`:: for `

Note that the first two are the same modules that are called for top
level bindings by , and the last two are really utility modules, but
they happen to have the functions needed for those code generation
cases.

### Memory and Register Management

`::`\
`  Module for `` which maps variable names`\
`  to all the volitile or stable locations where they are stored`\
`  (e.g. register, stack slot, computed from other expressions, etc.)`\
`  Provides the ``, `` and `` functions`\
`  for adding, modifying and looking up bindings.`

`::`\
`  Mostly utility functions for allocating and freeing stack slots.`\
`  But also has things on setting up update frames.`

`::`\
`  Functions for allocating objects that appear on the heap such as closures and constructors.`\
`  Also includes code for stack and heap checks and ``.`

### Function Calls and Parameter Passing

(Note: these will largely go away once CPS conversion is fully
implemented.)

`, ``, ``::`\
`  Handle different types of calls.`\
`::`\
`  Use by the others in this category to determine liveness and`\
`  to select in what registers and stack locations arguments and return`\
`  values get stored.`

### Misc utilities

`::`\
`  Utility functions for making bitmaps (e.g. `` with type ``)`\
`::`\
`  Stores info about closures and bindings.`\
`  Includes information about memory layout, how to call a binding (``)`\
`  and information used to build the info table (``).`\
`::`\
`  Storage manager representation of closures.`\
`  Part of !ClosureInfo but kept separate to "keep nhc happy."`\
`:: TODO`\
`:: TODO`

### Special runtime support

`:: Ticky-ticky profiling`\
`:: Cost-centre profiling`\
`:: Support for the Haskell Program Coverage (hpc) toolkit, inside GHC.`\
`::`\
`  Code generation for !GranSim (GRAN) and parallel (PAR).`\
`  All the functions are dead stubs except `` and ``.`

Ordering the Core-to-Core optimisation passes
=============================================

This page has notes about the ordering of optimisation phases. An
overview of the whole Core-to-Core optimisation pipeline can be found
\[wiki:Commentary/Compiler/Core2CorePipeline here\].

**NOTE:** This is old documentation and may not be very relevant any
more!

This ordering obeys all the constraints except (5)
--------------------------------------------------

`* full laziness`\
`* simplify with foldr/build`\
`* float-in`\
`* simplify`\
`* strictness`\
`* float-in`

\[check FFT2 still gets benefits with this ordering\]

Constraints
-----------

### 1. float-in before strictness

Reason: floating inwards moves definitions inwards to a site at which
the binding might well be strict. The strictness analyser will do a
better job of the latter than the former.

### 2. Don't simplify between float-in and strictness

...unless you disable float-let-out-of-let, otherwise the simiplifier's
local floating might undo some useful floating-in. This is a bad move,
because now y isn't strict. In the pre-float case, the binding for y is
strict. Mind you, this isn't a very common case, and it's easy to
disable float-let-from-let.

### 3. Want full-laziness before foldr/build

Reason: Give priority to sharing rather than deforestation. In the
post-full-laziness case, xs is shared between all applications of the
function. If we did foldr/build first, we'd have got and now we can't
share xs.

### 4. Want strictness after foldr/build

Reason: foldr/build makes new function definitions which can benefit
from strictness analysis. Here we clearly want to get strictness
analysis on g.

### 5. Want full laziness after strictness

Reason: absence may allow something to be floated out which would not
otherwise be. TOO BAD. This doesn't look a common case to me.

### 6. Want float-in after foldr/build

Reason: Desugaring list comprehensions + foldr/build gives rise to new
float-in opportunities. Now v could usefully be floated into the second
branch.

### 7. Want simplify after float-inwards

(Occurred in the prelude, compiling \`ITup2.hs\`, function
\`dfun.Ord.(\*,\*)\`) This is due to the following (that happens with
dictionaries): floating inwards will push the definition of a1 into m1
(supposing it is only used there): if we do strictness analysis now we
will not get a worker-wrapper for m1, because of the "let a1 ..."
(notice that a1 is not strict in its body).

Not having this worker wrapper might be very bad, because it might mean
that we will have to rebox arguments to m1 if they are already unboxed,
generating extra allocations, as occurs with m2 (cc) above.

To solve this problem we have decided to run the simplifier after
float-inwards, so that lets whose body is a HNF are floated out, undoing
the float-inwards transformation in these cases. We are then back to the
original code, which would have a worker-wrapper for m1 after strictness
analysis and would avoid the extra let in m2.

What we lose in this case are the opportunities for case-floating that
could be presented if, for example, a1 would indeed be demanded (strict)
after the floating inwards.

The only way of having the best of both is if we have the worker/wrapper
pass explicitly called, and then we could do with

`* float-in`\
`* strictness analysis`\
`* simplify`\
`* strictness analysis`\
`* worker-wrapper generation`

as we would

`* be able to detect the strictness of m1 after the first call to the strictness analyser, and exploit it with the simplifier (in case it was strict).`\
`* after the call to the simplifier (if m1 was not demanded) it would be floated out just like we currently do, before stricness analysis II and worker/wrapperisation.`

The reason to not do worker/wrapperisation twice is to avoid generating
wrappers for wrappers which could happen.

### 8. If full laziness is ever done after strictness

...remember to switch off demandedness flags on floated bindings! This
isn't done at the moment.

### 9. Ignore-inline-pragmas flag for final simplification

\[Occurred in the prelude, compiling ITup2.hs, function
dfun.Ord.(\*,\*)\] Sometimes (e.g. in dictionary methods) we generate
worker/wrappers for functions but the wrappers are never inlined. In
dictionaries we often have and if we create worker/wrappers for
f1,...,fn the wrappers will not be inlined anywhere, and we will have
ended up with extra closures (one for the worker and one for the
wrapper) and extra function calls, as when we access the dictionary we
will be acessing the wrapper, which will call the worker. The simplifier
never inlines workers into wrappers, as the wrappers themselves have
INLINE pragmas attached to them (so that they are always inlined, and we
do not know in advance how many times they will be inlined).

To solve this problem, in the last call to the simplifier we will ignore
these inline pragmas and handle the workers and the wrappers as normal
definitions. This will allow a worker to be inlined into the wrapper if
it satisfies all the criteria for inlining (e.g. it is the only
occurrence of the worker etc.).

### 10. Run Float Inwards once more after strictness-simplify

\[Occurred in the prelude, compiling \`IInt.hs\`, function
\`const.Int.index.wrk\`\] When workers are generated after strictness
analysis (worker/wrapper), we generate them with "reboxing" lets, that
simply reboxes the unboxed arguments, as it may be the case that the
worker will need the original boxed value: in this case the simplifier
will remove the binding for y as it is not used (we expected this to
happen very often, but we do not know how many "reboxers" are eventually
removed and how many are kept), and will keep the binding for x. But
notice that x is only used in \*one\* of the branches in the case, but
is always being allocated! The floating inwards pass would push its
definition into the True branch. A similar benefit occurs if it is only
used inside a let definition. These are basically the advantages of
floating inwards, but they are only exposed after the
S.A./worker-wrapperisation of the code! As we also have reasons to float
inwards before S.A. we have to run it twice.

Overall organisation of GHC
===========================

Start at the [GHC home page](http://haskell.org/ghc). The most important
links are in the left-hand column:

`* `[`Documentation`](http://haskell.org/haskellwiki/GHC)`.  This is the `*`user`*` documentation, aimed at people who use GHC, but don't care how it works.  It's on the Haskell Wiki (powered by MediaWiki), and we strongly encourage people to edit and improve it.`

`* `[`Developers`](http://hackage.haskell.org/trac/ghc)`.  This link takes you to the home page for `*`developers`*`; that is, people interested in hacking on GHC itself (i.e. you).  It's a Wiki too, but powered by Trac, and includes bug-tracking etc.  There is a big section called Developer Documentation: `**`please`
`help` `us` `to` `improve` `it`**`.`

`* `[`Download`](http://www.haskell.org/ghc/download.html)`.  At any moment, GHC has a `**`STABLE`
`branch`**` and the `**`HEAD`**`, both of which you can download from this page.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  * The STABLE branch is the current released version.  It has an even version number (e.g. 6.4, 6.6), with an extra suffix for patch-level release (e.g. 6.4.2).  Patch-level releses fix bugs; they do not change any APIs.`[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
`  * The HEAD is simply the latest, greatest version that we are working on; it may be broken on any given day, although you are encouraged not to break it gratuitiously.  The HEAD has an odd version numbers (e.g 6.5, 6.7).  Every night we build the HEAD, and dump the result on the download site under "Development snapshots", with a version number that encodes the date (e..g 6.5.20060831).`

`  A very useful link on the download page is the `[`documentation`
`for` `the`
`HEAD`](http://www.haskell.org/ghc/dist/current/docs/)` (under Development snapshots).  Useful because typesetting the documentation uses DocBook, which easy to install on every platform.`

GHC source code
===============

GHC's source code is several Darcs repositories. The important ones are:

<http://darcs.haskell.org/ghc>:: All of GHC: compiler, run-time system,
support utilities.

<http://darcs.hasekll.org/packages/pkg>:: A library package *pkg*. A
certain number of packages are essential to build GHC. They are listed
in and currently comprise: , , , , , , , , , , , .

<http://darcs.haskell.org/testsuite>:: GHC's test suite.

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
` `<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\
` `<meta http-equiv="Content-Style-Type" content="text/css" />\
` `<meta name="generator" content="pandoc" />\
` `

<title>
</title>
<style type="text/css">
code{white-space: pre;}

</style>
</head>
<body>
<div id="TOC">
-   <a href="#the-ghc-commentary-checking-types">The GHC Commentary:
    Checking Types</a>
    -   <a href="#the-overall-flow-of-things">The Overall Flow of
        Things</a>
        -   <a href="#entry-points-into-the-type-checker">Entry Points
            Into the Type Checker</a>
        -   <a href="#renaming-and-type-checking-a-module">Renaming and
            Type Checking a Module</a>
    -   <a href="#type-checking-a-declaration-group">Type Checking a
        Declaration Group</a>
    -   <a href="#type-checking-type-and-class-declarations">Type
        checking Type and Class Declarations</a>
    -   <a href="#more-details">More Details</a>
        -   <a href="#types-variables-and-zonking">Types Variables and
            Zonking</a>
        -   <a href="#type-representation">Type Representation</a>
        -   <a href="#type-checking-environment">Type Checking
            Environment</a>
        -   <a href="#expressions">Expressions</a>
        -   <a href="#handling-of-dictionaries-and-method-instances">Handling
            of Dictionaries and Method Instances</a>
    -   <a href="#connection-with-ghcs-constraint-solver">Connection
        with GHC's Constraint Solver</a>
    -   <a href="#generating-evidence">Generating Evidence</a>
    -   <a href="#the-solver">The Solver</a>
        -   <a href="#given-constraints">Given Constraints</a>
        -   <a href="#derived-constraints">Derived Constraints</a>
        -   <a href="#wanted-constraints">Wanted Constraints</a>

</div>
<h1 id="the-ghc-commentary-checking-types">
The GHC Commentary: Checking Types

</h1>
Probably the most important phase in the frontend is the type checker,
which is located at
<a href="GhcFile(compiler/typecheck/)" class="uri" title="wikilink">GhcFile(compiler/typecheck/)</a>.
GHC type checks programs in their original Haskell form before the
desugarer converts them into Core code. This complicates the type
checker as it has to handle the much more verbose Haskell AST, but it
improves error messages, as those message are based on the same
structure that the user sees.

GHC defines the abstract syntax of Haskell programs in
<a href="GhcModule(compiler/hsSyn/HsSyn.lhs)" class="uri" title="wikilink">GhcModule(compiler/hsSyn/HsSyn.lhs)</a>
using a structure that abstracts over the concrete representation of
bound occurences of identifiers and patterns. The module
<a href="GhcModule(compiler/typecheck/TcHsSyn.lhs)" class="uri" title="wikilink">GhcModule(compiler/typecheck/TcHsSyn.lhs)</a>
defines a number of helper function required by the type checker. Note
that the type
<a href="GhcModule(compiler/typecheck/TcRnTypes.lhs)" class="uri" title="wikilink">GhcModule(compiler/typecheck/TcRnTypes.lhs)</a>.\`TcId\`
used to represent identifiers in some signatures during type checking
is, in fact, nothing but a synonym for a
\[wiki:Commentary/Compiler/EntityTypes\#Typevariablesandtermvariables
plain Id\].

It is also noteworthy, that the representations of types changes during
type checking from \`HsType\` to \`TypeRep.Type\`. The latter is a
\[wiki:Commentary/Compiler/TypeType hybrid type\] representation that is
used to type Core, but still contains sufficient information to recover
source types. In particular, the type checker maintains and compares
types in their \`Type\` form.

<h2 id="the-overall-flow-of-things">
The Overall Flow of Things

</h2>
<code>\*

Updates
=======

Source files: $$\[GhcFile(rts/Updates.h)$$\\\],
$$\[GhcFile(rts/Updates.cmm)$$\\\]

----CategoryStub

.. contents::

`  :depth: 3`

..

Unique
------

\`\`Unique\`\`\\ s provide a fast comparison mechanism for more complex
things. Every \`\`RdrName\`\`, \`\`Name\`\`, \`\`Var\`\`, \`\`TyCon\`\`,
\`\`TyVar\`\`, etc. has a \`\`Unique\`\`. When these more complex
structures are collected (in \`\`UniqFM\`\`\\ s or other types of
collection), their \`\`Unique\`\` typically provides the key by which
the collection is indexed.

+----------------------------+ | == Current design == |
+----------------------------+ | A \`\`Unique\`\` consists of | | the
*domain* of the | | thing it identifies and a | | unique integer value |
| 'within' that domain. The | | two are packed into a | | single
\`\`Int\#\`\`, with the | | *domain* being the top 8 | | bits. |
+----------------------------+ | The domain is never | | inspected (SLPJ
believes). | | The sole reason for its | | existence is to provide a | |
number of different ranges | | of \`\`Unique\`\` values that | | are
guaranteed not to | | conflict. | +----------------------------+ | ===
Lifetime | +----------------------------+ | The lifetime of a | |
\`\`Unique\`\` is a single | | invocation of GHC, i.e. | | they must not
'leak' to | | compiler output, the | | reason being that | |
\`\`Unique\`\`\\ s may be | | generated/assigned | |
non-deterministically. | | When compiler output is | |
non-deterministic, it | | becomes significantly | | harder to, for
example, | | \[wiki:Commentary/Compiler/ | | RecompilationAvoidance | |
avoid recompilation\]. | | Uniques do not get | | serialised into .hi
files, | | for example. | +----------------------------+ | Note, that
"one compiler | | invocation" is not the | | same as the compilation of
| | a single \`\`Module\`\`. | | Invocations such as | | \`\`ghc
--make\`\` or | | \`\`ghc --interactive\`\` give | | rise to longer
invocation | | life-times. | +----------------------------+ | This is
also the reasons | | why \`\`OccName\`\`\\ s are | | *not* ordered based
on | | the \`\`Unique\`\`\\ s of their | | underlying | |
\`\`FastString\`\`\\ s, but | | rather | | *lexicographically* (see | |
[ | pes/OccName.lhs)](GhcFile(compiler/basicTy "wikilink") | | for
details). &gt; &gt; | | **SLPJ:** I am far from | | sure that the Ord
instance | | for \`\`OccName\`\` is ever | | used, so this remark is | |
probably misleading. Try | | deleting it and see where | | it is used
(if at all). &gt; | | **PKFH:** At least | | \`\`Name\`\` and
\`\`RdrName\`\` | | (partially) define their | | own \`\`Ord\`\`
instances in | | terms of the instance of | | \`\`OccName\`\`. Maybe
these | | \`\`Ord\`\` instances are also | | redundant, but for now it |
| seems wise to keep them | | in. When everything has | | \`\`Data\`\`
instances (after | | this and many other | | redesigns), I'm sure it | |
will be easier to find | | such dependency relations. |
+----------------------------+ | === Known-key things === |
+----------------------------+ | A hundred or two library | | entities
(types, classes, | | functions) are so-called | | "known-key things".
See | | \[wiki:Commentary/Compiler/ | | WiredIn | | this page\]. A
known-key | | thing has a fixed | | \`\`Unique\`\` that is fixed | |
when the compiler is | | built, and thus lives | | across all
invocations of | | that compiler. These | | known-key \`\`Unique\`\`\\ s
| | *are* written into .hi | | files. But that's ok | | because they are
fully | | deterministic and never | | change. |
+----------------------------+ | &gt; **PKFH** That's fine | | then; we
also know for | | sure these things fit in | | the 30 bits used in the |
| \`\`hi\`\`-files. I'll comment | | appropriately. |
+----------------------------+ | === Interface files === |
+----------------------------+ | Entities in a interface | | file (.hi
file) are, for | | the most part, stored in a | | symbol table, and
referred | | to (from elsewhere in the | | same interface file) by an |
| index into that table. | | Here are the details from | | [ |
inIface.lhs)](GhcFile(compiler/iface/B "wikilink"): | |

------------------------------------------------------------------------

Redesign (2014)
---------------

=== TL;DR The redesign is to accomplish the following: \\\* Allow
derivation of type class instances for \`\`Unique\`\` \\\* Restore
invariants from the original design; hide representation details \\\*
Eliminate violations of invariants and design-violations in other places
of the compiler (e.g. \`\`Unique\`\`\\ s shouldn't be written to
\`\`hi\`\`-files, but are). &gt; &gt; **SLPJ** I don't think this is a
design violation; see above. Do you have any other examples in mind?
&gt; **PKFH** Not really of design-violations (and no other
compiler-output stuff) other than the invariants mentioned above it,
just yet. The key point, though, is that there are a lot of comments in
\`\`Unique\`\` about not exporting things so that we know X, Y and Z,
but then those things *are* exported, so we don't know them to be true.
Case in point is the export of \`\`mkUnique\`\`, but also
\`\`mkUniqueGrimily\`\`. The latter has a comment 'only for
\`\`UniqSupply\`\`' but is also used in other places (like Template
Haskell). One redesign is to put this restriction in the name, so there
still is the facility offered by \`\`mkUniqueGrimily\`\`, but now it's
called \`\`mkUniqueOnlyForUniqSupply\`\` (and
\`\`mkUniqueOnlyForTemplateHaskell\`\`), the ugliness of which should
help, over time, to get rid of them.

=== Longer

In an attempt to give more of GHC's innards well-behaved instances of
\`\`Typeable\`\`, \`\`Data\`\`, \`\`Foldable\`\`, \`\`Traversable\`\`,
etc. the implementation of \`\`Unique\`\`\\ s was a bit of a sore spot.
They were implemented (20+ years earlier) using custom boxing, viz.
making automatic derivation of such type class instances hard. There was
already a comment asking why it wasn't simply a \`\`newtype\`\` around a
normal (boxed) \`\`Int\`\`. Independently, there was some discussion on
the mailinglists about the use of (signed) \`\`Int\`\`\\ s in places
where \`\`Word\`\`\\ s would be more appropriate. Further inspection of
the \`\`Unique\`\` implementation made clear that a lot of invariants
mentioned in comments had been violated by incremental edits. This is
discussed in more detail below, but these things together (the desire
for automatic derivation and the restoration of some important
invariants) motivated a moderate redesign.

=== Status Quo (pre redesign)

A \`\`Unique\`\` has a domain (\`\`TyCon\`\`, \`\`DataCon\`\`,
\`\`PrelName\`\`, \`\`Builtin\`\`, etc.) that was codified by a
character. The remainder of the \`\`Unique\`\` was an integer that
should be unique for said domain. This **was** once guaranteed through
the export list of
[GhcFile(compiler/basicTypes/Unique.lhs)](GhcFile(compiler/basicTypes/Unique.lhs) "wikilink"),
where direct access to the domain-character was hidden, i.e. were not
exported. This should have guaranteed that every domain was assigned its
own unique character, because only in
[GhcFile(compiler/basicTypes/Unique.lhs)](GhcFile(compiler/basicTypes/Unique.lhs) "wikilink")
could those \`\`Char\`\`\\ s be assigned. However, through this
separation of concerns leaked out to
[GhcFile(compiler/basicTypes/UniqSupply.lhs)](GhcFile(compiler/basicTypes/UniqSupply.lhs) "wikilink"),
because its \`\`Int\`\` argument is the *entire* \`\`Unique\`\` and not
just the integer part 'under' the domain character. &gt; &gt; **SLPJ**
OK, but to eliminate \`\`mkUniqueGrimily\`\` you need to examine the
calls, decide how to do it better, and document the new design. &gt;
**PKFH** See above; the solution for now is
\`\`mkUniqueOnlyForUniqSupply\`\`. A separate patch will deal with
trying to refactor/redesign \`\`UniqSupply\`\` if this is necessary.

The function \`\`mkSplitUniqSupply\`\` made the domain-character
accessible to all the other modules, by having a wholly separate
implementation of the functionality of \`\`mkUnique\`\`.

Where the intention was still to have a clean interface, the (would-be)
hidden \`\`mkUnique\`\` is only called by functions defined in the
\`\`Unique\`\` module with the corresponding character, e.g.

=== New plan

In the new design, the domains are explicitly encoded in a sum-type
\`\`UniqueDomain\`\`. At the very least, this should help make the code
a little more self-documenting *and* prevent accidental overlap in the
choice of bits to identify the domain. Since the purpose of
\`\`Unique\`\`\\ s is to provide *fast* comparison for different types
of things, the redesign should remain performance concious. With this in
mind, keeping the \`\`UniqueDomain\`\` and the integer-part explicitly
in the type seems unwise, but by choosing we win the ability to
automatically derive things and should also be able to test how far
optimisation has come in the past 20+ years; does default boxing with
\`\`newtype\`\`-style wrapping have (nearly) the same performance as
manual unboxing? This should follow from the tests.

The encoding is kept the same, i.e. the \`\`Word\`\` is still built up
with the domain encoded in the most significant bits and the
integer-part in the remaining bits. However, instead encoding the domain
as a \`\`Char\`\` in the (internal *and* external interface), we now
create an ADT (sum-type) that encodes the domain. This has two
advantages. First, it prevents people from picking domain-tags ad hoc an
possibly overlapping. Second, encoding in the \`\`Word\`\` does not rely
on the assumption that the domain requires and/or fits in 8 bits. Since
Haskell \`\`Char\`\`\\ s are unicode, the 8-bit assumption is wrong for
the old design. In other words, the above examples are changed to:

Ideal world scenario, the entire external interface would be: and the
instances for \`\`Eq\`\`, \`\`Ord\`\`, \`\`Data\`\`, etc. For now,
though, it will also have

`       `**`SLPJ`**```  I agree that a ``newtype`` around a ``Word`` is ```\
```        better than a ``data`` type around ``Int#``. That is a small, ```\
`       simple change. But I think you plan to do more than this, and`\
`       that "more" is not documented here. E.g. what is the new API to`\
```        ``Unique``?  ```**`PKFH`**` Added. See above.`

[PageOutline](PageOutline "wikilink")

The data type  and its friends
=============================

GHC compiles a typed programming language, and GHC's intermediate
language is explicitly typed. So the data type that GHC uses to
represent types is of central importance.

The single data type is used to represent \\\* Types (possibly of higher
kind); e.g. \`\`\[Int\]\`\`, \`\`Maybe\`\` \\\* Kinds (which classify
types and coercions); e.g. \`\`(\* -&gt; \*)\`\`, \`\`T :=: \[Int\]\`\`.
See \[wiki:Commentary/Compiler/Kinds\] \\\* Sorts (which classify
types); e.g. \`\`TY\`\`, \`\`CO\`\`

GHC's use of \[wiki:Commentary/Compiler/FC coercions and equality
constraints\] is important enough to deserve its own page.

The module exposes the representation because a few other modules (, , ,
etc) work directly on its representation. However, you should not
lightly pattern-match on ; it is meant to be an abstract type. Instead,
try to use functions defined by , etc.

Views of types
--------------

Even when considering only types (not kinds, sorts, coercions) you need
to know that GHC uses a *single* data type for types. You can look at
the same type in different ways:

- The "typechecker view" regards the type as a Haskell type, complete

`  with implicit parameters, class constraints, and the like. For`\
`  example: `` Functions in`\
```   ``TcType`` take this view of types; e.g. ``tcSplitSigmaTy`` splits up ```\
`  a type into its forall'd type variables, its constraints, and the`\
`  rest.`

- The "core view" regards the type as a Core-language type, where class

`  and implicit parameter constraints are treated as function arguments:`\
`  ````  Functions in ``Type`` take ```\
`  this view.`

The data type \`\`Type\`\` represents type synonym applications in
un-expanded form. E.g. Here \`\`f\`\`'s type doesn't look like a
function type, but it really is. The function \`\`Type.coreView :: Type
-&gt; Maybe Type\`\` takes a type and, if it's a type synonym
application, it expands the synonym and returns \`\`Just
<expanded-type>\`\`. Otherwise it returns \`\`Nothing\`\`.

Now, other functions use \`\`coreView\`\` to expand where necessary,
thus: Notice the first line, which uses the view, and recurses when the
view 'fires'. Since \`\`coreView\`\` is non-recursive, GHC will inline
it, and the optimiser will ultimately produce something like:

The representation of 
----------------------

Here, then is the representation of types (see
[GhcFile(compiler/types/TypeRep.hs)](GhcFile(compiler/types/TypeRep.hs) "wikilink")
for more details):

Invariant: if the head of a type application is a , GHC *always* uses
the constructor, not . This invariant is maintained internally by 'smart
constructors'. A similar invariant applies to ; is never used with an
arrow type.

Type variables are represented by the \`\`TyVar\`\` constructor of the
\[wiki:Commentary/Compiler/EntityTypes data type Var\].

Overloaded types
----------------

In Haskell we write but in Core the \`\`=&gt;\`\` is represented by an
ordinary \`\`FunTy\`\`. So f's type looks like this: Nevertheless, we
can tell when a function argument is actually a predicate (and hence
should be displayed with \`\`=&gt;\`\`, etc), using The various forms of
predicate can be extracted thus: These functions are defined in module
\`\`Type\`\`.

Classifying types
-----------------

GHC uses the following nomenclature for types:

**Unboxed**:: A type is unboxed iff its representation is other than a
pointer. Unboxed types are also unlifted.

**Lifted**:: A type is lifted iff it has bottom as an element. Closures
always have lifted types: i.e. any let-bound identifier in Core must
have a lifted type. Operationally, a lifted object is one that can be
entered. Only lifted types may be unified with a type variable.

**Data**:: A type declared with ****. Also boxed tuples.

**Algebraic**:: An algebraic data type is a data type with one or more
constructors, whether declared with or . An algebraic type is one that
can be deconstructed with a case expression. "Algebraic" is **NOT** the
same as "lifted", because unboxed (and thus unlifted) tuples count as
"algebraic".

**Primitive**:: a type is primitive iff it is a built-in type that can't
be expressed in Haskell.

Currently, all primitive types are unlifted, but that's not necessarily
the case. (E.g. Int could be primitive.)

Some primitive types are unboxed, such as Int\#, whereas some are boxed
but unlifted (such as \`\`ByteArray\#\`\`). The only primitive types
that we classify as algebraic are the unboxed tuples.

Examples of type classifications:

\\|\\| \\|\\| **Primitive** \\|\\| **Boxed** \\|\\| **Lifted** \\|\\|
**Algebraic** \\|\\| \\|\\| \`\`Int\#\`\` \\|\\| Yes \\|\\| No \\|\\| No
\\|\\| No \\|\\| \\|\\| \`\`ByteArray\#\`\` \\|\\| Yes \\|\\| Yes \\|\\|
No \\|\\| No \\|\\| \\|\\| \`\`(\# a, b \#)\`\` \\|\\| Yes \\|\\| No
\\|\\| No \\|\\| Yes \\|\\| \\|\\| \`\`( a, b )\`\` \\|\\| No \\|\\| Yes
\\|\\| Yes \\|\\| Yes \\|\\| \\|\\| \`\`\[a\]\`\` \\|\\| No \\|\\| Yes
\\|\\| Yes \\|\\| Yes \\|\\|

Package Compatibility
=====================

In GHC 6.8.1 we reorganised some of the contents of the packages we ship
with GHC, see \#710. The idea was to lessen the problem caused by the
base package being essentially static between GHC major releases. By
separating modules out of base and putting them into separate packages,
it is possible to updgrade these modules independently of GHC.

The reorganisations unfortunately exposed some problems with our package
infrastructure, in particular most packages that compiled with 6.6 do
not compile with 6.8.1 because they don't depend on the new packages.
Some instructions for upgrading packages are here: [Upgrading
packages](http://haskell.org/haskellwiki/Upgrading_packages).

We anticipated the problem to some extent, adding "configurations" to
Cabal to make it possible to write conditional package specifications
that work with multiple sets of dependencies. We are still left with the
problem that the \`.cabal\` files for all packages need to be updated
for GHC 6.8.1. This seems like the wrong way around: the change we made
to a few packages has to be propagated everywhere, when there should be
a way to confine it locally, at least for the purposes of continued
compatibility with existing source code. In many cases, the underlying
APIs are still available, just from a different place. (in general this
may not be true - modifications to packages may make changes to APIs
which require real changes to dependent packages).

Some of the problems that contributed to this situation can be
addressed. We wrote the [Package Versioning
Policy](http://haskell.org/haskellwiki/Package_versioning_policy) so
that packages can start using versions that reflect API changes, and so
that dependencies can start being precise about which dependencies they
work with. If we follow these guidelines, then

`* failures will be more predictable`\
`* failures will be more informative`

because dependencies and API changes are better documented. However, we
have no fewer failures than before, in fact we have more because
packages cannot now "accidentally work" by specifying loose dependency
ranges.

So the big question is, what changes do we need to make in the future to
either prevent this happening, or to reduce the pain when it does
happen? Below are collected various proposals. If the proposals get too
long we can separate them out into new pages.

1. Don't reorganise packages
----------------------------

We could do this, but that just hides the problem and we're still left
with a monolithic base package. We still have to contend with API
changes causing breakage.

2. Provide older version(s) of base with a new GHC release
----------------------------------------------------------

We could fork the base package for each new release, and keep compiling
the old one(s). Unfortunately we would then have to compile every other
package two (or more) times, once against each version of base. And if
we were to give the same treatment to any other library, we end up with
exponential blowup in the number of copies.

The GHC build gets slower, and the testing surface increases for each
release.

Furthermore, the package database cannot currently understand multiple
packages compiled against different versions of dependencies. One
workaround is to have multiple package databases, but that's not too
convenient.

4. Allow packages to re-export modules
--------------------------------------

Packages currently cannot re-export modules from other packages. Well,
that's not strictly true, it is possible to do this but it currently
requires an extra package and two stub modules per module to be
re-exported (see
[7](http://www.haskell.org/pipermail/haskell-cafe/2007-October/033141.html)).

This could be made easier. Suppose you could write this:

to construct a module called \`Data.Maybe\` that re-exports the module
\`Data.Maybe\` from package \`base-2.0\`. This extension to the import
syntax was proposed in PackageImports.

Using this extension, we can construct packages that re-export modules
using only one stub module per re-exported module, and Cabal could
generate the stubs for us given a suitable addition to the \`.cabal\`
file syntax.

Package re-exports are useful for

`* Constructing packages that are backwards-compatible with old packages by re-exporting parts of the new API.`\
`* Providing a single wrapper for choosing one of several underlying providers`

4.1 Provide backwards-compatible versions of base
-------------------------------------------------

So using re-exports we can construct a backwards-compatible version of
base (\`base-2.0\` that re-exports \`base-3.0\` and the other packages
that were split from it). We can do this for other packages that have
changed, too. This is good because:

`* Code is shared between the two versions of the package`\
`* Multiple versions of each package can coexist in the same program easily (unlike in proposal 2)`

However, this approach runs into problems when types or classes, rather
than just functions, change. Suppose in \`base-3.0\` we changed a type
somewhere; for example, we remove a constructor from the \`Exception\`
type. Now \`base-2.0\` has to provide the old \`Exception\` type. It can
do this, but the \`Exception\` type in \`base-2.0\` is now incompatible
with the \`Exception\` type in \`base-3.0\`, so every function that
refers to \`Exception\` must be copied into \`base-2.0\`. At this point
we start to need to recompile other packages against \`base-2.0\` too,
and before long we're back in the state of proposal (2) above.

This approach therefore doesn't scale to API changes that include types
and classes, but it can cope with changes to functions only.

4.2 Rename base, and provide a compatibility wrapper
----------------------------------------------------

This requires the re-exporting functionality described above. When
splitting base, we would rename the base package, creating several new
packages. e.g. \`base-3.0\` would be replaced by \`newbase-1.0\`,
\`concurrent-1.0\`, \`generics-1.0\`, etc. Additionally, we would
provide a wrapper called \`base-4.0\` that re-exports all of the new
packages.

Advantages:

`* Updates to existing packages are much easier (no configurations required)`\
`* Doesn't fall into the trap of trying to maintain a completely backwards-compatible version of the old API, as in 4.1`

Disadvantages:

`* All packages still break when the base API changes (if they are using precise dependencies on base, which they should be)`\
`` * Backwards compatibility cruft in the form of the `base` wrapper will be hard to get rid of; there's no ``\
`  incentive for packages to stop using it.  Perhaps we need a deprecation marker on packages.`\
`* Each time we split base we have to invent a new name for it, and we accumulate a new compatibility wrapper`\
`  for the old one.`

4.3 Don't rename base
---------------------

This is a slight variation on 4.2, in which instead of renaming \`base\`
to \`newbase\`, we simply provide two versions of \`base\` after the
split. Take the example of splitting \`base-3.0\` into \`base +
concurrent + generics\` again:

``  * `base-4.0` is the remaining contents of `base-3.0` after the split ``\
``  * `base-3.1` is a compatibility wrapper, re-exporting `base-4.0 + concurrent-1.0 + generics-1.0`. ``

The idea is that all existing packages that worked with \`base-3.0\`
will have or similar. To make these work after the split, all that is
needed is to modify the upper bound: which is better than requiring a
conditional dependency, as was the case with the \`base-3.0\` split. In
due course, these packages can be updated to use the new \`base-4.0\`.

Advantages: the same as 4.2, plus there's no need to rename \`base\` for
each split. Disadvantages: multiple versions of \`base\` could get
confusing. The upgrade path is still not completely smooth (existing
packages all need to be modified manually).

5. Do some kind of provides/requires interface in Cabal
-------------------------------------------------------

Currently, Cabal's idea of API is asymmetric and very coarse: the client
depends on a package by name and version only, the provider implements a
single package name and version by exposing a list of modules. That has
several disadvantages:

`* Cabal cannot ensure build safety: most errors will not show up before build-time (contrast that with Haskell's usual model of static type safety).`\
`* Cabal has no idea what a dependency consists of unless it is installed. even if it is installed, it only knows the modules exposed. The actual API might be defined in Haddock comments, but is not formally specified or verified.`

### 5.1 Make API specifications more symmetric

Just as a provider lists the modules it exposes, clients should list the
modules they import (this field should be inferred by a 'ghc -M'-style
dependency analysis). Advantages:

`* Cabal would have an idea which parts of a package a client depends on instead of defaulting to "every client needs everything" (example: clients using only parts of the old base not split off should be happy with the new base)`\
`* Cabal would have an idea what a missing dependency was meant to provide (example: clients using parts of the old base that have been split off could be offered the split-off packages as alternative providers of the modules imported)`

### 5.2 Make API specifications explicit

Currently, the name and version of a package are synonymous with its
API. That is like modules depending on concrete data type
representations instead of abstract types. It should not really matter
that the functionality needed by package P was only available in package
Q-2.3.42 at the time P was written. What should matter is which parts of
Q are needed for P, and which packages are able to provide those parts
when P is built.

Section 5.1 above suggests to make this specification at least at the
level of modules, in both providers and clients. But even if one wanted
to stay at the coarser level of API names and versions, one should
distinguish between an API and one of its implementing packages. Each
client should list the APIs it depends on, each provider should list the
APIs it can be called upon to provide.

One can achieve some of this in current Cabal by introducing
intermediate packages that represent named APIs to clients while
re-exporting implementations of those APIs by providers. Apart from
needing re-export functionality, this is more complicated than it should
be.

### 5.3 Make API specifications more specific

If one compares Cabal's ideas of packages and APIs with Standard ML's
module language, with its structures, functors, and interfaces forming
part of a statically typed functional program composition language, one
can see a lot of room for development.

6. Distributions at the Hackage level
-------------------------------------

The idea here is to group packages into "distributions" in Hackage, with
the property that all packages within a distribution are mutually
compatible. Todo... expand.

7. Allow package overlaps
-------------------------

This is not a solution to the problem of splitting a package but helps
in the case that we want to use a new package that provides an updated
version of some modules in an existing package. An example of this is
the bytestring and base package. The base-2.0 package included
Data.ByteString but it was split off into a bytestring package and not
included in base-3.0. At the moment ghc allows local .hs files to
provide modules that can shadow modules from a package but does not
packages to shadow each other.

So an extension that would help this case would be to let packages
shadow each other. The user would need to specify an ordering on
packages so ghc knows which way round the shadowing should go. This
could be specified by the order of the -package flags on the command
line, which is equivalent to the order in which they are listed in the
build-depends field in a .cabal file. This would be a relatively easy
extension to implement.

Note that it only solves the problem of backporting packages to be used
on top of older versions of the package they were split from. It also
provides a way for people to experiment with packages that provide
alternative implementations of standard modules.

There is potential for confusion if this is used too heavily however.
For example two packages built against standard and replacement modules
may not be able to be used together because they will re-export
different types.

The problem of lax version dependencies
---------------------------------------

Supposing that we used solution 2 above and had a base-2.x and a
base-3.x. If we take an old package and build it against base-2.x then
it will work and if we build it against base-3.x then it'll fail because
it uses modules from the split out packages like directory, bytestring
etc. So obviously Cabal should select base-2.x, but how is this decision
actually supposed to be made automatically? From a quick survey of the
packages on hackage we find that 85% specify unversioned dependencies on
the base package and none of them specify upper bounds for the version
of base. So presented with a package that says:

how are we to know if we should use base-2.x or base-3.x. It may be that
this package has been updated to work with base-3.x or that it only ever
used the parts of base-2.x that were not split off. This dependency does
not provide us with enough information to know which to choose. So we
are still left with the situation that every package must be updated to
specify an api version of base.

One possible remedy would be to call version 3 something other than
base. Any dependency on 'base' would then refer to the set of modules
that comprise base-2.x (this is (4.2) above, incedentally).

Note about this page
====================

`   `*`Apparently,` `this` `page` `is` `out` `of` `date` `and` `the`
`issue` `has` `been` `settled` `in` `favour` `of` `the` `syntax:`*\
`   `\
`   See also:`\
`   `[`8`](http://haskell.org/ghc/docs/latest/html/users_guide/syntax-extns.html#package-imports)

Explicit package imports
========================

This proposal is one possibility for addressing the question of
identifying which package is meant in an import declaration. For the
context, read the \[wiki:Commentary/Packages/GhcPackagesProposal GHC
packages summary page\] first.

The main idea of this proposal is to allow the programmer to specify the
source package in the import line, something like this: That would
presumably get the most recent installed incarnation of the package. If
you want a particular version of the package, we could allow The exact
syntax is unimportant. The important thing is that the programmer can
specify the package in the source text. Note that this fundamentally
conflicts with the second assumption we started with. We were trying to
avoid specifying "provenance" at the same time as "purpose", on the
grounds that we wanted to avoid editing lots of source text when the
provenance changed. (And so it begs the question, if we need to edit the
source anyway, why separate the syntax of packages from modules at all?)

If we adopt the idea that an import statement can specify the source
package, several design choices arise:

Is the 'from <package>' compulsory?
-----------------------------------

If you want to import A.B.C, a module exported by package "foo", can you
say just , or must you say ?

We think of this as rather like the question "If you import f from
module M, can you refer to it as plain "f", or must you refer to it as
"M.f"? The answer in Haskell 98 is that you can refer to it as plain "f"
so long as plain "f" is umambiguous; otherwise you can use a qualified
reference "M.f" to disambiguate.

We propose to adopt the same principle for imports. That is, an import
with no package specified, such as "", means:

`  Find all modules A.B.C exported by all exposed packages, or the package or program being compiled. If there is exactly one such module, that's the one to import. Otherwise report "ambiguous import".`

If the reference to A.B.C is ambiguous, you can qualify the import by
adding "".

Package versions
----------------

We probably want some special treatment for multiple versions of the
same package. What if you have both "foo-3.9" and "foo-4.0" installed,
both exporting A.B.C? This is jolly useful when you want to install new
packages, but keep old ones around so you can try your program with the
older one. So we propose that this is not regarded as ambiguous:
importing A.B.C gets the latest version, unless some compiler flag
(-hide-package) takes it of the running.

In short, an installed package can be of two kinds:

` * `**`Exposed`**`: the package's modules populate the global module namespace, and can be imported without mentioning the pacckage name explicitly (``).  Explicit "from" imports may be used to resolve ambiguity.`\
` * `**`Available`**`, but not exposed: the package can be used only by an explicit "from" import.  This is rather like "``, except at the package level.  `

Typically, if multiple versions of the same package are installed, then
all will be available, but only one will be exposed.

GHC's command-line flags (, ) can be used to manipulate which packages
are exposed, but typically an entire package or program will be compiled
with a single set of such flags. GHC does not curretly support in-module
control, thus , and we do not propose to change that.

Simon suggested that an installed package might be hidden (so that it
cannot be used at all) but I'm not sure why we need that.

Importing from the home package
-------------------------------

If A.B.C is in the package being compiled (which we call "the home
package"), and in an exposed package, and you say , do you get an
"ambiguous import" error , or does the current package override. And if
the former, how can you say "import A.B.C from the current package"?

One possibility is to reuqire the code to know its own package name, and
mention that in the import. For exmaple, in a module that is being
compiled as part package "foo", you'd say . What about modules that are
part of the main program (not a package at all). Perhaps you could then
say .

Another way is to have a special package name meaning "the home
package". The special name could be

`* ""`\
`* "home"`\
`* "this"`\
`* this (with no quotes)`

The 'as P' alias
----------------

We propose to maintain the local, within-module "as P" alias mechanism
unchanged. Thus: Here, the qualified name "M.T" refers to the T imported
from A.B.C in package "foo".

Qualified names
---------------

We propose that the default qualified name of an entity within a module
is just the module name plus the entity name. Thus If you want to import
multiple A.B.C's (from different packages) then perhaps they define
different entities, in which case there is no problem: But if they both
export entities with the same name, there is no alternative to using the
'as M' mechanism:

Exporting modules from other packages
-------------------------------------

It is perfectly OK to export entities, or whole modules, imported from
other packages:

Syntax
------

Should package names be in quotes? Probably yes, because they have a
different lexcal syntax to the rest of Haskell. ("foo-2.3" would parse
as three tokens, "foo", "-", and "2.3".

It's been suggested that one might want to import several modules from
one package in one go: What we don't like about that is that it needs a
new keyword "". Perhaps all imports can start with the keyword , and
then we are free to use extra (context-specific) keywords. (Haskell
already has several of these, such as . Something like this:

 Here the layout is explicit, but the braces and semicolons could be
avoided by making use of the layout rule as usual.

Indeed, we could allow this multiple form even for ordinary imports:

It is clear from the above examples that the keyword is redundant - the
presence of a string literal (or special keyword to denote the home
package) after the keyword is sufficient to distinguish per-package
imports from the ordinary shared-namespace imports, so the above could
instead be written as

### Syntax formalised and summarised

A possible syntax which covers everything in this proposal is therefore:

`  `**`import`**` [`*`package-name`*`] `**`{`**` `*`import-specifier`*` [`**`;`**` `*`import-specifier`*`] `**`}`**

where *package-name* is a string literal or the keyword , the
*import-specifier* corresponds to everything that is currently allowed
after the keyword , and the braces and semicolons would be added by the
layout rule.

### Proposal for Package Mounting

It may help to refer to \[wiki:Commentary/Packages/GhcPackagesProposal\]
for an introduction to some of the issues mentioned here.

A message by Frederik Eaton to the Haskell mailing list describing the
present proposal is archived:
[9](http://www.haskell.org/pipermail/libraries/2005-June/004009.html).
(Also, see note at the end of this document regarding an earlier
proposal by Simon Marlow)

This document will go over Frederik's proposal again in brief. The
proposal doesn't involve any changes to syntax, only an extra command
line option to , etc., and a small change to Cabal syntax.

In this proposal, during compilation of a module, every package would
have a "mount point" with respect to which its particular module
namespace would be resolved. Each package should have a default "mount
point", but this default would be overridable with an option to , etc.

For example, the library currently has module namespace:

In this proposal, it might instead have default mount point and
(internal) module namespace:

To most users of the X11 package, there would be no change - because of
the mounting, modules in that package would still appear with the same
names in places where the X11 package is imported: , etc. However, if
someone wanted to specify a different the mount point, he could use a
special compiler option, for instance :

(so the imported namespace would appear as , , etc.) Note that the
intention is for each option to refer to the package specified in the
preceding option, so to give package a mount point of we use the syntax

Ideally one would also be able to link to two different versions of the
same package, at different mount points:

(yielding , , ...; , , ...)

However, usually the default mount point would be sufficient, so most
users wouldn't have to learn about .

Additionally, Cabal syntax should be extended to support mounting. I
would suggest that the optional mount point should appear after a
package in the Build-Depends clause of a Cabal file:

And in the package Cabal file, a new clause to specify the default mount
point:

### Evaluation

This proposal has several advantages over the
\[wiki:Commentary/Packages/PackageImportsProposal\] proposal.

`* `*`No` `package` `names` `in`
`code`*`. In this proposal, package names would be decoupled from code. This is very important. It should be possible to rename a package (or create a new version of a package with a new name), and use it in a project, without editing every single module of the project and/or package. Even if the edits could be done automatically, they would still cause revision control headaches. Any proposal which puts package names in Haskell source code should be considered unacceptable.`

`* `*`No` `syntax`
`changes`*`. The [wiki:Commentary/Packages/PackageImportsProposal] proposal requires new syntax, but this proposal does not. Of course, in this proposal it would be slightly more difficult for the programmer to find out which package a module is coming from. He would have to look at the command line that compiles the code he's reading. However, I think that that is appropriate. Provenance should not be specified in code, since it changes all the time. (And there could be a simple debugging option to GHC which outputs a description of the namespace used when compiling each file)`

`* `*`Simpler` `module`
`names`*`. This proposal would allow library authors to use simpler module names in their packages, which would in turn make library code more readable, and more portable between projects. For instance, imagine that I wanted to import some of the code from the `` library into my own project. Currently, I would have to delete every occurrence of `` in those modules. Merging future changes after such an extensive modification would become difficult. This is a real problem, which I have encountered while using John Meacham's curses library. There are several different versions of that library being used by different people in different projects, and it is difficult to consolidate them because they all have different module names. The reason they have different module names is that package mounting hasn't been implemented yet. The [wiki:Commentary/Packages/PackageImportsProposal] proposal would not fix the problem.`

`* `*`Development` `decoupled` `from`
`naming`*`. (there is a bit of overlap with previous points here) In the present proposal, programmers would be able to start writing a library before deciding on a name for the library. For instance, every module in the `` library contains the prefix ``. This means that either the author of the library had to choose the name `` at the very beginning, or he had to make several changes to the text of each module after deciding on the name. Under the present proposal, he would simply call his modules ``, ``, ``, etc.; the `` prefix would be specified in the build system, for instance in the Cabal file.`

Frederik's mailing list message discusses some other minor advantages,
but the above points are the important ones. In summary, it is argued
that the above proposal should be preferred to
\[wiki:Commentary/Packages/PackageImportsProposal\] because it is both
easier to implement (using command line options rather than syntax), and
more advantageous for the programmer.

### Note on Package Grafting

A proposal by Simon Marlow for "package grafting" predates this one:
[10](http://www.haskell.org/pipermail/libraries/2003-August/001310.html).
However, the "package grafting" proposal is different in that it
suggests selecting a "mount point" at library installation time, where
in the present proposal, the "mount point" is selected each time a
module using the library in question is compiled. The difference is
important, as one doesn't really want to have to install a new copy of a
library just to use it with a different name. Also, Simon Marlow's
proposal puts package versions in the module namespace and therefore
source code, where we argue for decoupling source code from anything to
do with provenance - be it package names or version numbers.

[PageOutline](PageOutline "wikilink")

Alternative Proposal for Packages (with explicit namespaces)
------------------------------------------------------------

This proposal is an alternative to
\[wiki:Commentary/Packages/GhcPackagesProposal\]. Large parts overlap
with that proposal. To motivate this new proposal, let's consider
another proposed and desirable feature of the import/export language,
which may interact in interesting ways with packages.

A different, but related, problem
---------------------------------

A problem that has been mentioned several times on mailing lists, is
grafting part of a directory hierarchy into an arbitrary location
elsewhere in the hierarchy. (See
[11](http://www.haskell.org/pipermail/libraries/2005-June/004009.html))

Another way of expressing a similar wish is the ability to re-export
imports with a different qualified name, as in the scenario suggested by
the developers of the package gtk2hs:
[12](http://www.haskell.org/pipermail/libraries/2004-December/002800.html)

There are several desires in play here:

`* a desire to minimise typing of long qualified names`\
`* a desire to refer to "leaf" nodes of the hierarchy in a way that makes it easy to relocate those modules in the hierarchy, without needing to edit every import declaration that uses them`\
`* a desire to partially-qualify names for disambiguation`

Proposal
--------

We introduce the new concept of *namespace* as something that can be
declared in source code. A namespace can contain only module names. (The
specification of what module names are contained in a namespace is
rather like our current concept of a package, i.e. not declared in the
source code, but rather by some external mechanism e.g. grouping of
files in a filesystem hierarchy.)

There are now two separate kinds of .

`* `\
`* `

The new semi-reserved word is introduced, having special meaning only
directly after the keyword. There is a *level* difference in what this
new form of import means. The declaration brings into availability the
subset of the hierarchy of *module* names rooted in the package , at the
position . That is, if the package version contains the modules

`* Data.Foo.Bar`\
`* Data.Foo.Baz`\
`* Data.Bar`

then the namespace import brings into the "importable" namespace only
the modules

`* Data.Foo.Bar`\
`* Data.Foo.Baz`

However, for the program to use those modules, it is still necessary to
go ahead and actually them in the normal way, although the names used to
import them will now be *relative* to the available namespaces, rather
than absolute. So the declaration brings into scope all the entities
defined in . Like any normal import, these can be qualified or hidden.

Thus,

`* `` brings into scope a bunch of names for modules`\
`  from the given provenance.`\
`* `` brings into scope a bunch of entities from the given`\
`  module.`

### Naming a namespace

Are namespaces first class? Can we give them a name? Indeed, why not?

`* `\
`* `

Here, we have declared that we want to be able to refer to the namespace
as , and so, a subsequent specifically asks for the from the package ,
just in case there might be a module also available from another
namespace.

### What namespaces are available by default?

If no namespaces are explicitly brought into scope, what modules are
implicitly available?

`* Anything in the `*`current`*` package, i.e. the executable or library`\
`  whose modules are all physically rooted at the same location in the`\
`  filesystem as this module.`

`* Is there an implicit ``, just as there is an`\
`  implicit ``?`

### Namespace resolution

In essence, namespaces take over the role formerly played by commandline
arguments like and . The search path used by the compiler for finding
modules is now partially declared in the source code itself. (Note
however that that the search path is declared symbolically, involving
package names, not directories. This is a very important separation of
the thing itself from where it is stored.)

Resolution of which module is referred to by an import statement (taking
into account the namespaces) is just like the current process of
resolving which entity is referred to by program text (taking into
account the imported modules). The source text may import multiple
namespaces. If any module import is ambiguous (i.e. the module exists in
more than one namespace), it is a static error. Resolution is lazy, in
the sense that there is no error if namespaces contain the same module
name, only if the program tries to import that module name.

So when you say "import A.B.C", from what package does A.B.C come?

There must be a single namespace in scope containing a module called .
(Sidenote: or in fact a namespace called , containing a module named )

### Syntax

The precise syntax can be debated. New keywords like or could be
substituted for . The key important features however are the inclusion
of:

`* the package name (mandatory)`\
`* an optional package version, if several are available`\
`* an optional path to use as the root of the available namespace`\
`* an optional renaming`

### Exports

One might wonder whether it is now either necessary or desirable to
permit *namespaces* to be re-exported in the same way that *modules* can
be? For instance:

The idea is that any module saying would thereby implicitly open the
namespace of package at the root , in addition to having access to
entities defined in itself.

Note that, just as with a current module re-export it is no longer
possible for the importing location to use the original module name as a
qualifier; so with a namespace re-export, there is no way to refer to
the namespace in the importing location either. It is purely a signal to
the compiler telling it where to look for modules when resolving
imports.

I argue that namespace export *is* desirable, because it allows (but
does not require) all package (namespace) dependencies to be gathered
together in a single module for an entire project. With such an
organising principle, when dependencies change, there is only one source
file to update. But without namespace re-exports, it would be impossible
to localise those dependencies to a single file.

Note how this feature addresses several of the initial stated desires,
of reducing the verbosity of imports, and of referring to leaf modules
conveniently. For instance:

### Implicit imports

One could go further. If I write a qualified name in the source text,
must I also write at the top? The qualified entity is unambiguous,
whether or not there is an explicit import for it, because the module
qualification must be unambiguous within the current namespaces. In the
Gtk example above, this would eliminate the need for , and who knows how
many other imports, leaving a single to bring all of the qualified
entities into scope.

### Exposed vs Hidden packages

GHC's scheme of exposed vs hidden packages can now be replaced with full
source-code control of namespace visibility. To setup a default set of
exposed packages, you just write a module to export their namespaces:

and import it in every module of your project. Or if importing it
everywhere sounds too painful, one can even imagine that a compiler
might provide a command-line option (or use a configuration file) to
specify one distinguished module to be implicitly imported everywhere:

### What if you wanted to import A.B.C from P1 and A.B.C from P2 into the *same* module?

[PageOutline](PageOutline "wikilink")

Package Reorg
=============

In this page we collect proposals and design discussion for reorganising
the packages that come with compilers, and the contents of those
packages.

None of the ideas herein are claimed to belong to any particular person,
many of the ideas have been extracted from mailing list discussions, eg.

[`13`](http://www.haskell.org/pipermail/libraries/2006-November/006396.html)

Some of the points are GHC-specific. Please feel free to insert points
specific to other compilers.

Goals
-----

`* It would be good to have set of 'core' packages that is installed with`\
`  every Haskell implementation.  More on this at PackageReorg/Rationale page`\
`* Forwards compatibility.  Users would like their programs written against the 'core' packages to continue to work, without`\
`  modification to source text or build system, after upgrading the`\
`  compiler, or its packages, or switching to a different compiler.`\
`* Backwards compatibility.  Users would like to be able to take a`\
`  program written against some version of the 'core' packages, and`\
`  build it with an older compiler, accepting that they may have to`\
`  install newer versions of the 'core' packages in order to do so.`

It may not be possible to fully achieve these goals (in particular,
backwards compatibility), but that does not mean we should not aim for
them.

Proposal
--------

Here's a straw-man proposal

`* There is a set of packages that come with every conforming Haskell`\
`  implementation.  Let's call these the `**`Core` `Packages`**` to`\
`  avoid confusion (Bulat called these the "base packages", but that's an `\
``   over-used term given that there is a package called `base`). ``\
`  The good thing about the Core Packages is that`\
`  users know that they will be there, and they are consistent with`\
`  each other.`

`* Any particular implementation may install more packages by default;`\
``   for example GHC will install the `template-haskell` and `stm` ``\
`  packages.  Let's call these the `**`GHC` `Install`
`Packages`**`, '''Hugs`\
`  Install Packages''' etc; the Install Packages are a superset of the`\
`  Core Packages.`

### What is in the Core Packages?

The Core Packages are installed with every conforming Haskell
implementation. What should be in the Core? There is a tension:

` 1. `**`As` `much` `as`
`possible`**`; which means in practice widely-used and reasonably stable packages.  It is convenient for programmers to have as much as possible in a consistent, bundle that is (a) known to work together bundle, and (b) known to work on all implementations.  `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
` 2. `**`As` `little` `as`
`possible`**`; which in practice means enough to run Cabal so that you can run the Setup files that come when downloading new packages.  As Ian puts it: the less we force the implementations to come with, the quicker compilation will be when developing, the smaller Debian packages (for example) can be, the lower the disk space requirements to build GHC, the lower the time wasted when a Debian package (for example) build fails and the fewer packages we are tangling up with compiler release schedules.`

There's a real choice here: Bulat wants (1) and Ian wants (2).

Initial stab at (1):

``  * `base` ``\
``  * `Cabal` ``\
``  * `haskell98` ``\
``  * Some `regex` packages (precisely which?) ``\
``  * `unix` or `Win32`. Questionable, partly because it means the Core interface becomes platform-dependent; and partly because `Win32` would double the size of the Hugs distribution. ``\
``  * `parsec` ``\
``  * `mtl` ``\
``  * `time` ``\
``  * `network` ``\
``  * `QuickCheck` (questionable) ``\
``  * `HUnit` (questionable) ``

Initial stab at (2):

``  * `base` ``\
``  * `haskell98` ``\
``  * `Cabal` ``\
``  * `filepath` (?) ``

Bulat: i think that all regex packages should be included and of course
libs that helps testing. overall, it should be any general-purpose lib
that porters accept (enlarging this set makes users live easier, and
porters live harder)

about unix/win32 - these libs provide access to OS internals, not some
everywhere-portable API. moreover, other world-interfacing libs (i/o,
networking) should use APIs provided by these libs with a conditional
compilation (CPPery) tricks in order to provide portable APIs! current
situation where such libs use FFI isn't ideal. WinHugs size problem is
rather technical - it includes a lot of DLLs which contains almost the
same code

i agree to start with minimal stub, and then proceed with discussing
inclusion of each library. what we need now is requirements to include
library in this set and lifetime support procedure. so:

### Requirements to libraries to be included in core set

`* BSD-licensed, and even belongs to Haskell community?`\
`* portable (is sense of compiler and OS), may be just Haskell' compatible?`\
`* already widely used`\
`* shouldn't duplicate existing core libs functionality (?)`

Exact inclusion, support and exclusion processes?

### The base package

The base package is a bit special

`` * Package `base` is rather big at the moment.   ``

`* From a user's point of view it would be nicer to give it a`\
``   compiler-independent API.  (A module like `GHC.Exts` would move to ``\
``   a new package `ghc-base`.) ``

Thinking of GHC alone for a moment, we could have a package \`ghc-base\`
(which is pretty much the current \`base\`) and a thin wrapper package
\`base\` that re-exposes some, but not all, of what \`ghc-base\`
exposes. To support this re-exposing, we need a small fix to both GHC
and Cabal, but one that is independently desirable.

Similarly, Hugs could build \`hugs-base\` from the same souce code, by
using CPP-ery, exactly as now. The thin \`base\` wrapper package would
not change.

To make \`base\` smaller, we could remove stuff, and put it into
separate packages. But be careful: packages cannot be cyclic, so
anything that is moved out can't be used in \`base\`. Some chunks that
would currently be easy to split off are:

`* Data.!ByteString.* (plus future packed Char strings)`\
`* Control.Applicative (?), Data.Foldable, Data.Monoid (?), Data.Traversable, Data.Graph, Data.!IntMap, Data.!IntSet, Data.Map, Data.Sequence, Data.Set, Data.Tree`\
`* System.Console.!GetOpt`\
`* Text.!PrettyPrint.*`\
`* Text.Printf`

Some other things, such as arrays and concurrency, have nothing else
depending on them, but are so closely coupled with GHC's internals that
extracting them would require exposing these internals in the interface
of \`base\`.

Bulat: my ArrayRef library contains portable implementation of arrays.
there is only thin ghc/hugs-specific layer which should be provided by
ghcbase/hugsbase libs. except for MPTC problem (IArray/MArray classes
has multiple parameters), this library should be easily portable to any
other haskell compiler

See also BaseSplit.

### Other packages

Other non-core packages would probably have their own existence. That
is, they don't come with an implementation; instead you use
\`cabal-get\`, or some other mechanism, such as your OS's package
manager. Some of these currently come with GHC, and would no longer do
so

``  * `GLUT` ``\
``  * `ALUT` ``\
``  * `OpenAL` ``\
``  * `OpenGL` ``\
``  * `HGL` ``\
``  * `HUnit` ``\
``  * `ObjectIO` ``\
``  * `X11` ``\
``  * `arrows` ``\
``  * `cgi` ``\
``  * `fgl` ``\
``  * `html` ``\
``  * `xhtml` ``

Bulat: i propose to unbundle only graphics/sound libs because these
solves particular problems and tends to be large, non-portable (?) and
some are just legacy ones - like ObjectIO. we should keep everything
small & general purpose, including HUnit, arrows, fgl, html and xhtml,
and include even more: ByteString, regex-\*, Edison, Filepath, MissingH,
NewBinary, QuickCheck, monads

Testing
-------

We should separate out package-specifc tests, which should be part of
the repository for each package. Currently they are all squashed
together into the testsuite repository.

Implementation-specific notes
-----------------------------

### Notes about GHC

Currently GHC installs a set of packages by default, the so-called **GHC
Boot Packages**. They are graphed here, with arrows representing
dependencies between them: [Image(packagegraph.png,
800)](Image(packagegraph.png,_800) "wikilink")

These are exactly the libraries required to build GHC. That shouldn't be
the criterion for the core packages.

One reason we do this is because it means that every GHC installation
can build GHC. Less configure-script hacking. (NB: even today if you
upgrade any of these packages, and then build GHC, the build might fail
because the CPP-ery in GHC's sources uses only the version number of
GHC, not the version number of the package.)

Still, for convenience we'd probably arrange that the GHC Install
Packages included all the GHC Boot Packages.

Every GHC installation must include packages: \`base\`, \`ghc-prim\`,
\`integer\` and \`template-haskell\`, else GHC itself will not work. (In
fact \`haskell98\` is also required, but only because it is linked by
default.)

So GHC's Install Packages would be the Core Packages plus

`` * `template-haskell` ``\
`` * `editline` ``\
`` * `integer` ``\
`` * `ghc-prim` ``

You can upgrade any package, including \`base\` after installing GHC.
However, you need to take care. You must not change a number of things
that GHC "knows about". In particular, these things must not change

`* Name`\
`* Defining module`

GHC knows even more about some things, where you must not change

`* Type signature`\
`* For data types, the names, types, and order of the constructors`

The latter group are confined to packages base and template-haskell.

(Note: a few other packages are used by tests in GHC's test suite,
currently: \`mtl\`, \`QuickCheck\`. We should probably eliminate the mtl
dependency; but \`QuickCheck\` is used as part of the test
infrastructure itself, so we'll make it a GHC Boot Package.)

### Notes about Hugs

Recent distributions of Hugs come in two sizes, jumbo and minimal.
Minimal distributions include only the packages \`base\`, \`haskell98\`
and \`Cabal\`. (Hugs includes another package \`hugsbase\` containing
interfaces to Hugs primitives.) The requirements for this set are to

`* run Haskell 98 programs`\
`* allow packages to be added and upgraded using Cabal`

(Currently \`cpphs\` is a Haskell 98 program, so the latter implies the
former.)

It should be possible to upgrade even the core packages using Cabal.

Commentary: The Package System
==============================

See also: \[wiki:Commentary/Compiler/Packages Packages\], where we
describe how this is implemented in GHC.

Architecture
------------

GHC maintains a package database, that is basically a list of
\`InstalledPackageInfo\`. The \`InstalledPackageInfo\` type is defined
in \`Distribution.InstalledPackageInfo\` in Cabal, and both \`ghc-pkg\`
and GHC itself import it directly from there.

There are four main components of the package system:

`Cabal::`\
`  Cabal is a Haskell library, which provides basic data types for the package system, and support for building,`\
`  configuring, and installing packages.`

`GHC itself::`\
``   GHC reads the package database(s), understands the flags `-package`, `-hide-package`, etc., and uses the package database ``\
``   to find `.hi` files and library files for packages.  GHC imports modules from Cabal. ``

`` `ghc-pkg`:: ``\
``   The `ghc-pkg` tool manages the package database, including registering/unregistering packages, queries, and ``\
``   checking consistency.  `ghc-pkg ` also imports modules from Cabal. ``

`` `cabal-install`:: ``\
`  A tool built on top of Cabal, which adds support for downloading packages from Hackage, and building and installing`\
`  multiple packages with a single command.`

For the purposes of this commentary, we are mostly concerned with GHC
and \`ghc-pkg\`.

Identifying Packages
--------------------

`` `Cabal.PackageName` ("base"):: ``\
``    A string.  Defined in `Distribution.Package`.  Does not uniquely identify a package: the package ``\
`   database can contain several packages with the same name.`

`` `Cabal.PackageId` ("base-4.1.0.0"):: ``\
``    A `PackageName` plus a `Version`.  A `PackageId` names an API.  If two `PackageId`s are ``\
`   the same, they are assumed to have the same API.`\
`   `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
``    `InstalledPackageInfo` contains the field `sourcePackageId :: PackageId`. ``\
`   `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
``    In GHC 6.11, the `PackageId` also uniquely identifies a package instance in the package database, but ``\
`   only by convention (we may lift this restriction in the future, and allow the database to contain`\
``    multiple package instances with the same `PackageId` (and different `InstalledPackageId`s). ``

`` `Cabal.InstalledPackageId` ("base-4.1.0.0-1mpgjN")::  ``\
`   (introduced in GHC 6.12 / Cabal 1.7.2) A string that uniquely identifies a package instance in the database.`\
``    An `InstalledPackageId` identifies an ABI: if two `InstalledPackageIds` are the same, they have the ``\
`   same ABI.`\
`   `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
``    `InstalledPackageInfo` contains the field `installedPackageId :: InstalledPackageId`. ``\
`   `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
``    Dependencies between installed packages are identified by the `InstalledPackageId`.  An `InstalledPackageId` is ``\
``    chosen when a package is registered. It is chosen by calling `ghc --abi-hash` on the compiled modules and appending ``\
``    the hash as a suffix to the string representing the `PackageIdentifier`. ``

`` `GHC.PackageId` (these currently look like "base-4.1.0.0" in GHC 6.12):: ``\
``    Inside GHC, we use the type `PackageId`, which is a `FastString`.  The (Z-encoding of) `PackageId` prefixes each ``\
`   external symbol in the generated code, so that the modules of one package do not clash with those of another package,`\
`   even when the module names overlap.`

Design constraints
------------------

`1. We want [wiki:Commentary/Compiler/RecompilationAvoidance recompilation avoidance] to work.  This means that symbol names should not contain any information that varies too often, such as the ABI hash of the module or package.  The ABI of an entity should depend only on its definition, and the definitions of the things it depends on.`

`2. We want to be able to detect ABI incompatibility.  If a package is recompiled and installed over the top of the old one, and the new version is ABI-incompatible with the old one, then packages that depended on the old version should be detectably broken using the tools.`

`3. ABI compatibility:`\
`   * We want repeatable compilations.  Compiling a package with the same inputs should yield the same outputs.`\
`   * Furthermore, we want to be able to make compiled packages that expose an ABI that is compatible (e.g. a superset)`\
`     of an existing compiled package.`\
`   * Modular upgrades: we want to be able to upgrade an existing package without recompiling everything that depends`\
`     on it, by ensuring that the replacement is ABI-compatible.`\
`   * Shared library upgrades.  We want to be able to substitute a new ABI-compatible shared library for an old one, and all the existing binaries linked against the old version continue to work.`\
`   * ABI compatibility is dependent on GHC too; changes to the compiler and RTS can introduce ABI incompatibilities.  We`\
`     guarantee to only make ABI incompatible changes in a major release of GHC.  Between major releases, ABI compatibility`\
`     is ensured; so for example it should be possible to use GHC 6.12.2 with the packages that came with GHC 6.12.1.`

Right now, we do not have repeatable compilations, so while we cannot do
(3), we keep it in mind.

The Plan
--------

We need to talk about some more package Ids:

``  * `PackageSymbolId`: the symbol prefix used in compiled code. ``\
``  * `PackageLibId`: the package Id in the name of a compiled library file (static and shared). ``

### Detecting ABI incompatibility

``  * in the package database, dependencies specify the `InstalledPackageId`. ``

` * The package database will contain at most one instance of a given package/version combination.  The tools`\
`   are not currently able to cope with multiple instances (e.g. GHC's -package flag selects by name/version).`

` * If, say, package P-1.0 is recompiled and re-installed, the new instance of the package will almost`\
`   certainly have an incompatible ABI from the previous version.  We give the new package a distinct`\
``    `InstalledPackageId`, so that packages that depend on the old P-1.0 will now be detectably broken. ``

``  * `PackageSymbolId`: We do not use the `InstalledPackageId` as the symbol prefix in the compiled code, because  ``\
`   that interacts badly with [wiki:Commentary/Compiler/RecompilationAvoidance recompilation avoidance].  Every time we pick a`\
``    new unique `InstalledPackageId` (e.g. when reconfiguring the package), we would have to recompile ``\
``    the entire package.  Hence, the `PackageSymbolId` is picked deterministically for the package, e.g. ``\
``    it can be the `PackageIdentifier`. ``

``  * `PackageLibId`: we do want to put the `InstalledPackageId` in the name of a library file, however.  This allows ``\
`   ABI incompatibility to be detected by the linker.  This is important for shared libraries too: we`\
`   want an ABI-incompatible shared library upgrade to be detected by the dynamic linker.  Hence,`\
``    `PackageLibId` == `InstalledPackageId`. ``

### Allowing ABI compatibilty

`* The simplest scheme is to have an identifier for each distinct ABI, e.g. a pair of the package name and an integer`\
`  that is incremented each time an ABI change of any kind is made to the package.  The ABI identifier`\
``   is declared by the package, and is used as the `PackageSymbolId`.  Since packages with the same ABI identifier ``\
``   are ABI-compatible, the `PackageLibId` can be the same as the `PackageSymbolId`. ``

`* The previous scheme does not allow ABI-compatible changes (e.g. ABI extension) to be made.  Hence, we could`\
`  generalise it to a major/minor versioning scheme.`\
``   * the ABI major version is as before, the package name + an integer.  This is also the `PackageSymbolId`. ``\
`  * the ABI minor version is an integer that is incremented each time the ABI is extended in a compatible way.`\
`  * package dependencies in the database specify the major+minor ABI version they require, in addition to the`\
``     `InstalledPackageId`.  They may be satisfied by a greater minor version; when upgrading a package with an  ``\
``     ABI-compatible replacement, ghc-pkg updates dependencies to point to the new `InstalledPackageId`. ``\
``   * `PackageLibId` is the major version.  In the case of shared libraries, we may name the library using the ``\
`    major + minor versions, with a symbolic link from the major version to major+minor.`\
``   * the shared library `SONAME` is the major version. ``

`* The previous scheme only allows ABI-compatible changes to be made in a linear sequence.  If we want a tree-shaped`\
`  compatibility structure, then something more complex is needed (ToDo).`

`* The previous schemes only allow compatible ABI changes to be made.  If we want to allow incompatible changes to be`\
`  made, then we need something like ELF's symbol versioning.  This is probably overkill, since we will be making`\
`  incompatible ABI changes in the compiler and RTS at regular intervals anyway, so long-term ABI compatibility is`\
`  impractical at this stage.`

[PageOutline](PageOutline "wikilink")

The Parser
==========

\[Very incomplete. Please extend as you learn more.\]

The parser is written using

`* `[`Alex`](http://www.haskell.org/alex/)`, for lexical analysis.  Source file `[`GhcFile(compiler/parser/Lexer.x)`](GhcFile(compiler/parser/Lexer.x) "wikilink")\
`* `[`Happy`](http://www.haskell.org/happy/)`, for the parser itself.  Source file `[`GhcFile(compiler/parser/Parser.y)`](GhcFile(compiler/parser/Parser.y) "wikilink")`.`\
`` * `RdrHsSyn`, for Haskell support functions.  Source file  ``[`GhcFile(compiler/parser/RdrHsSyn.lhs)`](GhcFile(compiler/parser/RdrHsSyn.lhs) "wikilink")

Principles
----------

Making a parser parse *precisely* the right language is hard. So GHC's
parser follows the following principle:

`* `**`We` `often` `parse` `"over-generously",` `and` `filter` `out`
`the` `bad` `cases` `later.`**

Here are some examples:

`` * Patterns are parsed as expressions, and transformed from `HsExpr.HsExp` into `HsPat.HsPat` in `RdrHsSyn.checkPattern`.  An expression like `[x | x<-xs]` that doesn't look like a pattern is rejected by `checkPattern`. ``

`` * The context of a type is parsed as a type, and then converted into a context by `RdrHsSyn.checkContext`.  For example, when parsing ``

``   the parser can only discover that `(Read a, Num a)` is a context, rather than a type, when it meets the `=>`.  That requires infinite lookahead.  So instead we parse `(Read a, Num a)` as a tuple type, and then convert it to a context when we see the `=>`. ``

Sometimes the over-generous parsing is only dealt with by the renamer.
For example:

`* Infix operators are parsed as if they were all left-associative. The renamer uses the fixity declarations to re-associate the syntax tree.`

There are plenty more examples. A good feature of this approach is that
the error messages later in compilation tend to produce much more
helpful error messages. Errors generated by the parser itself tend to
say "Parse error on line X" and not much more.

The main point is this. If you are changing the parser, feel free to
make it accept more programs than it does at the moment, provided you
also add a later test that rejects the bad programs. Typically you need
this flexibility if some new thing you want to add makes the pars
ambiguous, and you need more context to disambiguate. Delicate hacking
of the LR grammar is to be discouraged. It's very hard to maintain and
debug.

Avoiding right-recursion
------------------------

Be sure to read [this
section](https://www.haskell.org/happy/doc/html/sec-sequences.html) of
the Happy manual for tips on avoiding right recursion. In GHC, the
preferred method is using a left-recursive \`OrdList\`, as below:

\`OrdList\` operationally works the same way as building a list in
reverse (as in the Happy manual), but it makes it less likely you'll
forget to call \`reverse\` when you need to get the \`final\` list out.

One interesting, non-obvious fact, is that if you \*do\* use a
right-recursive parser, the "extra semi-colons" production should NOT be
pluralized:

Indentation
-----------

Probably the most complicated interaction between the lexer and parser
is with regards to //whitespace-sensitive layout.// The most important
thing to know is that the lexer understands layout, and will output
virtual open/close curlies (productions \`vocurly\` and \`vccurly\`) as
well as semicolons, which can then be used as part of productions in
\`Parser.y\`. So for example, if you are writing a rule that will make
use of indentation, you should accept both virtual and literal curlies:

Notice the use of \`close\` rather than \`vccurly\`: \`close\` is a
production that accepts both \`vccurly\` and a Happy \`error\`; that is,
if we encounter an error in parsing, we try exiting an indentation
context and trying again. This ensures, for example, that the top-level
context can be closed even if no virtual curly was output.

The top-level of a Haskell file does not automatically have a layout
context; when there is no \`module\` keyword, a context is implicitly
pushed using \`missing\_module\_keyword\`.

When writing grammars that accept semicolon-separated sequences, be sure
to include a rule allowing for trailing semicolons (see the previous
section), otherwise, you will reject layout.

Syntax extensions
-----------------

Many syntactic features must be enabled with a \`LANGUAGE\` flag, since
they could cause existing Haskell programs to stop compiling, as turn
some identifiers into keywords. We primarily affect this change of
behavior in the lexer, by turning on/off certain tokens. This is done
using predicates, which let Alex turn token rules on and off depending
on what extensions are enabled:

To add a new syntax extension, add a constructor to \`ExtBits\` and set
the bit appropriately in \`mkPState\`.

Pinned Objects
==============

The GC does not support pinning arbitrary objects. Only objects that
have no pointer fields can be pinned. Nevertheless, this is a useful
case, because we often want to allocate garbage-collectable memory that
can be passed to foreign functions via the FFI, and we want to be able
to run the GC while the foreign function is still executing (for a
\`safe\` foreign call). Hence, the memory we allocated must not move.

Bytestrings are currently allocated as pinned memory, so that the
bytestring contents can be passed to FFI calls if necessary.

The RTS provides an API for allocating pinned memory, in
[GhcFile(includes/rts/storage/GC.h)](GhcFile(includes/rts/storage/GC.h) "wikilink"):

This allocates memory from the given Capability's nursery.

Pinned objects work in the GC as follows:

`* Pinned objects are allocated into a block of their own, not mixed up with unpinned objects.`\
`* The block containing pinned objects is marked as a `*`large`
`block`*`` , i.e. the `BF_LARGE` bit is set in `bd->flags`. ``\
`` * When encountering a live object in a `BF_LARGE` block, the GC never copies the object, instead it just re-links the whole block onto the `large_objects` list of the destination generation. ``\
`* The GC doesn't have to scavenge the pinned object, since it does not contain any pointers.  This is just as well, because we cannot scan blocks for live pinned objects, due to [wiki:Commentary/Rts/Storage/Slop slop].  Hence the restriction that pinned objects do not contain pointers.`

This means that using pinned objects may lead to memory fragmentation,
since a single pinned object keeps alive the whole block in which it
resides. If we were to implement a non-moving collector such as
\[wiki:Commentary/Rts/Storage/GC/Sweeping mark-region\], then we would
be able to reduce the impact of fragmentation due to pinned objects.

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>
Commentary/Rts/Storage/GC/Pinned

Overview
========

GHC is structured into two parts:

`` * The `ghc` package (in subdirectory `compiler`), which implements almost all GHC's functionality. It is an ordinary Haskell library, and can be imported into a Haskell program by saying `import GHC`. ``\
`` * The `ghc` binary (in subdirectory `ghc`) which imports the `ghc` package, and implements the I/O for the `ghci` interactive loop. ``

Here's an overview of the module structure of the top levels of GHC
library. (Note: more precisly, this is the plan. Currently the module
\`Make\` below is glommed into the giant module \`GHC\`.)

The driver pipeline
===================

The driver pipeline consist of a couple of phases that call other
programs and generate a series of intermediate files. Code responsible
for managing the order of phases is in
[GhcFile(compiler/main/DriverPhases.hs)](GhcFile(compiler/main/DriverPhases.hs) "wikilink"),
while managing the driver pipeline as a whole is coded in
[GhcFile(compiler/main/DriverPipeline.hs)](GhcFile(compiler/main/DriverPipeline.hs) "wikilink").
Note that driver pipeline is not the same thing as compilation pipeline:
the latter is part of the former.

Let's take a look at the overall structure of the driver pipeline. When
we compile or ("lhs" extension means that Literate Haskell is being
used) the following phases are being called (some of them depending on
additional conditions like file extensions or enabled flags):

`* Run the `**`unlit`
`pre-processor`**`, ``, to remove the literate markup, generating ``.  The `` processor is a C program kept in `[`GhcFile(utils/unlit)`](GhcFile(utils/unlit) "wikilink")`.`

`* Run the `**`C`
`preprocessor`**`` , `cpp`, (if  ``` is specified), generating ``.`

`* Run `**`the` `compiler`
`itself`**`. This does not start a separate process; it's just a call to a Haskell function.  This step always generates an [wiki:Commentary/Compiler/IfaceFiles `**`interface`
`file`**`] ``, and depending on what flags you give, it also generates a compiled file. As GHC supports three backend code generators currently (a native code generator, a C code generator and an llvm code generator) the possible range of outputs depends on the backend used. All three support assembly output:`\
`  * Object code: no flags required, file `` (supported by all three backends)`\
`  * Assembly code: flag ``, file `` (supported by all three backends)`\
`  * C code: flags ``, file `` (only supported by C backend)`

` * In the `` case:`\
`   * Run the `**`C`
`compiler`**``  on `Foo.hc`, to generate `Foo.s`. ``

``  * If `-split-objs` is in force, run the  ``**`splitter`**``  on `Foo.s`.  This splits `Foo.s` into lots of small files.  The idea is that the static linker will thereby avoid linking dead code. ``

``  * Run the assembler on `Foo.s`, or if `-split-objs` is in force, on each individual assembly file. ``

The compiler pipeline
=====================

The **compiler itself**, independent of the external tools, is also
structured as a pipeline. For details (and a diagram), see
\[wiki:Commentary/Compiler/HscMain\]

Video
=====

Video of compilation pipeline explanation from 2006: [Compilation
Pipeline](http://www.youtube.com/watch?v=dzSc8ACz_mw&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
and interface files (17'30")

Platforms
=========

Please read \[wiki:CrossCompilation this wiki page\] on cross
compilation for a better understanding of the situation here. There are
three platforms of interest to GHC when compiling and running:

`* The `**`Build`**` platform. This is the platform on which we are building GHC.`\
`* The `**`Host`**` platform. This is the platform on which we are going to run this GHC binary, and associated tools.`\
`* The `**`Target`**` platform. This is the platform for which this GHC binary will generate code.`

Limitations
-----------

At the moment, there is limited support for having different values for
build, host, and target. Please refer to the \[wiki:CrossCompilation
cross compilation\] page for more details. In particular:

The build platform is currently always the same as the host platform.
The build process needs to use some of the tools in the source tree, for
example ghc-pkg and hsc2hs.

If the target platform differs from the host platform, then this is
generally for the purpose of building .hc files from Haskell source for
porting GHC to the target platform. Full cross-compilation isn't
supported (yet).

Macros
------

In the compiler's source code, you may make use of the following CPP
symbols:

`* `*`xxx`*`` `_TARGET_ARCH` ``\
`* `*`xxx`*`` `_TARGET_VENDOR` ``\
`* `*`xxx`*`` `_TARGET_OS` ``\
`* `*`xxx`*`` `_HOST_ARCH` ``\
`* `*`xxx`*`` `_HOST_VENDOR` ``\
`* `*`xxx`*`` `_HOST_OS` ``

where *xxx* is the appropriate value: eg. \`i386\_TARGET\_ARCH\`.
However **GHC is moving away from using CPP for this purpose** in many
cases due to the problems it creates with supporting cross compilation.

So instead of it the new plan is to always build GHC as a cross compiler
and select the appropriate values and backend code generator to run and
runtime. For this purpose there is the Platform module
([GhcFile(compiler/utils/Platform.hs)](GhcFile(compiler/utils/Platform.hs) "wikilink")).
That contains various methods for querying the !DynFlags
([GhcFile(compiler/main/DynFlags.hs)](GhcFile(compiler/main/DynFlags.hs) "wikilink"))
value for what platform GHC is currently compiling for. You should use
these when appropriate over the CPP methods.

Pointer Tagging
===============

Paper: [Faster laziness using dynamic pointer
tagging](http://research.microsoft.com/pubs/67969/ptr-tagging.pdf)

In GHC we "tag" pointers to heap objects with information about the
object they point to. The tag goes in the low 2 bits (3 bits on a 64-bit
platform) of the pointer, which would normally be zero since heap
objects are always \[wiki:Commentary/Rts/Word word\]-aligned.

Meaning of the tag bits
-----------------------

The way the tag bits are used depends on the type of object pointed to:

`* If the object is a `**`constructor`**`, the tag bits contain the `*`constructor`
`tag`*`, if the number of`\
`  constructors in the datatype is less than 4 (less than 8 on a 64-bit platform).  If the number of`\
`  constructors in the datatype is equal to or more than 4 (resp 8), then the tag bits have the value 1, and the constructor tag`\
`  is extracted from the constructor's info table instead.`

`* If the object is a `**`function`**`, the tag bits contain the `*`arity`*` of the function, if the arity fits`\
`  in the tag bits.`

`* For a pointer to any other object, the tag bits are always zero.`

Optimisations enabled by tag bits
---------------------------------

The presence of tag bits enables certain optimisations:

`* In a case-expression, if the variable being scrutinised has non-zero tag bits, then we know`\
`  that it points directly to a constructor and we can avoid `*`entering`*` it to evaluate it.`\
`  Furthermore, for datatypes with only a few constructors, the tag bits will tell us `*`which`*\
`  constructor it is, eliminating a further memory load to extract the constructor tag from the`\
`  info table.`

`* In a [wiki:Commentary/Rts/HaskellExecution/FunctionCalls#Genericapply generic apply], if the function being applied has a tag value that indicates it has exactly the`\
`  right arity for the number of arguments being applied, we can jump directly to the function, instead of`\
`  inspecting its info table first.`

Pointer-tagging is a fairly significant optimisation: we measured 10-14%
depending on platform. A large proportion of this comes from eliminating
the indirect jumps in a case expression, which are hard to predict by
branch-prediction. The paper has full results and analysis.

Garbage collection with tagged pointers
---------------------------------------

The \[wiki:Commentary/Rts/Storage/GC garbage collector\] maintains tag
bits on the pointers it traverses. This is easier, it turns out, than
*reconstructing* tag bits. Reconstructing tag bits would require that
the GC knows not only the tag of the constructor (which is in the info
table), but also the family size (which is currently not in the info
table), since a constructor from a large family should always have tag
1. To make this practical we would probably need different closure types
for "small family" and "large family" constructors, and we already
subdivide the constructor closures types by their layout.

Additionally, when the GC eliminates an indirection it takes the tag
bits from the pointer inside the indirection. Pointers to indirections
always have zero tag bits.

Invariants
----------

Pointer tagging is *not* optional, contrary to what the paper says. We
originally planned that it would be: if the GC threw away all the tags,
then everything would continue to work albeit more slowly. However, it
turned out that in fact we really want to assume tag bits in some
places:

` * In the continuation of an algebraic case, R1 is assumed tagged`\
` * On entry to a non-top-level function, R1 is assumed tagged`

If we don't assume the value of the tag bits in these places, then extra
code is needed to untag the pointer. If we can assume the value of the
tag bits, then we just take this into account when indexing off R1.

This means that everywhere that enters either a case continuation or a
non-top-level function must ensure that R1 is correctly tagged. For a
case continuation, the possibilities are:

` * the scrutinee of the case jumps directly to the alternative if R1 is already tagged.`\
` * the constructor entry code returns to an alternative.  This code adds the correct tag.`\
` * if the case alternative fails a heap or stack check, then the RTS will re-enter the alternative after`\
`   GC.  In this case, our re-entry arranges to enter the constructor, so we get the correct tag by`\
`   virtue of going through the constructor entry code.`

For a non-top-level function, the cases are:

``  * unknown function application goes via `stg_ap_XXX` (see [wiki:Commentary/Rts/HaskellExecution/FunctionCalls#Genericapply Generic Apply]).   ``\
`   The generic apply functions must therefore arrange to correctly tag R1 before entering the function.`\
` * A known function can be entered directly, if the call is made with exactly the right number of arguments.`\
` * If a function fails its heap check and returns to the runtime to garbage collect, on re-entry the closure`\
`   pointer must be still tagged.`\
` * the PAP entry code jumps to the function's entry code, so it must have a tagged pointer to the function`\
`   closure in R1.  We therefore assume that a PAP always contains a tagged pointer to the function closure.`

In the second case, calling a known non-top-level function must pass the
function closure in R1, and this pointer *must* be correctly tagged. The
code generator does not arrange to tag the pointer before calling the
function; it assumes the pointer is already tagged. Since we arrange to
tag the pointer when the closure is created, this assumption is normally
safe. However, if the pointer has to be saved on the stack, say across a
call, then when the pointer is retrieved again we must either retag it,
or be sure that it is still tagged. Currently we do the latter, but this
imposes an invariant on the garbage collector: all tags must be retained
on non-top-level function pointers.

Pointers to top-level functions are not necessarily tagged, because we
don't always know the arity of a function that resides in another
module. When optimisation is on, we do know the arities of external
functions, and this information is indeed used to tag pointers to
imported functions, but when optimisation is off we do not have this
information. For constructors, the interface doesn't contain information
about the constructor tag, except that there may be an unfolding, but
the unfolding is not necessarily reliable (the unfolding may be a
constructor application, but in reality the closure may be a CAF, e.g.
if any of the fields are references outside the current shared library).

Compacting GC
-------------

Compacting GC also uses tag bits, because it needs to distinguish
between a heap pointer and an info pointer quickly. The compacting GC
has a complicated scheme to ensure that pointer tags are retained, see
the comments in
[GhcFile(rts/sm/Compact.c)](GhcFile(rts/sm/Compact.c) "wikilink").

Dealing with tags in the code
-----------------------------

Every time we dereference a pointer to a heap object, we must first zero
the tag bits. In the RTS, this is done with the inline function
(previously: macro) \`UNTAG\_CLOSURE()\`; in \`.cmm\` code this is done
with the \`UNTAG()\` macro. Surprisingly few places needed untagging to
be added.

Position-Independent Code and Dynamic Linking
=============================================

We need to generate position-independent code on most platforms when we
want our code to go into dynamic libraries (also referred to as shared
libraries or DLLs). On some platforms (AIX, powerpc64-linux,
x86\_64-darwin), PIC is required for all code.

To access things defined in a dynamic library, we might need to do
special things, such as look up the address of the imported thing in a
table of pointers, depending on what platform we are on.

How to access symbols
---------------------

A C compiler is in an unfortunate position when generating PIC code, as
it does not have any hints, whether an accessed symbol ends up in the
same dynamic library or if it is truely an external symbol (from the
dynamic library point of view). It can only generate non-PIC access for
symbols generated within the same object file. In Haskell, we can do
better as we assume all package code to end up in a single dynamic
library. Hence, all intra-package symbol accesses can be generated as
code that does direct access. For all inter-package accesses (package
haskell98 accessing symbols in package base, e.g.), we have to generate
PIC code. For the following we establish the following:

`* `*`object-local`
`symbols`*`, symbols within the same object file. Always generate direct access. `\
`* `*`package-local`
`symbols`*`, symbols within the same Haskell package. The NCG can generate direct access code, C compilers can't.`\
`* `*`local` `symbols`*`, either object-local or package-local.`\
`* `*`global`
`symbols`*`, symbol in different libraries/packages. Always generate PIC.`

CLabel.labelDynamic
-------------------

On most platforms, we can access any global symbol as if it was imported
from a dynamic library; this usually means a small performance hit (an
extra pointer dereference), but it is otherwise harmless. On some
platforms, we have to access all global symbols this way. On Windows, we
must know exactly which symbols are DLL-imported and which aren't.

Module \`CLabel\` contains a function \`labelDynamic :: CLabel -&gt;
Bool\` which is supposed to know whether a \`CLabel\` is imported from a
dynamic library. On Windows, this function needs to be exact; everywhere
else, we don't mind the occasional false positive.

Info Tables
-----------

Info tables are in the text segment, which is supposed to be read-only
and position-independent. Therefore, an info table *must not* contain
any absolute address; instead, all addresses in info tables are instead
encoded as relative offsets from the info label.

Note that this is done even when we are generating code that is
otherwise position-dependent, in order to preserve binary compatibility
between PIC and non-PIC.

It is not possible to generate those relative references from C code, so
for the via-C compilation route, we pretty-print these relative
references (\`CmmLabelDiffOff\` in cmm) as absolute references and have
the mangler convert them to relative references again.

Imported labels in SRTs (Windows)
---------------------------------

Windows doesn't support references to imported labels in the data
segment; on other platforms, the dynamic linker will just relocate the
pointers in the SRTs to point to the right symbols. There is a hack in
the code that tries to work around it; it might be bitrotted, and it
might have been made unnecessary by the GNU linker's new auto-import on
Windows.

PIC and dynamic linking support in the NCG
------------------------------------------

The module \`PositionIndependentCode\` lies at the heart of PIC and
dynamic linking support in the native code generator.

The basic idea is to call a function \`cmmMakeDynamicReference\` for all
labels accessed from the code during the cmm-to-cmm transformation
phase. This function will decide on the appropriate way to access the
given label for the current platform and the current combination of
-fPIC and -dynamic flags.

We extend Cmm and the \`CLabel\` module by a few things to allow us to
express all the different things that occur on different platforms:

The \`Cmm.GlobalReg\` datatype has a constructor \`PicBaseReg\`. This
PIC base register is the register relative to which position-independent
references are calculated. This can be a general-purpose register that
is allocated on a per-!CmmProc basis, or it can be a dedicated register,
like the instruction pointer \`%rip\` on x86\_64.

How things are done on different platforms
------------------------------------------

This section is a survey of how PIC and dynamic linking works on
different platforms. There are small snippets of assembly code for
several platforms, platforms that are similar to other platforms are
left out (e.g. powerpc-darwin is left out, because the logic is the same
as for i386-darwin). I hope the reader will not be too confused by
irrelevant differences between the platforms, such as the fact that
Darwin and Windows prefix all symbols with an underscore, and Linux
doesn't.

### Position dependent code

In the absence of PIC and dynamic linking, things are simple; when we
use a label in assembly code, the linker will make sure it points to the
right place.

Now, to access a symbol \`xfoo\` that has been imported from a dynamic
library, we do not want to mention the address of \`xfoo\` in the text
section, because it would need to be modified at load-time.

One solution is to allocate a pointer to the imported symbol in a
writable section and have the dynamic linker fill in this pointer table.
The pointer table itself resides at a statically known address. The
\_\_imp\_\_\* symbols on Windows are automatically generated by the
linker.

On Mac OS X, the same system is used for data imports, but this time we
have to define the symbol pointers ourselves. For references to code,
there is an additional mechanism available; we can jump to a small piece
of stub code that will resolve the symbol the first time it is used, in
order to reduce application load times. Unfortunately, everything on Mac
OS X requires 16-byte stack alignment, even the dynamic linker, so we
cannot use this for a tail call.

In theory, dynamic linking is transparent to position-dependent code on
Linux, i.e. the code for accessing imported labels should look exactly
the same as for non-imported labels. Unfortunately, things just don't
work as they should for strange stuff like info tables.

When the ELF static linker finds a jump or call to an imported symbol,
it automatically redirects the jump or call to a linker generated code
stub (in the so-called procedure linkage table, or PLT). The linker then
considers the label to be a code label and redirects all further
references to the label to the code stub, even if they are data
references. If this ever happens to an info label, our program will
crash, as there is no info table in front of the code stub.

When the ELF static linker finds a data reference to an imported symbol
(that it doesn't consider a code label), it allocates space for that
symbol in the executable's data section and issues an \`R\_COPY\`
relocation, which instructs the dynamic linker to copy the (initial)
contents of the symbol to its new place in the executable's image. All
references to the symbol from the dynamic library are relocated to point
to the symbol's new location, instead.

If \`R\_COPY\` is ever used for an info label, our program will also
crash, because the data we're interested in is \*before\* the info label
and is not copied to the symbol's new home.

Fortunately, if the static linker finds a pointer to an imported symbol
in a writable section, it just instructs the dynamic linker to update
that pointer to the symbols address, without doing anything "funny". We
can therefore work around these problems.

The workaround is inspired by the position-independent code that GCC
generates for powerpc-linux, a platform that is amazingly broken.

Things look pretty much the same on x86\_64-linux, powerpc-linux and
powerpc-darwin; PowerPC has the added handicap that it takes two
instructions to load a 32 bit quantity into a register. On
x86\_64-darwin, powerpc64-linux and all versions of AIX, PIC is
*required*.

### Position independent code

First, let it be said that there is no such thing as
position-independent code on Windows. The dynamic linker will just
patiently relocate all dynamic libraries that are not loaded at their
preferred base address. On all other platforms, PIC is at least strongly
recommended for dynamic libraries.

In an ideal world, there would be assembler instructions for referring
to things via an offset from the current instruction pointer. Jump
instructions are ip-relative on all platforms that GHC runs on, but for
data accesses, only x86\_64 is this ideal world.

On x86\_64, on both Linux and Mac OS X, we can use \`foo(%rip)\` to
encode an instruction pointer relative data reference to \`foo\`, and
\`foo@GOTPCREL(%rip)\` to encode an instruction pointer relative
referece to a linker-generated symbol pointer for symbol \`foo\`. A
linker-generated code stub for imported code can be accessed by
appending \`@PLT\` to the label on Linux, and is used implicitly when
necessary on Mac OS X.

Again, we have to avoid the code stubs for tail-calls and use the symbol
pointer instead, because there is a stack alignment requirement.

Other platforms are not nearly as nice; i386 and powerpc\[64\] do not
have a way of accessing the current instruction pointer or referring to
data relative to it. The \*only\* way to get at the current instruction
pointer is to issue a call instruction. To generate PIC code, we have to
do just that at the beginning of each function.

On Darwin, things are relatively straightforward:

There is one more small additional complication on Darwin. The assembler
doesn't support label difference expressions involving labels not
defined in the same source file, so we have to treat all symbols not
defined in the same source file as dynamically imported.

On Linux, we need to first calculate the address of the Global Offset
Table (GOT) and then use \`bar@GOT\` to refer to symbol pointers and
\`bar@GOTOFF\` to refer to a local symbol relative to the GOT. Also, the
linker-generated code-stubs (\`xfoo@PLT\`) require the address of the
GOT to be in register \`%ebx\` when they are invoked. The NCG currently
doesn't do this, so we avoid code stubs altogether on i386.

**To be done:** powerpc-linux, AIX/powerpc64-linux

Linking on ELF
--------------

To generate a DSO on ELF platform, we use GNU ld. Except for
\`-Bsymbolic\`, ld is invoked regularly with the \`-shared\` option, and
\`-o\` pointing to the output DSO file followed objects that in its sum
compose an entire package. In Haskell, we assume that there is a
one-to-one mapping from packages to DSOs. So, all parts of the base
package will end up in a libHSbase.so. As intra-package references are
not generated as PIC code, we have to supply all objects that make up a
package, so that ld is able to resolve these references before writing a
(.text) relocation free DSO library file. To enable these cross-object
relocations GNU ld needs \`-Bsymbolic\`.

Mangling dynamic library names
------------------------------

As Haskell DSOs might end up in standard library paths, and as they
might not be compatible among compilers and compiler version, we need to
mangle their names to include the compiler and its version.

The scheme is
libHS*<package>*-*<package-version>*-*<compiler><compilerversion>*.so.
E.g. libHSbase-2.1-ghc6.6.so

GHC Commentary: The C code generator
====================================

Source:
[GhcFile(compiler/cmm/PprC.hs)](GhcFile(compiler/cmm/PprC.hs) "wikilink")

This phase takes \[wiki:Commentary/Compiler/CmmType Cmm\] and generates
plain C code. The C code generator is very simple these days, in fact it
can almost be considered pretty-printing. It is only used for
unregisterised compilers.

Header files
------------

GHC was changed (from version 6.10) so that the C backend no longer uses
header files specified by the user in any way. The \`c-includes\` field
of a \`.cabal\` file is ignored, as is the \`-\#include\` flag on the
command-line. There were several reasons for making this change:

This has several advantages:

`* Via C compilation is consistent with the other backend with respect to FFI declarations:`\
`  all bind to the ABI, not the API.`\
` `\
`* foreign calls can now be inlined freely across module boundaries, since`\
`  a header file is not required when compiling the call.`\
` `\
`* bootstrapping via C will be more reliable, because this difference`\
`  in behavior between the two backends has been removed.`\
` `

There are some disadvantages:

`* we get no checking by the C compiler that the FFI declaration`\
`  is correct.`

`* we can't benefit from inline definitions in header files.`\
` `

Prototypes
----------

When a label is referenced by an expression, the compiler needs to know
whether to declare the label first, and if so, at what type.

C only lets us declare an external label at one type in any given source
file, even if the scopes of the declarations don't overlap. So we either
have to scan the whole code to figure out what the type of each label
should be, or we opt for declaring all labels at the same type and then
casting later. Currently we do the latter.

`* all labels referenced as a result of an FFI declaration`\
``   are declared as `extern StgWord[]`, including function labels. ``\
`  If the label is called, it is first cast to the correct`\
`  function type.  This is because the same label might be`\
`  referred to both as a function and an untyped data label in`\
`  the same module (e.g. Foreign.Marsal.Alloc refers to "free"`\
`  this way).  `

`* An exception is made to the above for functions declared with`\
``   the `stdcall` calling convention on Windows.  These functions must ``\
``   be declared with the `stdcall` attribute and a function type, ``\
``   otherwise the C compiler won't add the `@n` suffix to the symbol. ``\
``   We can't add the `@n` suffix ourselves, because it is illegal ``\
`  syntax in C.  However, we always declare these labels with the`\
``   type `void (*)(void)`, to avoid conflicts if the same function ``\
``   is called at different types in one module (see `Graphics.Win32.GDI.HDC.SelectObject`). ``

`` * Another exception is made for functions that are marked `never returns` in C--.  We ``\
``   have to put an `__attribute__((noreturn))` on the declaration for these functions, ``\
`  and it only works if the function is declared with a proper function type and`\
`  called without casting it to/from a pointer.  So only the correct prototype`\
`  will do here.`

`* all RTS symbols already have declarations (mostly with the correct`\
`  type) in `[`GhcFile(includes/StgMiscClosures.h)`](GhcFile(includes/StgMiscClosures.h) "wikilink")`, so no declarations are generated.`

`* certain labels are known to have been defined earlier in the same file,`\
`  so a declaration can be omitted (e.g. SRT labels)`

`` * certain math functions (`sin()`, `cos()` etc.) are already declared because ``\
`  we #include math.h, so we don't emit declarations for these.  We need`\
`  to #include math.h because some of these functions have inline`\
`  definitions, and we get terrible code otherwise.`

When compiling the RTS cmm code, we have almost no information about
labels referenced in the code. The only information we have is whether
the label is defined in the RTS or in another package: a label that is
declared with an import statement in the .cmm file is assumed to be
defined in another package (this is for dynamic linking, where we need
to emit special code to reference these labels).

For all other labels referenced by RTS .cmm code, we assume they are RTS
labels, and hence already declared in
[GhcFile(includes/StgMiscClosures.h)](GhcFile(includes/StgMiscClosures.h) "wikilink").
This is the only choice here: since we don't know the type of the label
(info, entry etc.), we can't generate a correct declaration.

[PageOutline](PageOutline "wikilink")

Primitive Operations (!PrimOps)
===============================

!PrimOps are functions that cannot be implemented in Haskell, and are
provided natively by GHC. For example, adding two values is provided as
the !PrimOp , and allocating a new mutable array is the !PrimOp .

!PrimOps are made available to Haskell code through the virtual module .
This module has no implementation, and its interface never resides on
disk: if is imported, we use a built-in value - see in
[GhcFile(compiler/iface/LoadIface.hs)](GhcFile(compiler/iface/LoadIface.hs) "wikilink").

It would also be useful to look at the
\[wiki:Commentary/Compiler/WiredIn Wired-in and known-key things\] wiki
page to understand this topic.

The primops.txt.pp file
-----------------------

The file
[GhcFile(compiler/prelude/primops.txt.pp)](GhcFile(compiler/prelude/primops.txt.pp) "wikilink")
includes all the information the compiler needs to know about a !PrimOp,
bar its actual implementation. For each !PrimOp, lists:

`* Its name, as it appears in Haskell code (eg. int2Integer#)`\
`* Its type`\
`* The name of its constructor in GHC's `` data type.`\
`* Various properties, such as whether the operation is commutable, or has side effects.`

For example, here's the integer multiplication !PrimOp:

The file is processed first by CPP, and then by the program (see
[GhcFile(utils/genprimopcode)](GhcFile(utils/genprimopcode) "wikilink")).
generates the following bits from :

`* Various files that are ``d into `[`GhcFile(compiler/prelude/PrimOp.hs)`](GhcFile(compiler/prelude/PrimOp.hs) "wikilink")`,`\
`  containing declarations of data types and functions describing the !PrimOps.  See`\
`  `[`GhcFile(compiler/Makefile)`](GhcFile(compiler/Makefile) "wikilink")`.`

`* ``, a file that contains (curried) wrapper`\
`  functions for each of the !PrimOps, so that they are accessible from byte-code, and`\
`  so that the [wiki:Commentary/Rts/Interpreter byte-code interpreter] doesn't need to implement any !PrimOps at all: it`\
`  just invokes the compiled ones from ``.`

`* ``, a source file containing dummy declarations for`\
`  all the !PrimOps, solely so that Haddock can include documentation for `\
`  in its documentation for the `` package.  The file `` is never`\
`  actually compiled, only processed by Haddock.`

Note that if you want to create a polymorphic primop, you need to return
, not .

Implementation of !PrimOps
--------------------------

!PrimOps are divided into two categories for the purposes of
implementation: inline and out-of-line.

### Inline !PrimOps

Inline !PrimOps are operations that can be compiled into a short
sequence of code that never needs to allocate, block, or return to the
scheduler for any reason. An inline !PrimOp is compiled directly into
\[wiki:Commentary/Rts/Cmm Cmm\] by the
\[wiki:Commentary/Compiler/CodeGen code generator\]. The code for doing
this is in
[GhcFile(compiler/codeGen/StgCmmPrim.hs)](GhcFile(compiler/codeGen/StgCmmPrim.hs) "wikilink").

### Out-of-line !PrimOps

All other !PrimOps are classified as out-of-line, and are implemented by
hand-written C-- code in the file
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink"). An
out-of-line !PrimOp is like a Haskell function, except that

`* !PrimOps cannot be partially applied.  Calls to all !PrimOps are made at the correct arity; this is ensured by `\
`  the [wiki:Commentary/Compiler/HscMain CorePrep] pass.`

`* Out-of-line !PrimOps have a special, fixed, [wiki:Commentary/Rts/HaskellExecution#CallingConvention calling convention]:`\
`  all arguments`\
`  are in the [wiki:Commentary/Rts/HaskellExecution#Registers registers] R1-R8.  This is to make it easy to write the`\
`  C-- code for these !PrimOps: we don't have to write code for multiple calling conventions.`

It's possible to provide inline versions of out-of-line !PimOps. This is
useful when we have enough static information to generated a short, more
efficient inline version. For example, a call to can be implemented more
efficiently as an inline !PrimOp as the heap check for the array
allocation can be combined with the heap check for the surrounding code.
See \`shouldInlinePrimOp\` in
[GhcFile(compiler/codeGen/StgCmmPrim.hs)](GhcFile(compiler/codeGen/StgCmmPrim.hs) "wikilink").

### Foreign out-of-line !PrimOps and \`foreign import prim\`

A new and somewhat more flexible form of out-of-line !PrimOp is the
foreign out-of-line !PrimOp. These are essentially the same but instead
of their Cmm code being included in the RTS, they can be defined in Cmm
code in any package and instead of knowledge of the !PrimOp being baked
into the compiler, they can be imported using special FFI syntax:

The string (e.g. "int2Integerzh") is the linker name of the Cmm
function. Using this syntax requires the extensions
\`ForeignFunctionInterface\`, \`GHCForeignImportPrim\`, \`MagicHash\`,
\`UnboxedTuples\` and \`UnliftedFFITypes\`. The current type restriction
is that all arguments and results must be unlifted types, with two
additional possibilities: An argument may (since GHC 7.5) be of type
\`Any\` (in which case the called function will receive a pointer to the
heap), and the result type is allowed to be an unboxed tuple. The
calling convention is exactly the same as for ordinary out-of-line
primops. Currently it is not possible to specify any of the !PrimOp
attributes.

The \`integer-gmp\` package now uses this method for all the primops
that deal with GMP big integer values. The advantage of using this
technique is that it is a bit more modular. The RTS does not need to
include all the primops. For example in the integer case the RTS no
longer needs to link against the GMP C library.

The future direction is to extend this syntax to allow !PrimOp
attributes to be specified. The calling convention for primops and
ordinary compiled Haskell functions may be unified in future and at that
time it the restriction on using only unlifted types may be lifted.

It has been suggested that we extend this !PrimOp definition and import
method to cover all !PrimOps, even inline ones. This would replace the
current \`primops.txt.pp\` system of builtin !PrimOps. The inline
!PrimOps would still be defined in the compiler but they would be
imported in any module via \`foreign import prim\` rather than appearing
magically to be exported from the \`GHC.Prim\` module. Hugs has used a
similar system for years (with the syntax \`primitive seq :: a -&gt; b
-&gt; b\`).

Adding a new !PrimOp
--------------------

To add a new primop, you currently need to update the following files:

`* `[`GhcFile(compiler/prelude/primops.txt.pp)`](GhcFile(compiler/prelude/primops.txt.pp) "wikilink")`, which includes the`\
`  type of the primop, and various other properties.  Syntax and`\
`  examples are in the file.`

`* if the primop is inline, then:`\
`  `[`GhcFile(compiler/codeGen/StgCmmPrim.hs)`](GhcFile(compiler/codeGen/StgCmmPrim.hs) "wikilink")` defines the translation of`\
`  the primop into ``.`\
`       `\
`* for an out-of-line primop:`\
`  * `[`GhcFile(includes/stg/MiscClosures.h)`](GhcFile(includes/stg/MiscClosures.h) "wikilink")` (just add the declaration),`\
`  * `[`GhcFile(rts/PrimOps.cmm)`](GhcFile(rts/PrimOps.cmm) "wikilink")` (implement it here)`\
`  * `[`GhcFile(rts/Linker.c)`](GhcFile(rts/Linker.c) "wikilink")` (declare the symbol for GHCi)`

`* for a foreign out-of-line primop You do not need to modify the rts or compiler at all.`\
``   * `yourpackage/cbits/primops.cmm`: implement your primops here. You have to arrange for the .cmm file to be compiled and linked into the package. The GHC build system has support for this. Cabal does not yet. ``\
``   * `yourpackage/TheCode.hs`: use `foreign import prim` to import the primops. ``

In addition, if new primtypes are being added, the following files need
to be updated:

` * `[`GhcFile(utils/genprimopcode/Main.hs)`](GhcFile(utils/genprimopcode/Main.hs) "wikilink")` -- extend ppType :: Type -> String function`\
` `\
` * `[`GhcFile(compiler/prelude/PrelNames.hs)`](GhcFile(compiler/prelude/PrelNames.hs) "wikilink")` -- add a new unique id using mkPreludeTyConUnique`

` * `[`GhcFile(compiler/prelude/TysPrim.hs)`](GhcFile(compiler/prelude/TysPrim.hs) "wikilink")` -- there are a raft of changes here; you need to create ``, `` and  `` variables. The most important thing to make sure you get right is when you make a PrimTyCon, you pick the correct `` for your type.  For example, if you`

Profiling
=========

GHC includes two types of profiling: cost-centre profiling and
ticky-ticky profiling. Additionally, HPC code coverage is not
"technically" profiling, but it uses a lot of the same mechanisms as
cost-centre profiling (you can read more about it at
\[wiki:Commentary/Hpc\]).

Cost-centre profiling operates at something close to the source level,
and ticky-ticky profiling operates at something much closer to the
machine level. This means that the two types of profiling are useful for
different tasks. Ticky-ticky profiling is mainly meant for compiler
implementors, and cost-centre profiling for mortals. However, because
cost-centre profiling operates at a high level, it can be difficult (if
not impossible) to use it to profile optimized code. Personally, I
(Kirsten) have had a lot of success using cost-centre profiling to find
problems that were due to my own bad algorithms, but less success once I
was fairly sure that I wasn't doing anything obviously stupid and was
trying to figure out why my code didn't get optimized as well as it
could have been.

You can't use cost-centre profiling and ticky-ticky profiling at the
same time; in the past, this was because ticky-ticky profiling relied on
a different closure layout, but now that's no longer the case. You
probably can't use both at the same time as it is unless you wanted to
modify the build system to allow using way=p and way=t at the same time
to build the RTS. I haven't thought about whether it would make sense to
use both at the same time.

Cost-centre profiling
---------------------

Cost-center profiling in GHC, e.g. of SCCs, consists of the following
components:

`* Data-structures for representing cost-centres in `[`GhcFile(compiler/profiling/CostCentre.lhs)`](GhcFile(compiler/profiling/CostCentre.lhs) "wikilink")`.`\
`* Front-end support in `[`GhcFile(compiler/deSugar/DsExpr.lhs)`](GhcFile(compiler/deSugar/DsExpr.lhs) "wikilink")`, for converting `` pragma into the `` constructor in Core.`\
`* Modifications to optimization behavior in `[`GhcFile(compiler/coreSyn/CoreUtils.lhs)`](GhcFile(compiler/coreSyn/CoreUtils.lhs) "wikilink")` and `[`GhcFile(compiler/coreSyn/CorePrep.lhs)`](GhcFile(compiler/coreSyn/CorePrep.lhs) "wikilink")` to prevent optimizations which would result in misleading profile information. Most of this is to handle the fact that SCCs also count entries (tickishCounts, also applies to [wiki:Commentary/Hpc]); otherwise the only relevant optimization is avoiding floating expressions out of SCCs. Note that the simplifier also has "ticks" (so it can decide when to stop optimizing); these are not the same thing at all.`\
`* The `` constructor in STG, and code generation for it `[`GhcFile(compiler/codeGen/StgCmmProf.hs)`](GhcFile(compiler/codeGen/StgCmmProf.hs) "wikilink")\
`* A pass over STG in `[`GhcFile(compiler/profiling/SCCfinal.lhs)`](GhcFile(compiler/profiling/SCCfinal.lhs) "wikilink")` to collect cost centres so that they can be statically declared by `[`GhcFile(compiler/profiling/ProfInit.hs)`](GhcFile(compiler/profiling/ProfInit.hs) "wikilink")`, and add extra SCCs in the case of ``; see also `[`GhcFile(compiler/profiling/NOTES)`](GhcFile(compiler/profiling/NOTES) "wikilink")\
`* Code-generation for setting labels found in `[`GhcFile(compiler/codeGen/StgCmmProf.hs)`](GhcFile(compiler/codeGen/StgCmmProf.hs) "wikilink")`, in particular saving and restoring CC labels and well as counting ticks; note that cost-centres even get their own constructor in C-- as CC_Labels (cost-centre labels).`\
`* Runtime support for initializing and manipulating the actual runtime `` structs which store information, in `[`GhcFile(rts/Profiling.c)`](GhcFile(rts/Profiling.c) "wikilink")`; headers are located in `[`GhcFile(includes/rts/prof/CCS.h)`](GhcFile(includes/rts/prof/CCS.h) "wikilink")

Ticky-ticky profiling
---------------------

Ticky-ticky profiling is very simple (conceptually): instrument the C
code generated by GHC with a lot of extra code that updates counters
when various (supposedly) interesting things happen, and generate a
report giving the values of the counters when your program terminates.
GHC does this instrumentation for you when you compile your program with
a special flag. Then, you use another flag to tell the RTS to generate
the profiling report.

You might want to use ticky-ticky profiling for one of the following two
reasons:

-   You are an implementor trying to understand the effect of an
    optimization in GHC more precisely.

<!-- -->

-   You are a user trying to observe the behavior of your programs with
    optimization turned on. GHC doesn't do certain transformations in
    the presence of cost centres, so cost-centre profiling can be less
    than accurate if you're trying to understand what really happens
    when you're compiling with .

I won't necessarily try to argue that ticky-ticky is useful at all for
the second group of people, but it's better than nothing, and perhaps
the ticky-ticky data could be used to build a better profiler.

For more info, including HOWTO details, see
\[wiki:Debugging/TickyTicky\]. like "computer is a net", nowadays
language is a library. there is nothing exceptional in C++ and Java
languages except for their huge library codebase that makes them so
widely appreciated

while it's impossible for Haskell to have the same level of libraries
maturity, we can try to do our best. Libraries was considered so
important, that in H98 report libs required more pages than language
itself. But, really, all libraries described there together is
appropriate only for learning and small programs - to do real work, we
need even much, much more

fortunately, now we have large enough set of libs. moreover, this set
grows each year. but these libs don't have official/recommended status.
now we have two languages - H98 as reported with its bare libs, which is
appropriate only for teaching, and real Haskell language with many
extensions and rich set of libs, used to develop real programs

with a language itself, now we go to standardize current practice and
include into language definition all popular extensions. this will close
the gap between standard and practice. Haskell' committee also plan to
define new version of standard Haskell library. but what a library can
be defined in this way? slightly extended version of standard Haskell98
lib? or, if it will be significantly extended - how much time this work
will require and isn't that a duplication of work done at libraries
list?

i propose not to try to define reality, but accept existing one and join
committee's work on new library definition with a current discussion of
core libraries, which should define a set of libs available on any
Haskell compiler on any platform - aren't goals the same?

instead of providing rather small and meaningless standard Haskell
library, now we can just include in Report docs existing and widely used
libs, such as Network, mtl and so on. This will mean that language,
defined in Haskell standard, can be used to write real programs, which
will be guaranteed to run in any Haskell environment.

of course, this mind game can't change anything in one moment. but it
will change \*accents\*

first, Haskell with its libraries will become language for a real work.
such extended language isn't small nor easy to master in full, but it is
normal for any mature programming environment. people learning Haskell
should select in which area they need to specialize - be it gaming or
web service development, and study appropriate subset of libs. people
teaching Haskell now can show how \*standard\* Haskell may be used to
solve real world problems, and this should change treatment of Haskell
as academic language. also, we may expect that books teaching Haskell
will start to teach on using standard libs, while their authors now
don't consider teaching for non-standard libs

second, by declaring these libs as standard ones we create sort of
lingua franca, common language spoken by all Haskell users. for example,
now there are about 10 serialization libs. by declaring one of them as
standard, we will make choice simpler for most of users (who don't need
very specific features) and allow them to speak in common language. in
other words, number of Haskell libs is so large now that we should
define some core subset in order to escape syndrome of Babel tower.
defining core libraries set is just sharing knowledge that some
libraries are more portable, easier to use, faster and so on, so they
become more popular than alternatives in this area

third. now we have Cabal that automates installation of any lib. next
year we will got Hackage that automates downloading and checking
dependencies. but these tools still can't replace a rich set of standard
libs shipped with compiler. there are still many places and social
situations where Internet downloading isn't available. Compiler can be
sold on CD, transferred on USB stick. and separate Haskell libs probably
will be not included here. Standard libraries bundled with compiler will
ensure that at least this set of libs will be available for any haskell
installation. Internet access shouldn't be a precondition for Haskell
usage! :)

fourth. now there is tendency to write ghc-specific libs. by defining
requirements to the standard libs we may facilitate development of more
portable, well documented and quick-checked ones. or may be some good
enough libraries will be passed to society which will "polish" them in
order to include in the set. anyway, i hope that \*extensible\* set of
standard libraries with a published requirements to such libs would
facilitate "polishing" of all Haskell libs just because ;)

and this leads us to other question - whether this set and API of each
library should be fixed in language standard or it can evolve during the
time?...

[PageOutline](PageOutline "wikilink")

, , and 
========

When the parser parses an identifier, it generates a . A is pretty much
just a string, or a pair of strings, for a qualified name, such as .
Here's the data type declaration, from
[GhcFile(compiler/basicTypes/RdrName.hs)](GhcFile(compiler/basicTypes/RdrName.hs) "wikilink"):

User-written code never gets translated into the last two alternatives.
They are used only internally by the compiler. For example, code
generated by might use an to refer to , ignoring whatever might happen
to be in scope (dammit).

The \`Module\` and \`ModuleName\` types
---------------------------------------

In GHC, a *module* is uniquely defined by a pair of the module name and
the package where the module is defined. The details are in
[GhcFile(compiler/basicTypes/Module.hs)](GhcFile(compiler/basicTypes/Module.hs) "wikilink")
and
[GhcFile(compiler/main/PackageConfig.hs)](GhcFile(compiler/main/PackageConfig.hs) "wikilink"),
but here are the key definitions: You'll notice that a \`Qual\`
\`RdrName\` contains a \`ModuleName\`; which module is referred to
depends on the import declarations in that module. In contrast, a
\`Orig\` \`RdrName\` refers to a unique \`Module\`.

The  type
--------

An is more-or-less just a string, like "foo" or "Tree", giving the
(unqualified) name of an entity. Well, not quite just a string, because
in Haskell a name like "C" could mean a type constructor or data
constructor, depending on context. So GHC defines a type \`OccName\`
that is a pair of a and a indicating which name space the name is drawn
from. The data type is defined (abstractly) in
[GhcFile(compiler/basicTypes/OccName.hs)](GhcFile(compiler/basicTypes/OccName.hs) "wikilink"):
The name spaces are:

Attaching the names to their name spaces makes it very convenient to
build mappings from names to things; where such a mapping might contain
two strings that are identical, they can be distinguished by the name
space, so when mapping s, a single map suffices.

[PageOutline](PageOutline "wikilink")

Recompilation Avoidance
=======================

What is recompilation avoidance?
--------------------------------

When GHC is compiling a module, it tries to determine early on whether

`* The object file (or byte-code in the case of GHCi) and [wiki:Commentary/Compiler/IfaceFiles interface file] exist from a previous compilation`\
`* Recompilation is sure to produce exactly the same results, so it`\
`  is not necessary.`

If both of these hold, GHC stops compilation early, because the existing
object code and interface are still valid. In GHCi and \`--make\`, we
must generate the \`ModDetails\` from the \`ModIface\`, but this is
easily done by calling \`MkIface.typecheckIface\`.

Example
-------

Let's use a running example to demonstrate the issues. We'll have four
modules with dependencies like this:

\`A.hs\`:

\`B.hs\`:

\`C.hs\`:

\`D.hs\`:

Why do we need recompilation avoidance?
---------------------------------------

### GHCi and \`--make\`

The simple fact is that when you make a small change to a large program,
it is often not necessary to recompile every module that depends
directly or indirectly on something that changed. In GHCi and
\`--make\`, GHC considers every module in the program in dependency
order, and decides whether it needs to be recompiled, or whether the
existing object code and interface will do.

### \`make\`

\`make\` works by checking the timestamps on dependencies and
recompiling things when the dependencies are newer. Dependency lists for
\`make\` look like this (generated by \`ghc -M\`):

Only the \`.hi\` files of the *direct imports* of a module are listed.
For example, \`A.o\` depends on \`C.hi\` and \`B.hi\`, but not \`D.hi\`.
Nevertheless, if D is modified, we might need to recompile A. How does
this happen?

` * first, make will recompile D because its source file has changed,`\
``    generating a new `D.o` and `D.hi`. ``

` * If after recompiling D, we notice that its interface is the same`\
``    as before, there is no need to modify the `.hi` file.  If the `.hi` ``\
``    file is not modified by the compilation, then `make` will notice ``\
``    and not recompile `B` or `C`, or indeed `A`.  This is an important ``\
`   optimisation.`

``  * Suppose the change to `D` did cause a change in the interface ``\
``    (e.g. the type of `f` changed).  Now, `make` will recompile both ``\
``    `B` and `C`.  Suppose that the interfaces to `B` and `C` ``\
``    remain the same: B's interface says only that it re-exports `D.f`, ``\
``    so the fact that `f` has a new type does not affect `B`'s ``\
`   interface.  `

``  * Now, `A`'s dependencies are unchanged, so `A` will not be ``\
``    recompiled.  But this is wrong: `A` might depend on something from ``\
``    `D` that was re-exported via `B` or `C`, and therefore need ``\
`   recompiling.`

To ensure that \`A\` is recompiled, we therefore have two options:

` 1. arrange that make knows about the dependency of A on D.`

``  2. arrange to touch `B.hi` and `C.hi` even if they haven't changed. ``

GHC currently does (2), more about that in a minute.

Why not do (1)? Well, then *every* time \`D.hi\` changed, GHC would be
invoked on \`A\` again. But \`A\` doesn't depend directly on \`D\`: it
imports \`B\`, and it might be therefore be insensitive to changes in
\`D\`. By telling make only about direct dependencies, we gain the
ability to avoid recompiling modules further up the dependency graph, by
not touching interface files when they don't change.

Back to (2). In addition to correctness (recompile when necessary), we
also want to avoid unnecessary recompilation as far as possible. Make
only knows about very coarse-grained dependencies. For example, it
doesn't know that changing the type of \`D.f\` can have no effect on
\`C\`, so \`C\` does not in fact need to be recompiled, because to do so
would generate exactly the same \`.o\` and \`.hi\` files as last time.
GHC does have enough information to figure this out, so when GHC is
asked to recompile a module it invokes the *recompilation checker* to
determine whether recompilation can be avoided in this case.

How does it work?
-----------------

We use
[fingerprints](http://en.wikipedia.org/wiki/Fingerprint_%28computing%29)
to uniquely identify the interface exposed by a module, and to detect
when it changes. In particular, we currently use 128-bit hashes produced
by the MD5 algorithm (see
[GhcFile(compiler/utils/Fingerprint.hsc)](GhcFile(compiler/utils/Fingerprint.hsc) "wikilink")).

An \[wiki:Commentary/Compiler/IfaceFiles interface file\] contains:

`* Various fingerprints:`\
`  * The `*`interface`
`hash`*`, which depends on the entire contents of the`\
`    interface file.  This is used to detect whether we should`\
`    update the interface on disk after recompiling the module.  If the`\
`    interface didn't change at all, then we don't want to touch the`\
``     on-disk version because that would cause `make` to perform more ``\
`    compilations.`\
`  * The `*`ABI` `hash`*`, which depends on everything that the module`\
`    exposes about its implementation: think of this as a hash of`\
`    `*`export-list` `hash`*` and `*`decls`*`.`\
`  * The `*`export-list` `hash`*`, which depends on `\
`    * The export list itself.  The export-list hash only depends on the `*`names`*` of the exports for the modules. The `*`types`*` of these exports are ignored in calculating the hash. Only a change of name or removal or addition of an export will change the hash. Not a type change of definition change.`\
`    * the `*`orphan`
`hash`*`, which depends on all the orphan instances/rules in the, and the orphan hashes of all orphan modules below this module in the dependency tree (see [#Orphans Orphans]). `\
`    * the package dependencies (see [#Packageversionchanges Package Version Changes]).`\
`* `*`exports`*`: what the module exports`\
`* `*`dependencies`*`: modules and packages that this module depends on`\
`* `*`usages`*`: what specific entities the module depends on`\
`* `*`decls`*`: what the module defines`\
`* various other stuff, but the above are the important bits`

To look at the contents of an interface, use \`ghc --show-iface\`. For
example, here's the output of \`ghc --show-iface D.hi\` for the module
\`D\` in our example:

Lines beginning \`import\` are the *usages*, and after the usages are
the decls.

### Deciding whether to recompile

If we already have an object file and interface file for a module, we
might not have to recompile it, if we can be sure the results will be
the same as last time.

`* If the source file has changed since the object file was created,`\
`  we better recompile.`

`* If anything else has changed in a way that would affect the results`\
`  of compiling this module, we must recompile.`

In order to determine the second point, we look at the *dependencies*
and *usages* fields of the old interface file. The dependencies
contains:

`* `*`dep_mods`*`: Transitive closure of home-package modules that are`\
`  imported by this module.  That is, all modules below the current`\
`  one in the dependency graph.`

`* `*`dep_pkgs`*`: Transitive closure of packages depended on by this`\
`  module, or by any module in `*`dep_mods`*`.`

`* other less important stuff.`

First, the direct imports of the current module are resolved to
\`Module\`s using \`Finder.findModule\` (a \`Module\` contains a module
name and a package identifier). If any of those \`Module\`s are not
listed amongst the dependencies of the old interface file, then either:

`* an exposed package has been upgraded`\
`* we are compiling with different package flags`\
`* a home module that was shadowing a package module has been removed`\
`* a new home module has been added that shadows a package module`

and we must recompile.

Second, the *usages* of the module are checked. The usages contains two
types of information:

`* for a module that was imported, the export-list fingerprint of the`\
`  imported module is recorded.  If any of the modules we imported now`\
`  has a different export list we must recompile, so we check the`\
`  current export-list fingerprints against those recorded in the`\
`  usages.`

`* for every external name mentioned in the source code, the`\
`  fingerprint of that name is recorded in the usages.  This is so`\
``   that if we mention for example an external function `M.f`, we'll ``\
``   recompile if `M.f`'s type has changed, or anything referred to ``\
``   by `M.f`'s type has changed, or `M.f`'s unfolding has changed ``\
`  (when -O is on), and so on.`

The interface files for everything in the usages are read (they'll
already be in memory if we're doing \`--make\`), and the current
versions for each of these entities checked against the usages from the
old interface file. If any of these versions has changed, the module
must be recompiled.

### Example

There are some tricky cases to consider.

Suppose we change the definition of \`D.f\` in the example, and make it
Now, ultimately we need to recompile \`A\`, because it might be using an
inlined copy of the old \`D.f\`, which it got via \`B\`.

It works like this:

`` * `D` is recompiled; the fingerprint of `D.f` changes ``\
`` * `B` is considered; it recorded a usage on the old `D.f`, so ``\
``   gets recompiled, and now its interface records a usage on the new `D.f` ``\
`` * `C` is considered; it doesn't need to be recompiled. ``\
`` * `A` is considered (if we're using make, this is because `B.hi` ``\
``   changed); it recorded a usage on the old `D.f`, and so gets ``\
`  recompiled.`

Now a slightly more tricky case: suppose we add an INLINE pragma to
\`D.f\` (this is a trick to prevent GHC from inlining \`D.h\`, so that
we can demonstrate dependencies between unfoldings). The code for D.hs
is now

Looking at the interface file we can see what happened (snipped
slightly):

Note that the unfolding of \`D.f\` mentions \`D.h\`.

Now, let's modify \`D.h\`, and look at the interface file again:

The fingerprint for \`D.h\` has changed, because we changed its
definition. The fingerprint for \`D.f\` has also changed, because it
depends on \`D.h\`. And consequently, the ABI hash has changed, and so
has the interface hash (although the export hash and orphan hash are
still the same). Note that it is significant that we used '-O' here. If
we hadn't used '-O' then a change of a definition doesn't change any of
the hashes because of the lack of inlining.

Why did the fingerprint for \`D.f\` have to change? This is vital,
because anything that referred to \`D.f\` must be recompiled, because it
may now see the new unfolding for \`D.h\`.

So the fingerprint of an entity represents not just the definition of
the entity itself, but also the definitions of all the entities
reachable from it - its transitive closure. The consequence of this is
that when recording usages we only have to record the fingerprints of
entities that were referred to directly in the source code, because the
transitive nature of the fingerprint means that we'll recompile if
anything reachable from these entities changes.

### How does fingerprinting work?

We calculate fingerprints by serialising the data to be fingerprinted
using the \`Binary\` module, and then running the md5 algorithm over the
serlialised data. When the data contains external \`Name\`s, the
serialiser emits the fingerprint of the \`Name\`; this is the way that
the fingerprint of a declaration can be made to depend on the
fingerprints of the things it mentions.

### Mutually recursive groups of entities

When fingerprinting a recursive group of entities, we fingerprint the
group as a whole. If any of the definitions changes, the fingerprint of
every entity in the group changes.

### Fixities

We include the fixity of an entity when computing its fingerprint.

### Instances

Instances are tricky in Haskell, because they aren't imported or
exported explicitly. Haskell requires that any instance defined in a
module directly or indirectly imported by the current module is visible.
So how do we track instances for recompilation, such that if a relevant
instance is changed, added, or removed anywhere beneath the current
module we will trigger a recompilation?

Here's how it works. For each instance we pick a distinguished entity to
attach the instance to - possibly the class itself, or a type
constructor mentioned in the instance. The entity we pick must be
defined in the current module; if there are none to pick, then the
instance is an orphan (more about those in the section on Orphans,
below).

Having picked the distinguished entity, when fingerprinting that entity
we include the instances. For example, consider an instance for class C
at type T. Any module that could use this instance must depend (directly
or indirectly) on both C and T, so it doesn't matter whether we attach
the instance to C or T - either way it will be included in the
fingerprint of something that the module depends on. In this way we can
be sure that if someone adds a new instance, or removes an existing
instance, if the instance is relevant to a module then it will affect
the fingerprint of something that the module depends on, and hence will
trigger recompilation.

In fact, we don't need to include the instance itself when
fingerprinting C or T, it is enough to include the DFun (dictionary
function) Id, since the type of this Id includes the form of the
instance. Furthermore, we *must* include the DFun anway, because we must
have a dependency on the dictionary and its methods, just in case they
are inlined in a client module. A DFun looks something like this:

Making a type or class depend on its instances can cause a lot of
recompilation when an instance changes. For example:

now the DFun for the instance \`C T\` will be attached to \`T\`, and so
\`T\`'s fingerprint will change when anything about the instance
changes, including \`C\` itself. So there is now have a dependency of
\`T\` on \`C\`, which can cause a lot of recompilation whenever \`C\`
changes. Modules using \`T\` who do not care about \`C\` will still be
recompiled.

This seems like it would cause a lot of unnecessary recompilation.
Indeed, in GHC 7.0.1 and earlier we tried to optimise this case, by
breaking the dependency of \`T\` on \`C\` and tracking usages of DFuns
directly - whenever a DFun was used, the typechecker would record the
fact, and a usage on the DFun would be recorded in the interface file.
Unfortunately, there's a bug in this plan (see \#4469). When we're using
\`make\`, we only recompile a module when any of the interfaces that it
directly imports have changed; but a DFun dependency can refer to any
module, not just the directly imported ones. Instead, we have to ensure
that if an instance related to a particular type or class has changed,
then the fingerprint on either the type or class changes, which is what
the current plan does. It would be nice to optimise this in a safe way,
and maybe in the future we will be able to do that.

### Orphans

What if we have no declaration to attach the instance to? Instances with
no obvious parent are called *orphans*, and GHC must read the interface
for any module that contains orphan instances below the current module,
just in case those instances are relevant when compiling the current
module.

Orphans require special treatment in the recompilation checker.

`* Every module has an `*`orphan`
`hash`*`, which is a fingerprint of all`\
`  the orphan instances (and rules) in the current module.`

`* The `*`export` `hash`*` depends on the `*`orphan`
`hash`*` of the current`\
`  module, and all modules below the current module in the dependency`\
`  tree.  This models the fact that all instances defined in modules`\
`  below the current module are available to importers of this module.`

So if we add, delete, or modify an orphan instance, the orphan hash of
the current module will change, and so will the export hash of the
current module. This will trigger recompilation of modules that import
the current module, which will cause their export hashes to change, and
so on up the dependency tree.

This means a lot of recompilation, but it is at least safe. The trick is
to avoid orphan instances as far as possible, which is why GHC has the
warning flag \`-fwarn-orphans\`.

### Rules

RULEs are treated very much like instances: they are attached to one
particular parent declaration, and if a suitable parent cannot be found,
they become orphans and are handled in the same way as orphan instances.

### On ordering

When fingerprinting a collection of things, for example the export list,
we must be careful to use a canonical ordering for the collection.
Otherwise, if we recompile the module without making any changes, we
might get a different fingerprint due to accidental reordering of the
elements.

Why would we get accidental reordering? GHC relies heavily on "uniques"
internally (see
[GhcFile(compiler/basicTypes/Unique.lhs)](GhcFile(compiler/basicTypes/Unique.lhs) "wikilink")):
every entity has a unique, and uniques are assigned semi-randomly.
Asking for the contents of a \`UniqSet\` or \`UniqFM\` will return the
elements in order of their uniques, which may vary from run to run of
the compiler.

The solution is to sort the elements using a stable ordering, such as
lexicographic ordering.

### Packages

We need to record usage information about package modules too, so that
we can correctly trigger recompilation if we depend on a package that
has changed. But packages change rarely, so it would be wasteful to
record detailed usage information for every entity that we use from an
external package (imagine recording the fingerprints for \`Bool\`,
\`Int\`, etc.). Instead, we simply record the ABI fingerprint for every
package module that was imported by the current module. That way, if
anything about the ABI of that package module has changed, then we can
trigger a recompilation.

(Correctly triggering recompilation when packages change was one of the
things we fixed when implementing fingerprints, see \#1372).

### Package version changes

If the version of a package is bumped, what forces recompilation of the
things that depend on it?

`1. If a module from the package is imported directly, then we will notice that the imported module is not amongst the dependencies of the module when it was compiled last, and force a recompilation (see [#Decidingwhethertorecompile Deciding whether to recompile]).`

`` 2. If a module from the old package is imported indirectly, then the old package will be amongst the package dependencies (`dep_pkgs . mi_deps`), so we must recompile otherwise these dependencies will be inconsistent.  The way we handle this case is by including the package dependencies in the  ``*`export`
`hash`*` of a module, so that other modules which import this module will automatically be recompiled when one of the package dependencies changes.  The recompiled module will have new package dependencies, which will force recompilation of its importers, and so on.  Therefore if a package version changes, the change will be propagated throughout the module dependency graph.`

Interface stability
-------------------

For recompilation avoidance to be really effective, we need to ensure
that fingerprints do not change unnecessarily. That is, if a module is
modified, it should be the case that the only fingerprints that change
are related to the parts of the module that were modified. This may seem
obvious, but it's surprisingly easy to get wrong. Here are some of the
ways we got it wrong in the past, and some ways we still get it wrong.

`` * Prior to GHC 6.12, dictionary functions were named something like `M.$f23`, where `M` is the module defining the instance, and the number `23` was generated by simply assigning numbers to the dictionary functions defined by `M` sequentially.  This is a problem for recompilation avoidance, because now removing or adding an instance in `M` will change the numbering, and force recompilation of anything that depends on any instance in `M`.  Worse, the numbers are assigned non-deterministically, so simply recompiling `M` without changing its code could change the fingerprints.  In GHC 6.12 we changed it so that dictionary functions are named after the class and type(s) of the instance, e.g. `M.$fOrdInteger`. ``

`* compiler-generated bindings used to be numbered in the same way, non-deterministically.  The non-determinism arises because Uniques are assigned by the compiler non-deterministically.  Well, they are deterministic but not in a way that you can sensibly control, because it depends on the order in which interface bindings are read, etc.  Internal mappings use Uniques as the key, so asking for the elements of a mapping gives a non-deterministic ordering.  The list of bindings emitted by the simplifier, although in dependency order, can vary non-deterministically within the constraints of the dependencies.  So if we number the compiler-generated bindings sequentially, the result will be a non-deterministic ABI.`\
`  `[`BR`](BR "wikilink")[`BR`](BR "wikilink")\
``   In GHC 6.12 we changed this so that compiler-generated bindings are given names of the form `f_x`, where `f` is the name of the exported Id that refers to the binding.  If there are multiple `f_x`s, then they are disambiguated with an integer suffix, but the numbers are assigned deterministically, by traversing the definition of `f` in depth-first left-to-right order to find references.  See `TidyPgm.chooseExternalIds`. ``

`* There are still some cases where an interface can change without changing the source code.  The ones we know about are listed in #4012`

The Register Allocator
======================

Overview
--------

The register allocator is responsible for assigning real/hardware regs
(hregs) to each of the virtual regs (vregs) present in the code emitted
by the native code generator. It also inserts spill/reload instructions
to save vregs to the stack in situations where not enough hregs are
available.

GHC currently provides three register allocation algorithms, one which
does simple linear scan and two version of graph coloring. Support for
linear scan is likely to be removed in a subequent version.

`* `**`Linear` `scan`**[`BR`](BR "wikilink")\
`  The linear allocator is turned on by default. This is what you get when you compile with ``. The linear allocator does a single pass through the code, allocating registers on a first-come-first-served basis. It is quick, and does a reasonable job for code with little register pressure. `

` This algorithm has no look-ahead. If say, a particular hreg will be clobbered by a function call, it does not know to avoid allocating to it in the code before the call, and subsequently inserts more spill/reload instructions than strictly needed.`

`* `**`Graph` `coloring`**` (enabled with ``)`[`BR`](BR "wikilink")\
`  The graph coloring algorithm operates on the code for a whole function at a time. From each function it extracts a register conflict graph which has a node for every vreg and an edge between two vregs if they are in use at the same time and thus cannot share the same hreg. The algorithm tries to assign hregs (imagined as colors) to the nodes so that no two adjacent nodes share the same color, if it can't then it inserts spill code, rebuilds the graph and tries again. `

` Graph coloring tends to do better than the linear allocator because the conflict graph helps it avoid the look-ahead problem. The coloring allocator also tries harder to allocate the source and destination of reg-to-reg move instructions to the same hreg. This is done by coalescing (merging) move-related nodes. If this succeeds then the associated moves can be erased.`

`* `**`Graph` `coloring` `with` `iterative`
`coalescing`**` (enabled with ``)`[`BR`](BR "wikilink")\
`  Iterative coalescing is an improvement over regular graph coloring whereby coalescing passes are interleaved with coloring passes. Iterative coalescing does a better job than regular graph coloring, but is slower because it must alternate between the coloring and coalescing of nodes.`

Code map
--------

For an outline of the code see
\[wiki:Commentary/Compiler/Backends/NCG/RegisterAllocator/Code\]

References
----------

If you decide to do some hacking on the register allocator then take a
look at (at least) these papers first:

**Iterated Register Coalescing**[BR](BR "wikilink") *George, Appel,
1996*[BR](BR "wikilink") Decribes the core graph coloring algorithm
used.

**A Generalised Algorithm for Graph-Coloring Register
Allocation**[BR](BR "wikilink") *Smith, Ramsey, Holloway,
2004*[BR](BR "wikilink") For a decription of how to deal with
overlapping register sets, which aren't fully implemented. Explains what
the , and functions are for.

**Design and Implementation of a Graph Coloring Register Allocator for
GCC**[BR](BR "wikilink") *Matz, 2003*[BR](BR "wikilink") For an overview
of techniques for inserting spill code.

Register pressure in Haskell code
---------------------------------

Present GHC compiled code places very little pressure on the register
set. Even on x86 with only 3 allocable registers, most modules do not
need spill/reloads. This is a mixed blessing - on one hand the conflict
graphs are small so we can avoid performance problems related to how the
graph is represented, on the other hand it can be hard to find code to
test against. Register pressure is expected to increase as the
Stg-&gt;Cmm transform improves.

In the meantime, here are some good sources for test code:

`* `**`Nofib`**[`BR`](BR "wikilink")\
`  Only a few nofib benchmarks create spills with ``, two are `` and ``.`

`* `**`Turn` `on` `profiling`**[`BR`](BR "wikilink")\
`  Register pressure increases significantly when the module is compiled with profiling. `[`14`](attachment:checkSpills.report)` gives tuples of `` present in output code generated by the three algorithms when compiled with ``. Left to right are the stats for the linear, graph coloring and iterative coalescing algorithms. Note that most modules compile with no spill/reloads inserted, but a few (notably ``) need several hundred.`

` I've found it useful to maintain three darcs repos when working on the allocator. `` compiled with `` for fast compilation during hacking, `` for testing with profiling turned on, and `` for running the validate script. Patches are created in ``, pushed into `` where `` is used to compile the nofib benchmarks with the most register pressure. Once we're happy that the performance is ok, the patch is then pushed into `` for validation before pushing to the main repo on `

`* `**`SHA` `from` `darcs`**[`BR`](BR "wikilink")\
`  The `` module from the darcs source, compiled with `` creates the most register pressure out of any Haskell code that I'm aware of. When compiling SHA1, GHC inlines several worker functions and the native code block that computes the hash ends up being around 1700 instructions long. vregs that live in the middle of the block have in the order of 30 conflict neighbors. (evidently, the conflict graph is too large for most of the graphviz layout algorithms to cope with)`

` For these reasons, `` can be treated as a good worst-case input to the allocator. In fact, the current linear allocator cannot compile it with `` on x86 as it runs out of stack slots, which are allocated from a static pool. Make sure to test any changes to the allocator against this module.`

Hacking/Debugging
-----------------

`* `**`Turn` `on` **[`BR`](BR "wikilink")\
`  Breaking the allocator can result in compiled programs crashing randomly (if you're lucky) or producing the wrong output. Make sure to always turn on ``. Doing this makes the allocator call `` after every spill/color stage. `` checks that all the edges point to valid nodes, that no conflicting nodes have the same color, and if the graph is supposed to be colored then all nodes are really colored.`

`* `**`Some` `useful` `dump` `flags`**

` `[`BR`](BR "wikilink")\
` Shows the code and conflict graph after ever spill/color stage. Also shows spill costs, and what registers were coalesced.`

` `[`BR`](BR "wikilink")\
` Gives statistics about how many spills/reloads/reg-reg-moves are in the output program.`

` `[`BR`](BR "wikilink")\
` Gives the final output code. `

` `[`BR`](BR "wikilink")\
` Diverts dump output to files. This can be used to get dumps from each module in a nofib benchmark.`\
\
` `

`* `**`Visualisation` `of` `conflict` `graphs`**[`BR`](BR "wikilink")\
`  Graphviz, available from `[`15`](http://www.graphviz.org)` can be used to make nice visualisations of the register conflict graphs. Use ``, and copy one of the graph descriptions into a new file `

` `\
` Here's two from `` compiled with ``:`

`  `[`16`](attachment:graph.dot)` -> `[`17`](attachment:graph.png)

`  `[`18`](attachment:graph-colored.dot)` -> `[`19`](attachment:graph-colored.png)

`* `**`checkSpills`**[`BR`](BR "wikilink")\
`  `[`20`](attachment:checkSpills.hs)` is a nasty, throw away script which can be used to automate the comparison of allocation algorithms. Copy it and a list of test like `[`21`](attachment:checkSpills.tests)` to the top level nofib directory, compile and run. It will build the nofib benchmarks in the list 6 times each, once each with each of the allocators to extract spill counts, and then once again to get compile timings which are unperterbed by the space leaks introduced by compiling with debugging turned on. It's only needed if you're hacking on the allocator, parses the nofib make output directly, and is likely to rot - which is why it isn't included in the main source tree.`

Runtime performance
-------------------

Runtime performance of the graph coloring allocator is proportional to
the size of the conflict graph and the number of build/spill cycles
needed to obtain a coloring. Most functions have graphs &lt; 100 nodes
and generate no spills, so register allocation is a small fraction of
overall compile time.

Possible Improvements
---------------------

These are some ideas for improving the current allocator, most
potentially useful first.

`* `**`Work` `lists` `for` `iterative`
`coalescing.`**[`BR`](BR "wikilink")\
`  The iterative coalescing alternates between scanning the graph for trivially colorable (triv) nodes and perforing coalescing. When two nodes are coalesced, other nodes that are not adjacent to the coalesced nodes do not change and do not need to be rescanned straight away. Runtime performance of the iterative coalescer could probably be improved by keeping a work-list of "nodes that might have become trivially colorable", to help find nodes that won't have changed.`

`* `**`Improve` `spill` `code`
`generator/cleaner.`**[`BR`](BR "wikilink")\
`  When spilling a particular vreg, the current spill code generator simply inserts a spill after each def and a reload before each use. This quickly reduces the density of conflicts in the graph, but produces inefficient code because more spill/reloads are inserted than strictly nessesary. Good code is recovered by the spill cleaner which runs after allocation and removes spill/reload instructions that aren't nessesary. Some things to try:`\
`  * `**`Spill` `coalescing`**[`BR`](BR "wikilink")` `\
`    No attempt is currently made to share spill slots between different vregs. Each named vreg is spilled to its own static spill slot on the C stack. The amount of stack space needed could be reduced by sharing spill slots between vregs so long as their live ranges do not overlap.`\
`  * `**`Try` `to` `split` `live` `ranges` `before`
`spilling`**[`BR`](BR "wikilink")\
`    If a live range has several use/defs then we could insert fresh reg-reg moves to break it up into several smaller live ranges. We then might get away with spilling just one section instead of the whole range. Not sure if this would be a win over the current situation. We would need spill-coalescing to be implemented before this so that we don't require an extra slot for each new live range.`\
`  * `**`Rematerialization`**[`BR`](BR "wikilink")\
`    As the spill cleaner walks through the code it builds a mapping of which slots and registers hold the same value. On each reload instruction, if the slot and reg are known to already have the same value then the reload can be erased. This mapping could be extended with constants, so that if a vreg holding a constant value cannot be allocated a hreg, the constant value can be rematerialized instead of being spilled/reloaded to a stack slot.`

`* `**`Revisit` `choosing` `of` `spill`
`candidates`**[`BR`](BR "wikilink")\
`  If the graph cannot be colored then a node/vreg must be chosen to be potentially spilled. Chaitin's forumula says to calculate the spill cost by adding up the number of uses and defs of that vreg and divide by the degree of the node. In the code that I've tested against, it's been better to just choose the live range that lives the longest. Perhaps this is because the 'real' spill cost would depend on the spills/reloads actually inserted, not a simple count of use/defs. Perhaps choosing the longest live range is just better for the particular kind of code that GHC generates.`

`* `**`Revisit` `trivColorable` `/` `aliasing` `of` `register`
`sets`**[`BR`](BR "wikilink")\
`  For the architectures currently supported, x86, x86_64 and ppc, the native code generator currently emits code using only two register classes `` and ``. As these classes are disjoint (ie, none of the regs from one class alias with with regs from another), checking whether a node of a certain class is trivially colorable reduces to counting up the number of neighbours of that class.`

` If the NCG starts to use aliasing register classes eg: both 32bit ``s and 64bit ``s on sparc; combinations of 8, 16, and 32 bit integers on x86 / x86_x6 or usage of sse / altivec regs in different modes, then this can be supported via the method described in [Smith et al]. The allocator was designed with this in mind - ie, by passing a function to test if a node is trivially colorable as a parameter to the coloring function - and there is already a description of the register set for x86 in `[`GhcFile(compiler/nativeGen/RegArchX86.hs)`](GhcFile(compiler/nativeGen/RegArchX86.hs) "wikilink")`, but the native code generator doesn't currently emit code to test it against.`

Haskell Excecution: Registers
=============================

Source files:
[GhcFile(includes/stg/Regs.h)](GhcFile(includes/stg/Regs.h) "wikilink"),
[GhcFile(includes/stg/MachRegs.h)](GhcFile(includes/stg/MachRegs.h) "wikilink")

During execution of Haskell code the following (virtual) registers are
always valid:

`` * `Hp` points to the byte before the first free byte in the (contiguous) allocation space. ``

`` * `HpLim` points to the last available byte in the current chunk of allocation space. ``

`` * `Sp` points to the youngest allocated byte of stack.  The stack grows downwards.  Why?  Because that means a return address is at a lower address than the stack frame it "knows about", and that in turn means that we can treat a stack frame very like a heap object, with an info pointer (return address) as its first word. ``

`` * `SpLim` points to the last (youngest) available byte in the current stack. ``

There are bunch of other virtual registers, used for temporary argument
passing, for words, floats and doubles: \`R1\` .. \`R10\`, \`F1\` ..
\`F4\`, \`D1\` .. \`D4\`, \`L1\` .. \`L2\`.

In a register-rich machine, many of these virtual registers will be
mapped to real registers. In a register-poor machine, they are instead
allocated in a static memory record, pointed to by a real register,
\`BaseReg\`.

The code generator knows how many real registers there are, and tries to
avoid using virtual registers that are not mapped to real registers. So,
for example, it does not use \`R5\` if the latter is memory-mapped;
instead, it passes arguments on the stack.

Relevant GHC parts for Demand Analysis results
==============================================

``  * `compiler/basicTypes/Demand.lhs` -- contains all information about demands and operations on them, as well as about serialization/deserialization of demand signatures. This module is supposed to be changed whenever the demand nature should be enhanced; ``

``  * `compiler/stranal/DmdAnal.lhs` -- the demand analysis itself. Check multiple comments to figure out main principles of the algorithm. ``

``  * `compiler/stranal/WorkWrap.lhs` -- a worker-wrapper transform, main client of the demand analysis. The function split is performed in `worthSplittingFun` basing on demand annotations of a function's parameters.  ``

``  *  `compiler/stranal/WwLib.lhs` -- a helper module for the worker-wrapper machinery. The "deep" splitting of a product type argument makes use of the strictness info and is implemented by the function `mkWWstr_one`. The function `mkWWcpr` makes use of the CPR info. ``

``  * `compiler/basicTypes/Id.lhs` -- implementation of identifiers contains a number of utility functions to check/set demand annotations of binders. All of them are just delegating to appropriate functions/fields of the `IdInfo` record; ``

``  * `compiler/basicTypes/IdInfo.lhs` -- `IdInfo` record contains all information about demand and strictness annotations of an identifier. `strictnessInfo` contains a representation of an abstract two-point demand transformer of a binder, considered as a reference to a value. `demandInfo` indicates, which demand is put to the identifier, which is a function parameter, if the function is called in a strict/used context. `seq*`-functions are invoked to avoid memory leaks caused by transforming new ASTs by each of the compiler passes (i.e., no thunks pointing to the parts of the processed trees are left).  ``

``  * `compiler/basicTypes/MkId.lhs` -- A machinery, responsible for generation of worker-wrappers makes use of demands. For instance, when a signature for a worker is generated, the following strictness signature is created: ``

``  In words, a non-bottoming demand type with `N` lazy/used arguments (`top`) is created for a worker, where `N` is just a worker's pre-computed arity. Also, particular demands are used when creating signatures for dictionary selectors (see `mkDictSelId`).  ``

``  * `compiler/prelude/primops.txt.pp` -- this file defines demand signatures for primitive operations, which are inserted by `cpp` pass on the module `compiler/basicTypes/MkId.lhs`; ``

``  * `compiler/coreSyn/CoreArity.lhs` -- demand signatures are used in order to compute the unfolding info of a function: bottoming functions should no be unfolded. See `exprBotStrictness_maybe` and `arityType`. ``

``  * `compiler/coreSyn/CoreLint.lhs` -- the checks are performed (in `lintSingleBinding`):  ``\
`   * whether arity and demand type are consistent (only if demand analysis already happened);`\
`   * if the binder is top-level or recursive, it's not demanded (i.e., its demand is not strict).`

``  * `compiler/coreSyn/CorePrep.lhs` -- strictness signatures are examining before converting expression to A-normal form. ``

``  * `compiler/coreSyn/MkCore.lhs` -- a bottoming strictness signature created for `error`-like functions (see `pc_bottoming_Id`). ``

``  * `compiler/coreSyn/PprCore.lhs` -- standard pretty-printing machinery, should be modified to change PP of demands. ``

``  * `compiler/iface/IfaceSyn.lhs`  -- serialization, grep for `HsStrictness` constructors. ``

``  * `compiler/iface/MkIface.lhs`  -- a client of `IfaceSyn`, see usages of `HsStrictness`. ``

``  * `compiler/iface/TcIface.lhs` -- the function `tcUnfolding` checks if an identifier binds a bottoming function in order to decide if it should be unfolded or not ``

``  * `compiler/main/TidyPgm.lhs` -- Multiple checks of an identifier to bind a bottoming expression, running a cheap-an-cheerful bottom analyser. See `addExternal` and occurrences of `exprBotStrictness_maybe`. ``

``  * `compiler/simplCore/SetLevels.lhs` -- It is important to zap demand information, when an identifier is moved to a top-level (due to let-floating), hence look for occurrences of `zapDemandIdInfo`. ``

``  * `compiler/simplCore/SimplCore.lhs` -- this module is responsible for running the demand analyser and the subsequent worker-wrapper split passes.  ``

``  * `compiler/simplCore/SimplUtils.lhs`  -- is a new arity is less than the arity of the demand type, a warning is emitted; check `tryEtaExpand`. ``

``  * `compiler/specialise/SpecConstr.lhs` -- strictness info is used when creating a specialized copy of a function, see `spec_one` and `calcSpecStrictness`. ``

[PageOutline](PageOutline "wikilink")

Remembered Sets
===============

Since in generational GC we may need to find all the live objects in a
young generation without traversing the older generation(s), we need a
record of the pointers from those old generations into the young
generations. This is termed the "remembered set".

In GHC each \`generation\` structure contains a field \`mut\_list\`,
which points to a chain of blocks. Each block in the chain contains a
list of pointers to objects in that generation which contain pointers to
objects in younger generations. There are alternative schemes, e.g.

`* Keeping track of each `*`pointer`*`, rather than `*`object`*` that points to a younger generation.  The remembered set would`\
`  be larger (possibly very much larger, in the case of arrays), but it would be more accurate, and traversing the`\
`  remembered set at GC time would be faster.`

`* Some GCs use "card-marking" schemes whereby the heap is divided into "cards" of a fixed size, and each card has a bit to`\
`  indicate whether that card contains pointers to a younger generation.  This is much less accurate than a remembered set,`\
`  but it is faster at runtime if a lot of mutation is taking place, and it takes less space than a remembered set.  In GHC`\
`  we typically do not have much mutation to worry about, so card marking would be a poor compromise in our case.`

The remembered set may contain duplicates, or it may contain pointers to
objects that don't really point to young generations.

Remembered set maintenance during mutation
------------------------------------------

While the mutator is running, we have to add any old-to-new generation
pointers that are created. Old-to-new pointers are created by mutating
(writing to) an object in the old generation, and catching these writes
is called a "write barrier".

A pointer can be added to a remembered set using

This adds the pointer \`p\` to the remembered set for generation
\`gen\`, using Capability \`cap\`. Each Capability has its own
remembered set for each generation, so that when running in parallel we
can update remembered sets without taking a lock, and also so that we
can take advantage of locality in the GC, by traversing a remembered set
on the same CPU that created it.

Here are the cases where we need a write barrier in GHC:

### Thunk Updates

Updating a thunk in an old generation. This is taken care of by the
update code, see
[GhcFile(rts/Updates.h)](GhcFile(rts/Updates.h) "wikilink").

### Mutable objects: MUT\_VAR, MVAR

For \`MUT\_VAR\`, the writer must call \`dirty\_MUT\_VAR\`:

(in [GhcFile(rts/sm/Storage.c)](GhcFile(rts/sm/Storage.c) "wikilink")).
The code generator inserts calls to \`dirty\_MUT\_VAR\` when it compiles
a call to the primitive \`writeMutVar\#\`.

\`dirty\_MUT\_VAR\` does the following: if the object's header is
\`MUT\_VAR\_CLEAN\`, then the header is set to \`MUT\_VAR\_DIRTY\`, and
the object is added to the remembered set if it resides in an old
generation. If the header was already \`MUT\_VAR\_DIRTY\`, no action is
taken.

\`MVAR\` is handled in the same way, with

### Arrays: MUT\_ARR\_PTRS

Unlike mutable variables and MVARs, mutable arrays are kept in the
remembered set permanently. This reflects the fact that mutable arrays
are likely to be written to more often, and there are likely to be fewer
of them. However, we still mark arrays according to whether the array is
dirty or not, using \`MUT\_ARR\_PTRS\_DIRTY\` and
\`MUT\_ARR\_PTRS\_CLEAN\`.

There are also \`MUT\_ARR\_PTRS\_FROZEN\` and
\`MUT\_ARR\_PTRS\_FROZEN0\`, which are used to indicate arrays that have
been frozen using \`unsafeFreezeArray\#\`. A frozen array is different
from a mutable array in the sense that while it may have old-to-new
pointers, it is not going to be mutated any further, and so we probably
want to use \[wiki:Commentary/Rts/Storage/GC/EagerPromotion eager
promotion\] on it.

### Threads: TSO

Threads (TSOs) have stacks, which are by definition mutable. Running a
thread is therefore an act of mutation, and if the thread resides in an
old generation, it must be placed in the remembered set. Threads have
two dirty bits: \`tso-&gt;dirty\` is set to non-zero if the thread's
stack or any part of the TSO structure may be dirty, and also there is a
bit \`TSO\_LINK\_DIRTY\` in \`tso-&gt;flags\` which is set if the TSO's
link field may be dirty. If the thread is executed, then
\`dirty\_TSO()\` must be called in order to set the \`tso-&gt;dirty\`
bit and add the TSO to the appropriate remembered set.

To set the TSO's link field, use \`setTSOLink()\` (from
[GhcFile(rts/sm/Storage.c)](GhcFile(rts/sm/Storage.c) "wikilink")) which
arranges to add the TSO to the remembered set if necessary.

there are a few exceptions where \`setTSOLink()\` does not need to be
called; see
[GhcFile(rts/sm/Storage.c)](GhcFile(rts/sm/Storage.c) "wikilink") for
details.

Remembered set maintenance during GC
------------------------------------

During GC, the principle of write barriers is quite similar: whenever we
create an old-to-new pointer, we have to record it in the remembered
set. The GC achieves this as follows:

`` * The GC thread structure has a field `gct->evac_gen` which specifies the desired destination generation. ``\
`` * there is a flag `gct->failed_to_evac`, which is set to true by `evacuate` if it did not manage to evacuate ``\
`  the object into the desired generation.`\
`` * after scavenging an object, `scavenge_block` checks the `failed_to_evac` flag, and if it is set, adds the object to the remembered set, using `recordMutableGen_GC()` (the equivalent of `recordMutableCap` for calling within the GC). ``

The renamer
===========

The renamer's Number One task is to replace
\[wiki:Commentary/Compiler/RdrNameType RdrNames\] with
\[wiki:Commentary/Compiler/NameType Names\]. For example, consider
(where all the variables are s). The result of renaming module M is:
where all these names are now s.

` * The top-level unqualifed `` "``" has become the `` `` ``.  `\
` * The occurrences "``" and "``" are both bound to this ``.  `\
` * The qualified `` "``" becomes the `` ``, because the function is defined in module K.  `\
` * The lambda-bound "``" becomes an `` name, here written ``.  (All the `` names have uniques too, but we often do not print them.)`

In addition, the renamer does the following things:

`* Sort out fixities. The parser parses all infix applications as `**`left-associative`**`, regardless of fixity.  For example "``" is parsed as "``".  The renamer re-associates such nested operator applications, using the fixities declared in the module.`

`* Dependency analysis for mutually-recursive groups of declarations.  This divides the declarations into strongly-connected components.`

`* Lots of lexical error checking: variables out of scope, unused bindings, unused imports, patterns that use the same binder many times, etc.`

The renamer sits between the parser and the typechecker. However, its
operation is quite tightly interwoven with the typechecker. This is
mainly due to support for Template Haskell, where spliced code has to be
renamed and type checked. In particular, top-level splices lead to
multiple rounds of renaming and type checking. It uses the
\[wiki:Commentary/Compiler/TcRnMonad same monad as the typechecker\].

The global renamer environment, 
--------------------------------

A big part of the renamer's task is to build the **global rdr-env** for
the module, of type . This environment allows us to take a qualified or
un-qualified and figure out which it means. The global rdr-env is built
by looking at all the imports, and the top-level declarations of the
module.

You might think that the global rdr-env would be a mapping from to , but
it isn't. Here is what it looks like, after at least three iterations
(all in
[GhcFile(compiler/basicTypes/RdrName.hs)](GhcFile(compiler/basicTypes/RdrName.hs) "wikilink")):
Here is how to understand these types:

`` * The environment (`GlobalRdrEnv`) maps an  ``` to a list of all entities with that occurrence name that are in scope (in any way).  `

`* Each of these is represented by a ``, which gives the entity's `` plus a specification of how it is in scope, its ``.  `

`* The `` has one of two forms.  Either it is in scope because it is defined in this module (``), or because it is imported.  In the latter case, the `` describes all the import statements that bring it into scope. `

`* An `` has two components: `\
`  * An `` that describes the entire import declaration. This is shared between all entities brought into scope by a particular import declaration.`\
`  * An `` that describes the import item that brought the entity into scope.`\
`For example, given`

`the `` would describe the `` and `` part, while the `` describes the `` part.  You can look in `` to see what an `` and `` are like!`\
`* The `` of an entity is the ```  under which it is grouped when the forms `T(..)` or `T(C,D)` are used in an export or import list.  In the `T(..)` form, all the things whose  ````  is `T` are chosen.  In the `T(C,D)` form, it is required that `C` and `D` have `T` as parents.   ``\
`  For example, `\
``   * The `Parent` of a data constructor is its data type ``\
``   * The `Parent` of a record field selector is its data type ``\
``   * The `Parent` of a class operation is its class ``

With all that information, we can give good error messages, especially
in the case where an occurrence "f" is ambiguous (i.e. different
entities, both called "f", were imported by different import
statements).

The global rdr-env is created by
[GhcFile(compiler/rename/RnNames.hs)](GhcFile(compiler/rename/RnNames.hs) "wikilink").

It is important to note that the global rdr-env is created *before* the
renamer actually descends into the top-level bindings of a module. In
other words, before performs the renaming of a module by way of , it
uses to set up the global rdr-env environment, which contains for all
imported and all locally defined toplevel binders. Hence, when the
helpers of come across the defining occurences of a toplevel , they
don't rename it by generating a new name, but they simply look up its
name in the global rdr-env.

Unused imports
--------------

See \[wiki:Commentary/Compiler/UnusedImports how the renamer reports
unused imports\]

Name Space Management
---------------------

(too much detail?)

As anticipated by the variants and of , some names should not change
during renaming, whereas others need to be turned into unique names. In
this context, the two functions and are important: The two functions
introduces new toplevel and new local names, respectively, where the
first two arguments to newTopSrcBinder determine the currently compiled
module and the parent construct of the newly defined name. Both
functions create new names only for
\[wiki:Commentary/Compiler/RdrNameType RdrNames\] that are neither exact
nor original.

Rebindable syntax
-----------------

(!ToDo: Not fully proof-read.)

In Haskell when one writes "3" one gets "fromInteger 3", where
"fromInteger" comes from the Prelude (regardless of whether the Prelude
is in scope). If you want to completely redefine numbers, that becomes
inconvenient. So GHC lets you say "-fno-implicit-prelude"; in that case,
the "fromInteger" comes from whatever is in scope. (This is documented
in the User Guide.)

This feature is implemented as follows (I always forget).

`* Names that are implicitly bound by the Prelude, are marked by the type ``. Moreover, the association list `` is set up by the renamer to map rebindable names to the value they are bound to. `\
`* Currently, five constructs related to numerals (``, ``, ``, ``, and ``) and two constructs related to do-expressions (`` and ``) have rebindable syntax. `\
`* When the parser builds these constructs, it puts in the built-in Prelude Name (e.g. ``). `\
`* When the renamer encounters these constructs, it calls ``. This checks for ``; if not, it just returns the same Name; otherwise it takes the occurrence name of the Name, turns it into an unqualified ``, and looks it up in the environment. The returned name is plugged back into the construct. `\
`* The typechecker uses the `` to generate the appropriate typing constraints. `

Replacing the Native Code Generator
===================================

The existence of LLVM is definitely an argument not to put any more
effort into backend optimisation in GHC, at least for those
optimisations that LLVM can already do. There's also the question of
whether it's worth extending the NCG to support SIMD primops. At the
moment only the LLVM backend supports these, but current processor
architectures will rely more and more on wide vector SIMD instructions
for performance. Given that the LLVM project is now stable and widely
used, it may be better to drop the NCG entirely (and delete the code).

However, there are a few ways that the LLVM backend needs to be improved
before it can be considered to be a complete replacement for the
existing NCG:

1\. Compilation speed. LLVM approximately doubles compilation time.
Avoiding going via the textual intermediate syntax would probably help
here.

2\. Shared library support (\#4210, \#5786). It works (or worked?) on a
couple of platforms. But even on those platforms it generated worse code
than the NCG due to using dynamic references for \*all\* symbols,
whereas the NCG knows which symbols live in a separate package and need
to use dynamic references.

3\. Some low-level optimisation problems (\#4308, \#5567). The LLVM
backend generates bad code for certain critical bits of the runtime,
perhaps due to lack of good aliasing information. This hasn't been
revisited in the light of the new codegen, so perhaps it's better now.

Someone should benchmark the LLVM backend against the NCG with new
codegen in GHC 7.8. It's possible that the new codegen is getting a
slight boost because it doesn't have to split up proc points, so it can
do better code generation for let-no-escapes. It's also possible that
LLVM is being penalised a bit for the same reason.

Other considerations:

1\. The GHC distribution would need to start shipping with its own copy
of LLVM. The LLVM code that GHC produces typically lags the current
version of LLVM, so we'd need to ensure there was a usable version.

2\. If we did ship our own version of LLVM, we could add custom plugins
to improve the GHC generated code. At one stage Max Bolingbroke wrote an
LLVM alias analysis plugin, but making it work against an arbitrary
existing LLVM version would be infeasible.

note (carter): If we're very thoughtful about the changes / extensions
to llvm needed for GHC, I'm somewhat confident that we could get any
such patches upstreamed to llvm proper. The down side of this is that
any such features would be subject to the llvm release cycle, plus we'd
want to make sure that we're not just completely changing what we'd like
upstreamed every ghc release cycle. The upside is that we'd get a lot
more scrutiny / feedback / checking by llvm devs than we'd get with our
own patched variant

Resource Limits
===============

This page describes a proposed resource limits capabilities for GHC. The
idea is to give users the ability to create and utilize resource
containers inside programs, and then provide in-program access to heap
census and other information. The semantics of resource containers are
quite similar to cost centers used in profiling, except that they do not
have "stack" semantics (more on this later). The end result is the
ability to impose resource limits on space usage.

Code generation changes
-----------------------

Resource limits is a new way (similar to profiled and dynamic). Here are
the relevant changes:

### Dynamic closure allocation

[GhcFile(compiler/codeGen/StgCmmHeap.hs)](GhcFile(compiler/codeGen/StgCmmHeap.hs) "wikilink"):allocDynClosureCmm
(via StgCmmCon, also handles StgCmmBind:mkRhsClosure/cgRhsStdThunk.
link\_caf needs special treatment.)

Changes to:

I.e. no change from un-profiled.

### CAF Allocation

[GhcFile(compiler/codeGen/StgCmmBind.hs)](GhcFile(compiler/codeGen/StgCmmBind.hs) "wikilink"):thunkCode

Here is an interesting bugger:

Notice the heap check serves for the later branch too. On the other
hand, the CCCS coincides with the later change. This seems to be the
general pattern. So we might be able to handle this CAF by
special-casing CAFs.

We also hit the slow function application path.

### Thunk code

[GhcFile(compiler/codeGen/StgCmmBind.hs)](GhcFile(compiler/codeGen/StgCmmBind.hs) "wikilink"):thunkCode

Changes to:

### Foreign calls

Changes to:

No change from unprofiled

Case split
----------

Do a nursery swap.

-   -   Warning:\*\* The rest of this document describes an old
        iteration of the system, which directly used

Front-end changes
-----------------

The basic idea behind this patch is that data collected during
\*\*profiling\*\* can also be used at runtime to enforce limits. So most
of the API involves (1) dynamically setting cost-centres, which GHC uses
to do profiling, and (2) querying and receiving callbacks when certain
events happen during profiling. Costs can be collected anywhere you
could have placed an annotation statically.

The general usage of this API goes like:

Another use-case is more fine-grained SCCs based on runtime properties,
not source-level features.

I am planning on providing semantics, based on GHC

Garbage Collection Roots
========================

The "roots" are the set of pointers that the GC starts traversing from,
i.e. the roots of the live object graph.

Most roots belong to a particular Capability. Traversing the roots of a
capbility is done by \`markSomeCapabilities()\` in
[GhcFile(rts/Capability.c)](GhcFile(rts/Capability.c) "wikilink"). The
roots of a Capability are:

`* The run queue (head and tail)`\
`* The wakeup queue (head and tail)`\
`` * For each Task on the `suspended_ccalling_tasks` list, the TSO for that Task ``\
`* The Spark Pool`\
`* Only for the non-threaded RTS: The blocked queue (head and tail), and the sleeping queue`

In addition, each Capability has a
\[wiki:Commentary/Rts/Storage/GC/RememberedSets remembered set\] for
each generation. A remembered set is a source of roots if that
generation is *not* being collected during this cycle; otherwise the
remembered set is discarded. During GC, all remembered sets are
discarded and new ones will be constructed for each generation and
Capability; see \`scavenge\_capability\_mut\_lists()\` in
[GhcFile(rts/sm/Scav.c)](GhcFile(rts/sm/Scav.c) "wikilink").

There are also roots from other parts of the system:

`` * Signal handlers (only in the non-threaded RTS; in the threaded RTS signal handlers are maintained by the IO manager in `GHC.Conc` rather than the RTS). ``\
`* [wiki:Commentary/Rts/Storage/GC/Weak Weak pointers]`\
`* [wiki:Commentary/Rts/Stable Stable pointers]`

[PageOutline](PageOutline "wikilink")

GHC Source Tree Roadmap: rts/
=============================

This directory contains the source code for the runtime system.

There are three types of files:

`::`\
`  Header files that are `*`private` `to` `the`
`RTS`*`.  That is, header files in this directory are`\
`  not shipped with GHC, and APIs they define are therefore intended to be private and not`\
`  usable by client code (in practice, we do not and probably cannot enforce this).  Header`\
`  files that we `*`do`*` ship with GHC are in the [wiki:Commentary/SourceTree/Includes includes]`\
`  directory.`

`::`\
`  C source code for the runtime system.  Conventions used in this code are described in`\
`  [wiki:Commentary/Rts/Conventions].`

`::`\
`  C-- code for parts of the runtime that are part of the Haskell execution environment: for`\
`  example, the implementation of primitives, exceptions, and so on.  A `` file is`\
`  pseudo C--: more or less C-- syntax with some omissions and some additional macro-like`\
`  extensions implemented by GHC.  The `` files are compiled using GHC itself: see`\
`  [wiki:Commentary/Rts/Cmm].`

### Subdirectories of rts/

`::`\
`::`\
`  POSIX and Win32-specific parts of the runtime respectively.  We try to put platform-specific stuff in these directories,`\
`  however not all of the RTS follows this convention right now.`

`::`\
`  Hooks for changing the RTS behaviour from client code, eg. changing the default heap size.`\
`  (see `[`User's` `Guide` `for` `more` `about`
`hooks`](https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/runtime-control.html#rts-hooks)`).`

`::`\
`  The [wiki:Commentary/Rts/Storage Storage Manager].`

### Haskell Execution

All this code runs on the Haskell side of the Haskell/C divide; is the
interface between the two layers.

[`Apply.cmm`](http://darcs.haskell.org/ghc/rts/Apply.cmm)`, `[`AutoApply.h`](http://darcs.haskell.org/ghc/rts/AutoApply.h)`, ``, `[`Apply.h`](http://darcs.haskell.org/ghc/rts/Apply.h)`::`\
` The eval/apply machinery.  Note: `` is the family`\
` of functions for performing generic application of unknown`\
` functions, this code depends on the number of registers available`\
` for argument passing, so it is generated automatically by the program`\
` `` in ``.`

[`Exception.cmm`](http://darcs.haskell.org/ghc/rts/Exception.cmm)`::`\
` Support for execptions.`

[`HeapStackCheck.cmm`](http://darcs.haskell.org/ghc/rts/HeapStackCheck.cmm)`::`\
` Code for preparing the stack when the current Haskell thread needs`\
` to return to the RTS, because we either ran out of heap or stack, or`\
` need to block (eg. ``), or yield.`

[`PrimOps.cmm`](http://darcs.haskell.org/ghc/rts/PrimOps.cmm)`::`\
` Implementation of out-of-line primitives (see [wiki:Commentary/PrimOps]).`

[`StgMiscClosures.cmm`](http://darcs.haskell.org/ghc/rts/StgMiscClosures.cmm)`::`\
` Some built-in closures, such as the family of small ``s and`\
` ``, and some built-in info tables such as `\
` and ``.`

[`StgStartup.cmm`](http://darcs.haskell.org/ghc/rts/StgStartup.cmm)`::`\
` Code that executes when a Haskell thread begins and ends.`

[`StgStdThunks.cmm`](http://darcs.haskell.org/ghc/rts/StgStdThunks.cmm)`::`\
` Some built-in thunks: [wiki:Commentary/Rts/Storage/HeapObjects#Selectorthunks selector thunks] and "apply" thunks.`

[`Updates.cmm`](http://darcs.haskell.org/ghc/rts/Updates.cmm)`, `[`Updates.h`](http://darcs.haskell.org/ghc/rts/Updates.h)`::`\
` [wiki:Commentary Updates].`

[`HCIncludes.h`](http://darcs.haskell.org/ghc/rts/HCIncludes.h)`::`\
` Header file included when compiling `` files via C.`

[`StgCRun.c`](http://darcs.haskell.org/ghc/rts/StgCRun.c)`, `[`StgRun.h`](http://darcs.haskell.org/ghc/rts/StgRun.h)`::`\
` The interface between the C execution layer and the Haskell`\
` execution layer.`

[`StgPrimFloat.c`](http://darcs.haskell.org/ghc/rts/StgPrimFloat.c)`::`\
` Floating-point stuff.`

[`STM.c`](http://darcs.haskell.org/ghc/rts/STM.c)`::`\
` Implementation of Software Transactional Memory.`

### The \[wiki:Commentary/Rts/Storage Storage Manager\]

[`sm/Storage.c`](http://darcs.haskell.org/ghc/rts/sm/Storage.c)`::`\
` Top-level of the storage manager.`

[`sm/MBlock.c`](http://darcs.haskell.org/ghc/rts/sm/MBlock.c)`, `[`sm/MBlock.h`](http://darcs.haskell.org/ghc/rts/sm/MBlock.h)`, `[`sm/OSMem.h`](http://darcs.haskell.org/ghc/rts/sm/OSMem.h)`::`\
` The "megablock" allocator; this is the thin layer between the RTS and`\
` the operating system for allocating memory.`

[`sm/BlockAlloc.c`](http://darcs.haskell.org/ghc/rts/sm/BlockAlloc.c)`, `[`sm/BlockAlloc.h`](http://darcs.haskell.org/ghc/rts/sm/BlockAlloc.h)`::`\
` The low-level block allocator, requires only ``.`

[`sm/GC.c`](http://darcs.haskell.org/ghc/rts/sm/GC.c)`, `[`sm/Scav.c`](http://darcs.haskell.org/ghc/rts/sm/Scav.c)`, `[`sm/Evac.c`](http://darcs.haskell.org/ghc/rts/sm/Evac.c)`, `[`sm/GCUtils.c`](http://darcs.haskell.org/ghc/rts/sm/GCUtils.c)`, `[`sm/MarkWeak.c`](http://darcs.haskell.org/ghc/rts/sm/MarkWeak.c)`::`\
` The generational copying garbage collector.`

[`sm/Compact.c`](http://darcs.haskell.org/ghc/rts/sm/Compact.c)`, `[`sm/Compact.h`](http://darcs.haskell.org/ghc/rts/sm/Compact.h)`::`\
` The compacting garbage collector.`

[`ClosureFlags.c`](http://darcs.haskell.org/ghc/rts/ClosureFlags.c)`::`\
` Determining properties of various types of closures.`

[`Sanity.c`](http://darcs.haskell.org/ghc/rts/Sanity.c)`, `[`Sanity.h`](http://darcs.haskell.org/ghc/rts/Sanity.h)`::`\
` A sanity-checker for the heap and related data structures.`

[`Stats.c`](http://darcs.haskell.org/ghc/rts/Stats.c)`, `[`Stats.h`](http://darcs.haskell.org/ghc/rts/Stats.h)`::`\
` Statistics for the garbage collector and storage manager.`

[`Stable.c`](http://darcs.haskell.org/ghc/rts/Stable.c)`::`\
` Stable names and stable pointers.`

[`Weak.c`](http://darcs.haskell.org/ghc/rts/Weak.c)`, `[`Weak.h`](http://darcs.haskell.org/ghc/rts/Weak.h)`::`\
` Weak pointers.`

### Data Structures

Data structure abstractions for use in the RTS:

[`Arena.c`](http://darcs.haskell.org/ghc/rts/Arena.c)`, `[`Arena.h`](http://darcs.haskell.org/ghc/rts/Arena.h)`::`\
` An arena allocator`

[`Hash.c`](http://darcs.haskell.org/ghc/rts/Hash.c)`, `[`Hash.h`](http://darcs.haskell.org/ghc/rts/Hash.h)`::`\
` A generic hash table implementation.`

### The \[wiki:Commentary/Rts/Scheduler Scheduler\]

[`Capability.c`](http://darcs.haskell.org/ghc/rts/Capability.c)`, `[`Capability.h`](http://darcs.haskell.org/ghc/rts/Capability.h)`::`\
` Capabilities: virtual CPUs for executing Haskell code.`

[`RaiseAsync.c`](http://darcs.haskell.org/ghc/rts/RaiseAsync.c)`, `[`RaiseAsync.h`](http://darcs.haskell.org/ghc/rts/RaiseAsync.h)`::`\
` Asynchronous exceptions.`

[`Schedule.c`](http://darcs.haskell.org/ghc/rts/Schedule.c)`, `[`Schedule.h`](http://darcs.haskell.org/ghc/rts/Schedule.h)`::`\
` The scheduler itself.`

[`Sparks.c`](http://darcs.haskell.org/ghc/rts/Sparks.c)`, `[`Sparks.h`](http://darcs.haskell.org/ghc/rts/Sparks.h)`::`\
` Sparks: the implementation of ``.`

[`ThreadLabels.c`](http://darcs.haskell.org/ghc/rts/ThreadLabels.c)`, `[`ThreadLabels.h`](http://darcs.haskell.org/ghc/rts/ThreadLabels.h)`::`\
` Labelling threads.`

[`Threads.c`](http://darcs.haskell.org/ghc/rts/Threads.c)`, `[`Threads.h`](http://darcs.haskell.org/ghc/rts/Threads.h)`::`\
` Various thread-related functionality.`

[`ThreadPaused.c`](http://darcs.haskell.org/ghc/rts/ThreadPaused.c)`::`\
` Suspending a thread before it returns to the RTS.`

[`Task.c`](http://darcs.haskell.org/ghc/rts/Task.c)`, `[`Task.h`](http://darcs.haskell.org/ghc/rts/Task.h)`::`\
` Task: an OS-thread abstraction.`

[`AwaitEvent.h`](http://darcs.haskell.org/ghc/rts/AwaitEvent.h)`::`\
` Waiting for events (non-threaded RTS only).`

[`Timer.c`](http://darcs.haskell.org/ghc/rts/Timer.c)`, `[`Timer.h`](http://darcs.haskell.org/ghc/rts/Timer.h)`,  `[`Ticker.h`](http://darcs.haskell.org/ghc/rts/Ticker.h)`::`\
` The runtime's interval timer, used for context switching and profiling.`

### C files: the \[wiki:Commentary/Rts/FFI FFI\]

[`Adjustor.c`](http://darcs.haskell.org/ghc/rts/Adjustor.c)`::`\
` Very hairy support for ``.`

[`HsFFI.c`](http://darcs.haskell.org/ghc/rts/HsFFI.c)`, `[`RtsAPI.c`](http://darcs.haskell.org/ghc/rts/RtsAPI.c)`::`\
` Implementation of the Haskell FFI C interface: ``,`\
` ``, etc.`\
` `

### The \[wiki:Commentary/Rts/Interpreter Byte-code Interpreter\]

[`Disassembler.c`](http://darcs.haskell.org/ghc/rts/Disassembler.c)`, `[`Disassembler.h`](http://darcs.haskell.org/ghc/rts/Disassembler.h)`::`\
[`Interpreter.c`](http://darcs.haskell.org/ghc/rts/Interpreter.c)`, `[`Interpreter.h`](http://darcs.haskell.org/ghc/rts/Interpreter.h)`::`\
` The [wiki:Commentary/Rts/Interpreter byte-code interpreter] and disassembler.`

[`Linker.c`](http://darcs.haskell.org/ghc/rts/Linker.c)`::`\
[`LinkerInternals.h`](http://darcs.haskell.org/ghc/rts/LinkerInternals.h)\
` The [wiki:Commentary/Rts/Linker dynamic object-code linker].`

### \[wiki:Commentary/Profiling Profiling\]

[`LdvProfile.c`](http://darcs.haskell.org/ghc/rts/LdvProfile.c)`, `[`LdvProfile.h`](http://darcs.haskell.org/ghc/rts/LdvProfile.h)`::`\
` Lag-drag-void profiling (also known as Biographical Profiling).`

[`ProfHeap.c`](http://darcs.haskell.org/ghc/rts/ProfHeap.c)`, `[`ProfHeap.h`](http://darcs.haskell.org/ghc/rts/ProfHeap.h)`::`\
` Generic heap-profilng support.`

[`Profiling.c`](http://darcs.haskell.org/ghc/rts/Profiling.c)`, `[`Profiling.h`](http://darcs.haskell.org/ghc/rts/Profiling.h)`::`\
` Generic profilng support.`

[`Proftimer.c`](http://darcs.haskell.org/ghc/rts/Proftimer.c)`, `[`Proftimer.h`](http://darcs.haskell.org/ghc/rts/Proftimer.h)`::`\
` The profiling timer.`

[`RetainerProfile.c`](http://darcs.haskell.org/ghc/rts/RetainerProfile.c)`, `[`RetainerProfile.h`](http://darcs.haskell.org/ghc/rts/RetainerProfile.h)`::`\
[`RetainerSet.c`](http://darcs.haskell.org/ghc/rts/RetainerSet.c)`, `[`RetainerSet.h`](http://darcs.haskell.org/ghc/rts/RetainerSet.h)`::`\
` Retainer profiling.`

[`Ticky.c`](http://darcs.haskell.org/ghc/rts/Ticky.c)`, `[`Ticky.h`](http://darcs.haskell.org/ghc/rts/Ticky.h)`::`\
` Ticky-ticky profiling (currently defunct; needs reviving).`

### RTS Debugging

[`Printer.c`](http://darcs.haskell.org/ghc/rts/Printer.c)`, `[`Printer.h`](http://darcs.haskell.org/ghc/rts/Printer.h)`::`\
` Generic printing for heap objects and stacks (not used much).`

[`Trace.c`](http://darcs.haskell.org/ghc/rts/Trace.c)`, `[`Trace.h`](http://darcs.haskell.org/ghc/rts/Trace.h)`::`\
` Generic support for various kinds of trace and debugging messages.  `

### The Front Panel

The front panel is currently defunct. It offers a graphical view of the
running Haskell program in real time, and was pretty cool when it
worked.

[`FrontPanel.c`](http://darcs.haskell.org/ghc/rts/FrontPanel.c)`, `[`FrontPanel.h`](http://darcs.haskell.org/ghc/rts/FrontPanel.h)`::`\
[`VisCallbacks.c`](http://darcs.haskell.org/ghc/rts/VisCallbacks.c)`, `[`VisCallbacks.h`](http://darcs.haskell.org/ghc/rts/VisCallbacks.h)`::`\
[`VisSupport.c`](http://darcs.haskell.org/ghc/rts/VisSupport.c)`, `[`VisSupport.h`](http://darcs.haskell.org/ghc/rts/VisSupport.h)`::`\
[`VisWindow.c`](http://darcs.haskell.org/ghc/rts/VisWindow.c)`, `[`VisWindow.h`](http://darcs.haskell.org/ghc/rts/VisWindow.h)`::`

### Other

[`Main.c`](http://darcs.haskell.org/ghc/rts/Main.c)`::`\
` The C `` function for a standalone Haskell program;`\
` basically this is just a client of ``.`

[`RtsFlags.c`](http://darcs.haskell.org/ghc/rts/RtsFlags.c)`::`\
` Understands the `` flags.`

[`RtsMessages.c`](http://darcs.haskell.org/ghc/rts/RtsMessages.c)`::`\
` Support for emitting messages from the runtime.`

[`RtsSignals.c`](http://darcs.haskell.org/ghc/rts/RtsSignals.c)`, `[`RtsSignals.h`](http://darcs.haskell.org/ghc/rts/RtsSignals.h)`::`\
` Signal-related stuff.`

Miscellaneous stuff:

[`RtsUtils.c`](http://darcs.haskell.org/ghc/rts/RtsUtils.c)`, `[`RtsUtils.h`](http://darcs.haskell.org/ghc/rts/RtsUtils.h)`::`\
[`GetTime.h`](http://darcs.haskell.org/ghc/rts/GetTime.h)`::`\
[`PosixSource.h`](http://darcs.haskell.org/ghc/rts/PosixSource.h)`::`\
[`Prelude.h`](http://darcs.haskell.org/ghc/rts/Prelude.h)`::`\
[`Typeable.c`](http://darcs.haskell.org/ghc/rts/Typeable.c)`::`\
[`RtsDllMain.c`](http://darcs.haskell.org/ghc/rts/RtsDllMain.c)`::`

### OLD stuff

`::`\
` Code for GUM: parallel GHC.  This is heavily bitrotted and currently doesn't work (as of GHC 6.6; it last worked around`\
` 5.02 I believe).`

`::`\
` Bitrotted code for GHC.NET.`

Sanity Checking
===============

Source code: [GhcFile(rts/Sanity.c)](GhcFile(rts/Sanity.c) "wikilink"),
[GhcFile(rts/Sanity.h)](GhcFile(rts/Sanity.h) "wikilink").

The purpose of sanity checking is to catch bugs in the RTS as early as
possible; if the program is going to crash, we want it to crash as soon
as possible after the error occurred. The problem with debugging the RTS
is that heap corruption can go unnoticed through several GC cycles,
making it particularly difficult to trace back to the erroneous code.

Sanity checking is turned on by the \`+RTS -DS\` option. We treat it
like an expensive assertion: normal assertions are allowed to take a few
extra percent of run time, so we don't mind having them on all the time
in a \`DEBUG\` RTS, but sanity checking may double the run time of the
program or worse. So the rule of thumb is that expensive assertions go
into sanity checking, cheap assertions are on in \`DEBUG\`, or possibly
even on all the time.

Sanity checking does a complete traversal of the heap after each GC to
look for dangling pointers (see \`checkHeap\` in
[GhcFile(rts/Sanity.c)](GhcFile(rts/Sanity.c) "wikilink")). For this it
needs to ensure that there is no \[wiki:Commentary/Rts/Storage/Slop
slop\], which is why we can only do this in a \`DEBUG\` runtime: the
slop-avoiding machinery is only on with \`DEBUG\`.

Sanity checking also turns on some other expensive checks: for example
in the \[wiki:Commentary/Rts/HaskellExecution\#Genericapply generic
apply\] code we check that the arguments point to valid closures.

[PageOutline](PageOutline "wikilink")

The Scheduler
=============

The scheduler is the heart of the runtime: it is the single part of the
system through which all entry to the Haskell world goes, and it handles
requests from outside to invoke Haskell functions (foreign export).

In this part of the commentary we'll discuss the *threaded* version of
the runtime (see \[wiki:Commentary/Rts/Config\]), that is, the version
of the runtime that uses multiple OS threads, because it is by far the
most complex beast.

See also [Edward Yang's blog
post](http://blog.ezyang.com/2013/01/the-ghc-scheduler/) (2013); some of
the material there has been incorporated here.

We begin by discussing the basic abstractions used in the scheduler.

OS Threads
----------

Source files:
[GhcFile(includes/rts/OSThreads.h)](GhcFile(includes/rts/OSThreads.h) "wikilink"),
[GhcFile(rts/win32/OSThreads.c)](GhcFile(rts/win32/OSThreads.c) "wikilink"),
[GhcFile(rts/posix/OSThreads.c)](GhcFile(rts/posix/OSThreads.c) "wikilink")

We assume that the OS provides some kind of native threads, and for SMP
parallelism we assume that the OS will schedule multiple OS threads
across the available CPUs.

OS threads are only used by the runtime for two reasons:

`* To support non-blocking foreign calls: a foreign call`\
`  should not block the other Haskell threads in the system from`\
`  running, and using OS threads is the only way to ensure that.`

`* To support SMP parallelism.`

Haskell threads are much lighter-weight (at least 100x) than OS threads.

When running on an SMP, we begin by creating the number of OS threads
specified by the \`+RTS -N\` option, although during the course of
running the program more OS threads might be created in order to
continue running Haskell code while foreign calls execute. Spare OS
threads are kept in a pool attached to each \`Capability\` (see
\[\#Capabilities\]).

The RTS provides a platform-independent abstraction layer for OS threads
in
[GhcFile(includes/rts/OSThreads.h)](GhcFile(includes/rts/OSThreads.h) "wikilink").

Haskell threads
---------------

A Haskell thread is represented by a Thread State Object
(\[wiki:Commentary/Rts/Storage/HeapObjects\#ThreadStateObjects TSO\]).
These objects are *garbage-collected*, like other closures in Haskell.
The TSO, along with the stack allocated with it (STACK), constitute the
primary memory overhead of a thread. Default stack size, in particular,
is controlled by the GC flag , and is 1k by default (Actually, your
usable stack will be a little smaller than that because this size also
includes the size of the struct, so that a lot of allocated threads will
fit nicely into a single block.) There are two kinds of Haskell thread:

`* A `*`bound`*` thread is created as the result of a `*`call-in`*` from`\
`  outside Haskell; that is, a call to `` or`\
`  ``.  A bound thread is tied to the`\
`  OS thread that made the call; all further foreign calls made by`\
`  this Haskell thread are made in the same OS thread.  (this is part`\
`  of the design of the FFI, described in the paper `\
`  `[`Extending` `the` `Haskell` `Foreign` `Function` `Inteface` `with`
`Concurrency`](http://www.haskell.org/~simonmar/papers/conc-ffi.pdf)`).`

`* An `*`unbound`*` thread is created by`\
`  ``.  Foreign calls made by an unbound`\
`  thread are made by an arbitrary OS thread.`

Initialization of TSOs is handled in in
[GhcFile(rts/Threads.c)](GhcFile(rts/Threads.c) "wikilink"); this
function is in turn invoked by , and in
[GhcFile(rts/RtsAPI.c)](GhcFile(rts/RtsAPI.c) "wikilink"). These
functions setup the initial stack state, which controls what the thread
executes when it actually gets run. These functions are the ones invoked
by the and other primops (recall entry-points for primops are located in
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink")).

Being garbage collected has two major implications for TSOs. First, TSOs
are not GC roots, so they will get GC'd if there is nothing holding on
to them (e.g. [in the case of
deadlock](http://blog.ezyang.com/2011/07/blockedindefinitelyonmvar)),
and their space is not automatically reclaimed when they finish
executing (so can cause memory leaks}}}. Usually, a TSO will be retained
by a Capability

Seq magic
=========

The innocent-looking \`seq\` operator causes all manner of mayhem in
GHC. This page summarises the issues. See also discussion in Trac
\#5129, \#5262

The baseline position
---------------------

Our initial story was that \`(seq e1 e2)\` meant precisely Indeed this
was \`seq\`'s inlining. This translation validates some important rules

But this approach has problems; see \`Note \[Deguaring seq\]\` in
\`DsUtils\`.

### Problem 1 (Trac \#1031)

Consider The \`\[CoreSyn let/app invariant\]\` (see \`CoreSyn\`) means
that, other things being equal, because the argument to the outer
\`seq\` has an unlifted type, we'll use call-by-value thus: But that is
bad for two reasons:

``  * we now evaluate `y` before `x`, and  ``\
``  * we can't bind `v` to an unboxed pair ``

Seq is very, very special! Treating it as a two-argument function,
strict in both arguments, doesn't work. We "fixed" this by treating
\`seq\` as a language construct, desugared by the desugarer, rather than
as a function that may (or may not) be inlined by the simplifier. So the
above term is desugared to:

### Problem 2 (Trac \#2273)

Consider Here the \`seq\` is designed to plug the space leak of
retaining \`(snd x)\` for too long.

If we rely on the ordinary inlining of \`seq\`, we'll get But since
\`chp\` is cheap, and the case is an alluring contet, we'll inline
\`chp\` into the case scrutinee. Now there is only one use of \`chp\`,
so we'll inline a second copy. Alas, we've now ruined the purpose of the
seq, by re-introducing the space leak: We can try to avoid doing this by
ensuring that the binder-swap in the case happens, so we get his at an
early stage: But this is fragile. The real culprit is the source
program. Perhaps we should have said explicitly But that's painful. So
the desugarer does a little hack to make \`seq\` more robust: a
saturated application of \`seq\` is turned **directly** into the case
expression, thus: So we desugar our example to: And now all is well.

Be careful not to desugar which stupidly tries to bind the datacon
'True'. This is easily avoided.

The whole thing is a hack though; if you define \`mySeq=seq\`, the hack
won't work on \`mySeq\`.

### Problem 3 (Trac \#5262)

Consider With the above desugaring we get and now ete expansion gives
Now suppose that we have Plainly \`(length xs)\` should be evaluated...
but it isn't because \`f\` has arity 2. (Without -O this doesn't
happen.)

### Problem 4: seq in the IO monad

See the extensive discussion in Trac \#5129.

### Problem 5: the need for special rules

Roman found situations where he had where he knew that \`f\` (which was
strict in \`n\`) would terminate if n did. Notice that the result of
\`(f n)\` is discarded. So it makes sense to transform to Rather than
attempt some general analysis to support this, I've added enough support
that you can do this using a rewrite rule: You write that rule. When GHC
sees a case expression that discards its result, it mentally transforms
it to a call to \`seq\` and looks for a RULE. (This is done in
\`Simplify.rebuildCase\`.) As usual, the correctness of the rule is up
to you.

To make this work, we need to be careful that \`seq\` is **not**
desguared into a case expression on the LHS of a rule.

To increase applicability of these user-defined rules, we also have the
following built-in rule for \`seq\` This eliminates unnecessary casts
and also allows other seq rules to match more often. Notably, and now a
user-defined rule for \`seq\` may fire.

A better way
============

Here's our new plan.

`` * Introduce a new primop `seq# :: a -> State# s -> (# a, State# s #)` (see be5441799b7d94646dcd4bfea15407883537eaaa) ``\
`` * Implement `seq#` by turning it into the obvious eval in the backend.  In fact, since the return convention for `(# State# s, a #)` is exactly the same as for `a`, we can implement `seq# s a` by `a` (even when it appears as a case scrutinee). ``\
`` * Define `evaluate` thus ``

That fixes problem 4.

We could go on and desugar \`seq\` thus:

and if we consider \`seq\#\` to be expensive, then we won't eta-expand
around it, and that would fix problem 3.

However, there is a concern that this might lead to performance
regressions in examples like this:

so \`f\` turns into

and we won't get to eta-expand the \`\\s\` as we would normally do (this
is pretty important for getting good performance from IO and ST monad
code).

Arguably \`f\` should be rewritten with a bang pattern, and we should
treat bang patterns as the eta-expandable seq and translate them
directly into \`case\`, not \`seq\#\`. But this would be a subtle
difference between \`seq\` and bang patterns.

Furthermore, we already have \`pseq\`, which is supposed to be a
"strictly ordered seq", that is it preserves evaluation order. So
perhaps \`pseq\` should be the one that more accurately implements the
programmer's intentions, leaving \`seq\` as it currently is.

We are currently pondering what to do here.

The GHC Commentary: Signals
===========================

This section describes how the RTS interacts with the OS signal
facilities. Throughout we use the term "signal" to refer to both
POSIX-style signals and Windows *ConsoleEvents*.

Signal handling differs between the *threaded* version of the runtime
and the non-threaded version (see \[wiki:Commentary/Rts/Config\]). Here
we discuss only the threaded version, since we expect that to become the
standard version in due course.

Source files:

`* POSIX signal handling:`\
`  * `[`GhcFile(rts/posix/Signals.h)`](GhcFile(rts/posix/Signals.h) "wikilink")`, `[`GhcFile(rts/posix/Signals.c)`](GhcFile(rts/posix/Signals.c) "wikilink")\
`* Windows console events:`\
`  * `[`GhcFile(rts/win32/ConsoleHandler.h)`](GhcFile(rts/win32/ConsoleHandler.h) "wikilink")`, `[`GhcFile(rts/win32/ConsoleHandler.c)`](GhcFile(rts/win32/ConsoleHandler.c) "wikilink")

Signal handling in the RTS
--------------------------

The RTS is interested in two signals: a timer signal, and an interrupt
signal.

### The timer signal

The timer signal is used for several things:

`* To cause the [wiki:Commentary/Rts/Scheduler scheduler] to context switch`\
`* Sampling for [wiki:Commentary/Profiling time profiling]`\
`* To detect deadlock (see [wiki:Commentary/Rts/Scheduler])`

Source files:

`* The timer interrupt handler, and starting/stopping the timer:`\
`  * `[`GhcFile(rts/Timer.h)`](GhcFile(rts/Timer.h) "wikilink")`, `[`GhcFile(rts/Timer.c)`](GhcFile(rts/Timer.c) "wikilink")\
`* Platform-independent ticker interface, used by the timer:`\
`  * `[`GhcFile(rts/Ticker.h)`](GhcFile(rts/Ticker.h) "wikilink")\
`* Posix implementation of ticker:`\
`  * `[`GhcFile(rts/posix/Itimer.h)`](GhcFile(rts/posix/Itimer.h) "wikilink")`, `[`GhcFile(rts/posix/Itimer.h)`](GhcFile(rts/posix/Itimer.h) "wikilink")\
`* Windows implementation of ticker:`\
`  * `[`GhcFile(rts/win32/Ticker.c)`](GhcFile(rts/win32/Ticker.c) "wikilink")

On Posix, the timer signal is implemented by calling \`timer\_create()\`
to generate regular \`SIGVTALRM\` signals (this was changed from SIGALRM
in \#850).

On Windows, we spawn a new thread that repeatedly sleeps for the timer
interval and then executes the timer interrupt handler.

The interrupt signal
--------------------

The interrupt signal is \`SIGINT\` on POSIX systems or
\`CTRL\_C\_EVENT/CTRL\_BREAK\_EVENT\`on Windows, and is normally sent to
the process when the user hits Control-C. By default, interrupts are
handled by the runtime. They can be caught and handled by Haskell code
instead, using \`System.Posix.Signals\` on POSIX systems or
\`GHC.ConsoleHandler\` on Windows systems. For example,
\[wiki:Commentary/Compiler/Backends/GHCi GHCi\] hooks the interrupt
signal so that it can abort the current interpreted computation and
return to the prompt, rather than terminating the whole GHCi process.

When the interrupt signal is received, the default behaviour of the
runtime is to attempt to shut down the Haskell program gracefully. It
does this by calling \`interruptStgRts()\` in
[GhcFile(rts/Schedule.c)](GhcFile(rts/Schedule.c) "wikilink") (see
\[wiki:Commentary/Rts/Scheduler\#ShuttingDown\]). If a second interrupt
signal is received, then we terminate the process immediately; this is
just in case the normal shutdown procedure failed or hung for some
reason, the user is always able to stop the process with two control-C
keystrokes.

Signal handling in Haskell code
-------------------------------

Source files:

` * POSIX: `[`GhcFile(rts/posix/Signals.h)`](GhcFile(rts/posix/Signals.h) "wikilink")`, `[`GhcFile(rts/posix/Signals.c)`](GhcFile(rts/posix/Signals.c) "wikilink")\
` * Windows: `[`GhcFile(rts/win32/ConsoleHandler.h)`](GhcFile(rts/win32/ConsoleHandler.h) "wikilink")`, `[`GhcFile(rts/win32/ConsoleHandler.c)`](GhcFile(rts/win32/ConsoleHandler.c) "wikilink")

A Haskell program can ask to install signal handlers, via the
\`System.Posix.Signals\` API, or \`GHC.ConsoleHandler\` on Windows. When
a signal arrives that has a Haskell handler, it is the job of the
runtime to create a new Haskell thread to run the signal handler and
place the new thread on the run queue of a suitable
\[wiki:Commentary/Rts/Scheduler\#Capabilities Capability\].

When the runtime is idle, the OS threads will all be waiting inside
\`yieldCapability()\`, waiting for some work to arrive. We want a signal
to be able to create a new Haskell thread and wake up one of these OS
threads to run it, but unfortunately the range of operations that can be
performed inside a POSIX signal handler is extremely limited, and
doesn't include any inter-thread synchronisation (because the signal
handler might be running on the same stack as the OS thread it is
communicating with).

The solution we use, on both Windows and POSIX systems, is to pass all
signals that arrive to the \[wiki:Commentary/Rts/IOManager IO Manager\]
thread. On POSIX this works by sending the signal number down a pipe, on
Windows it works by storing the signal number in a buffer and signaling
the IO Manager's \`Event\` object to wake it up. The IO Manager thread
then wakes up and creates a new thread for the signal handler, before
going back to sleep again.

RTS Alarm Signals and Foreign Libraries
---------------------------------------

When using foreign libraries through the Haskell FFI, it is important to
ensure that the foreign code is capable of dealing with system call
interrupts due to alarm signals GHC is generating.

For example, in this \`strace\` output a \`select\` call is interrupted,
but the foreign C code interprets the interrupt as an application error
and closes a critical file descriptor:

Once the C code was modified to deal with the interrupt properly, it
proceeded correctly (note that foreign call is restarted 3 times before
it succeeds).

Slop
====

Slop is unused memory between objects in the heap.

|| Object1 || ... Slop ... || Object2 ||

Why do we want to avoid slop?
-----------------------------

Slop makes it difficult to traverse an area of memory linearly, visiting
all the objects, because we can't tell where \`Object2\` starts in the
above diagram. We need to do linear traversals for two reasons,
currently:

`* [wiki:Commentary/Profiling/Heap Heap profiling] needs to perform a census on the whole heap.`\
`* [wiki:Commentary/Rts/Sanity Sanity checking] needs to ensure that all the pointers in the heap`\
`  point to valid objects.`

Additionally, linear traversals are useful for the mark phase of the
\[wiki:Commentary/Rts/Storage compacting garbage collector\], and would
be useful if we were to allow objects to be pinned arbitrarily
(currently pinned objects cannot contain pointers, which means they
don't need to be scavenged by the GC).

How does slop arise?
--------------------

Slop can arise for two reasons:

`* The compiled code allocates too much memory, and only fills part of it with objects.  For example,`\
`  when compiling code for a function like this:`

`  the code generator takes the maximum of the heap requirements of e1 and e2 and aggregates it into`\
``   the heap check at the beginning of the function `f` (to avoid doing too many heap checks).   ``\
``   Unfortunately that means either `e1` or `e2` has too much heap allocated to it, leaving some slop. ``\
`  We solve this problem by moving the heap pointer `*`backwards`*` before making a tail-call if`\
`  there is any heap slop.`

`* When an object is overwritten with a smaller object.  This happens in two ways:`\
`  [wiki:Commentary/Rts/HaskellExecution/Updates Updates] and [wiki:Commentary/Rts/Storage/HeapObjects#Blackholes Black Holes].`

What do we do about it?
-----------------------

We avoid the problem for \[wiki:Commentary/Profiling/Heap heap
profiling\] by arranging that we only ever do a census on a newly
garbage-collected heap, which has no slop in it (the garbage collector
never leaves slop between objects in the heap).

Slop does arise due to updates and black holes during normal execution,
and GHC does not attempt to avoid it (because avoiding or filling slop
during an update is costly). However, if we're doing
\[wiki:Commentary/Rts/Sanity sanity checking\], then we need to arrange
that slop is clearly marked: so in a \`DEBUG\` version of the RTS (see
\[wiki:Commentary/Rts/Config RTS configurations\]) the update code and
the blackhole code both arrange to fill slop with zeros: see the
\`FILL\_SLOP\` macro in
[GhcFile(rts/Updates.h)](GhcFile(rts/Updates.h) "wikilink"). Hence
sanity checking only works with a \`DEBUG\` version of the RTS.

[PageOutline](PageOutline "wikilink")

Layout of important files and directories
=========================================

This page summarises the overall file and directory structure of GHC. We
include both source files and generated files; the latter are always
identified "build-tree only".

Everything starts with the main GHC repository (see
\[wiki:Building/GettingTheSources\]). The build system calls that
directory \`\$(TOP)\`. All the paths below are relative to \`\$(TOP)\`.

Files in \`\$(TOP)\`
--------------------

**`` `packages` ``**`::`\
``  Despite the name "package", this file contains the master list of the *repositories* that make up GHC. It is parsed by `./boot`. ``

**`` `tarballs` ``**`::`\
` Lists the various tarballs (binary packages) that ghc relies on and where to unpack them during a build.`

**`` `validate` ``**`` :: Run `validate` (a shell script) before committing (see [wiki:TestingPatches]). The script is documented in the file itself. ``

**`Documentation`
`files`**`` :: `README`, `ANNOUNCE`, `HACKING`, `LICENSE`, `new_tc_notes` ``

**`GNU` `autoconf`
`machinery`**`` :: `aclocal.m4`, `config.guess`, `config.sub`, `configure.ac`, `install-sh`, `config.mk.in`, `settings.in` ``

**`` `Makefile` ``**`:: The top-level ``: see [wiki:Building/Architecture GHC Build System Architecture]. GHC requires`\
` `[`GNU` `make`](http://www.gnu.org/software/make/)`.`

**`Make` `system` `files`**`` :: `ghc.mk`, `MAKEHELP`, `SUBMAKEHELP` ``

\`libraries/\`
--------------

The \`libraries/\` directory contains all the packages that GHC needs to
build. It has one sub-directory for each package repository (e.g.
\`base\`, \`haskell98\`, \`random\`). Usually each such repository
builds just one package, but there is more than one in \`dph\`.

GHC's libraries are described in more detail on the
\[wiki:Commentary/Libraries libraries page\].

\`compiler/\`, \`docs/\`, \`ghc/\`
----------------------------------

These directories contain the main GHC compiler and documentation. The
\`compiler/\` directory contains the ghc package, which is linked into
an executable in the \`ghc/\` directory.

There is \[wiki:ModuleDependencies documentation of the intended module
dependency structure\] of the \`compiler/\` directory.

`* `**`` `compiler/ghc.cabal.in` ``**`` : the Cabal file for GHC is generated from this. If you add a module to GHC's source code, you must add it in the `ghc.cabal.in` file too, else you'll get link errors. ``

The following directories appear only in the build tree:

`* `**`` `compiler/stage1` ``**`` : generated files for the stage1 build of GHC. There are a handful of files (`ghc_boot_platform.h` etc), and a directory `compiler/stage1/build/` that contains all the `.o` and `.hi` files for the compiler. ``\
`* `**`` `compiler/stage2` ``**`: similarly stage2.`

You can't run a binary from here: look in the \`inplace/\` directory
below for that.

\`rts/\`
--------

Sources for the runtime system; see \[wiki:Commentary/SourceTree/Rts\].

\`includes/\`
-------------

Header files for the runtime system; see
\[wiki:Commentary/SourceTree/Includes\].

\`utils/\`, \`libffi/\`
-----------------------

The \`utils\` directory contains support utilities that GHC uses.

These utils may be built with the bootstrapping compiler, for use during
the build, or with the stage1 or stage2 compiler, for installing. Some
of them are built with both; we can't install the utils built with the
bootstrapping compiler as they may use different versions of C
libraries. The reason we use sometimes stage2 rather than stage1 is that
some utils, e.g. haddock, need the GHC API package.

`* `**`` `utils/ghc-cabal` ``**``  is a little program we use for building the libraries. It's similar to cabal-install, but without the dependencies on `http` etc. ``\
`* `**`` `utils/count_lines` ``**` is a program that counts the number of source-code lines in GHC's code-base. It distinguishes comments from non-comments.`

\`driver/\`
-----------

This contains some simple wrapper programs and scripts, for example the
\`ghci\` wrapper that invokes the \`ghc\` binary with the
\`--interactive\` flag. These wrappers tend to be executable programs on
Windows and scripts on Unix systems.

\`ghc-tarballs/\` (Windows only)
--------------------------------

This contains some tarball files (binary packages) that GHC relies upon.
Used for easier development / deployment on windows.

\`testsuite/\`, \`nofib/\`
--------------------------

The \`testsuite/\` and \`nofib/\` directories contain apparatus for
testing GHC.

`* [wiki:Building/RunningTests]`\
`* [wiki:Building/RunningNoFib]`

\`mk/\`, \`rules/\`
-------------------

The \`mk/\` and \`rules.mk\` directories contains all the build system
Makefile boilerplate; see \[wiki:Building/Architecture GHC Build System
Architecture\]. Some particular files are interesting:

` * `**`` `mk/build.mk` ``**`` : contains Makefile settings that control your build. Details [wiki:Building/Using here].  The file `mk/build.mk.sample` contains a starting point that you can copy to `mk/build.mk` if you want. ``\
` * `**`` `mk/are-validating.mk` ``**`` : this file records the fact that you are doing [wiki:TestingPatches validation], by containing the single line `Validating=YES`.  That in turn means the the build system gets its settings from `mk/validate-settings.mk` instead of from `mk/build.mk`.  Remove the file to stop validating. ``\
` * `**`` `mk/validate.mk` ``**`` : just like `build.mk`, but applies when validating.  Use this file to override the default settings for validation, which are in `mk/validate-settings.mk`. ``

\`distrib/\`
------------

Miscellaneous files for building distributions.

Stuff that appears only in a build tree
---------------------------------------

### \`inplace/\`

The \`inplace/\` directory is where we "install" stage1 and stage2
compilers, and other utility programs, when they are built, to be used
when building other things in the build tree. The layout is exactly the
same as that of an installed GHC on the host platform.

`  * `**`` `inplace/bin/` ``**`: executables, including `\
``     * `ghc-stage1` ``\
``     * `ghc-stage2` ``\
``     * `ghc-pkg` ``\
``     * `hasktags` ``\
``     * `hsc2hs` ``\
``     * `haddock` ``\
``     * `count_lines` ``\
``     * `compareSizes` ``

`  * `**`` `inplace/lib/` ``**`: suppporting libraries for the executables.`

### \`.../dist\*/\`

In many directories, \`dist\*\` subdirectories appear. These are where
Cabal, and the build system makefiles, put all of the files generated
while building. Some particularly interesting files are:

` * `**`` `docs/users_guide/users_guide/index.html` ``**`: the HTML for the user manual`\
` * `**`` `libraries/` ``*`lib`*`` `/dist-install/doc/html/` ``*`lib`***`: contains the Haddock'd documentation for library `*`lib`*

[PageOutline](PageOutline "wikilink")

------------------------------------------------------------------------

Stack Layout
------------

The stack-layout phase decides where to spill variables. The important
goals are to avoid memory traffic and to minimize the size of the stack
frame. Both of these goals are accomplished by reusing stack slots.

### Representing Stack Slots

For each stack slot, we introduce a new name, then treat the name as the
addressing expression for the slot. At the end of the pipeline, we
choose a stack layout, then replace each stack slot with its offset from
the stack pointer. The benefit is that we break the phase-ordering
problem: any phase of the compiler can name a stack slot.

For example, for a variable \`x\`, the expression \`SS(x)\` is the
address of the stack slot where we can spill \`x\`. (I don't think we
output any C-- that uses SS anymore, but the new code generator marks
its stack slots prior to layout with \`young<k> + 4\`, etc. -- Edward)
The stack is assumed to grow down, and we assume that the address
\`SS(x)\` points to the old end of the slot. Therefore, to address the
low address of a 4-byte slot, we would use the expression \`SS(x + 4)\`.
And we would spill \`x\` using the following instruction:

where refers to an address in memory.

But what about parameter passing? We use a similar technique, but this
time we describe the slot for each location as an offset within the area
where the parameters are passed. For example, we lower a function call

into approximately the following C--:

We use the following types to represent stack slots and
parameter-passing areas:

An \`Area\` represents space on the stack; it may use either the
\`RegSlot\` constructor to represent a single stack slot for a register
or the \`CallArea\` constructor to represent parameters passed to/from a
function call/return. In a young \`CallArea\`, the \`BlockId\` is the
label of the function call's continuation, and it passes parameters to
the call.

**Area layout and addressing**

`` * Each `Area` grows down, towards lower machine addresses.  ``\
`* `*`Offsets`*``  are always-positive byte displacements within an `Area`. ``\
`* The low-offset end is also called the "old end" of the area, the high-offset end is also called the "young end".`\
`* Notice that the low-offset (old) end has higher machine addresses.`\
`* Offset 0 (if we allowed it) would address the byte one `*`beyond`*``  the high-address end of the `Area`.  ``\
`` * Larger offsets (from the beginning of the `Area`) correspond to lower machine addresses. ``\
`` * Hence, to address a 4-byte object at the old end of `Area` a, we use the offset +4, thus `(CmmStackSlot a 4)`. ``

The \`Old\` call area is the initial state of the stack on entry to the
function (the overflow parameters and the return address) as well as any
arguments that will be passed to a tail call. (SLPJ believes that:) On
entry to the function, register \`Sp\` contains the address of the
youngest (lowest-address, highest offset) byte in the \`Old\` area.

Note that \`RegSlot\` areas are very small (since they only need to
store a single register), while \`CallArea\` are contiguous chunks of
arguments.

To name a specific location on the stack, we represent its address with
a new kind of \`CmmExpr\`: the \`CmmStackSlot\`. A \`CmmStackSlot\` is
just an integer offset into an \`Area\`. [BR](BR "wikilink")

Notice that a \`CmmStackSlot\` is an *address*, so we can say to make
\`Sp\` point to a particular stack slot. Use a \`CmmLoad\` to load from
the stack slot.

The following figure shows the layout of a \`CallArea\` for both the
outgoing parameters (function call) and incoming results (continuation
after returning from the function call). Note that the incoming and
outgoing parameters may be different, and they may overlap.

[Image(CallArea.png)](Image(CallArea.png) "wikilink")

A \`RegSlot\` is laid out in the same fashion, with the offset 0
pointing off the high byte of the stack slot. To address an 8-byte
double-word, we would use the offset 8. To address only the high word of
the same stack slot, we would use the offset 4.

Currently, the intermediate code does not explicitly use a virtual frame
pointer, but when we talk about offsets into the stack, we implicitly
assume that there is a virtual frame pointer that points just off the
oldest byte of the return address on entry to the procedures. Therefore,
on entry to the procedure, the offset of the (4-byte) return address is
4.

### Laying out the stack

The business of the stack-layout pass is to construct a mapping (fixed
across a single procedure) which assigns a virtual stack slot (i.e.
offset in bytes, relative to the virtual frame pointer) to each
\`Area\`.

A naive approach to laying out the stack would be to give each variable
its own stack slot for spilling, and allocate only the ends of the stack
frame for parameter-passing areas. But this approach misses two
opportunities for optimization:

`* Stack slots can be reused by variables that are never on the stack at the same time`\
`* If a function returns a variable on the stack, we might be able to use the return location as the variable's stack slot.`

As it turns out, it is quite common in GHC that the first definition of
a variable comes when its value is returned from a function call. If the
value is returned on the stack, then an important optimization is to
avoid copying that value to some other location on the stack. How is
that achieved? By making sure the location where the value is returned
is also its spill slot.

### A greedy algorithm

We rewrite the stack slots in two passes:

`` 1. Walk over the graph and choose an offset for each `Area`. ``\
`1. Walk over the graph, keeping track of the stack pointer, and rewrite each address of a stack slot with an offset from the stack pointer. Also, insert adjustments to the stack pointer before and after proc points.`

The details are in cmm/CmmProcPointZ.hs (they have not yet been
committed, but will be soon - Aug 4, 2008).

Layout of the stack
===================

Every \[wiki:Commentary/Rts/HeapObjects\#ThreadStateObjects TSO object\]
contains a stack. The stack of a TSO grows downwards, with the topmost
(most recently pushed) word pointed to by , and the bottom of the stack
given by .

The stack consists of a sequence of *stack frames* (also sometimes
called *activation records*) where each frame has the same layout as a
heap object:

|| Header || Payload... ||

There are several kinds of
\[wiki:Commentary/Rts/Storage/Stack\#KindsofStackFrame stack frames\],
but the most common types are those pushed when evaluating a expression:
The code for evaluating a pushes a new stack frame representing the
alternatives of the case, and continues by evaluating . When completes,
it returns to the stack frame pushed earlier, which inspects the value
and selects the appropriate branch of the case. The stack frame for a
includes the values of all the free variables in the case alternatives.

Info tables for stack frames
----------------------------

The info table for a stack frame has a couple of extra fields in
addition to the \[wiki:Commentary/Rts/HeapObjects\#InfoTables basic info
table layout\]. A stack-frame info table is defined by in
[GhcFile(includes/rts/storage/InfoTables.h)](GhcFile(includes/rts/storage/InfoTables.h) "wikilink").

[Image(ret-itbl-no-rv.png)](Image(ret-itbl-no-rv.png) "wikilink")

The *SRT* field points to the static reference table (SRT) for this
stack frame (see \[wiki:Commentary/Rts/Storage/GC/CAFs\] for details of
SRTs).

Layout of the payload
---------------------

Unlike heap objects which mainly have "pointers first" layout, in a
stack frame the pointers and non-pointers are intermingled. This is so
that we can support "stack stubbing" whereby a live variable stored on
the stack can be later marked as dead simply by pushing a new stack
frame that identifies that slot as containing a non-pointer, so the GC
will not follow it.

Stack frames therefore have
\[wiki:Commentary/Rts/HeapObjects\#Bitmaplayout bitmap layout\].

Kinds of Stack Frame
--------------------

The constants for the different types of stack frame are defined in
[GhcFile(includes/rts/storage/ClosureTypes.h)](GhcFile(includes/rts/storage/ClosureTypes.h) "wikilink").
More details about the layouts are available in
[GhcFile(includes/rts/storage/Closures.h)](GhcFile(includes/rts/storage/Closures.h) "wikilink")

`* `\
`* `\
`* `\
`* `` - (Explained a bit here: `[`https://ghc.haskell.org/trac/ghc/wiki/Commentary/Compiler/CPS#Notes`](https://ghc.haskell.org/trac/ghc/wiki/Commentary/Compiler/CPS#Notes)`)`\
`* `\
`* `\
`* `` - The stack is chunked now. Connected as a linked list. (Since Dec 2010: f30d527344db528618f64a25250a3be557d9f287,  `[`Blogpost`](https://ghc.haskell.org/trac/ghc/blog/stack-chunks)`)`\
`* `\
`* `\
`* `\
`* `

Video: [STG
language](http://www.youtube.com/watch?v=v0J1iZ7F7W8&list=PLBkRCigjPwyeCSD_DFxpd246YIF7_RDDI)
(17'21")

The STG syntax data types
=========================

Before code generation, GHC converts the Core-language program into .
The basic ideas are still pretty much exactly as described in the paper
[Implementing lazy functional languages on stock hardware: the Spineless
Tagless
G-machine](http://research.microsoft.com/en-us/um/people/simonpj/papers/spineless-tagless-gmachine.ps.gz).

The best way to think of STG is as special form of
\[wiki:Commentary/Compiler/CoreSynType Core\]. Specifically, the
differences are these (see
[GhcFile(compiler/stgSyn/StgSyn.hs)](GhcFile(compiler/stgSyn/StgSyn.hs) "wikilink")):

`* Function arguments are atoms (literals or variables), of type ``.`\
`* The right hand side of a let-binding, ``, is either`\
``    * `StgRhsCon`: a constructor application, or  ``\
``    * `StgRhsClosure`:  ``**`lambda-form`**` (possibly with zero arguments, in which case it's a thunk).`\
`* Constructor applications are saturated.`\
`* Applications of primitive operators are saturated.`\
`* Lambdas can only appear the right-hand side of a let-binding.  (There is an expression form ``, but it is only used during the Core-to-STG transformation, not in a valid STG program.)`\
`* Types have largely been discarded, retaining only enough type information as is needed to guide code generation. There is an `` checker, which makes some consistency checks, but the !CoreLint guarantee that "if the program passes Lint it cannot crash" has been lost.`

In addition, the STG program is decorated with the results of some
analyses:

``  * Every lambda-form (`StgRhsClosure`) lists its free variables.  These are the variables that are in the thunk of function closure that is allocated by the let. ``

` * Every lambda-form gives its [wiki:Commentary/Rts/CAFs `**`Static`
`Reference`
`Table`**`] or `**`SRT`**`.  You should think of the SRT as the `*`top-level`*` free variables of the body.  They do not need to be dynamically allocated in the heap object, but they do need to be accessible from the object's info-table, so that the garbage collector can find the CAFs kept alive by the object.`

` * A `` expression is decorated with its `**`live`
`variables`**`; that is, variables reachable from the continuation of the case.  More precisely, two sets of live variables, plus the SRT for the continuation.  Todo: say more.`

` * The STG program has a new construct called `**`let-no-escape`**`, that encodes so-called `**`join`
`points`**`. Variables bound by a let-no-escape are guaranteed to be tail-calls, not embedded inside a data structure, in which case we don`

GHC Commentary: Software Transactional Memory (STM)
===================================================

This document gives an overview of the runtime system (RTS) support for
GHC's STM implementation. We will focus on the case where fine grain
locking is used ().

Some details about the implementation can be found in the papers
["Composable Memory
Transactions"](http://research.microsoft.com/en-us/um/people/simonpj/papers/stm/stm.pdf)
and ["Transactional memory with data
invariants"](http://research.microsoft.com/en-us/um/people/simonpj/papers/stm/stm-invariants.pdf).
Additional details can be found in the Harris et al book ["Transactional
memory"](http://www.morganclaypool.com/doi/abs/10.2200/s00272ed1v01y201006cac011).
Some analysis on performance can be found in the paper ["The Limits of
Software Transactional
Memory"](https://www.bscmsrc.eu/sites/default/files/cf-final.pdf) though
this work only looks at the coarse grain lock version. Many of the other
details here are gleaned from the comments in the source code.

Background
==========

This document assumes the reader is familiar with some general details
of GHC's execution and memory layout. A good starting point for this
information is can be found here:
\[wiki:Commentary/Compiler/GeneratedCode Generated Code\].

Definitions
-----------

### Useful RTS terms

`Corresponds to a CPU. The number of capabilities should match the number of CPUs. See [wiki:Commentary/Rts/Scheduler#Capabilities Capabilities].`

TSO

` Thread State Object. The state of a Haskell thread. See [wiki:Commentary/Rts/Storage/HeapObjects#ThreadStateObjects Thread State Objects].`

Heap object

` Objects on the heap all take the form of an `` structure with a header pointing and a payload of data. The header points to code and an info table. See [wiki:Commentary/Rts/Storage/HeapObjects Heap Objects].`

### Transactional Memory terms

Read set

` The set of ``s that are read, but not written to during a transaction.`

Write set

` The set of ``s that are written to during a transaction. In the code each written `` is called an "update entry" in the transactional record.`

Access set

` All ``s accessed during the transaction.`

While GHC's STM does not have a separate read set and write set these
terms are useful for discussion.

Retry

` Here we will use the term retry exclusively for the blocking primitive in GHC's STM. This should not be confused with the steps taken when a transaction detects that it has seen an inconsistent view of memory and must start again from the beginning.`

Failure

` A failed transaction is one that has seen inconsistent state. This should not be confused with a successful transaction that executes the `` primitive.`

------------------------------------------------------------------------

Overview of Features
====================

At the high level, transactions are computations that read and write to
s with changes only being committed atomically after seeing a consistent
view of memory. Transactions can also be composed together, building new
transactions out of existing transactions. In the RTS each transaction
keeps a record of its interaction with the s it touches in a . A pointer
to this record is stored in the TSO that is running the transaction.

Reading and Writing
-------------------

The semantics of a transaction require that when a is read in a
transaction, its value will stay the same for the duration of execution.
Similarly a write to a will keep the same value for the duration of the
transaction. The transaction itself, however, from the perspective of
other threads can apply all of its effects in one moment. That is, other
threads cannot see intermediate states of the transaction, so it is as
if all the effects happen in a single moment.

As a simple example we can consider a transaction that transfers value
between two accounts:

No other thread can observe the value in without also observing in .

Blocking
--------

Transactions can choose to block until changes are made to s that allow
it to try again. This is enabled with an explicit . Note that when
changes are made the transaction is restarted from the beginning.

Continuing the example, we can choose to block when there are
insufficient funds:

Choice
------

Any blocking transaction can be composed with to choose an alternative
transaction to run instead of blocking. The primitive operation creates
a nested transaction and if this first transaction executes , the
effects of the nested transaction are rolled back and the alternative
transaction is executed. This choice is biased towards the first
parameter. A validation failure in the first branch aborts the entire
transaction, not just the nested part. An explicit is the only mechanism
that gives partial rollback.

We now can choose the account that has enough funds for the transfer:

Data Invariants
---------------

Invariants support checking global data invariants beyond the atomicity
transactions demand. For instance, a transactional linked list (written
correctly) will never have an inconsistent structure due to the
atomicity of updates. It is no harder to maintain this property in a
concurrent setting then in a sequential one with STM. It may be desired,
however, to make statements about the consistency of the *data* in a
particular a sorted linked list is sorted, not because of the structure
(where the s point to) but instead because of the data in the structure
(the relation between the data in adjacent nodes). Global data invariant
checks can be introduced with the operation which demands that the
transaction it is given results in and that it continues to hold for
every transaction that is committed globally.

We can use data invariants to guard against negative balances:

Exceptions
----------

Exceptions inside transactions should only propagate outside if the
transaction has seen a consistent view of memory. Note that the
semantics of exceptions allow the exception itself to capture the view
of memory from inside the transaction, but this transaction is not
committed.

------------------------------------------------------------------------

Overview of the Implementation
==============================

We will start this section by considering building GHC's STM with only
the features of reading and writing. Then we will add then and finally
data invariants. Each of the subsequent features adds more complexity to
the implementation. Taken all at once it can be difficult to understand
the subtlety of some of the design choices.

------------------------------------------------------------------------

Transactions that Read and Write.
---------------------------------

With this simplified view we only support , , and as well as all the STM
type class instances except .

### Transactional Record

The overall scheme of GHC's STM is to perform all the effects of a
transaction locally in the transactional record or . Once the
transaction has finished its work locally, a value based consistency
check determines if the values read for the entire access set are
consistent. This only needs to consider the and the main memory view of
the access set as it is assumed that main memory is always consistent.
This check also obtains locks for the write set and with those locks we
can update main memory and unlock. Rolling back the effects of a
transaction is just forgetting the current and starting again.

The transactional record itself will have an entry for each
transactional variable that is accessed. Each entry has a pointer to the
heap object and a record of the value that the held when it was first
accessed.

### Starting

A transaction starts by initializing a new () assigning the TSO's
pointer to the new then executing the transaction's code.

(See [GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") and
[GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") ).

### Reading

When a read is attempted we first search the for an existing entry. If
it is found, we use that local view of the variable. On the first read
of the variable, a new entry is allocated and the value of the variable
is read and stored locally. The original does not need to be accessed
again for its value until a validation check is needed.

In the coarse grain version, the read is done without synchronization.
With the fine grain lock, the lock variable is the of the structure.
While reading an inconsistent value is an issue that can be resolved
later, reading a value that indicates a lock and handing that value to
code that expects a different type of heap object will almost certainly
lead to a runtime failure. To avoid this the fine grain lock version of
the code will spin if the value read is a lock, waiting to observe the
lock released with an appropriate pointer to a heap object.

(See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") )

### Writing

Writing to a requires that the variable first be in the . If it is not
currently in the , a read of the 's value is stored in a new entry (this
value will be used to validate and ensure that no updates were made
concurrently to this variable).

In both the fine grain and coarse grain lock versions of the code no
synchronization is needed to perform the write as the value is stored
locally in the until commit time.

(See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") )

### Validation

Before a transaction can make its effects visible to other threads it
must check that it has seen a consistent view of memory while it was
executing. Most of the work is done in by checking that s hold their
expected values.

For the coarse grain lock version the lock is held before entering
through the writing of values to s. With the fine grain lock, validation
acquires locks for the write set and reads a version number consistent
with the expected value for each in the read set. After all the locks
for writes have been acquired, The read set is checked again to see if
each value is still the expected value and the version number still
matches ().

(See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") and )

### Committing

Before committing, each invariant associated with each accessed needs to
be checked by running the invariant transaction with its own . The read
set for each invariant is merged into the transaction as those reads
must be included in the consistency check. The is then validated. If
validation fails, the transaction must start over from the beginning
after releasing all locks. In the case of the coarse grain lock
validation and commit are in a critical section protected by the global
STM lock. Updates to s proceeds while holding the global lock.

With the fine grain lock version when validation, including any
read-only phase, succeeds, two properties will hold simultaneously that
give the desired atomicity:

-   Validation has witnessed all s with their expected value.
-   Locks are held for all of the s in the write set.

Commit can proceed to increment each locked 's field and unlock by
writing the new value to the field. While these updates happen
one-by-one, any attempt to read from this set will spin while the lock
is held. Any reads made before the lock was acquired will fail to
validate as the number of updates will change.

(See [GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") and
[GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") )

### Aborting

Aborting is simply throwing away changes that are stored in the .

(See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") )

### Exceptions

An exception in a transaction will only propagate outside of the
transaction if the transaction can be validated. If validation fails,
the whole transaction will abort and start again from the beginning.
Nothing special needs to be done to support the semantics allowing the
view *inside* the aborted transaction.

(See [GhcFile(rts/Exception.cmm)](GhcFile(rts/Exception.cmm) "wikilink")
which calls from [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink")).

------------------------------------------------------------------------

Blocking with 
--------------

We will now introduce the blocking feature. To support this we will add
a watch queue to each where we can place a pointer to a blocked TSO.
When a transaction commits we will now wake up the TSOs on watch queues
for s that are written.

The mechanism for is similar to exception handling. In the simple case
of only supporting blocking and not supporting choice, an encountered
retry should validate, and if valid, add the TSO to the watch queue of
every accessed (see [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink")
and ). Locks are acquired for all s when validating to control access to
the watch queues and prevent missing an update to a before the thread is
sleeping. In particular if validation is successful the locks are held
after the return of , through the return to the scheduler, after the
thread is safely paused (see
[GhcFile(rts/HeapStackCheck.cmm)](GhcFile(rts/HeapStackCheck.cmm) "wikilink")
), and until is called. This ensures that no updates to the s are made
until the TSO is ready to be woken. If validation fails, the is
discarded and the transaction is started from the beginning. (See
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") )

When a transaction is committed, each write that it makes to a is
preceded by waking up each TSO in the watch queue. Eventually these TSOs
will be run, but before restarting the transaction its is validated
again if valid then nothing has changed that will allow the transaction
to proceed with a different result. If invalid, some other transaction
has committed and progress may be possible (note there is the additional
case that some other transaction is merely holding a lock temporarily,
causing validation to fail). The TSO is not removed from the watch
queues it is on until the transaction is aborted (at this point we no
longer need the ) and the abort happens after the failure to validate on
wakeup. (See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") and )

------------------------------------------------------------------------

Choice with 
------------

When executes it searches the stack for either a or the outer (the
boundary between normal execution and the transaction). The former is
placed on the stack by an (see
[GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") ) and if
executing the first branch we can partially abort and switch to the
second branch, otherwise we propagate the further. In the latter case
this represents a transaction that should block and the behavior is as
above with only .

How do we support a "partial abort"? This introduces the need for a
nested transaction. Our will now have a pointer to an outer (the field).
This allows us to isolate effects from the branch of the that we might
need to abort. Let's revisit the features that need to take this into
account.

`* `**`Reading`**` -- Reads now search the chain of nested transactions in addition to the local ``. When an entry is found in a parent it is copied into the local ``. Note that there is still only a single access to the actual `` through the life of the transaction (until validation).`\
`* `**`Writing`**` -- Writes, like reads, now search the parent ``s and the write is stored in the local copy.`\
`* `**`Retry`**` -- As described above, we now need to search the stack for a `` and if found, aborting the nested transaction and attempting the alternative or propagating the retry instead of immediately working on blocking.`\
`* `**`Validation`**` -- If we are validating in the middle of a running transaction we will need to validate the whole nest of transactions.`[`BR`](BR "wikilink")`(See `[`GhcFile(rts/STM.c)`](GhcFile(rts/STM.c) "wikilink")` `` and its uses in `[`GhcFile(rts/Exception.cmm)`](GhcFile(rts/Exception.cmm) "wikilink")` and `[`GhcFile(rts/Schedule.c)`](GhcFile(rts/Schedule.c) "wikilink")`)`\
`* `**`Committing`**` -- Just as we now have a partial abort, we need a partial commit when we finish a branch of an ``. This commit is done with `` which validates just the inner `` and merges updates back into its parent. Note that an update is distinguished from a read only entry by value. This means that if a nested transaction performs a write that reverts a value this is a change and must still propagate to the parent (see ticket #7493).`\
`* `**`Aborting`**` -- There is another subtle issue with how choice and blocking interact. When we block we need to wake up if there is a change to `*`any`*` accessed ``. Consider a transaction:`[`BR`](BR "wikilink")[`BRIf`](BR "wikilink")` both `` and `` execute `` then even though the effects of `` are thrown away, it could be that a change to a `` that is only in the access set of `` will allow the whole transaction to succeed when it is woken.`[`BRTo`](BR "wikilink")` solve this problem, when a branch on a nested transaction is aborted the access set of the nested transaction is merged as a read set into the parent ``. Specifically if the `` is in `*`any`*` `` up the chain of nested transactions it must be ignored, otherwise it is entered as a new entry (retaining just the read) in the parent ``.`[`BR`](BR "wikilink")`(See again ticket #7493 and `[`GhcFile(rts/STM.c)`](GhcFile(rts/STM.c) "wikilink")` ``)`\
`* `**`Exceptions`**` -- The only change needed here each `` on the stack represents a nested transaction. As the stack is searched for a handler, at each encountered `` the nested transaction is aborted. When the `` is encountered we then know that there is no nested transaction.`[`BR`](BR "wikilink")`(See `[`GhcFile(rts/Exception.cmm)`](GhcFile(rts/Exception.cmm) "wikilink")` ``)`

(See [GhcFile(rts/PrimOps.cmm)](GhcFile(rts/PrimOps.cmm) "wikilink") and
)

------------------------------------------------------------------------

Invariants
----------

We will start this section with an overview of some of the details then
review with notes on the changes from the choice case.

### Details

As a transaction is executing it can collect dynamically checked data
invariants. These invariants are transactions that are never committed,
but if they raise an exception when executed successfully that exception
will propagate out of the atomic frame.

` Primitive operation that adds an invariant (transaction to run) to the queue of the current `` by calling ``.`

` A wrapper for `` (to give it the `` type).`

` This is the `` from the "Transactional memory with data invariants" paper. The action immediately runs, wrapped in a nested transaction so that it will never commit but will have an opportunity to raise an exception. If successful, the originally passed action is added to the invariant queue.`

` Takes an `` action that results in a `` and adds an invariant that throws an exception when the result of the transaction is ``.`

The bookkeeping for invariants is in each s queue and the s field. Each
invariant is in a structure that includes the action, the where it was
last executed, and a lock. This is added to the current s queue when is
executed.

When a transaction completes, execution will reach the and the s will be
(a nested transaction would have a before the to handle cases of
non-empty ). The frame will then check the invariants by collecting the
invariants it needs to check with , dequeuing each, executing, and when
(or if) we get back to the frame, aborting the invariant action. If the
invariant failed to hold, we would not get here due to an exception and
if it succeeds we do not want its effects. Once all the invariants have
been checked, the frame will to commit.

Which invariants need to be checked for a given transaction? Clearly
invariants introduced in the transaction will be checked these are added
to the s queue directly when is executed. In addition, once the
transaction has finished executing, we can look at each entry in the
write set and search its watch queue for any invariants.

Note that there is a in the package in which matches the from the
[beauty](http://research.microsoft.com/pubs/74063/beautiful.pdf) chapter
of "Beautiful code":

It requires no additional runtime support. If it is a transaction that
produces the argument it will be committed (when ) and it is only a one
time check, not an invariant that will be checked at commits.

### Changes from Choice

With the addition of data invariants we have the following changes to
the implementation:

`* `**`Retrying`**` -- A retry in an invariant indicates that the invariant could not proceed and the whole transaction should block. This special case is detected when an `` is encountered with a nest of transactions (i.e. when the `` field is not ``). The invariant is simply aborted and execution proceeds to `` (see `[`GhcFile(rts/PrimOps.cmm)`](GhcFile(rts/PrimOps.cmm) "wikilink")` ``).`\
`* `**`Commiting`**` -- Commit now needs a phase where it runs invariants after the code of the transaction has completed but before commit. The implementation recycles the structure already in place for this phase so special cases are needed in the `` that collects invariants and works through them one at a time then moves on to committing (see `[`GhcFile(rts/PrimOps.cmm)`](GhcFile(rts/PrimOps.cmm) "wikilink")` ``).`[`BRTo`](BR "wikilink")` efficiently handle invariants they need to only be checked when a relevant data dependency changes. This means we can associate them with the `` of the last commit that needed to check the invariant at the cost of serializing invariant handling commits. This is enforced by the lock on each invariant. If it cannot be acquired the whole transaction must start over.`[`BRAt`](BR "wikilink")` commit time, each invariant is locked and the read set for the last commited transaction of each invariant is merged into the ``.`[`BRValidation`](BR "wikilink")` acuqires lock for all entries in the `` (not just the writes). After validation, each invariant is removed from the watch queue of each `` it previously depended on, then the `` that was used when executing the invariant code is updated to reflect the values from the final execution of the main transaction and each ``, being a data depenency of the invariant, has the invariant added to its watch queue.`[`BR`](BR "wikilink")`(See `[`GhcFile(rts/STM.c)`](GhcFile(rts/STM.c) "wikilink")` ``, `` and ``)`\
`* `**`Exceptions`**` -- When an exception propagates to the `` there are now two states that it could encounter. If there is no enclosing `` we are not dealing with an exception from an invariant and it proceeds as above. Seeing a nest of transactions indicates that the transaction was checking an invariant when it encountered the exception. The effect of a failed invariant `*`is`*` this exception so nothing special needs to be done except to validate and abort both the outer transaction and the nested transaction (see `[`GhcFile(rts/Exception.cmm)`](GhcFile(rts/Exception.cmm) "wikilink")` ``).`

------------------------------------------------------------------------

Other Details
-------------

This section describes some details that can be discussed largely in
isolation from the rest of the system.

### Detecting Long Running Transactions

While the type system enforces STM actions to be constrained to STM side
effects, pure computations in Haskell can be non-terminating. It could
be that a transaction sees inconsistent data that leads to
non-termination that would never happen in a program that only saw
consistent data. To detect this problem, every time a thread yields it
is validated. A validation failure causes the transaction to be
condemned.

### Transaction State

Each has a field that holds the status of the transaction. It can be one
of the following:

` The transaction is actively running.`

` The transaction has seen an inconsistency.`

` The transaction has committed and is in the process of updating `` values.`

` The transaction has aborted and is working to release locks.`

` The transaction has hit a `` and is waiting to be woken.`

If a state is (some inconsistency was seen) validate does nothing. When
a top-level transaction is aborted in , if the state is it will remove
the watch queue entries for the . Similarly if a waiting is condemned
via an asynchronous exception when a validation failure is observed
after a thread yield, its watch queue entries are removed. Finally a in
the state is not condemned by a validation. In this case the is already
waiting for a wake up from a that changes and observing an inconsistency
merely indicates that this will happen soon.

In the work of Keir Fraser a transaction state is used for cooperative
efforts of transactions to give lock-free properties for STM systems.
The design of GHC's STM is clearly influenced by this work and seems
close to some of the algorithms in Fraser's work. It does not, however,
implement what would be required to be lock-free or live-lock free (in
the fine grain lock code). For instance, if two transactions and are
committing at the same time and has read and written while has read and
written , both the transactions can fail to commit. For example,
consider the interleaving:

||**\`T1\`** || **\`TVar\`** || **\`T2\`** ||**Action** || ||\`A 0 0\`
|| \`A 0\` || ||\`T1\` read A || || || \`B 0\` || \`B 0 0\` ||\`T2\`
read B || ||\`B 0 1\` || || ||\`T1\` write B 1 || || || || \`A 0 1\`
||\`T2\` write A 1 || ||\`A 0 0 0\` || \`A 0\` || ||\`T1\` Validation
Part 1 (read A) || || || \`A T2\` || ||\`T2\` Validation (Lock A) || ||
|| \`B 0\` || \`B 0 0 0\` ||\`T2\` Validation (Read B) || || || \`B T1\`
|| ||\`T1\` Validation Part 2 (Lock B) ||

Note: the first and third columns are the local state of the s and the
second column is the values of the structures. Each entry has the
expected value followed by the new value and a number of updates field
when it is read for validation.

At this point and both perform their and both could (at least one will)
discover that a in their read set is now locked. This leads to both
transactions aborting. The chances of this are narrow but not impossible
(see ticket \#7815). Fraser's work avoids this by using the transaction
status and the fact that locks point back to the holding the lock to
detect other transactions in a read only check (read phase) and
resolving conflicts so that at least one of the transactions can commit.

A simpler example can also cause both transactions to abort. Consider
two transactions with the same write set, but the writes entered the s
in a different order. Both transactions could encounter a lock from the
other before they have a chance to release locks and get out of the way.
Having an ordering on lock could avoid this problem but would add a
little more complexity.

### GC and ABA

GHC's STM does comparisons for validation by value. Since these are
always pure computations these values are represented by heap objects
and a simple pointer comparison is sufficient to know if the same value
is in place. This presents an ABA problem however if the location of
some value is recycled it could appear as though the value has not
changed when, in fact, it is a different value. This is avoided by
making the fields of the entries pointers into the heap followed by the
garbage collector. As long as a is still alive it will keep the original
value it read for a alive.

### Management of s

The structure is built as a list of chunks to give better locality and
amortize the cost of searching and allocating entries. Additionally s
are recycled to aid locality further when a transaction is aborted and
started again. Both of these details add a little complexity to the
implementation that is abated with some macros such as and .

### Tokens and Version Numbers.

When validating a transaction each entry in the is checked for
consistency. Any entry that is an update (in the write set) is locked.
This locking is a visible effect to the rest of the system and prevents
other committing transactions from progress. Reads, however, are not
going to be updated. Instead we check that a read to the value matches
our expected value, then we read a version number (the field) and check
again that the expected value holds. This gives us a read of that is
consistent with the holding the expected value. Once all the locks for
the write set are acquired we know that only our transaction can have an
effect on the write set. All that remains is to rule out some change to
the read set while we were still acquiring locks for the writes. This is
done in the read phase (with ) which checks first if the value matches
the expectation then checks if the version numbers match. If this holds
for each entry in the read set then there must have existed a moment,
while we held the locks for all the write set, where the read set held
all its values. Even if some other transaction committed a new value and
yet another transaction committed the expected value back the version
number will have been incremented.

All that remains is managing these version numbers. When a is updated
its version number is incremented before the value is updated with the
lock release. There is the unlikely case that the finite version numbers
wrap around to an expected value while the transaction is committing
(even with a 32-bit version number this is *highly* unlikely to happen).
This is, however, accounted for by allocating a batch of tokens to each
capability from a global variable. Each time a transaction is started it
decrements it's batch of tokens. By sampling at the beginning of commit
and after the read phase the possibility of an overflow can be detected
(when more then 32-bits worth of commits have been allocated out).

(See [GhcFile(rts/STM.c)](GhcFile(rts/STM.c) "wikilink") , , , , and )

### Implementation Invariants

Some of the invariants of the implementation:

`* Locks are only acquired in `[`GhcFile(rts/STM.c)`](GhcFile(rts/STM.c) "wikilink")` and are always released before the end of a function call (with the exception of `` which must release locks after the thread is safe).`\
`* When running a transaction each `` is read exactly once and if it is a write, is updated exactly once.`\
`* Main memory (``s) always holds consistent values or locks of a partially updated commit. That is a set of reads at any moment from ``s will result in consistent data if none of the values are locks.`\
`* A nest of ``s has a matching nest of ``s ending with an `` on the stack. One exception to this is when checking data invariants the invariant's `` is nested under the top level `` without a ``.`

### Fine Grain Locking

The locks in fine grain locking () are at the level and are implemented
by placing the locking thread's in the s current value using a compare
and swap (). The value observed when locking is returned by . To test if
a is locked the value is inspected to see if it is a (checking that the
closure's info table pointer is to ). If a is found will spin reading
the s current value until it is not a and then attempt again to obtain
the lock. Unlocking is simply a write of the current value of the .
There is also a conditional lock which will obtain the lock if the s
current value is the given expected value. If the is already locked this
will not be the case (the value would be a ) and if the has been updated
to a new (different) value then locking will fail because the value does
not match the expected value. A compare and swap is used for .

This arrangement is useful for allowing a transaction that encounters a
locked to know which particular transaction is locked (used in
algorithms in from Fraser). GHC's STM does not, however, use this
information.

Bibliography
------------

Fraser, Keir. *Practical lock-freedom*. Diss. PhD thesis, University of
Cambridge Computer Laboratory, 2004.

Jones, Simon Peyton. "Beautiful concurrency." *Beautiful Code: Leading
Programmers Explain How They Think* (2007): 385-406.

Harris, Tim, et al. "Composable memory transactions." *Proceedings of
the tenth ACM SIGPLAN symposium on Principles and practice of parallel
programming.* ACM, 2005.

Harris, Tim, James Larus, and Ravi Rajwar. "Transactional memory."
*Synthesis Lectures on Computer Architecture* 5.1 (2010): 1-263.

Harris, Tim, and Simon Peyton Jones. "Transactional memory with data
invariants." *First ACM SIGPLAN Workshop on Languages, Compilers, and
Hardware Support for Transactional Computing (TRANSACT'06), Ottowa.*
2006.

GHC Commentary: Storage
=======================

GHC's storage manager is designed to be quite flexible: there are a
large number of tunable parameters in the garbage collector, and partly
the reason for this was because we wanted to experiment with tweaking
these settings in the context of Haskell.

[Image(sm-top.png)](Image(sm-top.png) "wikilink")

`* [wiki:Commentary/Rts/Storage/HeapObjects Layout of Heap Objects]`\
`* [wiki:Commentary/Rts/Storage/Stack Layout of the Stack]`\
`* [wiki:Commentary/Rts/Storage/Slop Slop]`\
`* [wiki:Commentary/Rts/Storage/BlockAlloc The Block Allocator]`\
`* [wiki:Commentary/Rts/Storage/GC The Garbage Collector]`\
`* [wiki:Commentary/Rts/Storage/HeapAlloced The HEAP_ALLOCED() macro]`

See also:

`* [wiki:Commentary/Rts/HaskellExecution/PointerTagging Pointer tagging]`

General overview
================

GHC's approach to strictness analysis is that of "demand analysis", a
backwards analysis in which strictness analysis and absence analysis are
done in a single pass. In the future, analysis to perform unboxing, as
well as other analyses, may be implemented within this framework as
well.

IMPORTANT NOTE
==============

The rest of this commentary describes code that is not checked in to the
HEAD yet.

Update: as of 2014-02-12, newer documentation (apparently on the same
topic and apparently more up-to-date) is available at
[Commentary/Compiler/Demand](Commentary/Compiler/Demand "wikilink") (I
am not an expert on the GHC internals though). Also,
[GhcFile(compiler/basicTypes/NewDemand.lhs)](GhcFile(compiler/basicTypes/NewDemand.lhs) "wikilink")
is not any more in the sources, replaced by (or renamed to?)
[GhcFile(compiler/basicTypes/Demand.lhs)](GhcFile(compiler/basicTypes/Demand.lhs) "wikilink").

The demand analyzer
===================

Most of the demand analyzer lives in two files:

`* `[`GhcFile(compiler/basicTypes/NewDemand.lhs)`](GhcFile(compiler/basicTypes/NewDemand.lhs) "wikilink")` (defines the datatypes used by the demand analyzer, and some functions on them)`\
`* `[`GhcFile(compiler/stranal/DmdAnal.lhs)`](GhcFile(compiler/stranal/DmdAnal.lhs) "wikilink")` (the demand analyzer itself)`

The demand analyzer does strictness analysis, absence analysis, and
box-demand analysis in a single pass. (!ToDo: explain what these are.)

In
[GhcFile(compiler/stranal/DmdAnal.lhs)](GhcFile(compiler/stranal/DmdAnal.lhs) "wikilink"),
is the function that performs demand analysis on an expression. It has
the following type: The first argument is an environment mapping
variables onto demand signatures. (!ToDo: explain more.) The second
argument is the demand that's being placed on the expression being
analyzed, which was determined from the context already. The third
argument is the expression being analyzed. returns a pair of a new
expression (possibly with demand information added to any
\[wiki:Commentary/Compiler/NameType Ids\] in it), and a .

Important datatypes
-------------------

 A demand consists of usage information, along with information about
usage of the subcomponents of the expression it's associated with.

 Usage information consists of a triple of three properties: strictness
(or evaluation demand), usage demand, and box demand.

 Something that is may or may not be evaluated. Something that is will
definitely be evaluated at least to its outermost constructor. Something
that is will be fully evaluated (e.g., in , can be said to have
strictness , because it doesn't matter how much we evaluate -- this
expression will diverge anyway.)

 In the context of function arguments, an argument that is is never used
by its caller (e.g., syntactically, it doesn't appear in the body of the
function at all). An argument that is will be used zero or one times,
but not more. Something that is may be used zero, one, or many times --
we don't know.

 Again in the context of function arguments, an argument that is is a
value constructed by a data constructor of a product type whose "box" is
going to be needed. For example, we say that } "uses the box", so in ,
has box-demand information . In }, doesn't "use the box" for its
argument, so in , has box-demand information . When in doubt, we assume
.

 For a compound data value, the type describes demands on its
components. means that we don't know anything about the expression's
type. says "this expression has a product type, and the demands on its
components consist of the demands in the following list". If the is
supplied, that means that this expression must be cast using the given
coercion before it is evaluated. (!ToDo: explain this more.)

(!ToDo: explain why all the above information is important)

Though any expression can have a associated with it, another datatype, ,
is associated with a function body.

 A consists of a (which provides demands for all explicitly mentioned
free variables in a functions body), a list of s on the function's
arguments, and a , which indicates whether this function returns an
explicitly constructed product:

The function takes a strictness environment, an
\[wiki:Commentary/Compiler/NameType Id\] corresponding to a function,
and a representing demand on the function -- in a particular context --
and returns a , representing the function's demand type in this context.
Demand analysis is implemented as a backwards analysis, so takes the
demand on a function's result (which was inferred based on how the
function's result is used) and uses that to compute the demand type of
this particular occurrence of the function itself.

 has four cases, depending on whether the function being analyzed is a
\[wiki:Commentary/Compiler/EntityTypes data constructor\] worker, an
imported (global) function, a local -bound function, or "anything else"
(e.g., a local lambda-bound function).

The data constructor case checks whether this particular constructor
call is saturated. If not, it returns , indicating that we know nothing
about the demand type. If so, it returns a with an empty environment
(since there are no free variables), a list of arg-demands based on the
that was passed in to (that is, the demand on the result of the data
constructor call), and a taken from the constructor Id's strictness
signature.

There are a couple of tricky things about the list of arg-demands:

`* If the result demand (i.e., the passed-in demand) has its box demanded, then we want to make sure the box is demanded in each of the demands for the args. (!ToDo: this may not be true)`\
`* If the result demand is not strict, we want to use `*`n`*` copies of `` as the list of arg-demands, where `*`n`*` is this data constructor's arity.`

(!ToDo: explain the other cases of )

\[wiki:Commentary/Compiler/StrictnessAnalysis/KirstenNotes even more
sketchy notes\]

\[wiki:Commentary/Compiler/StrictnessAnalysis/Examples\]

Symbol Names
============

Since Haskell allows many symbols in constructor and variable names that
C compilers or assembly might not allow (e.g. :, %, \#) these have to be
encoded using z-encoding. The encoding is as follows. See
[GhcFile(compiler/utils/Encoding.hs)](GhcFile(compiler/utils/Encoding.hs) "wikilink").

Tuples
------

|| Decoded || Encoded || Comment || || \`()\` || Z0T || Unit / 0-tuple
|| || || || There is no Z1T || || \`(,)\` || Z2T || 2-tuple || ||
\`(,,)\` || Z3T || 3-tuple || || ... || || And so on ||

Unboxed Tuples
--------------

|| Decoded || Encoded || Comment || || || || There is no Z0H || || \`(\#
\#)\` || Z1H || unboxed 1-tuple (note the space) || || \`(\#,\#)\` ||
Z2H || unboxed 2-tuple || || \`(\#,,\#)\` || Z3H || unboxed 3-tuple ||
|| ... || || And so on ||

Alphanumeric Characters
-----------------------

|| Decoded || Encoded || Comment || || a-y, A-Y, 0-9 || a-y, A-Y, 0-9 ||
Regular letters don't need escape sequences || || z, Z || zz, ZZ || 'Z'
and 'z' must be escaped ||

Constructor Characters
----------------------

|| Decoded || Encoded || Comment || || \`(\` || ZL || Left || || \`)\`
|| ZR || Right || || \`\[\` || ZM || 'M' before 'N' in \[\] || || \`\]\`
|| ZN || || || \`:\` || ZC || Colon ||

Variable Characters
-------------------

|| Decoded || Encoded || Mnemonic || || \`&\` || za || Ampersand || ||
\`|\` || zb || Bar || || \`\^\` || zc || Caret || || \`\$\` || zd ||
Dollar || || \`=\` || ze || Equals || || \`&gt;\` || zg || Greater than
|| || \`\#\` || zh || Hash || || \`.\` || zi || The dot of the 'i' || ||
\`&lt;\` || zl || Less than || || \`-\` || zm || Minus || || \`!\` || zn
|| Not || || \`+\` || zp || Plus || || \`'\` || zq || Quote || || \`\\\`
|| zr || Reverse slash || || \`/\` || zs || Slash || || \`\*\` || zt ||
Times sign || || \`\_\` || zu || Underscore || || \`%\` || zv || (TODO:
I don't know what the mnemonic for this one is. Perhaps relatiVe or
diVide?) ||

Other
-----

Any other character is encoded as a 'z' followed by its hex code (lower
case, variable length) followed by 'U'. If the hex code starts with 'a',
'b, 'c', 'd', 'e' or 'f', then an extra '0' is placed before the hex
code to avoid conflicts with the other escape characters.

Examples
--------

|| Before || After || || \`Trak\` || \`Trak\` || || \`foo\_wib\` ||
\`foozuwib\` || || \`&gt;\` || \`zg\` || || \`&gt;1\` || \`zg1\` || ||
\`foo\#\` || \`foozh\` || || \`foo\#\#\` || \`foozhzh\` || ||
\`foo\#\#1\` || \`foozhzh1\` || || \`fooZ\` || \`fooZZ\` || || \`:+\` ||
\`ZCzp\` || || \`()\` || \`Z0T\` || || \`(,,,,)\` || \`Z5T\` || || \`(\#
\#)\` || \`Z1H\` || || \`(\#,,,,\#)\` || \`Z5H\` ||

\[ Up: \[wiki:Commentary/Compiler/TypeChecker\] \]

The monad for renaming, typechecking, desugaring
================================================

The renamer, typechecker, interface-file typechecker, and desugarer all
share a certain amount in common: they must report errors, handle
environments, do I/O, etc. Furthermore, because of Template Haskell we
have to interleave renaming and typechecking. So all four share a common
monad, called . This infrastructure is defined by the following modules:

` * `[`GhcFile(compiler/utils/IOEnv.lhs)`](GhcFile(compiler/utils/IOEnv.lhs) "wikilink")`: extends the IO monad with an environment (just a simple reader monad).`\
` * `[`GhcFile(compiler/typecheck/TcRnTypes)`](GhcFile(compiler/typecheck/TcRnTypes) "wikilink")`: builds the `` monad on top of ``:`\
` * `[`GhcFile(compiler/typecheck/TcRnMonad)`](GhcFile(compiler/typecheck/TcRnMonad) "wikilink")`: defines lots of access functions for the renamer, typechecker, and interface typechecker.`\
` * `[`GhcFile(compiler/typecheck/DsMonad)`](GhcFile(compiler/typecheck/DsMonad) "wikilink")`: specialises the `` monad for the desugarer.`

The typechecker and renamer use *exactly* the same monad, ; the
desugarer and interface-file checker use different instantiations of .
To give you the idea, here is how the monad looks: The details of the
global environment type and local environment type are also defined in
[GhcFile(compiler/typecheck/TcRnTypes.lhs)](GhcFile(compiler/typecheck/TcRnTypes.lhs) "wikilink").
Side effecting operations, such as updating the unique supply, are done
with TcRefs, which are simply a synonym for IORefs.

(NB out-of-date, but maybe historically useful; cf
\[wiki:Debugging/TickyTicky\])

Kirsten's sketchy notes on getting ticky to work
================================================

Macros for bumping ticky counters are now defined in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink").
Currently, code compiled with the flag fails to link because the macros
rely on counter variables (things with names like being declared, but
there are actually no declarations for them. I'll add those declarations
to
[GhcFile(includes/RtsExternal.h)](GhcFile(includes/RtsExternal.h) "wikilink")
so I can get something working. Really, there should be something that
automatically generates both the macros that are in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink") and the
declarations for the corresponding variables, so that they stay in sync.

Actually, maybe it would make more sense to add a new file, or
something, which contains only ticky counter declarations (the same
declarations that still exist in
[GhcFile(includes/StgTicky.h)](GhcFile(includes/StgTicky.h) "wikilink"),
which isn't used anymore), and that include that from
[GhcFile(includes/RtsExternal.h)](GhcFile(includes/RtsExternal.h) "wikilink").

No -- put actual declarations for counter variables in another file, or
something, and include that only from
[GhcFile(rts/Ticky.c)](GhcFile(rts/Ticky.c) "wikilink"); put *extern*
declarations for those counters in , still included from
[GhcFile(includes/RtsExternal.h)](GhcFile(includes/RtsExternal.h) "wikilink").
Then later we can automatically generate both and . The reason for this
is that the ticky **macros** are all over the place and they refer to
the ticky counters, so the ticky counters have to be **declared**
someplace that everyone includes, but of course the actual
initializations only need to happen in one place. (Maybe there's a
better way to do this...)

No, there don't need to be two files; I was confused. Just .

Huh - we define ticky macros now in but we can only include that in CMM
files and some C files, like , use ticky macros. This makes my brain
hurt a little. ''' Index by Title ''' | ''' \[RecentChanges Index by
Date\] '''

[TitleIndex(format=group,min=4)](TitleIndex(format=group,min=4) "wikilink")

The GHC Commentary: Checking Types
==================================

Probably the most important phase in the frontend is the type checker,
which is located at
[GhcFile(compiler/typecheck/)](GhcFile(compiler/typecheck/) "wikilink").
GHC type checks programs in their original Haskell form before the
desugarer converts them into Core code. This complicates the type
checker as it has to handle the much more verbose Haskell AST, but it
improves error messages, as those message are based on the same
structure that the user sees.

GHC defines the abstract syntax of Haskell programs in
[GhcModule(compiler/hsSyn/HsSyn.lhs)](GhcModule(compiler/hsSyn/HsSyn.lhs) "wikilink")
using a structure that abstracts over the concrete representation of
bound occurences of identifiers and patterns. The module
[GhcModule(compiler/typecheck/TcHsSyn.lhs)](GhcModule(compiler/typecheck/TcHsSyn.lhs) "wikilink")
defines a number of helper function required by the type checker. Note
that the type
[GhcModule(compiler/typecheck/TcRnTypes.lhs)](GhcModule(compiler/typecheck/TcRnTypes.lhs) "wikilink").\`TcId\`
used to represent identifiers in some signatures during type checking
is, in fact, nothing but a synonym for a
\[wiki:Commentary/Compiler/EntityTypes\#Typevariablesandtermvariables
plain Id\].

It is also noteworthy, that the representations of types changes during
type checking from \`HsType\` to \`TypeRep.Type\`. The latter is a
\[wiki:Commentary/Compiler/TypeType hybrid type\] representation that is
used to type Core, but still contains sufficient information to recover
source types. In particular, the type checker maintains and compares
types in their \`Type\` form.

The Overall Flow of Things
--------------------------

`` * `TcRnDriver` is the top level.  It calls ``\
``   * `TcTyClsDecls`: type and class declaration ``\
``   * `TcInstDcls`: instance declarations ``\
``   * `TcBinds`: value bindings ``\
``     * `TcExpr`: expressions ``\
``     * `TcMatches`: lambda, case, list comprehensions ``\
``     * `TcPat`: patterns ``\
``   * `TcForeign`: FFI declarations ``\
``   * `TcRules`: rewrite rules ``\
``   * `TcHsTypes`: kind-checking type signatures ``\
``   * `TcValidity`: a second pass that walks over things like types or type constructors, checking a number of extra side conditions. ``

`* The constraint solver consists of:`\
``   * `TcSimplify`: top level of the constraint solver ``\
``   * `TcCanonical`: canonicalising constraints ``\
``   * `TcInteract`: solving constraints where they interact with each other ``\
``   * `TcTypeNats`: solving natural-number constraints ``\
``   * `TcSMonad`: the monad of the constraint solver (built on top of the main typechecker monad) ``\
``   * `TcEvidence`: the data types used for evidence (mostly pure) ``\
``   * `TcUnify`: solves unification constraints "on the fly"; if it can't, it generates a constraint for the constraint solver to deal with later ``\
``   * `TcErrors`: generates good error messages from the residual, unsolved constraints. ``[`BR`](BR "wikilink")\
`The best place reading for the constraint solver is the paper `[`Modular`
`type` `inference` `with` `local`
`assumptions`](http://www.haskell.org/haskellwiki/Simonpj/Talk:OutsideIn)

`* Underlying infrastructure:`\
``   * `TcRnTypes`: a big collection of the types used during type checking ``\
`  * [wiki:Commentary/Compiler/TcRnMonad TcRnMonad]: the main typechecker monad`\
``   * `TcType`: pure functions over types, used by the type checker ``\
`  `

### Entry Points Into the Type Checker

The interface of the type checker (and
\[wiki:Commentary/Compiler/Renamer renamer\]) to the rest of the
compiler is provided by
[GhcModule(compiler/typecheck/TcRnDriver.lhs)](GhcModule(compiler/typecheck/TcRnDriver.lhs) "wikilink").
Entire modules are processed by calling \`tcRnModule\` and GHCi uses
\`tcRnStmt\`, \`tcRnExpr\`, and \`tcRnType\` to typecheck statements and
expressions, and to kind check types, respectively. Moreover,
\`tcTopSrcDecls\` is used by Template Haskell - more specifically by
\`TcSplice.tc\_bracket\` - to type check the contents of declaration
brackets.

### Renaming and Type Checking a Module

The functions \`tcRnModule\` and \`tcRnModuleTcRnM\` control the
complete static analysis of a Haskell module. They set up the combined
renamer and type checker monad, resolve all import statements, take care
of hi-boot files, initiate the actual renaming and type checking
process, and finally, wrap off by processing the export list.

The actual type checking and renaming process is initiated via
\`TcRnDriver.tcRnSrcDecls\`, which uses a helper called
\`tc\_rn\_src\_decls\` to implement the iterative renaming and type
checking process required by [Template
Haskell](http://darcs.haskell.org/ghc/docs/comm/exts/th.html) (TODO:
Point at new commentary equivalent). After it invokes
\`tc\_rn\_src\_decls\`, it simplifies type constraints and zonking (see
below regarding the later).

The function \`tc\_rn\_src\_decls\` partitions static analysis of a
whole module into multiple rounds, where the initial round is followed
by an additional one for each toplevel splice. It collects all
declarations up to the next splice into an \`HsDecl.HsGroup\`. To rename
and type check that declaration group it calls
\`TcRnDriver.rnTopSrcDecls\` and \`TcRnDriver.tcTopSrcDecls\`.
Afterwards, it executes the splice (if there are any left) and proceeds
to the next group, which includes the declarations produced by the
splice.

The renamer, apart from renaming, computes the global type checking
environment, of type \`TcRnTypes.TcGblEnv\`, which is stored in the
\[wiki:Commentary/Compiler/TcRnMonad type checking monad\] before type
checking commences.

Type Checking a Declaration Group
---------------------------------

The type checking of a declaration group, performed by \`tcTopSrcDecls\`
and its helper function \`tcTyClsInstDecls\`, starts by processing of
the type and class declarations of the current module, using the
function \`TcTyClsDecls.tcTyAndClassDecls\`. This is followed by a first
round over instance declarations using \`TcInstDcls.tcInstDecls1\`,
which in particular generates all additional bindings due to the
deriving process. Then come foreign import declarations
(\`TcForeign.tcForeignImports\`) and default declarations
(\`TcDefaults.tcDefaults\`).

Now, finally, toplevel value declarations (including derived ones) are
type checked using \`TcBinds.tcTopBinds\`. Afterwards,
\`TcInstDcls.tcInstDecls2\` traverses instances for the second time.
Type checking concludes with processing foreign exports
(\`TcForeign.tcForeignExports\`) and rewrite rules
(\`TcRules.tcRules\`). Finally, the global environment is extended with
the new bindings.

Type checking Type and Class Declarations
-----------------------------------------

Type and class declarations are type checked in a couple of phases that
contain recursive dependencies - aka *knots*. The first knot encompasses
almost the whole type checking of these declarations and forms the main
piece of \`TcTyClsDecls.tcTyAndClassDecls\`.

Inside this big knot, the first main operation is kind checking, which
again involves a knot. It is implemented by \`kcTyClDecls\`, which
performs kind checking of potentially recursively-dependent type and
class declarations using kind variables for initially unknown kinds.
During processing the individual declarations some of these variables
will be instantiated depending on the context; the rest gets by default
kind \* (during *zonking* of the kind signatures). Type synonyms are
treated specially in this process, because they can have an unboxed
type, but they cannot be recursive. Hence, their kinds are inferred in
dependency order. Moreover, in contrast to class declarations and other
type declarations, synonyms are not entered into the global environment
as a global \`TyThing\`. (\`TypeRep.TyThing\` is a sum type that
combines the various flavours of typish entities, such that they can be
stuck into type environments and similar.)

More Details
------------

### Types Variables and Zonking

During type checking type variables are represented by mutable variables
- cf. the [variable
story](http://darcs.haskell.org/ghc/docs/comm/the-beast/vars.html#TyVar)
(TODO: Point at new commentary equivalent). Consequently, unification
can instantiate type variables by updating those mutable variables. This
process of instantiation is (for reasons that elude me) called
[zonking](http://dictionary.reference.com/browse/zonk) in GHC's sources.
The zonking routines for the various forms of Haskell constructs are
responsible for most of the code in the module
[GhcModule(compiler/typecheck/TcHsSyn.lhs)](GhcModule(compiler/typecheck/TcHsSyn.lhs) "wikilink"),
whereas the routines that actually operate on mutable types are defined
in
[GhcModule(compiler/typecheck/TcMType.lhs)](GhcModule(compiler/typecheck/TcMType.lhs) "wikilink");
this includes the zonking of type variables and type terms, routines to
create mutable structures and update them as well as routines that check
constraints, such as that type variables in function signatures have not
been instantiated during type checking. The actual type unification
routine is \`uTys\` in the module
[GhcModule(compiler/typecheck/TcUnify.lhs)](GhcModule(compiler/typecheck/TcUnify.lhs) "wikilink").

All type variables that may be instantiated (those in signatures may
not), but haven't been instantiated during type checking, are zonked to
\`()\`, so that after type checking all mutable variables have been
eliminated.

### Type Representation

The representation of types is fixed in the module
[GhcModule(compiler/types/TypeRep.lhs)](GhcModule(compiler/types/TypeRep.lhs) "wikilink")
and exported as the data type \`Type\`. Read the comments in the
\`TypeRep\` module! A couple of points:

`` * Type synonym applications are represented as a `TyConApp` with a `TyCon` that contains the expansion.  The expansion is done on-demand by `Type.coreView`.  Unexpanded type synonyms are useful for generating comprehensible error messages. ``

`` * The `PredTy` constructor wraps a type constraint argument (dictionary, implicit parameter, or equality).  They are expanded on-demand by `coreView`. ``

As explained in
[GhcModule(compiler/typecheck/TcType.lhs)](GhcModule(compiler/typecheck/TcType.lhs) "wikilink"),
GHC supports rank-N types, but during type inference maintains the
restriction that type variables cannot be instantiated to quantified
types (i.e., the type system is predicative). However the type system of
Core is fully impredicative.

### Type Checking Environment

During type checking, GHC maintains a *type environment* whose type
definitions are fixed in the module
[GhcModule(compiler/typecheck/TcRnTypes.lhs)](GhcModule(compiler/typecheck/TcRnTypes.lhs) "wikilink")
with the operations defined in
[GhcModule(compiler/typecheck/TcEnv.lhs)](GhcModule(compiler/typecheck/TcEnv.lhs) "wikilink").
Among other things, the environment contains all imported and local
instances as well as a list of *global* entities (imported and local
types and classes together with imported identifiers) and *local*
entities (locally defined identifiers). This environment is threaded
through the \[wiki:Commentary/Compiler/TcRnMonad type checking monad\].

### Expressions

Expressions are type checked by
[GhcModule(compiler/typecheck/TcExpr)](GhcModule(compiler/typecheck/TcExpr) "wikilink").

Usage occurences of identifiers are processed by the function tcId whose
main purpose is to \[\#HandlingofDictionariesandMethodInstances
instantiate overloaded identifiers\]. It essentially calls
\`TcInst.instOverloadedFun\` once for each universally quantified set of
type constraints. It should be noted that overloaded identifiers are
replaced by new names that are first defined in the LIE (Local Instance
Environment?) and later promoted into top-level bindings.

### Handling of Dictionaries and Method Instances

GHC implements overloading using so-called *dictionaries*. A dictionary
is a tuple of functions -- one function for each method in the class of
which the dictionary implements an instance. During type checking, GHC
replaces each type constraint of a function with one additional
argument. At runtime, the extended function gets passed a matching class
dictionary by way of these additional arguments. Whenever the function
needs to call a method of such a class, it simply extracts it from the
dictionary.

This sounds simple enough; however, the actual implementation is a bit
more tricky as it wants to keep track of all the instances at which
overloaded functions are used in a module. This information is useful to
optimise the code. The implementation is the module
[GhcModule(compiler/typecheck/Inst.lhs)](GhcModule(compiler/typecheck/Inst.lhs) "wikilink").

The function \`instOverloadedFun\` is invoked for each overloaded usage
occurrence of an identifier, where overloaded means that the type of the
identifier contains a non-trivial type constraint. It proceeds in two
steps: (1) Allocation of a method instance (\`newMethodWithGivenTy\`)
and (2) instantiation of functional dependencies. The former implies
allocating a new unique identifier, which replaces the original
(overloaded) identifier at the currently type-checked usage occurrence.

The new identifier (after being threaded through the LIE) eventually
will be bound by a top-level binding whose rhs contains a partial
application of the original overloaded identifier. This papp applies the
overloaded function to the dictionaries needed for the current instance.
In GHC lingo, this is called a *method*. Before becoming a top-level
binding, the method is first represented as a value of type Inst.Inst,
which makes it easy to fold multiple instances of the same identifier at
the same types into one global definition. (And probably other things,
too, which I haven't investigated yet.)

**Note:** As of 13 January 2001 (wrt. to the code in the CVS HEAD), the
above mechanism interferes badly with RULES pragmas defined over
overloaded functions. During instantiation, a new name is created for an
overloaded function partially applied to the dictionaries needed in a
usage position of that function. As the rewrite rule, however, mentions
the original overloaded name, it won't fire anymore -- unless later
phases remove the intermediate definition again. The latest CVS version
of GHC has an option '-fno-method-sharing', which avoids sharing
instantiation stubs. This is usually/often/sometimes sufficient to make
the rules fire again.

Connection with GHC's Constraint Solver
---------------------------------------

The solver for the type nats is implemented as an extra stage in GHC's
constrraint solver (see \`TcInteract.thePipeline\`).

The following modules contain most of the code relevant for the solver:

``  * `TcTypeNats`:      The main solver machinery       ``\
``  * `TcTypeNatsRules`: The rules used by the solver ``\
``  * `TcTYpeNatsEval`:  Functions for direct evaluation on constants ``

Generating Evidence
-------------------

The solver produces evidence (i.e., proofs) when computing new "given"
constraints, or when solving existing "wanted" constraints. The evidence
is constructed by applications of a set of pre-defined rules. The rules
are values of type \`TypeRep.CoAxiomRule\`. Conceptually, rules have the
form: The rules have the usual logical meaning: the variables are
universally quantified, and the assumptions imply the concluson. As a
concrete example, consider the rule for left-cancellation of addtion:

The type \`CoAxiomRule\` also supports infinte literal-indexed families
of simple axioms using constructor \`CoAxiomTyLit\`. These have the
form: In this case \`conclusion\` is an equation that contains no type
variables but may depend on the literals in the name of the family. For
example, the basic definitional axiom for addition,
\`TcTypeNatsRules.axAddDef\`, uses this mechanism: At present, the
assumptions and conclusion of all rules are equations between types but
this restriction is not important and could be lifted in the future.

The rules used by the solver are in module \`TcTypeNatsRules\`.

The Solver
----------

The entry point to the solver is \`TcTypeNats.typeNatStage\`.

We start by examining the constraint to see if it is obviously
unsolvable (using function \`impossible\`), and if so we stash it in the
constraint-solver's state and stop. Note that there is no assumption
that \`impossible\` is complete, but it is important that it is sound,
so if \`impossible\` returns \`True\`, then the constraint is definitely
unsolvable, but if \`impossible\` returns \`False\`, then we don't know
if the constraint is solvable or not.

The rest of the stage proceeds depending on the type of constraint, as
follows.

### Given Constraints

Given constraints correspond to adding new assumptions that may be used
by the solver. We start by checking if the new constraint is trivial
(using function \`solve\`). A constraint is considered to be trivial if
it matches an already existing constraint or a rule that is known to the
solver. Such given constraints are ignored because they do not
contribute new information. If the new given is non-trivial, then it
will be recorded to the inert set as a new fact, and we proceed to
"interact" it with existing givens, in the hope of computing additional
useful facts (function \`computeNewGivenWork\`).

IMPORTANT: We assume that "given" constraints are processed before
"wanted" ones. A new given constraint may be used to solve any existing
wanted, so every time we added a new given to the inert set we should
move all potentially solvable "wanted" constraint from the inert set
back to the work queue. We DON'T do this, because it is quite
inefficient: there is no obvious way to compute which "wanted"s might be
affected, so we have to restart all of them!

The heart of the interaction is the function \`interactCt\`, which
performs one step of "forward" reasoning. The idea is to compute new
constraints whose proofs are made by an application of a rule to the new
given, and some existing givens. These new constraints are added as new
work, to be processed further on the next iteration of GHC's constraint
solver.

Aside: when we compute the new facts, we check to see if any are obvious
contradictions. This is not strictly necessary because they would be
detected on the next iteration of the solver. However, by doing the
check early we get slightly better error messages because we can report
the original constraint as being unsolvable (it leads to a
contradiction), which tends to be easier to relate to the original
program. Of course, this is not completely fool-proof---it is still
possible that a contradiction is detected at a later iteration. An
alternative idea---not yet implemented---would be to examine the proof
of a contradiction and extract the original constraints that lead to it
in the first place.

### Derived Constraints

\`\`Derived\`\` constraints are facts that are implied by the
constraints in the inert set. They do not have complete proofs because
they may depend on proofs of as yet unsolved wanted constraints. GHC
does not associate any proof terms with derived constraints (to keep
things simple?). In the constraint solver, they are mostly used as
"hints". For example, consider the wanted constraint , where is a free
unification variable. These are the steps we'll take to solve the
constraint:

The type-nat solver processes derived constraints in a similar fashion
to given constraints (\`computeNewDerivedWork\`): it checks to see if
they are trivially known and, if not, then it tries to generate some
additional derived constraints. The main difference is that derived
constraints can be interacted with all existing constraints to produce
new facts, while given constraints only interact with other givens.

### Wanted Constraints

The main purpose of the solver is to discharge \`\`wanted\`\`
constraints (the purpose of processing given and derived constraints is
to help solve existing wanted goals). When we encounter a new wanted
goals we proceed as follows:

`   1. Try to solve the goal, using a few different strategies:`\
``        1. Try to see if it matches the conclusion of an iff rule (`solveIff`). Aassumptions of rule become new wanted work. ``\
``        2. Try to see if it matches an axiom exactly (`solve`) ``\
``        3. Try the ordering solver for `<=` goals (`solveLeq`) ``\
`       4. Try to use a (possibly synthesized) assumption`

`   2. If that didn't work:`\
`     1. Wanted is added to the inert set`\
``      2. Check to see if any of the existing wanteds in the inert set can be solved in terms of the new goal (`reExamineWanteds`) ``\
`     3. Generate new derived facts.`

#### Using IFF Rules

These rules are used to replace a wanted constraint with a collection of
logically equivalent wanted constraints. If a wanted constraint matches
the head of one of these rules, than it is solved using the rules, and
the we generate new wanted constraints for the rule's assumptions.

The following are important properties of IFF rules:

` * They need to be sound (of course!)`\
` * The assumptions need to be logically equivalent to the conclusion (i.e., they should not result in a harder problem to solve than the original goal).`\
` * The assumptions need to be `*`simpler`*` from the point of view of the constraint solver (i.e., we shouldn't end up with the original goal after some steps---this would lead to non-termination).`

At present, IFF rules are used to define certain operators in terms of
others. For example, this is the only rule for solving constraints about
subtraction:

#### Using Axioms

Basic operators are defined with an infinite family of axiom schemes. As
we can't have these written as a long list (searching might never
stop!), we have some custom code that checks to see if a constraint
might be solvable using one of the definitional axioms (see
\`solveWithAxiom\`, \`byAxiom\`).

#### Using the Order Model

Constraints about the ordering of type-level numbers are kept in a
datastructure (\`LeqFacts\`) which forms a \`\`model'' of the
information represented by the constraints (in a similar fashion to how
substitutions form a model for a set of equations).

The purpose of the model is to eliminate redundant constraints, and to
make it easy to find proofs for queries of the form \`x &lt;= y\`. In
practise, of particular interest are questions such as \`1 &lt;= x\`
because these appear as assumptions on a number of rules (e.g.,
cancellation of multiplication). In the future, this model could also be
used to implement an interval analysis, which would compute intervals
approximating the values of variables.

TODO: At present, this model is reconstructed every time it needs to be
used, which is a bit inefficient. Perhaps it'd be better to use this
directly as the representation of \`&lt;=\` constraints in the inert
set.

The model is a directed acyclic graph, as follows:

``  * vertices: constants or variables (of kind `Nat`) ``\
``  * edges: the edge from `A` to `B` is a proof that `A <= B`. ``

So, to find a proof of \`A &lt;= B\`, we insert \`A\` and \`B\` in the
model, and then look for a path from \`A\` to \`B\`. The proofs on the
path can be composed using the rule for transitivity of \`&lt;=\` to
form the final proof.

When manipulating the model, we maintain the following "minimality"
invariant: there should be no direct edge between two vertices \`A\` and
\`B\`, if there is a path that can already get us from \`A\` to \`B.
Here are some examples (with edges pointing upwards)

The purpose of the invariant is to eliminate redundant information.
Note, however, that it does not guarantee that there is a unique way to
prove a goal.

#### Using Extended Assumptions

Another way to prove a goal is to look it up in the assumptions. If the
goal matched an assumption exactly, then GHC would have already solved
it in one of its previous stages of the constraint solver. However, due
to the commutativity and associativity of some of the operators, it is
possible to have goal that could be solved by assumption, only if the
assumption was "massaged" a bit.

This "massaging" is implemented by the function \`widenAsmps\`, which
extends the set of assumption by performing a bit of forward reasoning
using a limited set of rules. Typically, these are commutativity an
associativity rules, and the \`widenAsmps\` function tries to complete
the set of assumptions with respect to these operations. For example:

Note that the extended assumptions are very similar to derived
constraints, except that we keep their proofs.

#### Re-examining Wanteds

If none of the strategies for solving a wanted constraint worked, then
the constraint is added to the inert set. Since we'd like to keep the
inert set minimal, we have to see if any of the existing wanted
constraints might be solvable in terms of the new wanted
(\`reExamineWanteds\`).

It is good to keep the inert set minimal for the following reasons:

` * Inferred types are nicer,`\
` * It helps GHC to solve constraints by "inlining" (e.g., if we`\
``    have only a single constraint `x + y ~ z`, then we can eliminate it ``\
``    by replacing all occurrences of `z` with `x + y`, however we can't ``\
``    do that if we ended up with two constraints `(x + y ~ z, y + x ~ z)). ``

We consider each (numeric) wanted constraint in the inert set and check
if we can solve it in terms of the new wanted and all other wanteds. If
so, then it is removed from the inert set, otherwise it stays there.

Note that we can't implement this by kicking out the existing wanted
constraints and putting them back on the work queue, because this would
lead to non-termination. Here is an example of how this might happen:

Perhaps there is a way around this but, for the moment, we just
re-examine the numeric wanteds locally, without going through the
constraint solver pipe-line.

[PageOutline](PageOutline "wikilink")

The data type  and its friends
=============================

GHC compiles a typed programming language, and GHC's intermediate
language is explicitly typed. So the data type that GHC uses to
represent types is of central importance.

The single data type is used to represent

`` * Types (possibly of higher kind); e.g. `[Int]`, `Maybe` ``\
`` * Kinds (which classify types and coercions); e.g. `(* -> *)`, `T :=: [Int]`.  See [wiki:Commentary/Compiler/Kinds] ``\
`` * Sorts (which classify types); e.g. `TY`, `CO` ``

GHC's use of \[wiki:Commentary/Compiler/FC coercions and equality
constraints\] is important enough to deserve its own page.

The module exposes the representation because a few other modules (, , ,
etc) work directly on its representation. However, you should not
lightly pattern-match on ; it is meant to be an abstract type. Instead,
try to use functions defined by , etc.

Views of types
--------------

Even when considering only types (not kinds, sorts, coercions) you need
to know that GHC uses a *single* data type for types. You can look at
the same type in different ways:

`* The "typechecker view" regards the type as a Haskell type, complete with implicit parameters, class constraints, and the like.  For example:`

`` Functions in `TcType` take this view of types; e.g. `tcSplitSigmaTy` splits up a type into its forall'd type variables, its constraints, and the rest. ``

`* The "core view" regards the type as a Core-language type, where class and implicit parameter constraints are treated as function arguments:`

`` Functions in `Type` take this view. ``

The data type \`Type\` represents type synonym applications in
un-expanded form. E.g. Here \`f\`'s type doesn't look like a function
type, but it really is. The function \`Type.coreView :: Type -&gt; Maybe
Type\` takes a type and, if it's a type synonym application, it expands
the synonym and returns \`Just <expanded-type>\`. Otherwise it returns
\`Nothing\`.

Now, other functions use \`coreView\` to expand where necessary, thus:
Notice the first line, which uses the view, and recurses when the view
'fires'. Since \`coreView\` is non-recursive, GHC will inline it, and
the optimiser will ultimately produce something like:

The representation of 
----------------------

Here, then is the representation of types (see
[GhcFile(compiler/types/TypeRep.hs)](GhcFile(compiler/types/TypeRep.hs) "wikilink")
for more details):

Invariant: if the head of a type application is a , GHC *always* uses
the constructor, not . This invariant is maintained internally by 'smart
constructors'. A similar invariant applies to ; is never used with an
arrow type.

Type variables are represented by the \`TyVar\` constructor of the
\[wiki:Commentary/Compiler/EntityTypes data type Var\].

Overloaded types
----------------

In Haskell we write but in Core the \`=&gt;\` is represented by an
ordinary \`FunTy\`. So f's type looks like this: Nevertheless, we can
tell when a function argument is actually a predicate (and hence should
be displayed with \`=&gt;\`, etc), using The various forms of predicate
can be extracted thus: These functions are defined in module \`Type\`.

Classifying types
-----------------

GHC uses the following nomenclature for types:

**`Unboxed`**`:: A type is unboxed iff its representation is other than a pointer. Unboxed types are also unlifted.`

**`Lifted`**`:: A type is lifted iff it has bottom as an element. Closures always have lifted types:  i.e. any let-bound identifier in Core must have a lifted type.  Operationally, a lifted object is one that can be entered. Only lifted types may be unified with a type variable.`

**`Data`**`:: A type declared with `****`.  Also boxed tuples.`

**`Algebraic`**`:: An algebraic data type is a data type with one or more constructors, whether declared with `` or ``.   An algebraic type is one that can be deconstructed with a case expression.  "Algebraic" is `**`NOT`**` the same as "lifted",  because unboxed (and thus unlifted) tuples count as "algebraic".`

**`Primitive`**`:: a type is primitive iff it is a built-in type that can't be expressed    in Haskell.`\
` `\
` Currently, all primitive types are unlifted, but that's not necessarily the case.  (E.g. Int could be primitive.)`

``  Some primitive types are unboxed, such as Int#, whereas some are boxed but unlifted (such as `ByteArray#`).  The only primitive types that we classify as algebraic are the unboxed tuples. ``

Examples of type classifications:

|| || **Primitive** || **Boxed** || **Lifted** || **Algebraic** || ||
\`Int\#\` || Yes || No || No || No || || \`ByteArray\#\` || Yes || Yes
|| No || No || || \`(\# a, b \#)\` || Yes || No || No || Yes || || \`(
a, b )\` || No || Yes || Yes || Yes || || \`\[a\]\` || No || Yes || Yes
|| Yes ||

Unique
------

\`Unique\`s provide a fast comparison mechanism for more complex things.
Every \`RdrName\`, \`Name\`, \`Var\`, \`TyCon\`, \`TyVar\`, etc. has a
\`Unique\`. When these more complex structures are collected (in
\`UniqFM\`s or other types of collection), their \`Unique\` typically
provides the key by which the collection is indexed.

------------------------------------------------------------------------

Current design
--------------

A \`Unique\` consists of the *domain* of the thing it identifies and a
unique integer value 'within' that domain. The two are packed into a
single \`Int\#\`, with the *domain* being the top 8 bits.

The domain is never inspected (SLPJ believes). The sole reason for its
existence is to provide a number of different ranges of \`Unique\`
values that are guaranteed not to conflict.

=== Lifetime

The lifetime of a \`Unique\` is a single invocation of GHC, i.e. they
must not 'leak' to compiler output, the reason being that \`Unique\`s
may be generated/assigned non-deterministically. When compiler output is
non-deterministic, it becomes significantly harder to, for example,
\[wiki:Commentary/Compiler/RecompilationAvoidance avoid recompilation\].
Uniques do not get serialised into .hi files, for example.

Note, that "one compiler invocation" is not the same as the compilation
of a single \`Module\`. Invocations such as \`ghc --make\` or \`ghc
--interactive\` give rise to longer invocation life-times.

This is also the reasons why \`OccName\`s are *not* ordered based on the
\`Unique\`s of their underlying \`FastString\`s, but rather
*lexicographically* (see
[GhcFile(compiler/basicTypes/OccName.lhs)](GhcFile(compiler/basicTypes/OccName.lhs) "wikilink")
for details). &gt; &gt; **SLPJ:** I am far from sure that the Ord
instance for \`OccName\` is ever used, so this remark is probably
misleading. Try deleting it and see where it is used (if at all). &gt;
**PKFH:** At least \`Name\` and \`RdrName\` (partially) define their own
\`Ord\` instances in terms of the instance of \`OccName\`. Maybe these
\`Ord\` instances are also redundant, but for now it seems wise to keep
them in. When everything has \`Data\` instances (after this and many
other redesigns), I'm sure it will be easier to find such dependency
relations.

### Known-key things

A hundred or two library entities (types, classes, functions) are
so-called "known-key things". See \[wiki:Commentary/Compiler/WiredIn
this page\]. A known-key thing has a fixed \`Unique\` that is fixed when
the compiler is built, and thus lives across all invocations of that
compiler. These known-key \`Unique\`s *are* written into .hi files. But
that's ok because they are fully deterministic and never change.

&gt; **PKFH** That's fine then; we also know for sure these things fit
in the 30 bits used in the \`hi\`-files. I'll comment appropriately.

### Interface files

Entities in a interface file (.hi file) are, for the most part, stored
in a symbol table, and referred to (from elsewhere in the same interface
file) by an index into that table. Here are the details from
[GhcFile(compiler/iface/BinIface.lhs)](GhcFile(compiler/iface/BinIface.lhs) "wikilink"):

------------------------------------------------------------------------

Redesign (2014)
---------------

=== TL;DR The redesign is to accomplish the following:

`` * Allow derivation of type class instances for `Unique` ``\
`* Restore invariants from the original design; hide representation details`\
`` * Eliminate violations of invariants and design-violations in other places of the compiler (e.g. `Unique`s shouldn't be written to `hi`-files, but are). ``

&gt; &gt; **SLPJ** I don't think this is a design violation; see above.
Do you have any other examples in mind? &gt; **PKFH** Not really of
design-violations (and no other compiler-output stuff) other than the
invariants mentioned above it, just yet. The key point, though, is that
there are a lot of comments in \`Unique\` about not exporting things so
that we know X, Y and Z, but then those things *are* exported, so we
don't know them to be true. Case in point is the export of \`mkUnique\`,
but also \`mkUniqueGrimily\`. The latter has a comment 'only for
\`UniqSupply\`' but is also used in other places (like Template
Haskell). One redesign is to put this restriction in the name, so there
still is the facility offered by \`mkUniqueGrimily\`, but now it's
called \`mkUniqueOnlyForUniqSupply\` (and
\`mkUniqueOnlyForTemplateHaskell\`), the ugliness of which should help,
over time, to get rid of them.

=== Longer

In an attempt to give more of GHC's innards well-behaved instances of
\`Typeable\`, \`Data\`, \`Foldable\`, \`Traversable\`, etc. the
implementation of \`Unique\`s was a bit of a sore spot. They were
implemented (20+ years earlier) using custom boxing, viz. making
automatic derivation of such type class instances hard. There was
already a comment asking why it wasn't simply a \`newtype\` around a
normal (boxed) \`Int\`. Independently, there was some discussion on the
mailinglists about the use of (signed) \`Int\`s in places where
\`Word\`s would be more appropriate. Further inspection of the
\`Unique\` implementation made clear that a lot of invariants mentioned
in comments had been violated by incremental edits. This is discussed in
more detail below, but these things together (the desire for automatic
derivation and the restoration of some important invariants) motivated a
moderate redesign.

=== Status Quo (pre redesign)

A \`Unique\` has a domain (\`TyCon\`, \`DataCon\`, \`PrelName\`,
\`Builtin\`, etc.) that was codified by a character. The remainder of
the \`Unique\` was an integer that should be unique for said domain.
This **was** once guaranteed through the export list of
[GhcFile(compiler/basicTypes/Unique.lhs)](GhcFile(compiler/basicTypes/Unique.lhs) "wikilink"),
where direct access to the domain-character was hidden, i.e. were not
exported. This should have guaranteed that every domain was assigned its
own unique character, because only in
[GhcFile(compiler/basicTypes/Unique.lhs)](GhcFile(compiler/basicTypes/Unique.lhs) "wikilink")
could those \`Char\`s be assigned. However, through this separation of
concerns leaked out to
[GhcFile(compiler/basicTypes/UniqSupply.lhs)](GhcFile(compiler/basicTypes/UniqSupply.lhs) "wikilink"),
because its \`Int\` argument is the *entire* \`Unique\` and not just the
integer part 'under' the domain character. &gt; &gt; **SLPJ** OK, but to
eliminate \`mkUniqueGrimily\` you need to examine the calls, decide how
to do it better, and document the new design. &gt; **PKFH** See above;
the solution for now is \`mkUniqueOnlyForUniqSupply\`. A separate patch
will deal with trying to refactor/redesign \`UniqSupply\` if this is
necessary.

The function \`mkSplitUniqSupply\` made the domain-character accessible
to all the other modules, by having a wholly separate implementation of
the functionality of \`mkUnique\`.

Where the intention was still to have a clean interface, the (would-be)
hidden \`mkUnique\` is only called by functions defined in the
\`Unique\` module with the corresponding character, e.g.

=== New plan

In the new design, the domains are explicitly encoded in a sum-type
\`UniqueDomain\`. At the very least, this should help make the code a
little more self-documenting *and* prevent accidental overlap in the
choice of bits to identify the domain. Since the purpose of \`Unique\`s
is to provide *fast* comparison for different types of things, the
redesign should remain performance concious. With this in mind, keeping
the \`UniqueDomain\` and the integer-part explicitly in the type seems
unwise, but by choosing we win the ability to automatically derive
things and should also be able to test how far optimisation has come in
the past 20+ years; does default boxing with \`newtype\`-style wrapping
have (nearly) the same performance as manual unboxing? This should
follow from the tests.

The encoding is kept the same, i.e. the \`Word\` is still built up with
the domain encoded in the most significant bits and the integer-part in
the remaining bits. However, instead encoding the domain as a \`Char\`
in the (internal *and* external interface), we now create an ADT
(sum-type) that encodes the domain. This has two advantages. First, it
prevents people from picking domain-tags ad hoc an possibly overlapping.
Second, encoding in the \`Word\` does not rely on the assumption that
the domain requires and/or fits in 8 bits. Since Haskell \`Char\`s are
unicode, the 8-bit assumption is wrong for the old design. In other
words, the above examples are changed to:

Ideal world scenario, the entire external interface would be: and the
instances for \`Eq\`, \`Ord\`, \`Data\`, etc. For now, though, it will
also have

&gt; &gt; **SLPJ** I agree that a \`newtype\` around a \`Word\` is
better than a \`data\` type around \`Int\#\`. That is a small, simple
change. But I think you plan to do more than this, and that "more" is
not documented here. E.g. what is the new API to \`Unique\`? &gt;
**PKFH** Added. See above.

Unpacking primitive fields
==========================

This page describes a proposal to automatically unpack (strict)
primitive fields. A primitive fields is a field that when unpacked has a
pointer-sized representation. Examples include \`Int\`, \`Word\`,
\`Float\`, and \`newtype\`s thereof.

Goals and non-goals
-------------------

This proposal is about changing the default behavior of GHC, not
changing expressiveness. Users can still use \`UNPACK\` and \`NOUNPACK\`
to explicitly control the memory representation of fields.

There are two goals:

`1. Reduce the amount of boilerplate experienced programmers have to write: As of Feb 18th 2012, the `[`bytestring`](http://hackage.haskell.org/package/bytestring)`, `[`text`](http://hackage.haskell.org/package/text)`, and `[`containers`](http://hackage.haskell.org/package/containers)``  packages had 46 fields that matched the definition of primitive given above. 43 of these had an explicit `UNPACK` pragma (and the remaining 3 could have had one without changing the performance of the program.) ``

`` 2. To provide better defaults for beginner and intermediate level Haskellers. Not unpacking e.g. `Int` fields can have a large, negative effect on performance and many beginner and intermediate level Haskellers are bitten by this. ``

Detailed design
---------------

Benchmarks
----------

Unused imports
==============

GHC has a series of bugs related to the "report unused imports" flags,
including \#1148, \#2267, \#1074, \#2436, \#10117.

This page describes a new design.

The current story
-----------------

Currently (GHC 6.10) we report three different things:

`* warnUnusedModules: import M, where nothing is used from M`\
`* warnUnusedImports: import M(f), where f is unused, and M doesn't fall under warnUnusedModules`\
`* warnDuplicateImports: import M + import M(f), even when f is used complain about duplicate import of f`

Examples
--------

The hard bit is to specify what the warning should do. Consider these
examples, where \`Foo\` exports \`x\` and \`y\`, and \`FooPlus\`
re-exports all of \`Foo\`, plus \`z\`: Which import is redudant, in each
case?

Also: we might warn if you import the same module more than once, and
the imports can be combined (ie they have the same 'qualified' and 'as'
attributes) Here both are used, but we might want to suggest combining
them.

Specfication
------------

We can at least agree on this:

`* If the warning suggests that an import can be omitted, and you omit it,`\
`  the program should still compile.`\
`* It's not worth trying to be too subtle.  The 90% case is very simple.`

Say that an *import-item* is either an entire import-all decl (eg
\`import Foo\`), or a particular item in an import list (eg \`import
Foo( ..., x, ...)\`). The general idea is that for each use of an
imported name, we will attribute that use to one (or possibly more)
import-items. Then, any import items with no uses attributed to them are
unused, and are warned about. More precisely:

`` 1.  For every `RdrName` in the program text, find all the import-items that brought it     into scope.  The lookup mechanism on `RdrNames` already takes account of whether the `RdrName` was qualified, and which imports have the right qualification etc, so this step is very easy. ``

`2. Choose one of these, the "chosen import-item", and mark it "used".  `

`3.  Now bleat about any import-items that are unused.  For a decl`\
`` `import Foo(x,y)`, if both the `x` and `y` items are unused, it'd be better ``\
`to bleant about the entire decl rather than the individual items.`

The import-item choosing step 2 implies that there is a total order on
import-items. We say import-item A \`\`dominates\`\` import-item B if we
chooose A over B. Here is one possible dominance relationship:

`` * `import Foo` dominates `import Foo(x)`.  (You could also argue that the  ``\
`  reverse should hold.)`\
`* Otherwise choose the textually first one.`

Other notes:

`* The algorithm chooses exactly one import-item in step 2.  It would`\
`also be sound to choose more than one if there was a tie, but then completely-duplicate`\
`imports might not be reported.`

`` * Note that if we have an import item `import Foo (Bar(bar))`, then ``\
`` it's marked as used if either `Bar` or `bar` are used.  We could have yet finer ``\
`resolution and report even unused sub-items.`

`` * We should retain the special case of not warning about `import Foo ()`, which implies "instance declarations only". ``

------------------------------------------------------------------------

Implementation
--------------

We want to collect the set of all \`RdrNames\` that are mentioned in the
program. We must collect **\`RdrNames\`** not \`Names\`: Here both
imports are required, but you can only tell that by seeing the RdrNames,
not by knowing that the name 'x' is used.

I think that all lookups go through either, \`RnEnv.lookupGreRn\_maybe\`
or \`RnEnv.lookup\_sub\_bndr\`. So in \`RnEnv.lookupGreRn\_maybe\`, if
\`(gre\_prov gre)\` is \`(Imported \_)\`, and in
\`RnEnv.lookup\_sub\_bndr\`, put \`rdr\_name\` in a new in \`TcGblEnv\`.
All the \`tcg\_used\_rdrnames\` are in scope; if not, we report an error
and do not add it to \`tcg\_used\_rdrnames\`.

Other notes

``  * Any particular (in-scope) used `RdrName` is bought into scope by ``\
``  one or more `RdrName.ImportSpec`'s.  You can find these `ImportSpecs` ``\
` in the GRE returned by the lookup.`

``  * The unit of "unused import" reporting is one of these `ImportSpecs`. ``

``  * Suppose that 'rn' is a used, imported `RdrName`, and 'iss' is  ``\
``  the `[ImportSpecs]` that brought it into scope.  Then, to a first  ``\
` approximation all the iss are counted 'used'.  `

``  * We can compare `ImportSpecs` for equality by their `SrcSpans` ``

``  * In `TcRnDriver.tcRnImports`, save import_decls in a new ``\
``  `tcg_rn_rdr_imports :: Maybe [LImportDecl RdrName]` ``\
``  in `TcGblEnv` ``

------------------------------------------------------------------------

Algorithm
---------

The algorithm for deciding which imports have been used is based around
this datatype:

We convert import declarations into trees of \`ImportInfo\`s, e.g.
becomes (only the \`SDoc\` and \`\[RdrName\]\` fields are given, as
that's the interesting bit) If a node in the tree is marked as used,
then so are all nodes above it. For example, given the tree a use of
\`"D"\` marks both the first and third lines as used.

When we come to giving warnings, if a node is unused then we warn about
it, and do not descend into the rest of that subtree, as the node we
warn about subsumes its children. If the node is marked as used then we
descend, looking to see if any of its children are unused.

Here are how some example imports map to trees of \`ImportInfo\`,
assuming \`Foo\` exports \`a\`, \`b\`, \`D(c1, c2)\`.

These trees are built by \`RnNames.mkImportInfo\`. In
\`RnNames.warnUnusedImportDecls\` we make two lists of \`ImportInfo\`s;
one list contains all the explicit imports, e.g. and the other contains
the implicit imports, e.g.

Then \`RnNames.markUsages\` is called for each \`RdrName\` that was used
in the program. The current implementation marks all explicit import as
used unless there are no such imports, in which case it marks all
implicit imports as used. A small tweak to \`markUsages\` would allow it
to mark only the first import it finds as used.

As well as the \`RdrName\`s used in the source, we also need to mark as
used the names that are exported. We first call
\`RnNames.expandExports\` to expand \`D(..)\` into \`D(c1, c2)\`, and
then call \`RnNames.markExportUsages\`. Normally this just marks the
\`RdrName\`s as used in the same way that uses in the module body are
handled, but it is also possible for an entire module to be "used", if
\`module Foo\` is in the export list. In this case
\`RnNames.markModuleUsed\` does the hard work, marking every module
imported with that name as used.

Updates
=======

Source files:
[GhcFile(rts/Updates.h)](GhcFile(rts/Updates.h) "wikilink"),
[GhcFile(rts/Updates.cmm)](GhcFile(rts/Updates.cmm) "wikilink")

------------------------------------------------------------------------

CategoryStub

The user manual
===============

GHC's user manual contains documentation intended for users of GHC. They
are not interested in how GHC works; they just want to use it.

The user manual is held in
[GhcFile(docs/user\_guide)](GhcFile(docs/user_guide) "wikilink"), and is
written in !ReStructuredText format (\`.rst\` files). This allows us to
typeset it as HTML pages, or as LaTeX.

See also the \[wiki:Building/Docs notes on building the documentation\].

See the "Care and feeding of your GHC User's Guide" section for
conventions and a basic introduction to ReST.

GHC Boot Library Version History
================================

This table lists the versions of GHC against those of its boot
libraries, including most notably the \`base\` library. This may be
useful if you ever want to find out which version of the \`base\`
package was bundled with which version of GHC or vice versa.

See also: LanguagePragmaHistory, which lists the language extensions
added and/or removed in each GHC version.

|| ||= **HEAD** =||= **7.10.3** =||= **7.10.2** =||= **7.10.1** =||=
**7.8.4** =||= **7.8.3** =||= **7.8.2** =||= **7.8.1** =||= **7.6.3**
=||= **7.6.2** =||= **7.6.1** =||= **7.4.2** =||= **7.4.1** =||=
**7.2.2** =||= **7.2.1** =||= **7.0.4** =||= **7.0.3** =||= **7.0.2**
=||= **7.0.1** =|| ||=\`Cabal\` =|| 1.23.0.0 || 1.22.5.0 || 1.22.4.0 ||
1.22.2.0 || 1.18.1.5 |||||| 1.18.1.3 |||||| 1.16.0 |||| 1.14.0 ||||
1.12.0 || 1.10.2.0 |||| 1.10.1.0 || 1.10.0.0 || ||=\`Win32\` =||||||||
2.3.1.0 |||||||| 2.3.0.2 |||||| 2.3.0.0 |||| 2.2.2.0 |||| 2.2.1.0
|||||||| 2.2.0.2 || ||=\`array\` =|||||||| 0.5.1.0 |||||||| 0.5.0.0
|||||| 0.4.0.1 |||| 0.4.0.0 |||| 0.3.0.3 |||||||| 0.3.0.2 || ||=\`base\`
=|| 4.9.0.0 || 4.8.2.0 || 4.8.1.0 || 4.8.0.0 || 4.7.0.2 || 4.7.0.1 ||||
4.7.0.0 |||| 4.6.0.1 || 4.6.0.0 || 4.5.1.0 || 4.5.0.0 || 4.4.1.0 ||
4.4.0.0 |||||| 4.3.1.0 || 4.3.0.0 || ||=\`bin-package-db\` =|| *none*
|||||||||||||||||||||||||||||||||||| 0.0.0.0 || ||=\`binary\` =||
0.8.0.0 |||| 0.7.5.0 || 0.7.3.0 |||||||| 0.7.1.0 |||||| 0.5.1.1 ||||
0.5.1.0 |||| 0.5.0.2\* |||||||| *none* || ||=\`bytestring\` =|| 0.10.7.0
|||||| 0.10.6.0 |||||||| 0.10.4.0 |||| 0.10.0.2 || 0.10.0.0 |||| 0.9.2.1
|||| 0.9.2.0 |||||| 0.9.1.10 || 0.9.1.8 || ||=\`containers\` =|| 0.5.7.1
|||||| 0.5.6.2 |||||||| 0.5.5.1 |||||| 0.5.0.0 |||| 0.4.2.1 |||| 0.4.1.0
|||||||| 0.4.0.0 || ||=\`deepseq\` =|| 1.4.2.0 |||||| 1.4.1.1 ||||||||
1.3.0.2 |||||| 1.3.0.1 |||| 1.3.0.0 |||||||||||| *none* ||
||=\`directory\` =|| 1.2.5.0 |||||| 1.2.2.0 |||||||| 1.2.1.0 ||||
1.2.0.1 || 1.2.0.0 |||| 1.1.0.2 |||| 1.1.0.1 |||||||| 1.1.0.0 ||
||=\`extensible-exceptions\` =|||||||||||||||||||||| *none* |||| 0.1.1.4
|||| 0.1.1.3 |||||||| 0.1.1.2 || ||=\`ffi\` =||||||||||||||||||||||||||
*none* |||||||||||| 1.0 || ||=\`filepath\` =|| 1.4.1.0 |||||| 1.4.0.0
|||||||| 1.3.0.2 |||||| 1.3.0.1 |||| 1.3.0.0 |||| 1.2.0.1 ||||||||
1.2.0.0 || ||=\`ghc\` =|| 7.11.20151220\* || 7.10.3\* || 7.10.2\* ||
7.10.1\* || 7.8.4\* || 7.8.3\* || 7.8.2\* || 7.8.1\* || 7.6.3\* ||
7.6.2\* || 7.6.1\* || 7.4.2\* || 7.4.1\* || 7.2.2\* || 7.2.1\* ||
7.0.4\* || 7.0.3\* || 7.0.2\* || 7.0.1\* || ||=\`ghc-binary\`
=|||||||||||||||||||||||||||||| *none* |||||||| 0.5.0.2\* ||
||=\`ghc-boot\` =|| 0.0.0.0 |||||||||||||||||||||||||||||||||||| *none*
|| ||=\`ghc-prim\` =|| 0.5.0.0 |||||| 0.4.0.0 |||||||| 0.3.1.0 ||||||
0.3.0.0 |||||||||||||||| 0.2.0.0 || ||=\`ghci\` =|| 0
|||||||||||||||||||||||||||||||||||| *none* || ||=\`haskeline\` =||
0.7.2.2 |||||| 0.7.2.1 |||| 0.7.1.2 |||||||||||||||||||||||||| *none* ||
||=\`haskell2010\` =|||||||| *none* |||||||| 1.1.2.0\* |||||| 1.1.1.0\*
|||| 1.1.0.1\* |||| 1.1.0.0\* |||||||| 1.0.0.0\* || ||=\`haskell98\`
=|||||||| *none* |||||||| 2.0.0.3\* |||||| 2.0.0.2\* |||| 2.0.0.1\* ||||
2.0.0.0\* |||||| 1.1.0.1 || 1.1.0.0 || ||=\`hoopl\` =|| 3.10.2.0 ||||||
3.10.0.2 |||||||| 3.10.0.1 |||||| 3.9.0.0 |||| 3.8.7.3 |||| 3.8.7.1
|||||||| *none* || ||=\`hpc\` =|||||||| 0.6.0.2 |||||||| 0.6.0.1 ||||||
0.6.0.0 |||| 0.5.1.1 |||| 0.5.1.0 |||||||| 0.5.0.6 || ||=\`integer-gmp\`
=|||||||| 1.0.0.0 |||||||| 0.5.1.0 |||||| 0.5.0.0 |||| 0.4.0.0 ||||
0.3.0.0 |||||| 0.2.0.3 || 0.2.0.2 || ||=\`old-locale\` =|||||||| *none*
|||||||| 1.0.0.6 |||||| 1.0.0.5 |||| 1.0.0.4 |||| 1.0.0.3 ||||||||
1.0.0.2 || ||=\`old-time\` =|||||||| *none* |||||||| 1.1.0.2 ||||||
1.1.0.1 |||| 1.1.0.0 |||| 1.0.0.7 |||||||| 1.0.0.6 || ||=\`pretty\` =||
1.1.3.2 |||||| 1.1.2.0 |||||||| 1.1.1.1 |||||||||| 1.1.1.0 |||| 1.1.0.0
|||||||| 1.0.1.2 || ||=\`process\` =|| 1.4.1.0 |||||| 1.2.3.0 ||||||||
1.2.0.0 |||||| 1.1.0.2 |||| 1.1.0.1 |||| 1.1.0.0 |||||| 1.0.1.5 ||
1.0.1.4 || ||=\`random\` =|||||||||||||||||||||||||||||| *none* ||||||||
1.0.0.3 || ||=\`rts\` =|||||||||||||||||||||||||||||||||||||| 1.0 ||
||=\`template-haskell\` =|| 2.11.0.0 |||||| 2.10.0.0 |||||||| 2.9.0.0
|||||| 2.8.0.0 |||| 2.7.0.0 |||| 2.6.0.0 |||||||| 2.5.0.0 ||
||=\`terminfo\` =|| 0.4.0.2 |||||| 0.4.0.1 |||| 0.4.0.0
|||||||||||||||||||||||||| *none* || ||=\`time\` =|| 1.6 |||||| 1.5.0.1
|||||||| 1.4.2 |||||| 1.4.0.1 |||| 1.4 |||| 1.2.0.5 |||||||| 1.2.0.3 ||
||=\`transformers\` =|| 0.5.0.0 |||||| 0.4.2.0 |||||||| 0.3.0.0
|||||||||||||||||||||| *none* || ||=\`unix\` =|| 2.7.1.1 |||||| 2.7.1.0
|||||||| 2.7.0.1 |||| 2.6.0.1 || 2.6.0.0 || 2.5.1.1 || 2.5.1.0 ||||
2.5.0.0 |||||| 2.4.2.0 || 2.4.1.0 || ||=\`xhtml\` =|||||||||||| 3000.2.1
|||||||||||||||||||||||||| *none* || || ||= **HEAD** =||= **7.10.3**
=||= **7.10.2** =||= **7.10.1** =||= **7.8.4** =||= **7.8.3** =||=
**7.8.2** =||= **7.8.1** =||= **7.6.3** =||= **7.6.2** =||= **7.6.1**
=||= **7.4.2** =||= **7.4.1** =||= **7.2.2** =||= **7.2.1** =||=
**7.0.4** =||= **7.0.3** =||= **7.0.2** =||= **7.0.1** =||

Note: A \`\*\` after the version number denotes the package being hidden
by default.

A table covering some GHC 6.\* releases can be found at
<https://wiki.haskell.org/Libraries_released_with_GHC>

= Warnings and Deprecations

For now, see the relevant [GHC User's Guide
Section](http://downloads.haskell.org/~ghc/latest/docs/html/users_guide/pragmas.html#warning-deprecated-pragma)
describing the \`DEPRECATE\` and \`WARNING\` pragmas.

TODO

GHC Commentary: Weak Pointers and Finalizers
============================================

------------------------------------------------------------------------

CategoryStub [PageOutline](PageOutline "wikilink")

Work in Progress on the LLVM Backend
====================================

This page is meant to collect together information about people working
on (or interested in working on) LLVM in GHC, and the projects they are
looking at. See also the \[wiki:Commentary/Compiler/NewCodeGen state of
play of the whole back end\]. This is more a page of ideas for
improvements to the LLVM backend and less so an indication of actual
work going on.

### LLVM IR Representation

The LLVM IR is modeled in GHC using an algebraic data type to represent
the first order abstract syntax of the LLVM assembly code. The LLVM
representation lives in the 'Llvm' subdirectory and also contains code
for pretty printing. This is the same approach taken by EHC's LLVM
Back-end, and we adapted the module developed by them for this purpose.

The current design is overly complicated and could be faster. It uses
String + show operations for printing for example when it should be
using !FastString + Outputable. Before simplifying this design though it
would be good to investigate using the LLVM API instead of the assembly
language for interacting with LLVM. This would be done most likely by
using the pre-existing Haskell LLVM API bindings found
[here](http://hackage.haskell.org/package/llvm). This should hopefully
provide a speed up in compilation speeds which is greatly needed since
the LLVM back-end is \~2x slower at the moment.

### TABLES\_NEXT\_TO\_CODE

We now support
\[wiki:Commentary/Compiler/Backends/LLVM/Issues\#TABLES\_NEXT\_TO\_CODE
TNTC\] using an approach of gnu as subsections. This seems to work fine
but we would like still to move to a pure LLVM solution. Ideally we
would implement this in LLVM by allowing a global variable to be
associated with a function, so that LLVM is aware that the two will be
laid out next to each other and can better optimise (e.g using this
approach LLVM should be able to perform constant propagation on
info-tables).

**Update (30/06/2010):** The current TNTC solution doesn't work on Mac
OS X. So we need to implement an LLVM based solution. We currently
support OS X by post processing the assembly. Pure LLVM is a nicer way
forward.

### LLVM Alias Analysis Pass

**Update: This has been implemented, needs more work though**

LLVM doesn't seem to do a very good job of figuring out what can alias
what in the code generated by GHC. We should write our own alias
analysis pass to fix this.

### Optimise LLVM for the type of Code GHC produces

At the moment only a some fairly basic benchmarking has been done of the
LLVM back-end. Enough to give an indication of how it performs on the
whole (well as far as you trust benchmarks anyway) and of what it can
sometimes achieve. However this is by no means exauhstive or probably
even close to it and doesn't give us enough information about the areas
where LLVM performs badly. The LLVM optimisation pass also at the moment
just uses the standard '-O\[123\]' levels, which like GCC entail a whole
bunch of optimisation passes. These groups are designed for C programs
mostly.

So:

`* More benchmarking, particularly finding some bad spots for the LLVM back-end and generating a good picture of the characteristics of the back-end.`\
`* Look into the LLVM optimiser, e.g perhaps some more work in the style of `[`Don's`
`work`](http://donsbot.wordpress.com/2010/03/01/evolving-faster-haskell-programs-now-with-llvm/)\
`* Look at any new optimisation passes that could be written for LLVM which would help to improve the code it generates for GHC.`\
`* Look at general fixes/improvement to LLVM to improve the code it generates for LLVM.`\
`* Sometimes there is a benefit from running the LLVM optimiser twice of the code (e.g opt -O3 | opt -O3 ...). We should add a command line flag that allows you to specify the number of iterations you want the LLVM optimiser to do.`

### Update the Back-end to use the new Cmm data types / New Code Generator

There is ongoing work to produce a new, nicer, more modular code
generator for GHC (the slightly confusingly name code generator in GHC
refers to the pipeline stage where the Core IR is compiled to the Cmm
IR). The LLVM back-end could be updated to make sure it works with the
new code generator and does so in an efficient manner.

### LLVM's Link Time Optimisations

One of LLVM's big marketing features is its support for link time
optimisation. This does things such as in-lining across module
boundaries, more aggressive dead code elimination... etc). The LLVM
back-end could be updated to make use of this. Roman apparently tried to
use the new 'gold' linker with GHC and it doesn't support all the needed
features.

`* `[`22`](http://llvm.org/releases/2.6/docs/LinkTimeOptimization.html)\
`* `[`23`](http://llvm.org/docs/GoldPlugin.html)

### LLVM Cross Compiler / Port

This is more of an experimental idea but the LLVM back-end looks like it
would make a great choice for Porting LLVM. That is, instead of porting
LLVM through the usual route of via-C and then fixing up the NCG, just
try to do it all through the LLVM back-end. As LLVM is quite portable
and supported on more platforms then GHC, it would be an interesting and
valuable experiment to try to port GHC to a new platform by simply
getting the LLVM back-end working on it. (The LLVM back-end works in
both unregistered and registered mode, another advantage for porting
compared to the C and NCG back-ends).

It would also be interesting to looking into improving GHC to support
cross compiling and doing this through the LLVM back-end as it should be
easier to fix up to support this feature than the C or NCG back-ends.

### Get rid of Proc Point Splitting

When Cmm code is first generated a single Haskell function will be
mostly compiled to one Cmm function. This Cmm function isn't passed to
the backends though as the CPS style used in it requires that the
backends be able to take the address of labels in a function since
they're used as return points. The C backend can't support this. While
there is a GNU C extension allowing the address of a label to be taken,
the address can only be used locally (in the same function). So what
proc point splitting does is cut a single Cmm function into multiple top
level Cmm functions so that instead of needing to take the address of a
label, we now take the address of a function.

It would be nice to get rid of proc point splitting. This is one of the
goals for the new code generator. This will give us much bigger Cmm
functions which should give more room for LLVM to optimise. There is an
issue though that LLVM doesn't support taking the address of a local
label either. So will need to add support to LLVM for taking label
addresses or convert CPS style into something more direct if thats
possible.

### Don't Pass Around Dead STG Registers

**Update: This has been implemented**

At the moment in the LLVM backend we always pass around the pinned STG
registers as arguments for every Cmm function. A huge amount of the time
though we aren't storing anything in the STG registers, they are dead
really. If we can treat the correctly as dead then LLVM will have more
free registers and the allocator should do a better job. We need to
change the STG -&gt; Cmm code generator to attach register liveness
information at function exit points (e.g calls, jumps, returns).

e.g This [bug (\#4308)](http://hackage.haskell.org/trac/ghc/ticket/4308)
is as a result of this problem.

[PageOutline](PageOutline "wikilink")

Wired-in and known-key things
=============================

There are three categories of entities that GHC "knows about"; that is,
information about them is baked into GHC's source code.

` * [wiki:Commentary/Compiler/WiredIn#Wiredinthings Wired-in things] --- GHC knows everything about these`\
` * [wiki:Commentary/Compiler/WiredIn#Knownkeythings Known-key things] --- GHC knows the `*`name`*`, including the ``, but not the definition`\
` * [wiki:Commentary/Compiler/WiredIn#OrigRdrNamethings Orig RdrName  things] --- GHC knows which module it's defined in`

Wired-in things
---------------

A **Wired-in thing** is fully known to GHC. Most of these are \`TyCon\`s
such as \`Bool\`. It is very convenient to simply be able to refer to
\`boolTyCon :: TyCon\` without having to look it up in an environment.

All \[wiki:Commentary/Compiler/TypeType\#Classifyingtypes primitive
types\] are wired-in things, and have wired-in \`Name\`s. The primitive
types (and their \`Names\`) are all defined in
[GhcFile(compiler/prelude/TysPrim.hs)](GhcFile(compiler/prelude/TysPrim.hs) "wikilink").

The non-primitive wired-in type constructors are defined in
[GhcFile(compiler/prelude/TysWiredIn.hs)](GhcFile(compiler/prelude/TysWiredIn.hs) "wikilink").
There are a handful of wired-in \`Id\`s in
[GhcFile(compiler/basicTypes/MkId.hs)](GhcFile(compiler/basicTypes/MkId.hs) "wikilink").
There are no wired-in classes (they are too complicated).

All the non-primitive wired-in things are *also* defined in GHC's
libraries, because even though GHC knows about them we still need to
generate code for them. For example, \`Bool\` is a wired-in type
constructor, but it is still defined in \`GHC.Base\` because we need the
info table etc for the data constructors. Arbitrarily bad things will
happen if the wired-in definition in
[GhcFile(compiler/prelude/TysWiredIn.hs)](GhcFile(compiler/prelude/TysWiredIn.hs) "wikilink")
differs from that in the library module.

All wired-in things have a \`WiredIn\` \`Name\` (see
\[wiki:Commentary/Compiler/NameType Names\]), which in turn contains the
thing. See \[wiki:Commentary/Compiler/CaseStudies/Bool a case study of
Bool implementation\] for more details.

Known-key things
----------------

A **known-key thing** has a fixed, pre-allocated \`Unique\` or **key**.
They should really be called "known-Name" things, because the baked-in
knowledge is:

`` * Its defining `Module` ``\
`` * Its `OccName` ``\
`` * Its `Unique` ``

Almost all known-key names are defined in
[GhcFile(compiler/prelude/PrelNames.hs)](GhcFile(compiler/prelude/PrelNames.hs) "wikilink");
for example: .

The point about known-key things is that GHC knows its *name*, but not
its *definition*. The definition must still be read from an interface
file as usual. The known key just allows an efficient lookup in the
environment.

Initialisation
--------------

When reading an interface file, GHC might come across "GHC.Base.Eq",
which is the name of the \`Eq\` class. How does it match up this
occurrence in the interface file with \`eqClassName\` defined in
\`PrelNames\`? Because the global name cache maintained by the renamer
is initialised with all the known-key names. This is done by the
(hard-to-find) function \`HscMain.newHscEnv\`: Notice that the
initialisation embraces both the wired-in and ("basic") known-key names.

\`Orig\` \`RdrName\` things
---------------------------

An **Orig !RdrName thing** has a top-level definition of a \`RdrName\`,
using the \`Orig\` constructor. Here, the baked-in information is:

``  * Its defining `Module` ``\
``  * Its `OccName` ``

Again, almost all of these are in
[GhcFile(compiler/prelude/PrelNames.hs)](GhcFile(compiler/prelude/PrelNames.hs) "wikilink").
Example: .

GHC Commentary: The Word
========================

The most important type in the runtime is , defined in
[GhcFile(includes/stg/Types.h)](GhcFile(includes/stg/Types.h) "wikilink").
A word is defined to be the same size as a pointer on the current
platform. All these types are interconvertible without losing
information, and have the same size (as reported by ):

`::`\
` An unsiged integral type of word size`

`::`\
` A signed integral type of word size`

`::`\
` Pointer to `

The word is the basic unit of allocation in GHC: the heap and stack are
both allocated in units of a word. Throughout the runtime we often use
sizes that are in units of words, so as to abstract away from the real
word size of the underlying architecture.

The \`StgWord\` type is also useful for storing the *size* of a memory
object, since an \`StgWord\` is guaranteed to at least span the range of
addressable memory. It is rather like \`size\_t\` in this respect,
although we prefer to use \`StgWord\` in the RTS sources.

C-- only understands units of bytes, so we have various macros in
[GhcFile(includes/Cmm.h)](GhcFile(includes/Cmm.h) "wikilink") to make
manipulating things in units of words easier in files.
