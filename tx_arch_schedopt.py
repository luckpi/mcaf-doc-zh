# -*- coding: utf-8 -*-
import txutil

rel = "architecture/schedopt"
title_zh = "3.6. 调度与优化"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "Scheduling and Optimization": "调度与优化",
    "Scheduling": "调度",
    "Requirements": "需求",
    "Implementation notes": "实现说明",
    "Cooperative Scheduling": "协作调度",
    "Call tree": "调用树",
    "Thread safety": "线程安全",
    "Optimization": "优化",
    "The Compleat Inliner: A Primer": "内联完全指南：入门",
    "Configuration Parameters": "配置参数",
    "State Machine": "状态机",
    # TOC entries
    "3.6. Scheduling and Optimization": "3.6. 调度与优化",
    "3.6.1. Scheduling": "3.6.1. 调度",
    "3.6.1.1. Requirements": "3.6.1.1. 需求",
    "3.6.1.2. Implementation notes": "3.6.1.2. 实现说明",
    "3.6.1.2.1. Cooperative Scheduling": "3.6.1.2.1. 协作调度",
    "3.6.1.2.2. Call tree": "3.6.1.2.2. 调用树",
    "3.6.1.2.3. Thread safety": "3.6.1.2.3. 线程安全",
    "3.6.2. Optimization": "3.6.2. 优化",
    "3.6.2.1. The Compleat Inliner: A Primer": "3.6.2.1. 内联完全指南：入门",
    # Requirements
    "MCAF has the following set of requirements in terms of scheduling:":
        "MCAF 在调度方面有以下需求：",
    "should be called once at system startup": "应在系统启动时调用一次",
    "should be called at each iteration of the main loop. This does not have to be executed periodically, but the minimum repetition rate should be approximately 100Hz to service the various features.":
        "应在主循环的每次迭代时调用。这不要求周期性执行，但最小重复频率应约为 100Hz，以服务各种功能。",
    "The board handler function,": "板级处理函数，",
    ", should be called periodically by the application once every 0.1ms – 10ms. This period value should be entered in the Customize page of motorBench":
        "，应由应用程序周期性调用，频率为每 0.1ms – 10ms 一次。此周期值应在 motorBench",
    'Development Suite for the customizable parameter "Ui service period". This function does not have a hard real-time requirement.':
        ' Development Suite 的 Customize 页面中为可定制参数"Ui service period"输入。此函数没有硬实时要求。',
    "MCAF control": "MCAF 控制",
    "routines are time-critical, and need to execute synchronously to the":
        "例程是时间关键的，需要与",
    "cycle.": "周期同步执行。",
    # Implementation notes
    "The MCAF scheduler architecture is fairly simple. It uses cooperative scheduling with a main thread (the entry point from the":
        "MCAF 调度器架构相当简单。它使用协作调度，包含一个主线程（从",
    "function) and one": "函数的入口点）和各一个",
    "each for the application timer interrupt and the ADC interrupt.":
        "分别用于应用定时器中断和 ADC 中断。",
    "Flow diagram showing the main thread, application timer interrupt and the ADC interrupt":
        "流程图展示了主线程、应用定时器中断和 ADC 中断",
    "The main thread contains initialization functions that run once at startup, and a main loop to execute tasks which are not time-critical.":
        "主线程包含在启动时运行一次的初始化函数，以及一个用于执行非时间关键任务的主循环。",
    "The application timer handles periodic application and board-related tasks that do not have hard real-time requirements.":
        "应用定时器处理没有硬实时要求的周期性应用和板级相关任务。",
    "The ADC": "ADC",
    "handles tasks that are time-critical, and executes synchronously to the":
        "处理时间关键的任务，并与",
    "cycle:": "周期同步执行：",
    "triggered by": "由",
    "low center, to reject switching-frequency harmonics": "低中心触发，以抑制开关频率谐波",
    "triggered when all conversions are complete": "在所有转换完成时触发",
    "timing margin is designed to ensure that time between between register assignment and update is sufficient to meet critical control latency requirements (see":
        "时序裕量设计用于确保寄存器赋值与更新之间的时间足以满足关键控制延迟要求（见",
    "Timing relationship between control ISR and PWM.":
        "控制 ISR 与 PWM 之间的时序关系。",
    "Center-aligned PWM can typically be configured either for single or double updates; in single-update mode the PWM generators are updated from software registers at the beginning of each PWM period, yielding symmetrical waveforms, whereas in double-update mode the PWM generators are updated from software registers at the beginning and at center of each PWM period, yielding potentially asymmetric waveforms with twice the update rate. In each case the critical code represents calculations from ADC readings needed to compute new PWM values, and should complete in time for the next PWM generator update.":
        "中心对齐 PWM 通常可配置为单更新或双更新模式；在单更新模式下，PWM 发生器在每个 PWM 周期开始时从软件寄存器更新，产生对称波形；而在双更新模式下，PWM 发生器在每个 PWM 周期的开始和中心处从软件寄存器更新，产生可能非对称的波形，更新速率翻倍。在每种情况下，关键代码代表从 ADC 读数计算新 PWM 值所需的计算，并应在下一次 PWM 发生器更新之前完成。",
    "Most time-critical portion of ADC": "ADC 中最时间关键的部分",
    ": Read": "：读取",
    "result, calculate, update": "结果，计算，更新",
    "Sufficient CPU time is left over for other calculations:":
        "剩余的 CPU 时间足以进行其他计算：",
    "tasks which are also time-critical, but their requirements are not as stringent":
        "同样时间关键的任务，但其要求不那么严格",
    "tasks which are require some degree of coordination with those tasks running at the ADC":
        "需要与在 ADC",
    "rate, so that relocation in the main loop is tricky":
        "速率下运行的任务有一定程度协调的任务，因此在主循环中重新定位比较棘手",
    "Some examples of tasks include": "任务的一些示例包括",
    "A current loop that runs once every control ADC": "每次控制 ADC",
    "(time-critical, part of": "（时间关键，是",
    "latency bottleneck)": "延迟瓶颈的一部分）",
    "A velocity loop that runs once every N ISRs (for example N=20)":
        "每 N 个 ISR 运行一次的速度环（例如 N=20）",
    "Other minor tasks, such as monitoring, that run in the ADC":
        "在 ADC",
    "service routine that runs from the ADC": "服务例程，从 ADC",
    "and synchronizes MCAPI motor data with control variables within MCAF motor data":
        "运行，并将 MCAPI 电机数据与 MCAF 电机数据中的控制变量同步",
    "User interface and diagnostic kernel elements that run more slowly in the main loop":
        "在主循环中较慢运行的用户界面和诊断内核元素",
    # Cooperative Scheduling
    'The term "cooperative scheduling" means that each task runs to completion without blocking, before the next one executes; there is not an operating system which preemptively switches threads of execution before a task has completed.':
        '"协作调度"一词意味着每个任务在下一次执行之前运行至完成而不阻塞；不存在一个操作系统在任务完成之前抢占式地切换执行线程。',
    "With this approach, scheduling constraints must be handled explicitly by the designer, rather than at run-time as in an operating system. Typical constraints are":
        "在这种方法中，调度约束必须由设计者显式处理，而不是像操作系统那样在运行时处理。典型的约束包括",
    "computation of the current control loop between": "之间的电流控制环计算",
    "sampling and": "采样与",
    "update must be complete before the end of the": "更新必须在",
    "period, so that the effective input-output delay is one sampling period.":
        "周期结束之前完成，以使有效输入-输出延迟为一个采样周期。",
    "completion of the ADC": "ADC",
    "must occur prior to the next ADC": "必须在下一次 ADC",
    "interrupt, so that the next ADC": "中断之前完成，以便下一次 ADC",
    "is not delayed": "不被延迟",
    "Scheduling constraints can be checked manually, by using the":
        "调度约束可以手动检查，通过使用",
    "timestamp feature of the test harness": "测试框架的时间戳功能",
    "to record timer values, in order to make sure that worst-case execution times are acceptable.":
        "来记录定时器值，以确保最坏情况执行时间是可接受的。",
    # Call tree
    "A sample call tree is shown below in": "示例调用树如下",
    ". This shows many (but not all) of the function calls that take place in the ADC":
        "所示。这展示了 ADC",
    ". The time between reading of": "中发生的许多（但不是全部）函数调用。读取",
    "and update of": "与更新",
    "duty cycles should involve time-critical tasks; other tasks should generally be deferred. Version 1.0 of the MCAF includes a few minor routines that we plan on moving after the":
        "占空比之间的时间应涉及时间关键任务；其他任务通常应推迟。MCAF 版本 1.0 包含一些我们计划在",
    "update to minimize the critical control latency.":
        "更新之后移动的次要例程，以最小化关键控制延迟。",
    # Thread safety
    "Because the main thread can be interrupted by the control ISR, shared state must be handled carefully.":
        "由于主线程可能被控制 ISR 中断，共享状态必须小心处理。",
    "This shared state is marked with a": "此共享状态用",
    "qualifier, so that the compiler does not make incorrect assumptions. Shared state includes:":
        "限定符标记，以使编译器不会做出错误假设。共享状态包括：",
    "External interface data in": "外部接口数据在",
    "(system_state.h)": "(system_state.h)",
    "Test harness information in": "测试框架信息在",
    "and": "和",
    "Watchdog state in": "看门狗状态在",
    "(isr.c and main.c)": "(isr.c 和 main.c)",
    "motor data in": "电机数据在",
    "Thread safety concerns involving this shared state have been addressed in MCAF as follows:":
        "MCAF 中涉及此共享状态的线程安全问题已按如下方式解决：",
    "No individual items of shared data are larger than 16 bits (each item can be read and written atomically in the dsPIC 16-bit architecture)":
        "没有单个共享数据项大于 16 位（每项可以在 dsPIC 16 位架构中原子读取和写入）",
    "MCAF does not require mutually consistent state across multiple items of data":
        "MCAF 不要求多个数据项之间的状态相互一致",
    "The only shared state that has multiple writers is": "唯一有多个写入者的共享状态是",
    ", where the interaction between main and control ISR threads is simple and not prone to concurrency errors (main thread sets count to zero and does not read the count; control ISR increments count and isn't interrupted by the main thread)":
        "，其中主线程与控制 ISR 线程之间的交互简单且不易出现并发错误（主线程将计数置零且不读取计数；控制 ISR 递增计数且不被主线程中断）",
    "functions executing from the main thread use": "从主线程执行的函数使用",
    "flag to claim ownership of the shared MCAPI motor data structure while they are executing a critical section of code. Refer to MCAPI section,":
        "标志来声明对共享 MCAPI 电机数据结构的所有权，同时执行代码的关键部分。参见 MCAPI 部分，",
    "Handling Concurrency": "处理并发",
    ", for more information.": "，了解更多信息。",
    "If a more stringent concurrency requirement is needed in the future, shared state will be protected by additional means, for example briefly disabling interrupts, or usage of non-blocking threadsafe data structures.":
        "如果将来需要更严格的并发要求，共享状态将通过额外手段保护，例如短暂禁用中断，或使用非阻塞的线程安全数据结构。",
    # Optimization
    "The MCAF has four requirements that impact execution time requirements:":
        "MCAF 有四个影响执行时间需求的要求：",
    "Provide a designated feature set (particular series of algorithms running at the control ADC":
        "提供指定的功能集（以控制 ADC",
    "rate)": "速率运行的特定算法系列）",
    "Meet timing requirements with": "在 XC16 中以",
    "compiler optimization level in XC16 (": "编译器优化级别满足时序要求（",
    "are faster but are only available in the premium licenses for XC16)":
        "更快，但仅在 XC16 的高级许可证中可用）",
    "Be modular and maintainable: follow good software engineering practices":
        "模块化且可维护：遵循良好的软件工程实践",
    "Be efficient so that sufficient CPU cycles remain for customer applications":
        "高效，以便为客户应用留出足够的 CPU 周期",
    "These pose an interesting dilemma. Good software engineering practices encourage refactoring large, complex software functions into small, simple, maintainable functions, each handling a single, well-defined purpose. But doing so in C adds additional stack frames, which tend to add execution time. This can be significant in systems with high update rates.":
        "这些要求构成了一个有趣的困境。良好的软件工程实践鼓励将大型、复杂的软件函数重构为小型、简单、可维护的函数，每个函数处理单一、明确的目的。但在 C 语言中这样做会增加额外的栈帧，往往会增加执行时间。在更新速率高的系统中，这可能非常显著。",
    "For example, the following code contains a function": "例如，以下代码包含一个函数",
    "for constraining a set of 3 duty cycle values between allowable limits and write hardware registers:":
        "用于将一组 3 个占空比值约束在允许的范围内并写入硬件寄存器：",
    "The": "",
    "function body is only 16 lines, but it can be simplified further into sub-functions that handle clipping and updating the hardware registers:":
        "函数体仅有 16 行，但可以进一步简化为处理裁剪和更新硬件寄存器的子函数：",
    "Now we have functions with a maximum body length of 5 lines, each of which are simpler. Furthermore, it is easier to avoid copy-paste errors like the ones below:":
        "现在我们有了最大函数体长度为 5 行的函数，每个都更简单。此外，更容易避免如下所示的复制粘贴错误：",
    "We compiled the code in": "我们编译了",
    "with XC16 1.25 targeting the dsPIC33E256MC506, and analyzed the results for maximum cycle counts:":
        "中的代码，使用 XC16 1.25 针对 dsPIC33E256MC506，并分析了最大周期计数的结果：",
    "Listing 3.17": "代码清单 3.17",
    "Listing 3.18": "代码清单 3.18",
    "Listing 3.19": "代码清单 3.19",
    "Listing 3.20": "代码清单 3.20",
    "Listing 3.21": "代码清单 3.21",
    "Listing 3.22": "代码清单 3.22",
    "Listing 3.23": "代码清单 3.23",
    "Listing 3.24": "代码清单 3.24",
    "Listing 3.25": "代码清单 3.25",
    "Listing 3.26": "代码清单 3.26",
    "— one big function": "——一个大函数",
    "— refactored": "——重构后",
    "— refactored + inline": "——重构 + 内联",
    "The refactoring in": "中的重构",
    "added 49 cycles under": "在",
    "but not in": "下增加了 49 个周期，但在",
    "or": "或",
    ". Why?": "下则没有。为什么？",
    "The cost of a function call in the 33E architecture is": "33E 架构中函数调用的开销为",
    "are caller saved, to allow for arguments and return values;": "由调用者保存，用于参数和返回值；",
    "are callee saved)": "由被调用者保存）",
    "The refactored version of": "重构后的",
    "contains 4 function calls, so this adds 40 extra cycles for the":
        "包含 4 次函数调用，因此",
    "instructions, and the other 9 cycles involve register moves to comply with function call conventions.":
        "指令增加了 40 个额外周期，其余 9 个周期涉及符合函数调用约定的寄存器移动。",
    "optimizations, the XC16 compiler automatically inlines small functions. We can coerce XC16 into doing this under":
        "优化下，XC16 编译器会自动内联小函数。我们可以通过添加",
    "by adding the": "关键字来强制 XC16 在",
    "keyword:": "下执行此操作：",
    "This technique is used frequently in the MCAF to keep execution time low, but still allow for modular refactoring. You will see":
        "这种技术在 MCAF 中经常使用，以保持低执行时间，同时仍允许模块化重构。您会看到",
    "used frequently in functions that are either very simple or called only once.":
        "在非常简单或仅调用一次的函数中频繁使用。",
    "If you are interested in using": "如果您有兴趣在自己的代码中使用",
    "in your own code, please read the following section, before you start sprinkling it around haphazardly.":
        "，请在开始随意使用之前阅读以下部分。",
    # The Compleat Inliner
    "keyword in C is a tool, and like all tools, it can be used both appropriately and inappropriately. Two things to keep in mind are:":
        "关键字在 C 中是一个工具，与所有工具一样，它可以被恰当使用，也可以被不当使用。需要记住两点：",
    "Please be aware that in C, the": "请注意，在 C 中，",
    "keyword is a": "关键字是对编译器的一个",
    "hint": "提示",
    "to the compiler, not a requirement.": "，而非要求。",
    "In theory the compiler is free to ignore it; in practice it can be a useful tool.":
        "理论上编译器可以自由忽略它；在实践中它可以是一个有用的工具。",
    "Keep a good sense of proportion, and understand how often your code executes.":
        "保持良好的比例感，并理解代码执行的频率。",
    "We discussed an example of reducing a function from 105 cycles to 56 cycles. In a 70MIPS dsPIC":
        "我们讨论了一个将函数从 105 个周期减少到 56 个周期的示例。在 70MIPS 的 dsPIC",
    "DSC device, this would save 700 nanoseconds.":
        "DSC 器件上，这将节省 700 纳秒。",
    "If this is in code that executes once per second, it would be an insignificant improvement, and":
        "如果这在每秒执行一次的代码中，改进微不足道，而",
    "does have some significant disadvantages, discussed later in this section":
        "确实有一些显著的缺点，将在本节后面讨论",
    "If this is in code that executes at a 20 kHz rate, it would save 1.4% of the CPU, which is not a huge savings, but it is significant for adding":
        "如果这在以 20 kHz 速率执行的代码中，将节省 1.4% 的 CPU，这不是很大的节省，但在两个简单实例中添加",
    "in two simple instances.": "是显著的。",
    "With that as a prologue, here are some general rules for inlining in C.":
        "以此为序言，以下是在 C 中使用内联的一些通用规则。",
    "Don't do it": "不要这样做",
    "Ignore Rule #1 if a function is very small.":
        "如果函数非常小，请忽略规则 #1。",
    'Good candidates for inlining are functions that are less than ≈70 cycles, whether that is the total time, or the time excluding 2nd-level calls, as in "adapter" functions like the one shown below:':
        '内联的良好候选者是少于约 70 个周期的函数，无论是总时间，还是排除二级调用的时间，如以下所示的"适配器"函数：',
    "Ignore Rule #1 if a function is called only once.":
        "如果函数仅被调用一次，请忽略规则 #1。",
    "Ignore Rule #1 if you are desperate to optimize.":
        "如果您迫切需要优化，请忽略规则 #1。",
    "Desperation can lead to poor decision-making, so don't do it lightly.":
        "迫切感可能导致糟糕的决策，所以不要轻率行事。",
    "If you ignore Rule #1, don't inline blindly.":
        "如果您忽略规则 #1，不要盲目内联。",
    "5a. Use": "5a. 使用",
    "(this keeps the intermediate assembly files generated by the compiler) and develop habit of spot-checking the compiler output":
        "（这会保留编译器生成的中间汇编文件）并养成抽查编译器输出的习惯",
    "5b. Measure execution times — code execution time will be dependent on how inline functions are used, and may change unexpectedly upon changes in caller code.":
        "5b. 测量执行时间——代码执行时间将取决于内联函数的使用方式，并可能在调用者代码更改时意外变化。",
    "Call sites (point of use)": "调用点（使用位置）",
    "must": "必须",
    "be in the same compilation unit as the inline function definition":
        "与内联函数定义在同一编译单元中",
    "Assembly code generation is determined by the compiler": "汇编代码生成由编译器决定",
    "The compiler processes one compilation unit at a time": "编译器一次处理一个编译单元",
    "The compiler can't see the source of other compilation units": "编译器无法看到其他编译单元的源代码",
    "The compiler does not see the source directly; instead it sees the output of the preprocessor (effectively one .c file + any":
        "编译器不直接看到源代码；而是看到预处理器的输出（实际上是一个 .c 文件 + 任何",
    "d .h files)": "d 的 .h 文件）",
    'The linker can only relocate addresses; it can\'t change the sequence of instructions (some newer compiler toolchains have link-time / "whole program" optimization which get around this restriction — if you have such a toolchain you should probably rethink your use of':
        '链接器只能重定位地址；它不能改变指令序列（一些较新的编译器工具链具有链接时/"全程序"优化功能，可以绕过此限制——如果您有这样的工具链，您可能应该重新考虑对',
    "6a.": "6a.",
    '"Local" function definitions': '"局部"函数定义',
    "(function definition and call site in the same .c file) —":
        "（函数定义和调用点在同一 .c 文件中）——",
    "is sufficient.": "就足够了。",
    "6b.": "6b.",
    '"Shared" function definitions': '"共享"函数定义',
    "(call site in a .c file, function definition in a .h file) — this requires the use of":
        "（调用点在 .c 文件中，函数定义在 .h 文件中）——这需要使用",
    ". The": "。",
    "keyword prevents the function from being referenced from other compilation units, effectively giving each compilation unit its own private copy; otherwise, the linker will complain about duplicates.":
        "关键字防止函数被其他编译单元引用，实际上为每个编译单元提供了自己的私有副本；否则，链接器会抱怨重复定义。",
    "Understand the consequences": "了解后果",
    "when you": "当您对函数使用",
    "a function": "时",
    "Using": "使用",
    'in a .h file causes transitive dependencies. See the following table: (the → symbol means "depends on")':
        '在 .h 文件中会导致传递依赖。请参见下表：（→ 符号表示"依赖于"）',
    "No inline static": "无 inline static",
    "Use of inline static": "使用 inline static",
    "The function implementation cannot be secret": "函数实现不能保密",
    "The function cannot be put into a precompiled library, which means, for example, that if you are creating a library and you have access to the premium version of XC16, you can't compile it with":
        "函数不能放入预编译库中，这意味着，例如，如果您正在创建库并且有权访问 XC16 的高级版本，则无法使用",
    "to make it available to library customers who do not have access to":
        "编译它，以使其对无权访问",
    "More code space is typically needed, in order to support multiple call sites. For example, don't do this:":
        "通常需要更多代码空间，以支持多个调用点。例如，不要这样做：",
    "Aside from producing ambiguously-ordered execution — in expressions like":
        "除了产生顺序不明确的执行外——在类似",
    "there is no guaranteed order": "的表达式中没有保证的顺序",
    ": the compiler may choose to execute": "：编译器可以选择先执行",
    "first or it may choose to execute": "或先执行",
    "first, so side-effects like calls to": "，因此对",
    "may not always appear in the same order — calling": "的调用等副作用可能不总是以相同顺序出现——调用",
    "will create code that asks the compiler to inline 143 separate calls to":
        "将创建要求编译器内联 143 个单独的",
    ", which is probably a waste of code space.":
        "调用的代码，这可能是对代码空间的浪费。",
    "Execution time is not fixed": "执行时间不固定",
    "— depending on the caller, the compiler may produce optimized assembly code differently at each call site.":
        "——根据调用者的不同，编译器可能在每个调用点产生不同的优化汇编代码。",
    'Inlined functions "lose their identity"': '内联函数"失去身份"',
    "Debugging may be harder (you don't see an entry in the call stack, and breakpoints may not work)":
        "调试可能更困难（您在调用栈中看不到条目，断点可能不起作用）",
    "They don't appear separately in the linker map": "它们不会单独出现在链接器映射中",
    "Language lawyers will say you can't depend on it": "语言律师会说您不能依赖它",
    ". (in theory they are right, in practice they are wrong… at least until the next version of the compiler has changes that break your code)":
        "。（理论上他们是对的，实践中他们是错的……至少直到编译器的下一个版本做出破坏您代码的更改）",
    "Continued vigilance is required (see Rule #5) to ensure inlining works as expected":
        "需要持续警惕（参见规则 #5）以确保内联按预期工作",
    "can be a powerful tool in programming C on embedded systems, but it comes with costs, and should only be used with appropriate care.":
        "可以是在嵌入式系统上编程 C 的强大工具，但它伴随着成本，应仅在适当谨慎的情况下使用。",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
