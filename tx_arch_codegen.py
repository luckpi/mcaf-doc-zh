# -*- coding: utf-8 -*-
import txutil

rel = "architecture/codegen"
title_zh = "3.4. 代码生成"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "Code Generation": "代码生成",
    "Why Code Generation?": "为何使用代码生成？",
    "How Does Code Generation Work?": "代码生成如何工作？",
    "Data Model Preparation": "数据模型准备",
    "Conditional code generation": "条件代码生成",
    "Further Information": "更多信息",
    "State management": "状态管理",
    "Configuration Parameters": "配置参数",
    # TOC entries (section number + title in one text node)
    "3.4. Code Generation": "3.4. 代码生成",
    "3.4.1. Why Code Generation?": "3.4.1. 为何使用代码生成？",
    "3.4.2. How Does Code Generation Work?": "3.4.2. 代码生成如何工作？",
    "3.4.2.1. Data Model Preparation": "3.4.2.1. 数据模型准备",
    "3.4.2.2. Conditional code generation": "3.4.2.2. 条件代码生成",
    "3.4.2.3. Further Information": "3.4.2.3. 更多信息",
    # intro paragraph
    "The MCAF utilizes the": "MCAF 使用",
    "templating engine for generating code. This section describes an overview of the code generation process; while it is not necessary for understanding the output code, it may be helpful to understand some of the context behind the MCAF.":
        "模板引擎来生成代码。本节描述代码生成过程的概述；虽然这对于理解输出代码并非必要，但了解 MCAF 背后的一些背景可能会有所帮助。",
    # Why Code Generation
    "Some of the reasons for using code generation were mentioned in the": "使用代码生成的一些原因已在",
    "introduction": "简介",
    "Management of multiple hardware configurations": "多种硬件配置的管理",
    "— by using code generation, the MCAF can support the many combinations of processor, board,":
        "——通过使用代码生成，MCAF 可以用单一固件包支持处理器、板卡、",
    ", motor, and load with a single firmware package.":
        "、电机和负载的多种组合。",
    "Automation of the tuning process": "整定过程的自动化",
    "Development Suite includes algorithms that will automatically tune the current and velocity controllers.":
        "Development Suite 包含可自动整定电流和速度控制器的算法。",
    "There are also some more subtle reasons:": "还有一些更微妙的原因：",
    "The C language has only limited support for computation at design time":
        "C 语言对设计时计算的支持非常有限",
    "— essentially there are two mechanisms:": "——本质上只有两种机制：",
    "constant-folding — the compiler will turn expressions like":
        "常量折叠——编译器会在编译时将",
    "into a single value (22) at compile-time rather than run-time":
        "这样的表达式转换为单个值 (22)，而非在运行时计算",
    "preprocessor — the C preprocessor will substitute text in":
        "预处理器——C 预处理器会在编译时（即编译之前）替换",
    "expressions at compile-time (just prior to compilation)":
        "表达式中的文本",
    "These do not provide features for testing or verification. They are very fragile and often lead to errors, which either occur silently or with cryptic compiler messages. These issues are discussed in more detail in the next section on":
        "这些机制不提供测试或验证功能。它们非常脆弱，常常导致错误，而且错误要么静默发生，要么产生难以理解的编译器消息。这些问题将在下一节关于",
    "configuration parameters": "配置参数",
    "Code generation can offer UI-driven flexibility.": "代码生成可以提供 UI 驱动的灵活性。",
    "For example, motorBench": "例如，motorBench",
    "Development Suite has the capability to present a choice among several alternative options (for example: choosing a sensorless position estimator)":
        "Development Suite 能够在多个可选选项之间提供选择（例如：选择无传感器位置估计器）",
    "and then utilize appropriate source files from the MCAF firmware package to implement the selected option. (Note: the initial version of motorBench":
        "，然后利用 MCAF 固件包中适当的源文件来实现所选选项。（注：motorBench",
    "Development Suite does not provide this feature, but it is planned for a future version.)":
        "Development Suite 的初始版本不提供此功能，但计划在未来版本中实现。）",
    # How Does Code Generation Work
    "Code generation in the MCAF is driven by a": "MCAF 中的代码生成由",
    "templating engine": "模板引擎",
    "that operates on a static": "驱动，它作用于一个静态的",
    "firmware package": "固件包",
    "and a dynamic": "和一个动态的",
    "data model": "数据模型",
    "The templating engine consists primarily of FreeMarker, but has other components as well, for example to support the use of configuration files, conditional code generation, and Jython scripts.":
        "模板引擎主要由 FreeMarker 组成，但也包含其他组件，例如用于支持配置文件、条件代码生成和 Jython 脚本的组件。",
    "The firmware package contains a fixed (static) set of template files, configuration files, and Jython scripts used to generate the source code.":
        "固件包包含一组固定的（静态）模板文件、配置文件和 Jython 脚本，用于生成源代码。",
    "The data model is a set of named key-value pairs that is used by the code generation application (CGA, of which motorBench":
        "数据模型是一组命名的键值对，供代码生成应用程序（CGA，其中 motorBench",
    "Development Suite is the primary example) to organize different items of information in known places that are referenced by the firmware package. The data model will generally change from one code generation run to the next.":
        "Development Suite 是主要示例）使用，用于将不同的信息项组织在固件包所引用的已知位置。数据模型通常在每次代码生成运行之间会发生变化。",
    "The templating engine": "模板引擎",
    "renders": "渲染",
    "files in the firmware package, using the data model to determine the parts of the output files which are dependent on input data from the CGA. In some cases, the rendering operation is just a verbatim copy with no input dependencies; in others, complex calculations may occur; but in many cases, rendering is just simple expression evaluation and substitution.":
        "固件包中的文件，使用数据模型来确定输出文件中依赖于 CGA 输入数据的部分。在某些情况下，渲染操作只是没有输入依赖的逐字复制；在其他情况下，可能会进行复杂的计算；但在许多情况下，渲染只是简单的表达式求值和替换。",
    "For example, we could have the template file shown in": "例如，我们可以有",
    "Listing 3.1": "代码清单 3.1",
    ", along with the data model shown in": "中所示的模板文件，以及",
    "Listing 3.2": "代码清单 3.2",
    "This would render into the output file shown in": "这将渲染为",
    "Listing 3.3": "代码清单 3.3",
    "The template contains special placeholders such as": "模板包含特殊的占位符，例如",
    "and": "和",
    "which FreeMarker calls": "，FreeMarker 将其称为",
    "interpolations": "插值",
    ". These contain an expression which is evaluated and substituted into the output text.":
        "。这些占位符包含一个表达式，该表达式会被求值并替换到输出文本中。",
    "Such an example isn’t very useful for motor control, but the same expression evaluation and substitution mechanism can also be used to generate C code or comments, as shown in":
        "这样的示例对电机控制来说不太实用，但同样的表达式求值和替换机制也可用于生成 C 代码或注释，如",
    "Listing 3.4": "代码清单 3.4",
    "Listing 3.5": "代码清单 3.5",
    ", which render to": "和",
    "Listing 3.6": "代码清单 3.6",
    # Data Model Preparation
    "Values can end up in the data model by several mechanisms:":
        "值可以通过以下几种机制进入数据模型：",
    "From the CGA": "来自 CGA",
    "Development Suite). This will typically occur when there are values needed from customer-entered configuration data (motor name, number of poles, etc.) or when the values are computed by the CGA itself (automatically-tuned control loop gains).":
        "Development Suite）。这通常发生在需要来自客户输入的配置数据（电机名称、极数等）的值时，或者当值由 CGA 自身计算（自动整定的控制环增益）时。",
    "From a configuration file in the MCAF firmware package.":
        "来自 MCAF 固件包中的配置文件。",
    "This will typically be used to manage certain constants that are common to the application framework, but should be decoupled from the CGA, so that they can be updated as part of improvements in the application framework package.":
        "这通常用于管理应用框架通用的某些常量，但应与 CGA 解耦，以便作为应用框架包改进的一部分进行更新。",
    "From a Jython script in the MCAF framework package.":
        "来自 MCAF 框架包中的 Jython 脚本。",
    "This will typically be used to handle computations that are not part of the CGA’s core functions, such as slew rates or other derived constants that are closely coupled to the application framework package itself.":
        "这通常用于处理不属于 CGA 核心功能的计算，例如压摆率或其他与应用框架包本身紧密耦合的派生常量。",
    "The templating engine doesn’t care where values came from, only that the named locations in the data model which are referenced by templates in the firmware package contain valid values that can be used to generate text strings in output files.":
        "模板引擎不关心值的来源，只关心数据模型中被固件包模板引用的命名位置包含可用于在输出文件中生成文本字符串的有效值。",
    "The process of determining the data model can be envisioned as shown in":
        "确定数据模型的过程可以设想为如",
    ". In general, motorBench": "所示。一般来说，motorBench",
    "Development Suite and the MCAF provide or compute engineering values, which are then represented as fixed-point integers in the generated code by appropriate choices of engineering unit scaling factors.":
        "Development Suite 和 MCAF 提供或计算工程值，然后通过适当选择工程单位缩放因子，在生成的代码中表示为定点整数。",
    "Data model production process": "数据模型生成过程",
    # Conditional code generation
    "Sometimes we need to provide different content based upon something in the data model: for example, selecting among several position/velocity estimators. The templating engine supports this.":
        "有时我们需要根据数据模型中的某些内容提供不同的内容：例如，在多个位置/速度估计器之间进行选择。模板引擎支持此功能。",
    "Per-character/per-line conditional generation": "逐字符/逐行条件生成",
    "There are conditional features available in FreeMarker (the": "FreeMarker 中有可用的条件功能（",
    "directive, for example) which behave similarly to the": "指令，例如），其行为类似于 C 中的",
    "preprocessor directives in C, except that they are processed at code-generation time rather than at compile-time. These may be used sparingly to enable or disable particular lines of code, or to select from more than one alternative.":
        "预处理器指令，不同之处在于它们在代码生成时而非编译时处理。这些功能可以谨慎使用，以启用或禁用特定的代码行，或从多个选项中进行选择。",
    "Per-file conditional generation": "逐文件条件生成",
    "For inclusion or exclusion of entire modules, there are features in the templating engine that allow the template author to associate a particular source file with a “tag” to designate that this source file will be rendered only if the tag is present in a known location in the data model. This relieves the CGA from having to know which files should be included or excluded; instead, the CGA lists which tags to include as named features, and the application framework package then contains the association of tag name with source files.":
        '对于整个模块的包含或排除，模板引擎中有一些功能允许模板作者将特定源文件与一个"标签"关联，以指定该源文件仅在数据模型中的已知位置存在该标签时才被渲染。这使 CGA 无需知道应包含或排除哪些文件；相反，CGA 列出要包含的标签作为命名功能，然后应用框架包包含标签名称与源文件的关联。',
    # Further Information
    "For further information on the code generation process, please": "有关代码生成过程的更多信息，请",
    "contact Microchip": "联系 Microchip",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
