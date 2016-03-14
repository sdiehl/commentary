Table of Contents
--------------

* [Pipeline](HscMain.wiki)
  - [Parser](Parser.wiki)
  - [Renamer](Parser.wiki)
  - [Typechecker](Typechecker.wiki)
  - [Simplifier](Core2CorePipeline.wiki)
  - [Backends](Backends.wiki)
    - [NCG](NCG.wiki)
  - [GeneratedCode](GeneratedCode.wiki)

* [Key Data Typess](KeyDataTypes.wiki)
  - [Source Langauge](HsSynType.wiki)
  - [Source Names](RdrNameType.wiki)
  - [Module Types](ModueTypes.wiki)
  - [Name Types](NameType.wiki)
  - [Entity Types](EntityTypes.wiki)
  - Types
    - [Types](TypeType.wiki)
    - [Kinds](Kinds.wiki)
    - [Equality types and coercions](FC.wiki)
  - [Core](CoreSynType.wiki)
  - [sTG](StgSynType.wiki)
  - [Cmm](CmmType.wiki)

Monads
------

* GHC
* P
* Hsc
* TcRn
* DsM
* SimplM
* MonadUnique

Session
---------

* HscEnv
* DynFlags
* Settings
* UniqEnv
* Target
* TargetId
* HscTarget
* GhcMod
* ModSummary
* InteractiveContext
* TypeEnv
* GlobalRdrEnv
* TcGblEnv
* FixityEnv
* Module
* ModuleName
* ModGuts
* ModuleInfo
* ModDetails
* AvailInfo
* Class
* ClsInt
* FamInst
* InstEnv
* TyCon
* DataCon
* TyThing
* RdrName
* Name
* Var
* Type
* DataConRep
* SrcLoc
* SrcSpan
* Located
* GhcException
* Token

HsSyn
--------

- HsModule
- HsBind
- HsDecl
- HsExpr
- HsGroup
- HsLit
- Pat
- HsType

CoreSyn
--------

- Expr
- Arg
- Alt
- AltCon
- Bind

StgSyn
--------

Artifacts
----------

* ParsedModule
* TypecheckedModule
* DesugaredModule
* CoreModule
