"""Conceptual Computer Science items for Part III. Original MCQs, TRE style."""

from qutil import fixed

def c(topic, q, qh, a, ah, b, bh, c_, ch, ans, ex, pre=False):
    return fixed("cs", topic, q, qh, [a, b, c_], [ah, bh, ch], ans, ex, pre=pre)


def build_cs():
    R = []
    A = R.append

    # fundamentals
    A(c("fundamentals", "1 KB in binary memory measurement equals:", "बाइनरी माप में 1 KB बराबर है:",
        "1024 bytes", "1024 बाइट", "1000 bits", "1000 बिट", "1024 bits", "1024 बिट", 0,
        "मेमोरी में 1 KB = 1024 बाइट। 1 बाइट = 8 बिट।"))
    A(c("fundamentals", "ASCII is fundamentally a:", "ASCII मूलतः है:",
        "7-bit character code", "7-बिट वर्ण कोड", "16-bit floating format", "16-बिट फ्लोटिंग प्रारूप", "32-bit instruction set", "32-बिट निर्देश सेट", 0,
        "मानक ASCII 7 बिट का है, जिससे 128 संकेत बनते हैं। विस्तारित ASCII 8 बिट का है।"))
    A(c("fundamentals", "Which memory is volatile?", "कौन-सी मेमोरी अस्थायी (वोलेटाइल) है?",
        "RAM", "रैम", "ROM", "रोम", "CD-ROM", "सीडी-रोम", 0,
        "बिजली जाते ही RAM का डेटा मिट जाता है। ROM और CD-ROM अवाष्पशील हैं।"))
    A(c("fundamentals", "Which of the following is non-volatile?", "निम्न में कौन अवाष्पशील है?",
        "ROM", "रोम", "DRAM", "डीरैम", "SRAM cache", "एसरैम कैश", 0,
        "ROM बिजली के बिना भी डेटा रखती है। DRAM और SRAM दोनों वोलेटाइल हैं।"))
    A(c("fundamentals", "The brain of the computer is commonly called the:", "कम्प्यूटर का मस्तिष्क किसे कहते हैं?",
        "CPU", "सीपीयू", "Monitor", "मॉनिटर", "Printer", "प्रिंटर", 0,
        "CPU निर्देशों को लाता, समझता और चलाता है। मॉनिटर और प्रिंटर आउटपुट उपकरण हैं।"))
    A(c("fundamentals", "Which is an output device?", "कौन आउटपुट डिवाइस है?",
        "Printer", "प्रिंटर", "Keyboard", "कीबोर्ड", "Mouse", "माउस", 0,
        "प्रिंटर परिणाम दिखाता/छापता है। कीबोर्ड और माउस इनपुट उपकरण हैं।"))
    A(c("fundamentals", "BIOS is stored in:", "BIOS कहाँ संचित रहता है?",
        "ROM", "रोम", "A typical hard-disk file that vanishes when power fails", "ऐसी हार्ड-डिस्क फाइल जो बिजली जाते ही मिट जाए", "Cache only", "केवल कैश", 0,
        "BIOS फर्मवेयर ROM/फ्लैश में रहता है ताकि मशीन चालू होते ही उपलब्ध हो।"))
    A(c("fundamentals", "Which numbering system does a digital computer use internally for arithmetic?", "डिजिटल कम्प्यूटर आंतरिक गणना के लिए कौन-सी संख्या प्रणाली इस्तेमाल करता है?",
        "Binary", "बाइनरी", "Decimal only", "केवल दशमलव", "Roman", "रोमन", 0,
        "इलेक्ट्रॉनिक स्विच दो अवस्थाएँ रखते हैं, इसलिए आंतरिक गणना बाइनरी में होती है।"))
    A(c("fundamentals", "SSD differs from HDD mainly because SSD:", "SSD, HDD से मुख्यतः इस कारण भिन्न है कि SSD:",
        "has no spinning magnetic platter", "उसमें घूमती चुंबकीय प्लेट नहीं होती", "cannot store files", "फाइलें नहीं रख सकता", "is a printer", "एक प्रिंटर है", 0,
        "SSD फ्लैश मेमोरी इस्तेमाल करता है। HDD में घूमती डिस्क और हेड होते हैं।"))
    A(c("fundamentals", "Which of the following is system software?", "निम्न में सिस्टम सॉफ्टवेयर कौन है?",
        "Operating system", "ऑपरेटिंग सिस्टम", "Payroll application", "वेतन अनुप्रयोग", "Web browser game", "वेब ब्राउजर गेम", 0,
        "ऑपरेटिंग सिस्टम हार्डवेयर चलाता है, इसलिए सिस्टम सॉफ्टवेयर है। वेतन कार्यक्रम अनुप्रयोग सॉफ्टवेयर है।"))

    # digital
    A(c("digital", "A NAND gate is called a universal gate because:", "NAND गेट को सार्वत्रिक गेट क्यों कहते हैं?",
        "Any Boolean function can be made using only NAND gates", "केवल NAND से कोई भी बूलियन फलन बनाया जा सकता है", "It can add two decimal numbers directly", "यह दो दशमलव संख्याएँ सीधे जोड़ देता है", "It stores data without power", "यह बिना बिजली डेटा रखता है", 0,
        "NAND और NOR दोनों सार्वत्रिक गेट हैं।"))
    A(c("digital", "Which of the following is also a universal gate?", "निम्न में कौन भी सार्वत्रिक गेट है?",
        "NOR", "NOR", "XOR", "XOR", "AND", "AND", 0,
        "NOR अकेले हर बूलियन फलन बना सकता है। AND और XOR अकेले सार्वत्रिक नहीं हैं।"))
    A(c("digital", "The output of an AND gate is 1 only when:", "AND गेट का आउटपुट 1 तभी होता है जब:",
        "all inputs are 1", "सभी इनपुट 1 हों", "any one input is 1", "कोई एक इनपुट 1 हो", "all inputs are 0", "सभी इनपुट 0 हों", 0,
        "AND का आउटपुट सभी इनपुट के 1 होने पर ही 1 होता है। कोई एक 1 OR का लक्षण है।"))
    A(c("digital", "The output of an OR gate is 0 only when:", "OR गेट का आउटपुट 0 तभी होता है जब:",
        "all inputs are 0", "सभी इनपुट 0 हों", "any one input is 1", "कोई एक इनपुट 1 हो", "all inputs are 1", "सभी इनपुट 1 हों", 0,
        "OR तभी 0 देता है जब हर इनपुट 0 हो।"))
    A(c("digital", "In a half adder, the sum output is:", "हाफ एडर में योग आउटपुट होता है:",
        "XOR of the two inputs", "दोनों इनपुट का XOR", "AND of the two inputs", "दोनों इनपुट का AND", "OR of the two inputs", "दोनों इनपुट का OR", 0,
        "हाफ एडर: Sum = A XOR B और Carry = A AND B।"))
    A(c("digital", "In a half adder, the carry output is:", "हाफ एडर में कैरी आउटपुट होता है:",
        "AND of the two inputs", "दोनों इनपुट का AND", "XOR of the two inputs", "दोनों इनपुट का XOR", "NOT of A", "A का NOT", 0,
        "कैरी तभी 1 होता है जब दोनों बिट 1 हों, यानी AND।"))
    A(c("digital", "A full adder differs from a half adder because it has:", "फुल एडर हाफ एडर से इसलिए भिन्न है क्योंकि उसमें होता है:",
        "an extra carry-in", "एक अतिरिक्त कैरी-इन", "only one input", "केवल एक इनपुट", "no sum output", "कोई योग आउटपुट नहीं", 0,
        "फुल एडर में A, B और Cin तीन इनपुट होते हैं।"))
    A(c("digital", "Which flip-flop removes the race-around problem of the JK flip-flop?", "JK फ्लिप-फ्लॉप की रेस-अराउंड समस्या कौन दूर करता है?",
        "Master-slave JK", "मास्टर-स्लेव JK", "An unclocked SR latch used as a counter", "काउंटर की तरह इस्तेमाल होने वाला बिना क्लॉक का SR लैच", "A simple wire", "एक साधारण तार", 0,
        "मास्टर-स्लेव विन्यास में आउटपुट घड़ी की एक ही धार पर बार-बार नहीं बदलता।"))
    A(c("digital", "A D flip-flop is used mainly to:", "D फ्लिप-फ्लॉप मुख्यतः किस काम आता है?",
        "store one bit", "एक बिट संचित करना", "add two 8-bit numbers in one gate", "एक गेट में दो 8-बिट संख्याएँ जोड़ना", "generate a network packet", "नेटवर्क पैकेट बनाना", 0,
        "D फ्लिप-फ्लॉप घड़ी के किनारे पर अपना इनपुट याद रखता है, इसलिए यह एक-बिट मेमोरी है।"))
    A(c("digital", "How many select lines does a 1-to-8 demultiplexer need?", "1-से-8 डीमल्टीप्लेक्सर को कितनी सिलेक्ट लाइनें चाहिए?",
        "3", "3", "8", "8", "1", "1", 0,
        "8 आउटपुट के लिए log2(8) = 3 सिलेक्ट लाइनें चाहिए।"))
    A(c("digital", "EEPROM differs from EPROM because EEPROM can be erased by:", "EEPROM, EPROM से भिन्न है क्योंकि EEPROM मिटाया जा सकता है:",
        "electrical signals", "विद्युत संकेतों से", "ultraviolet light only", "केवल पराबैंगनी प्रकाश से", "shaking the chip", "चिप हिलाकर", 0,
        "EPROM पराबैंगनी प्रकाश से मिटता है। EEPROM विद्युत रूप से मिटता और लिखता है।"))
    A(c("digital", "SRAM stores a bit using:", "SRAM एक बिट किससे रखता है?",
        "a flip-flop", "फ्लिप-फ्लॉप", "a charged capacitor that must be refreshed", "ऐसा आवेशित संधारित्र जिसे रिफ्रेश करना पड़ता है", "a magnetic tape", "चुंबकीय टेप", 0,
        "SRAM फ्लिप-फ्लॉप से बनता है। DRAM संधारित्र पर चार्ज रखता है और रिफ्रेश चाहता है।"))
    A(c("digital", "DRAM must be refreshed because:", "DRAM को रिफ्रेश क्यों करना पड़ता है?",
        "the charge on its capacitor leaks", "उसके संधारित्र का आवेश रिस जाता है", "it is made of ROM cells", "यह ROM सेल से बना है", "it has no address lines", "इसमें एड्रेस लाइन नहीं होती", 0,
        "DRAM का संधारित्र धीरे-धीरे डिस्चार्ज होता है, इसलिए समय-समय पर रिफ्रेश जरूरी है।"))
    A(c("digital", "The 2's complement system is preferred for signed integers because:", "चिह्नित पूर्णांकों के लिए 2's complement क्यों पसंद किया जाता है?",
        "subtraction can be done by addition of the complement", "घटाव, पूरक को जोड़कर किया जा सकता है", "it cannot represent zero", "यह शून्य नहीं दर्शा सकता", "it uses a separate subtractor for every bit and no adder", "यह हर बिट के लिए अलग सबट्रैक्टर रखता है और एडर नहीं", 0,
        "2's complement में जोड़ने वाला ही परिपथ घटाव भी कर लेता है और शून्य का एक ही रूप होता है।"))
    A(c("digital", "Which code is a minimum-change code, where neighbours differ by one bit?", "कौन-सा कोड न्यूनतम-परिवर्तन कोड है, जिसमें पड़ोसी एक बिट से भिन्न होते हैं?",
        "Gray code", "ग्रे कोड", "BCD used as a Gray code", "BCD को ग्रे कोड मानकर", "Excess-3 used as a one-bit code", "एक्ससेस-3 को एक-बिट कोड मानकर", 0,
        "ग्रे कोड में क्रमागत संख्याएँ केवल एक बिट बदलती हैं। इससे कुछ यांत्रिक त्रुटियाँ घटती हैं।"))
    A(c("digital", "An encoder with 8 inputs has how many outputs?", "8 इनपुट वाले एनकोडर के कितने आउटपुट होते हैं?",
        "3", "3", "8", "8", "16", "16", 0,
        "8-टू-3 एनकोडर आठ में से एक सक्रिय इनपुट को 3-बिट कोड में बदलता है।"))
    A(c("digital", "Which of the following is correct?", "निम्न में कौन सही है?",
        "NAND is universal", "NAND सार्वत्रिक है", "NOR is universal", "NOR सार्वत्रिक है", "AND alone is universal", "केवल AND सार्वत्रिक है", 3,
        "(A) और (B) सही हैं। केवल AND से NOT नहीं बनता, इसलिए वह अकेले सार्वत्रिक नहीं है। अतः (D)।"))
    A(c("digital", "De Morgan's first law says that the complement of a product equals:", "डी मॉर्गन का पहला नियम कहता है कि गुणनफल का पूरक बराबर है:",
        "the sum of the complements", "पूरकों का योग", "the product of the complements", "पूरकों का गुणन", "the same product", "वही गुणनफल", 0,
        "¬(A·B) = ¬A + ¬B। पूरकों का गुणन दूसरे नियम ¬(A+B) = ¬A·¬B का है।"))

    # COA
    A(c("coa", "The sequence fetch–decode–execute is called the:", "फेच–डिकोड–एक्जीक्यूट क्रम को कहते हैं:",
        "instruction cycle", "इंस्ट्रक्शन साइकिल", "DMA burst only", "केवल DMA बर्स्ट", "context switch of a thread", "थ्रेड का कॉन्टेक्स्ट स्विच", 0,
        "CPU हर निर्देश को लाता है, समझता है और चलाता है। यही निर्देश चक्र है।"))
    A(c("coa", "DMA is used to:", "DMA का उपयोग होता है:",
        "transfer data without continuous CPU intervention", "लगातार CPU के हस्तक्षेप के बिना डेटा भेजना", "compile a C program", "C प्रोग्राम कम्पाइल करना", "replace the ALU", "ALU को बदलना", 0,
        "डायरेक्ट मेमोरी एक्सेस में डिवाइस और मेमोरी के बीच डेटा जाता है और CPU केवल शुरुआत व अंत पर काम करता है।"))
    A(c("coa", "In a direct-mapped cache, a memory block can go to:", "डायरेक्ट-मैप्ड कैश में एक मेमोरी ब्लॉक जा सकता है:",
        "only one cache line", "केवल एक कैश लाइन में", "any line in the cache", "कैश की किसी भी लाइन में", "only the disk", "केवल डिस्क पर", 0,
        "डायरेक्ट मैपिंग में इंडेक्स बिट्स एक ही लाइन तय करते हैं। फुली असोसिएटिव में कोई भी लाइन हो सकती है।"))
    A(c("coa", "In a fully associative cache, a block may be placed in:", "फुली असोसिएटिव कैश में ब्लॉक रखा जा सकता है:",
        "any cache line", "किसी भी कैश लाइन में", "only line number 0", "केवल लाइन संख्या 0 में", "only ROM", "केवल ROM में", 0,
        "फुली असोसिएटिव कैश में प्लेसमेंट की कोई इंडेक्स बाध्यता नहीं होती।"))
    A(c("coa", "Locality of reference explains why:", "लोकलिटी ऑफ रेफरेंस समझाती है कि क्यों:",
        "a small cache can still give many hits", "छोटा कैश भी बहुत हिट दे सकता है", "disks are faster than registers", "डिस्क रजिस्टर से तेज होती है", "ROM is volatile", "ROM वोलेटाइल है", 0,
        "प्रोग्राम थोड़े समय में पास के पतों और हाल के पतों को फिर इस्तेमाल करते हैं, इसलिए छोटा कैश काम आता है।"))
    A(c("coa", "Write-back cache differs from write-through because write-back:", "राइट-बैक कैश राइट-थ्रू से भिन्न है क्योंकि राइट-बैक:",
        "updates main memory only when the block is replaced", "मुख्य मेमोरी को तभी अपडेट करता है जब ब्लॉक हटे", "writes memory on every store immediately and never marks a dirty bit", "हर स्टोर पर तुरंत मेमोरी लिखता है और डर्टी बिट नहीं रखता", "cannot be used with a CPU", "CPU के साथ इस्तेमाल नहीं हो सकता", 0,
        "राइट-थ्रू हर लिखत पर मेमोरी भी लिखता है। राइट-बैक ब्लॉक को डर्टी रखता है और बाद में लिखता है।"))
    A(c("coa", "RISC processors generally have:", "RISC प्रोसेसर में सामान्यतः होता है:",
        "a simple, fixed instruction format", "सरल, निश्चित निर्देश प्रारूप", "very complex instructions that do a whole program", "ऐसे बहुत जटिल निर्देश जो पूरा प्रोग्राम कर दें", "no registers", "कोई रजिस्टर नहीं", 0,
        "RISC सरल निर्देश और रजिस्टर-आधारित काम पर जोर देता है। CISC में निर्देश जटिल होते हैं।"))
    A(c("coa", "The ALU performs:", "ALU करता है:",
        "arithmetic and logical operations", "अंकगणित और तार्किक संक्रियाएँ", "only printing", "केवल छपाई", "only disk scheduling", "केवल डिस्क शेड्यूलिंग", 0,
        "अंकगणितीय और तार्किक इकाई जोड़, घटाव, AND, OR जैसे काम करती है।"))
    A(c("coa", "A program counter holds:", "प्रोग्राम काउंटर रखता है:",
        "the address of the next instruction", "अगले निर्देश का पता", "the result of the last addition only", "केवल पिछले जोड़ का परिणाम", "the name of the user", "उपयोगकर्ता का नाम", 0,
        "PC या IP अगले लाए जाने वाले निर्देश का पता रखता है।"))
    A(c("coa", "Interrupt-driven I/O is better than programmed I/O because:", "इंटरप्ट-ड्रिवन I/O प्रोग्राम्ड I/O से बेहतर है क्योंकि:",
        "the CPU need not poll the device continuously", "CPU को उपकरण से लगातार पूछते रहना नहीं पड़ता", "interrupts remove the need for a device", "इंटरप्ट से उपकरण की जरूरत खत्म हो जाती है", "it works only without a CPU", "यह केवल बिना CPU के चलता है", 0,
        "डिवाइस तैयार होने पर इंटरप्ट भेजता है। पोलिंग में CPU बार-बार स्टेटस जाँचता रहता है।"))
    A(c("coa", "Which memory is fastest among these?", "इनमें सबसे तेज मेमोरी कौन-सी है?",
        "CPU registers", "CPU रजिस्टर", "Main memory", "मुख्य मेमोरी", "Magnetic disk", "चुंबकीय डिस्क", 0,
        "रजिस्टर सबसे तेज, फिर कैश, फिर RAM, फिर डिस्क।"))
    A(c("coa", "Booth’s algorithm is used for:", "बूथ का एल्गोरिथ्म किसके लिए है?",
        "multiplication of signed binary numbers", "चिह्नित बाइनरी संख्याओं का गुणन", "sorting a linked list", "लिंक्ड लिस्ट को छाँटना", "deadlock detection", "डेडलॉक पहचान", 0,
        "बूथ एल्गोरिथ्म चिह्नित द्विआधारी गुणन को 2's complement में कुशलता से करता है।"))
    A(c("coa", "Endianness describes:", "एंडियननेस बताती है:",
        "the order of bytes in a multi-byte value", "बहु-बाइट मान में बाइटों का क्रम", "the speed of the CPU fan", "CPU पंखे की गति", "the number of users", "उपयोगकर्ताओं की संख्या", 0,
        "लिटल एंडियन में LSB छोटे पते पर होता है। बिग एंडियन में MSB छोटे पते पर होता है।"))

    # DS
    A(c("ds", "A stack follows:", "स्टैक अनुसरण करता है:",
        "LIFO", "LIFO", "FIFO", "FIFO", "Random eviction only", "केवल यादृच्छिक निष्कासन", 0,
        "स्टैक में जो आखिर में आया वह पहले निकलता है। कतार FIFO है।"))
    A(c("ds", "A queue follows:", "कतार अनुसरण करती है:",
        "FIFO", "FIFO", "LIFO", "LIFO", "Sorted order only", "केवल क्रमबद्ध क्रम", 0,
        "कतार में जो पहले आया वह पहले निकलता है।"))
    A(c("ds", "Inorder traversal of a binary search tree produces:", "बाइनरी सर्च ट्री का इनऑर्डर ट्रैवर्सल देता है:",
        "keys in sorted order", "कुंजियाँ क्रमबद्ध क्रम में", "keys in reverse level order always", "हमेशा उलटा लेवल ऑर्डर", "only the leaves", "केवल पत्ते", 0,
        "BST में बायाँ < रूट < दायाँ। इनऑर्डर बायाँ-रूट-दायाँ होने से क्रमबद्ध सूची मिलती है।"))
    A(c("ds", "A queue is the natural structure for:", "कतार स्वाभाविक संरचना है:",
        "breadth-first search", "ब्रेड्थ-फर्स्ट सर्च", "depth-first search recursion stack", "डेप्थ-फर्स्ट की रिकर्सन स्टैक", "expression evaluation with a stack", "स्टैक से व्यंजक गणना", 0,
        "BFS पड़ोसियों को कतार में रखता है। DFS स्टैक या रिकर्सन इस्तेमाल करता है।"))
    A(c("ds", "Which operation is O(1) at one end of a linked-list stack?", "लिंक्ड-लिस्ट स्टैक के एक सिरे पर कौन-सी संक्रिया O(1) है?",
        "Push and pop at the head", "हेड पर पुश और पॉप", "Finding the minimum in an unsorted list of n nodes without extra data", "अतिरिक्त डेटा के बिना n नोड की असॉर्टेड लिस्ट में न्यूनतम खोजना", "Binary search on the unsorted list", "असॉर्टेड लिस्ट पर बाइनरी सर्च", 0,
        "हेड पॉइंटर वाले स्टैक में पुश और पॉप स्थिर समय में होते हैं। न्यूनतम खोज रैखिक है।"))
    A(c("ds", "A complete binary tree with n nodes has height of order:", "n नोड वाले पूर्ण बाइनरी ट्री की ऊँचाई की कोटि है:",
        "log n", "log n", "n", "n", "n²", "n²", 0,
        "हर स्तर लगभग दोगुना होता है, इसलिए ऊँचाई Θ(log n) है।"))
    A(c("ds", "An AVL tree maintains:", "AVL ट्री बनाए रखता है:",
        "balance factor of every node in {−1, 0, 1}", "हर नोड का बैलेंस फैक्टर {−1, 0, 1} में", "all keys equal", "सभी कुंजियाँ समान", "no rotations ever", "कभी कोई रोटेशन नहीं", 0,
        "AVL में बाएँ और दाएँ उपवृक्षों की ऊँचाई का अंतर अधिकतम 1 रहता है। असंतुलन पर रोटेशन होता है।"))
    A(c("ds", "A hash table gives average-case search time of:", "हैश टेबल में खोज का औसत समय है:",
        "O(1)", "O(1)", "O(n log n) always, even with a good hash", "अच्छे हैश के बावजूद हमेशा O(n log n)", "O(n²) as the designed average", "डिज़ाइन किया औसत O(n²)", 0,
        "अच्छे हैश और कम लोड फैक्टर पर औसत खोज O(1) होती है। टक्कर होने पर श्रृंखला लंबी हो सकती है।"))
    A(c("ds", "Chaining handles a hash collision by:", "चेनिंग हैश टक्कर को कैसे सँभालती है?",
        "keeping a linked list at the bucket", "बकेट पर लिंक्ड लिस्ट रखकर", "deleting the key forever", "कुंजी को हमेशा मिटाकर", "changing the key’s value to zero only", "कुंजी का मान केवल शून्य कर", 0,
        "एक ही हैश वाली कुंजियाँ उस बकेट की लिस्ट में जुड़ जाती हैं।"))
    A(c("ds", "A binary tree with n nodes has how many edges, if it is connected as a tree?", "ट्री के रूप में जुड़े n नोड वाले बाइनरी ट्री में कितने किनारे होते हैं?",
        "n − 1", "n − 1", "n", "n", "n(n − 1)/2", "n(n − 1)/2", 0,
        "हर ट्री में किनारे = नोड − 1। n(n−1)/2 पूर्ण ग्राफ का सूत्र है।"))
    A(c("ds", "Postfix expression evaluation uses a:", "पोस्टफिक्स व्यंजक की गणना किससे होती है?",
        "stack", "स्टैक", "queue of operators only with no values", "बिना मानों के केवल ऑपरेटरों की कतार", "hash table of syntax errors", "सिंटैक्स त्रुटियों की हैश टेबल", 0,
        "ऑपरेंड स्टैक पर रखे जाते हैं और ऑपरेटर आते ही दो मान निकालकर परिणाम वापस रख दिया जाता है।"))
    A(c("ds", "A priority queue is efficiently implemented with a:", "प्रायोरिटी क्यू को कुशलता से किससे बनाते हैं?",
        "heap", "हीप", "unsorted tape that must be rewound fully for every operation", "ऐसा असॉर्टेड टेप जिसे हर संक्रिया पर पूरा उल्टा घुमाना पड़े", "single Boolean variable", "एक बूलियन चर", 0,
        "बाइनरी हीप में डालना और न्यूनतम/अधिकतम निकालना O(log n) में होता है।"))
    A(c("ds", "In a max-heap, the parent is:", "मैक्स-हीप में माता-पिता होता है:",
        "greater than or equal to its children", "अपने बच्चों से बड़ा या बराबर", "always a leaf", "हमेशा पत्ता", "smaller than both children", "दोनों बच्चों से छोटा", 0,
        "मैक्स-हीप में रूट सबसे बड़ा होता है। मिन-हीप में माता-पिता छोटा होता है।"))
    A(c("ds", "Which of the following is correct?", "निम्न में कौन सही है?",
        "Stack is LIFO", "स्टैक LIFO है", "Queue is FIFO", "कतार FIFO है", "Stack is FIFO", "स्टैक FIFO है", 3,
        "(A) और (B) सही हैं। (C) गलत है। अतः (D)।"))

    # algorithms
    A(c("algo", "Binary search requires the array to be:", "बाइनरी सर्च के लिए ऐरे का होना जरूरी है:",
        "sorted", "क्रमबद्ध", "a linked list of random values with no order and no extra index", "बिना क्रम और बिना अतिरिक्त इंडेक्स की यादृच्छिक लिंक्ड लिस्ट", "of odd length only", "केवल विषम लंबाई", 0,
        "बाइनरी सर्च बीच वाला तत्व देखकर आधा भाग छोड़ती है। बिना क्रम के यह सही नहीं रहती।"))
    A(c("algo", "The average time of quicksort is:", "क्विकसॉर्ट का औसत समय है:",
        "O(n log n)", "O(n log n)", "O(n²) as its average", "औसत के रूप में O(n²)", "O(log n)", "O(log n)", 0,
        "अच्छे पिवट पर औसत O(n log n) है। सबसे खराब स्थिति, जब पिवट हमेशा किनारे का हो, O(n²) है।"))
    A(c("algo", "The worst-case time of quicksort is:", "क्विकसॉर्ट का सबसे खराब समय है:",
        "O(n²)", "O(n²)", "O(n log n) in every worst case", "हर खराब स्थिति में O(n log n)", "O(1)", "O(1)", 0,
        "पहले से क्रमबद्ध इनपुट और खराब पिवट चयन पर क्विकसॉर्ट O(n²) हो जाता है।"))
    A(c("algo", "Mergesort is:", "मर्जसॉर्ट है:",
        "O(n log n) and stable", "O(n log n) और स्टेबल", "O(n²) and unstable by design", "डिज़ाइन से O(n²) और अस्थिर", "a hashing method", "एक हैशिंग विधि", 0,
        "मर्जसॉर्ट हमेशा O(n log n) लेता है और समान कुंजियों का क्रम नहीं बिगाड़ता, इसलिए स्टेबल है।"))
    A(c("algo", "Heapsort has worst-case time:", "हीपसॉर्ट का सबसे खराब समय है:",
        "O(n log n)", "O(n log n)", "O(n²)", "O(n²)", "O(n)", "O(n)", 0,
        "हीप बनाकर बार-बार रूट निकालने की कीमत O(n log n) है।"))
    A(c("algo", "Bubble sort’s typical time complexity is:", "बबल सॉर्ट की सामान्य समय जटिलता है:",
        "O(n²)", "O(n²)", "O(log n)", "O(log n)", "O(n log n) as its standard bound", "मानक सीमा के रूप में O(n log n)", 0,
        "पासों में पास के तत्वों की अदला-बदली के कारण बबल सॉर्ट O(n²) है।"))
    A(c("algo", "Insertion sort’s best case, on a sorted array, is:", "क्रमबद्ध ऐरे पर इंसर्शन सॉर्ट की सर्वोत्तम स्थिति है:",
        "O(n)", "O(n)", "O(n²) even when already sorted", "पहले से क्रमबद्ध होने पर भी O(n²)", "O(1)", "O(1)", 0,
        "अगर ऐरे क्रमबद्ध है तो हर तत्व एक ही तुलना में अपनी जगह रह जाता है, कुल O(n)।"))
    A(c("algo", "Dijkstra’s algorithm requires edge weights to be:", "डायक्स्ट्रा एल्गोरिथ्म के लिए किनारों के भार होने चाहिए:",
        "non-negative", "ऋणेतर", "always negative", "हमेशा ऋणात्मक", "complex numbers", "सम्मिश्र संख्याएँ", 0,
        "डायक्स्ट्रा ऋणात्मक भार पर सही नहीं रहता। ऋणात्मक भार के लिए बेलमैन-फोर्ड इस्तेमाल होता है।"))
    A(c("algo", "BFS on an unweighted graph finds:", "अभारित ग्राफ पर BFS निकालता है:",
        "a shortest path in number of edges", "किनारों की संख्या में सबसे छोटा पथ", "a minimum spanning tree by itself", "अपने आप न्यूनतम स्पैनिंग ट्री", "a topological order of a graph that has a cycle", "चक्र वाले ग्राफ का टोपोलॉजिकल क्रम", 0,
        "सभी भार 1 हों तो BFS किनारे-गिनती में सबसे छोटा रास्ता देता है। MST के लिए प्रिम या क्रुस्कल चाहिए।"))
    A(c("algo", "Kruskal’s algorithm finds a:", "क्रुस्कल का एल्गोरिथ्म निकालता है:",
        "minimum spanning tree", "न्यूनतम स्पैनिंग ट्री", "shortest path from one source in a graph with negative cycles", "ऋणात्मक चक्र वाले ग्राफ में एक स्रोत से सबसे छोटा पथ", "maximum flow", "अधिकतम प्रवाह", 0,
        "क्रुस्कल किनारों को भार के क्रम में जोड़ता है और चक्र बनाने वाला किनारा छोड़ता है।"))
    A(c("algo", "A spanning tree of a connected graph with n vertices has:", "n शीर्षों वाले जुड़े ग्राफ के स्पैनिंग ट्री में होते हैं:",
        "n − 1 edges", "n − 1 किनारे", "n edges", "n किनारे", "n² edges", "n² किनारे", 0,
        "स्पैनिंग ट्री सभी शीर्षों को जोड़ता है और चक्र नहीं रखता, इसलिए किनारे n−1 होते हैं।"))
    A(c("algo", "The comparison-sort lower bound is:", "तुलना-आधारित सॉर्ट की निचली सीमा है:",
        "Ω(n log n)", "Ω(n log n)", "Ω(n)", "Ω(n)", "Ω(1)", "Ω(1)", 0,
        "तुलनाओं से निर्णय-वृक्ष की ऊँचाई कम से कम log(n!) यानी Ω(n log n) होती है। काउंटिंग सॉर्ट तुलना नहीं करता।"))
    A(c("algo", "Counting sort is suitable when:", "काउंटिंग सॉर्ट तब उपयुक्त है जब:",
        "keys are integers in a limited range", "कुंजियाँ सीमित परास के पूर्णांक हों", "keys are arbitrary strings with no bound", "कुंजियाँ बिना सीमा की मनमानी स्ट्रिंग हों", "the array must be sorted by comparisons only and keys are real numbers", "ऐरे केवल तुलना से छाँटना हो और कुंजियाँ वास्तविक संख्याएँ हों", 0,
        "काउंटिंग सॉर्ट O(n + k) है, जहाँ k परास है। परास बहुत बड़ा हो तो यह महँगा पड़ जाता है।"))
    A(c("algo", "Topological sort is defined for a:", "टोपोलॉजिकल सॉर्ट किसके लिए परिभाषित है?",
        "directed acyclic graph", "दिशात्मक चक्रहीन ग्राफ", "undirected graph with a cycle", "चक्र वाले अदिश ग्राफ", "complete undirected graph only", "केवल पूर्ण अदिश ग्राफ", 0,
        "DAG में किनारों की दिशा का सम्मान करते हुए रेखीय क्रम निकाला जा सकता है। चक्र हो तो ऐसा क्रम नहीं होता।"))
    A(c("algo", "The recurrence T(n) = 2T(n/2) + O(n) solves to:", "पुनरावृत्ति T(n) = 2T(n/2) + O(n) का हल है:",
        "O(n log n)", "O(n log n)", "O(n)", "O(n)", "O(log n)", "O(log n)", 0,
        "यह मर्जसॉर्ट वाली पुनरावृत्ति है। मास्टर प्रमेय से O(n log n) मिलता है।"))
    A(c("algo", "Which of the following is correct?", "निम्न में कौन सही है?",
        "Mergesort worst case is O(n log n)", "मर्जसॉर्ट की खराब स्थिति O(n log n) है", "Binary search needs a sorted array", "बाइनरी सर्च को क्रमबद्ध ऐरे चाहिए", "Dijkstra allows negative-weight cycles safely", "डायक्स्ट्रा ऋणात्मक चक्रों को सुरक्षित ढंग से सँभालता है", 3,
        "(A) और (B) सही हैं। डायक्स्ट्रा ऋणात्मक भार पर भरोसेमंद नहीं है। अतः (D)।"))

    # programming
    A(c("programming", "In C, the value of an uninitialized automatic local variable is:", "C में अनारंभीकृत ऑटोमैटिक स्थानीय चर का मान होता है:",
        "indeterminate", "अनिर्धारित", "always 0 by the language rule for auto locals", "भाषा-नियम से auto स्थानीय चर हमेशा 0", "always NULL for an int", "int के लिए हमेशा NULL", 0,
        "static और वैश्विक चर शून्य से शुरू होते हैं। साधारण स्थानीय चर का मान कचरा हो सकता है।"))
    A(c("programming", "malloc in C returns memory that is:", "C में malloc जो मेमोरी देता है वह:",
        "uninitialized", "अनारंभीकृत", "always filled with zero", "हमेशा शून्य से भरी", "taken from the instruction ROM", "इंस्ट्रक्शन ROM से ली गई", 0,
        "शून्य से भरी मेमोरी के लिए calloc इस्तेमाल होता है। malloc केवल ब्लॉक देता है।"))
    A(c("programming", "A memory leak in C usually means:", "C में मेमोरी लीक का अर्थ प्रायः है:",
        "allocated memory was never freed", "आवंटित मेमोरी कभी मुक्त नहीं हुई", "a comment was deleted", "एक टिप्पणी मिट गई", "the compiler optimised a loop", "कम्पाइलर ने लूप अनुकूलित किया", 0,
        "malloc से ली जगह free न करने पर प्रोग्राम चलते हुए मेमोरी खोता रहता है।"))
    A(c("programming", "In call by value:", "कॉल बाय वैल्यू में:",
        "the function receives a copy of the argument", "फलन को तर्क की प्रति मिलती है", "the callee always changes the caller’s variable", "बुलाने वाला चर हमेशा बदल जाता है", "no arguments can be passed", "कोई तर्क नहीं भेजा जा सकता", 0,
        "प्रति बदलने से मूल चर नहीं बदलता। मूल बदलने के लिए C में पता भेजते हैं।"))
    A(c("programming", "In C, the expression a[i] is equivalent to:", "C में व्यंजक a[i] समतुल्य है:",
        "*(a + i)", "*(a + i)", "a + *i", "a + *i", "&a + i with no dereference", "बिना डिरेफरेंस के &a + i", 0,
        "ऐरे का नाम पहले तत्व का पता होता है। a[i] उसी पते से i तत्व आगे का मान है।"))
    A(c("programming", "A recursive function must have:", "रिकर्सिव फलन में होना ही चाहिए:",
        "a base case", "आधार स्थिति", "no parameters", "कोई पैरामीटर नहीं", "a global variable only and no return", "केवल वैश्विक चर और कोई रिटर्न नहीं", 0,
        "आधार स्थिति रुकने की शर्त है। उसके बिना कॉल स्टैक बढ़ता रहता है।"))
    A(c("programming", "Java programs are compiled into:", "जावा प्रोग्राम कम्पाइल होकर बनते हैं:",
        "bytecode for the JVM", "JVM के लिए बाइटकोड", "a single native .exe that never needs a runtime", "ऐसी एक नेटिव .exe जिसे कभी रनटाइम न चाहिए", "only assembly for the 8085", "केवल 8085 की असेंबली", 0,
        "javac बाइटकोड बनाता है और JVM उसे चलाती है। इसी से ‘एक बार लिखो, कहीं भी चलाओ’ कहा जाता है।"))
    A(c("programming", "Python is mainly:", "पायथन मुख्यतः है:",
        "an interpreted language", "एक इंटरप्रेटेड भाषा", "a language that must be assembled for the 8085 before any run", "ऐसी भाषा जिसे हर रन से पहले 8085 पर असेंबल करना पड़ता है", "a markup language", "एक मार्कअप भाषा", 0,
        "पायथन स्रोत को इंटरप्रेटर/बाइटकोड के जरिए चलाया जाता है। HTML मार्कअप है।"))
    A(c("programming", "Which header is required in C for printf?", "C में printf के लिए कौन-सा हैडर चाहिए?",
        "stdio.h", "stdio.h", "math.h only", "केवल math.h", "stdlib.h only for printf", "printf के लिए केवल stdlib.h", 0,
        "printf और scanf का घोषणा-पत्र stdio.h में है। math.h गणित फलनों के लिए है।"))
    A(c("programming", "The break statement inside a loop:", "लूप के अंदर break कथन:",
        "terminates that loop", "उस लूप को समाप्त करता है", "skips only the next statement and continues the loop", "केवल अगला कथन छोड़ता है और लूप जारी रहता है", "restarts the computer", "कम्प्यूटर पुनः चालू करता है", 0,
        "break लूप या स्विच से बाहर कर देता है। अगला कथन छोड़ने का काम continue करता है।"))
    A(c("programming", "continue inside a loop:", "लूप के अंदर continue:",
        "skips the rest of the current iteration", "वर्तमान चक्कर का शेष भाग छोड़ देता है", "ends the whole program", "पूरा प्रोग्राम समाप्त कर देता है", "deletes the array", "ऐरे मिटा देता है", 0,
        "continue नियंत्रण को लूप की अगली जाँच पर ले जाता है।"))
    A(c("programming", "In C, sizeof(char) is:", "C में sizeof(char) होता है:",
        "1", "1", "4 always on every historical compiler as a language rule different from 1", "भाषा-नियम से हमेशा 4, 1 से भिन्न", "0", "0", 0,
        "C मानक sizeof(char) को 1 परिभाषित करता है। int का आकार कार्यान्वयन पर निर्भर है।"))

    # OOP
    A(c("oop", "Encapsulation means:", "एनकैप्सुलेशन का अर्थ है:",
        "bundling data with the methods that operate on it, and hiding details", "डेटा और उस पर काम करने वाली विधियों को बाँधना तथा विवरण छिपाना", "writing only global variables", "केवल वैश्विक चर लिखना", "removing all classes", "सभी क्लास हटाना", 0,
        "एनकैप्सुलेशन डेटा और व्यवहार को एक इकाई में रखता है और अनावश्यक विवरण छिपाता है।"))
    A(c("oop", "Inheritance provides:", "इनहेरिटेंस देता है:",
        "reuse of a base class by a derived class", "आधार क्लास का व्युत्पन्न क्लास द्वारा पुनः उपयोग", "only multiple main methods", "केवल अनेक main विधियाँ", "deletion of the base class", "आधार क्लास को मिटाना", 0,
        "व्युत्पन्न क्लास आधार क्लास के सदस्य पाती है और उन्हें बढ़ा सकती है।"))
    A(c("oop", "Method overriding means:", "मेथड ओवरराइडिंग का अर्थ है:",
        "a subclass provides its own version of a superclass method", "उपवर्ग, सुपरक्लास की विधि का अपना रूप देता है", "two methods in one class differ only by parameter list", "एक ही क्लास में दो विधियाँ केवल पैरामीटर सूची से भिन्न हों", "a variable changes type at runtime without a class", "बिना क्लास के चर रनटाइम पर प्रकार बदले", 0,
        "ओवरराइडिंग रनटाइम पॉलिमॉर्फिज्म है। पैरामीटर बदलना ओवरलोडिंग है।"))
    A(c("oop", "Method overloading is decided at:", "मेथड ओवरलोडिंग का निर्णय होता है:",
        "compile time", "कम्पाइल समय", "only after the program has finished", "केवल प्रोग्राम समाप्त होने के बाद", "link time of a pure virtual call", "शुद्ध वर्चुअल कॉल के लिंक समय पर नहीं, बल्कि यह ओवरराइडिंग है", 0,
        "ओवरलोडिंग कम्पाइल-टाइम पॉलिमॉर्फिज्म है, क्योंकि हस्ताक्षर पहले से معلوم होता है।"))
    A(c("oop", "A pure virtual function in C++ makes the class:", "C++ में शुद्ध वर्चुअल फलन क्लास को बना देता है:",
        "abstract", "अमूर्त", "final and instantiable with no restriction", "अंतिम और बिना रोक के वस्तु बनाने योग्य", "a namespace", "एक नेमस्पेस", 0,
        "शुद्ध वर्चुअल फलन वाली क्लास की वस्तु सीधे नहीं बनाई जा सकती।"))
    A(c("oop", "Java does not support:", "जावा समर्थन नहीं करता:",
        "multiple class inheritance", "एकाधिक क्लास इनहेरिटेंस", "interfaces", "इंटरफेस", "single inheritance", "एकल इनहेरिटेंस", 0,
        "जावा में एक क्लास केवल एक क्लास को विस्तार देती है। अनेक इंटरफेस लागू किए जा सकते हैं।"))
    A(c("oop", "A constructor:", "कन्स्ट्रक्टर:",
        "initialises a newly created object", "नई बनी वस्तु को आरम्भ करता है", "is called only when the object is deleted", "केवल वस्तु मिटते समय बुलाया जाता है", "must return int", "int लौटाना जरूरी है", 0,
        "कन्स्ट्रक्टर वस्तु बनते समय चलता है। मिटते समय डिस्ट्रक्टर या जावा में गार्बेज कलेक्टर काम आता है।"))
    A(c("oop", "Which of the following is correct?", "निम्न में कौन सही है?",
        "Overloading is compile-time polymorphism", "ओवरलोडिंग कम्पाइल-टाइम पॉलिमॉर्फिज्म है", "Overriding is run-time polymorphism", "ओवरराइडिंग रन-टाइम पॉलिमॉर्फिज्म है", "Overloading and overriding are the same thing", "ओवरलोडिंग और ओवरराइडिंग एक ही चीज हैं", 3,
        "(A) और (B) सही हैं। दोनों एक नहीं हैं। अतः (D)।"))

    # OS
    A(c("os", "A process is:", "प्रोसेस है:",
        "a program in execution", "क्रियान्वयन में एक प्रोग्राम", "only the source file on disk", "केवल डिस्क पर स्रोत फाइल", "a keyboard", "एक कीबोर्ड", 0,
        "प्रोग्राम निष्क्रिय फाइल है। चलने पर वह प्रोसेस बनता है और उसका PCB होता है।"))
    A(c("os", "A thread is:", "थ्रेड है:",
        "a lightweight unit of execution inside a process", "प्रोसेस के अंदर निष्पादन की हल्की इकाई", "a separate address space that never shares memory", "ऐसा अलग पता-स्थान जो कभी मेमोरी साझा नहीं करता", "a file system", "एक फाइल सिस्टम", 0,
        "एक प्रोसेस के थ्रेड कोड और डेटा साझा करते हैं, पर अपना स्टैक रखते हैं।"))
    A(c("os", "Which is NOT a necessary condition for deadlock?", "डेडलॉक की आवश्यक शर्त कौन-सी नहीं है?",
        "Preemption of every resource is freely allowed", "हर संसाधन को स्वतंत्र रूप से छीना जा सके", "Mutual exclusion", "परस्पर अपवर्जन", "Circular wait", "वृत्तीय प्रतीक्षा", 0,
        "डेडलॉक की चार शर्तें हैं: म्यूचुअल एक्सक्लूजन, होल्ड एंड वेट, नो प्रीएम्पशन, सर्कुलर वेट। स्वतंत्र प्रीएम्पशन इनके विपरीत है।"))
    A(c("os", "Round Robin scheduling uses a:", "राउंड रॉबिन शेड्यूलिंग इस्तेमाल करती है:",
        "time quantum", "टाइम क्वांटम", "shortest job chosen only once at the start and never switched", "शुरुआत में एक बार चुना गया सबसे छोटा काम जिसे कभी न बदला जाए", "banker’s matrix only", "केवल बैंकर मैट्रिक्स", 0,
        "हर प्रोसेस को क्वांटम भर चलने का मौका मिलता है, फिर वह कतार के अंत में चला जाता है।"))
    A(c("os", "Belady’s anomaly can occur in:", "बेलेडी की विसंगति हो सकती है:",
        "FIFO page replacement", "FIFO पेज रिप्लेसमेंट", "LRU as a typical case of Belady", "बेलेडी के सामान्य उदाहरण के रूप में LRU", "the optimal algorithm", "इष्टतम एल्गोरिथ्म", 0,
        "FIFO में फ्रेम बढ़ाने पर भी फॉल्ट बढ़ सकते हैं। LRU और ऑप्टिमल स्टैक एल्गोरिथ्म हैं और यह विसंगति नहीं दिखाते।"))
    A(c("os", "Thrashing happens when:", "थ्रैशिंग तब होती है जब:",
        "the system spends most of its time paging", "सिस्टम अपना अधिकांश समय पेजिंग में लगाए", "the CPU is idle because there is no program", "कोई प्रोग्राम न होने से CPU खाली हो", "the disk is removed", "डिस्क निकाल दी जाए", 0,
        "बहुत अधिक मल्टीप्रोग्रामिंग से हर प्रोसेस को कम फ्रेम मिलते हैं और पेज फॉल्ट ही पेज फॉल्ट होते रहते हैं।"))
    A(c("os", "Internal fragmentation is typical of:", "आंतरिक विखंडन किसमें आम है?",
        "fixed-size paging", "निश्चित आकार की पेजिंग", "segmentation only, with no unused space inside a segment", "केवल सेगमेंटेशन, जिसमें खंड के अंदर खाली जगह न हो", "a contiguous file that uses every byte", "ऐसी सन्निहित फाइल जो हर बाइट इस्तेमाल करे", 0,
        "पेज का आखिरी हिस्सा खाली रह सकता है। सेगमेंटेशन में बाहरी विखंडन अधिक चर्चित है।"))
    A(c("os", "The Banker’s algorithm is used for:", "बैंकर एल्गोरिथ्म किसके लिए है?",
        "deadlock avoidance", "डेडलॉक परिहार", "CPU scheduling by time slice", "टाइम स्लाइस से CPU शेड्यूलिंग", "disk formatting", "डिस्क फॉर्मेटिंग", 0,
        "बैंकर एल्गोरिथ्म सुरक्षित अवस्था जाँचकर संसाधन तभी देता है जब डेडलॉक न बने।"))
    A(c("os", "A semaphore is used for:", "सेमाफोर इस्तेमाल होता है:",
        "process synchronisation", "प्रोसेस तुल्यकालन", "compiling SQL", "SQL कम्पाइल करना", "pixel colour", "पिक्सेल का रंग", 0,
        "डाइक्स्ट्रा का सेमाफोर wait और signal से क्रिटिकल सेक्शन और गिनती दोनों सँभालता है।"))
    A(c("os", "The fork() system call in Unix returns 0 to:", "यूनिक्स में fork() सिस्टम कॉल 0 किसे लौटाता है?",
        "the child process", "चाइल्ड प्रोसेस", "the parent process", "पैरेंट प्रोसेस", "neither; it returns −1 to both on success", "किसी को नहीं; सफलता पर दोनों को −1", 0,
        "सफल fork में बच्चे को 0 और माता-पिता को बच्चे का PID मिलता है। विफलता पर माता-पिता को −1 मिलता है।"))
    A(c("os", "A zombie process is one that:", "जॉम्बी प्रोसेस वह है जो:",
        "has finished but whose parent has not yet collected its status", "समाप्त हो चुकी है पर माता-पिता ने अभी उसकी स्थिति नहीं ली", "is running on two CPUs at once by definition", "परिभाषा से एक साथ दो CPU पर चल रही है", "has no PID", "जिसका कोई PID नहीं", 0,
        "बच्चा समाप्त हो चुका है, पर wait न होने से उसकी एंट्री प्रोसेस टेबल में रहती है।"))
    A(c("os", "Demand paging means:", "डिमांड पेजिंग का अर्थ है:",
        "a page is loaded only when it is referenced", "पेज तभी लाया जाता है जब उसका संदर्भ हो", "all pages are loaded before execution and never fault", "निष्पादन से पहले सभी पेज लाद दिए जाते हैं और फॉल्ट नहीं होता", "pages are stored in the register file", "पेज रजिस्टर फाइल में रखे जाते हैं", 0,
        "शुरुआत में पूरा प्रोग्राम मेमोरी में नहीं आता। जरूरत पर पेज फॉल्ट होकर पेज आता है।"))
    A(c("os", "SCAN disk scheduling moves the head:", "SCAN डिस्क शेड्यूलिंग हेड को चलाती है:",
        "in one direction serving requests, then reverses", "एक दिशा में अनुरोध पूरे करती है, फिर उल्टी चलती है", "randomly", "यादृच्छिक रूप से", "only toward cylinder 0 and then stops forever", "केवल सिलिंडर 0 की ओर और फिर हमेशा रुक जाती है", 0,
        "SCAN लिफ्ट की तरह एक दिशा में जाते हुए अनुरोध लेती है और सिरे पर दिशा बदलती है।"))
    A(c("os", "Which of the following is correct about deadlock?", "डेडलॉक के बारे में कौन सही है?",
        "Circular wait is a necessary condition", "वृत्तीय प्रतीक्षा एक आवश्यक शर्त है", "Mutual exclusion is a necessary condition", "परस्पर अपवर्जन एक आवश्यक शर्त है", "Deadlock can occur with only one process that needs no second resource and no wait", "केवल एक प्रोसेस से डेडलॉक हो सकता है जिसे न दूसरे संसाधन की जरूरत हो न प्रतीक्षा", 3,
        "(A) और (B) आवश्यक शर्तें हैं। एक अकेला प्रोसेस बिना प्रतीक्षा के डेडलॉक नहीं बनाता। अतः (D)।"))

    # DBMS
    A(c("dbms", "A primary key:", "प्राथमिक कुंजी:",
        "uniquely identifies a row and cannot be NULL", "पंक्ति को अद्वितीय पहचानती है और NULL नहीं हो सकती", "may be duplicated", "दोहराई जा सकती है", "must be a foreign key of the same table pointing to itself with duplicates", "उसी तालिका की ऐसी विदेशी कुंजी होनी चाहिए जो दोहराव रखे", 0,
        "प्राथमिक कुंजी अद्वितीय और NOT NULL होती है।"))
    A(c("dbms", "A foreign key:", "विदेशी कुंजी:",
        "refers to a candidate key of another relation", "दूसरे संबंध की उम्मीदवार कुंजी की ओर संकेत करती है", "must always be the table’s only column", "हमेशा तालिका का एकमात्र स्तम्भ होनी चाहिए", "forbids joins", "जॉइन मना करती है", 0,
        "फॉरेन की संदर्भित कुंजी के मानों तक सीमित रहकर संबंध जोड़ती है।"))
    A(c("dbms", "Third normal form removes:", "तीसरी सामान्य रूप हटाता है:",
        "transitive dependency of non-key attributes", "गैर-कुंजी गुणों की संक्रमणीय निर्भरता", "all tables", "सभी तालिकाएँ", "the primary key itself", "स्वयं प्राथमिक कुंजी", 0,
        "3NF में कोई गैर-प्रमुख गुण किसी अन्य गैर-प्रमुख गुण पर संक्रमण से निर्भर नहीं रहना चाहिए।"))
    A(c("dbms", "Second normal form removes:", "दूसरी सामान्य रूप हटाती है:",
        "partial dependency on a composite key", "संयुक्त कुंजी पर आंशिक निर्भरता", "all foreign keys", "सभी विदेशी कुंजियाँ", "NULL values by forbidding them in every column", "हर स्तम्भ में NULL मना करके", 0,
        "2NF के लिए पहले 1NF चाहिए और आंशिक निर्भरता नहीं होनी चाहिए।"))
    A(c("dbms", "ACID ‘A’ stands for:", "ACID में ‘A’ का अर्थ है:",
        "Atomicity", "परमाणुता", "Availability only in the CAP sense inside ACID", "ACID के अंदर CAP वाले अर्थ में केवल उपलब्धता", "Aggregation", "एकत्रीकरण", 0,
        "ACID: Atomicity, Consistency, Isolation, Durability। उपलब्धता CAP प्रमेय का शब्द है।"))
    A(c("dbms", "GRANT and REVOKE are:", "GRANT और REVOKE हैं:",
        "DCL commands", "DCL आदेश", "DDL commands that create tables", "तालिका बनाने वाले DDL आदेश", "TCL commands that commit a transaction", "लेनदेन कमिट करने वाले TCL आदेश", 0,
        "डेटा कंट्रोल लैंग्वेज अधिकार देती और लेती है। COMMIT और ROLLBACK TCL हैं। CREATE DDL है।"))
    A(c("dbms", "COMMIT is a:", "COMMIT है:",
        "TCL command", "TCL आदेश", "DDL command", "DDL आदेश", "DML command that only reads rows", "केवल पंक्तियाँ पढ़ने वाला DML आदेश", 0,
        "COMMIT लेनदेन को स्थायी करता है। यह ट्रांजैक्शन कंट्रोल लैंग्वेज का हिस्सा है।"))
    A(c("dbms", "HAVING differs from WHERE because HAVING:", "HAVING, WHERE से भिन्न है क्योंकि HAVING:",
        "filters groups after aggregation", "एकत्रीकरण के बाद समूहों को छानता है", "filters rows before grouping and cannot use aggregates", "समूह से पहले पंक्तियाँ छानता है और समुच्चय नहीं इस्तेमाल कर सकता — यह WHERE है", "sorts the output", "आउटपुट क्रमबद्ध करता है", 0,
        "WHERE समूह बनने से पहले लगता है। HAVING समूहों पर शर्त लगाता है, जैसे COUNT के बाद।"))
    A(c("dbms", "A view is:", "व्यू है:",
        "a stored query that looks like a virtual table", "एक संचित क्वेरी जो आभासी तालिका जैसी दिखती है", "always a physical copy that cannot be defined by SELECT", "हमेशा ऐसी भौतिक प्रति जिसे SELECT से परिभाषित न किया जा सके", "an index", "एक इंडेक्स", 0,
        "व्यू की परिभाषा क्वेरी होती है। साधारण व्यू अपना अलग डेटा नहीं रखता।"))
    A(c("dbms", "INNER JOIN returns:", "INNER JOIN लौटाता है:",
        "only matching rows from both tables", "केवल दोनों तालिकाओं की मेल खाती पंक्तियाँ", "all rows of the left table even without a match", "बिना मेल के भी बाईं तालिका की सभी पंक्तियाँ", "the Cartesian product with no condition ever", "बिना किसी शर्त के हमेशा कार्तीय गुणन", 0,
        "इनर जॉइन केवल मेल रखता है। बिना मेल की बाईं पंक्तियाँ LEFT JOIN में आती हैं।"))
    A(c("dbms", "NULL in SQL means:", "SQL में NULL का अर्थ है:",
        "unknown or missing", "अज्ञात या अनुपस्थित", "zero", "शून्य", "an empty string in every DBMS by definition", "परिभाषा से हर DBMS में खाली स्ट्रिंग", 0,
        "NULL शून्य या खाली स्ट्रिंग नहीं है। NULL के साथ तुलना UNKNOWN देती है।"))
    A(c("dbms", "An index is used mainly to:", "इंडेक्स मुख्यतः किसके लिए होता है?",
        "speed up search", "खोज तेज करना", "remove the need for a key", "कुंजी की जरूरत मिटाना", "store images only", "केवल चित्र रखना", 0,
        "इंडेक्स खोज को तेज करता है, पर लिखने पर अतिरिक्त लागत आती है।"))
    A(c("dbms", "Which of the following is correct?", "निम्न में कौन सही है?",
        "WHERE filters rows before grouping", "WHERE समूह से पहले पंक्तियाँ छानता है", "HAVING filters groups", "HAVING समूह छानता है", "NULL is the same as zero", "NULL और शून्य एक ही हैं", 3,
        "(A) और (B) सही हैं। NULL शून्य नहीं है। अतः (D)।"))
    A(c("dbms", "1NF requires that attribute values be:", "1NF माँग करता है कि गुणों के मान हों:",
        "atomic", "परमाण्विक", "lists of lists", "सूचियों की सूचियाँ", "duplicate primary keys", "दोहराई प्राथमिक कुंजियाँ", 0,
        "पहली सामान्य रूप में हर कॉलम में अविभाज्य मान होता है, दोहराव वाला समूह नहीं।"))
    A(c("dbms", "A candidate key is:", "उम्मीदवार कुंजी है:",
        "a minimal superkey", "एक न्यूनतम सुपरकी", "any column that may contain duplicates and nulls as the key", "कोई भी स्तम्भ जो कुंजी होते हुए दोहराव और नल रखे", "a view", "एक व्यू", 0,
        "सुपरकी पंक्ति पहचानती है। उसमें से अनावश्यक गुण हटा दें तो उम्मीदवार कुंजी बचती है।"))

    # networks
    A(c("network", "HTTP uses port:", "HTTP पोर्ट इस्तेमाल करता है:",
        "80", "80", "443", "443", "25", "25", 0,
        "HTTP 80, HTTPS 443, SMTP 25 और DNS 53 पर चलता है।"))
    A(c("network", "HTTPS uses port:", "HTTPS पोर्ट इस्तेमाल करता है:",
        "443", "443", "80", "80", "21", "21", 0,
        "HTTPS, TLS के साथ सामान्यतः पोर्ट 443 पर चलता है। FTP का नियंत्रण पोर्ट 21 है।"))
    A(c("network", "DNS uses port:", "DNS पोर्ट इस्तेमाल करता है:",
        "53", "53", "23", "23", "110", "110", 0,
        "DNS पोर्ट 53 है। टेलनेट 23 और POP3 110 है।"))
    A(c("network", "SSH commonly uses port:", "SSH सामान्यतः पोर्ट इस्तेमाल करता है:",
        "22", "22", "21", "21", "80", "80", 0,
        "सुरक्षित रिमोट लॉगिन SSH पोर्ट 22 पर होता है।"))
    A(c("network", "IPv4 addresses are:", "IPv4 पते होते हैं:",
        "32 bits", "32 बिट", "128 bits", "128 बिट", "48 bits", "48 बिट", 0,
        "IPv4 32 बिट और IPv6 128 बिट का होता है। MAC पता 48 बिट का होता है।"))
    A(c("network", "IPv6 addresses are:", "IPv6 पते होते हैं:",
        "128 bits", "128 बिट", "32 bits", "32 बिट", "16 bits", "16 बिट", 0,
        "IPv6 का पता 128 बिट का होता है।"))
    A(c("network", "A MAC address is typically:", "MAC पता सामान्यतः होता है:",
        "48 bits", "48 बिट", "32 bits", "32 बिट", "128 bits", "128 बिट", 0,
        "ईथरनेट MAC पता 48 बिट का होता है।"))
    A(c("network", "A switch works mainly at:", "स्विच मुख्यतः किस परत पर काम करता है?",
        "the data-link layer", "डेटा-लिंक परत", "the physical layer only, like a hub that floods every port always as its only job", "केवल भौतिक परत, हब की तरह जो हर पोर्ट पर हमेशा बाढ़ ही करे", "the application layer as a mail server", "अनुप्रयोग परत पर मेल सर्वर की तरह", 0,
        "स्विच MAC पते देखकर फ्रेम आगे भेजता है, यह परत 2 का काम है। राउटर परत 3 पर IP देखता है।"))
    A(c("network", "A router works mainly at:", "राउटर मुख्यतः किस परत पर काम करता है?",
        "the network layer", "नेटवर्क परत", "the physical layer only", "केवल भौतिक परत", "the session layer only", "केवल सत्र परत", 0,
        "राउटर IP पते के आधार पर पैकेट का मार्ग चुनता है।"))
    A(c("network", "TCP differs from UDP because TCP is:", "TCP, UDP से भिन्न है क्योंकि TCP है:",
        "connection-oriented and reliable", "कनेक्शन-उन्मुख और विश्वसनीय", "connectionless and without retransmission", "कनेक्शनहीन और बिना पुनःप्रेषण", "a physical cable", "एक भौतिक केबल", 0,
        "TCP कनेक्शन बनाता है और खोए खंड दोबारा भेजता है। UDP हल्का और कनेक्शनहीन है।"))
    A(c("network", "The TCP handshake uses:", "TCP हैंडशेक इस्तेमाल करता है:",
        "three steps: SYN, SYN-ACK, ACK", "तीन चरण: SYN, SYN-ACK, ACK", "one step only", "केवल एक चरण", "five emails", "पाँच ईमेल", 0,
        "तीन-चरणीय हैंडशेक से दोनों पक्ष क्रम संख्याएँ तय करते हैं।"))
    A(c("network", "The loopback address in IPv4 is:", "IPv4 में लूपबैक पता है:",
        "127.0.0.1", "127.0.0.1", "192.168.0.1", "192.168.0.1", "10.0.0.1", "10.0.0.1", 0,
        "127.0.0.1 उसी मशीन की ओर लौटता है। 192.168 और 10 निजी पते हैं।"))
    A(c("network", "Which is a private IPv4 range?", "कौन-सी निजी IPv4 सीमा है?",
        "10.0.0.0/8", "10.0.0.0/8", "8.8.8.0/24 as a private block by definition", "परिभाषा से निजी ब्लॉक के रूप में 8.8.8.0/24", "1.1.1.0/24", "1.1.1.0/24", 0,
        "निजी सीमाएँ 10/8, 172.16/12 और 192.168/16 हैं। 8.8.8.8 सार्वजनिक DNS है।"))
    A(c("network", "SMTP is used to:", "SMTP इस्तेमाल होता है:",
        "send email", "ईमेल भेजना", "resolve domain names", "डोमेन नाम सुलझाना", "transfer files as its original role in place of FTP", "FTP की जगह अपनी मूल भूमिका में फाइलें भेजना", 0,
        "सिंपल मेल ट्रांसफर प्रोटोकॉल मेल भेजता है। नाम सुलझाने का काम DNS का है।"))
    A(c("network", "OSI has how many layers?", "OSI में कितनी परतें हैं?",
        "7", "7", "4", "4", "5", "5", 0,
        "OSI मॉडल में 7 परतें हैं। TCP/IP मॉडल को प्रायः 4 परतों में पढ़ाया जाता है।"))
    A(c("network", "Which of the following is correct?", "निम्न में कौन सही है?",
        "IPv4 is 32 bits", "IPv4 32 बिट है", "IPv6 is 128 bits", "IPv6 128 बिट है", "MAC address is 32 bits", "MAC पता 32 बिट है", 3,
        "(A) और (B) सही हैं। MAC सामान्यतः 48 बिट होता है। अतः (D)।"))
    A(c("network", "CSMA/CD was used in classic:", "CSMA/CD क्लासिक रूप में इस्तेमाल होता था:",
        "Ethernet", "ईथरनेट", "postal mail", "डाक", "a CPU register", "CPU रजिस्टर", 0,
        "कैरियर सेंस मल्टीपल एक्सेस विद कोलिजन डिटेक्शन पुराने साझे ईथरनेट की विधि थी।"))
    A(c("network", "NAT is used to:", "NAT किसके लिए इस्तेमाल होता है?",
        "map private addresses to a public address", "निजी पतों को सार्वजनिक पते पर मैप करना", "encrypt a disk with AES by definition of the acronym NAT", "संक्षिप्त नाम NAT की परिभाषा से डिस्क को AES से एन्क्रिप्ट करना", "replace DNS", "DNS को बदलना", 0,
        "नेटवर्क एड्रेस ट्रांसलेशन कई निजी होस्टों को कम सार्वजनिक पतों से बाहर निकलने देता है।"))

    # security
    A(c("security", "AES is a:", "AES है:",
        "symmetric cipher", "सममित बीजलेख", "hash function that replaces SHA by definition", "परिभाषा से SHA की जगह लेने वाला हैश फलन", "routing protocol", "रूटिंग प्रोटोकॉल", 0,
        "AES एक ही कुंजी से एन्क्रिप्ट और डिक्रिप्ट करता है। यह सममित है।"))
    A(c("security", "RSA is based on the difficulty of:", "RSA किस कठिनाई पर आधारित है?",
        "factoring large integers", "बड़ी पूर्णांकों का गुणनखंड", "sorting", "छँटाई", "adding bits", "बिट जोड़ना", 0,
        "RSA में सार्वजनिक और निजी कुंजी बड़े अभाज्यों के गुणन से बनती हैं। गुणनखंड निकालना कठिन माना जाता है।"))
    A(c("security", "A cryptographic hash should be:", "क्रिप्टोग्राफिक हैश को होना चाहिए:",
        "one-way", "एक-तरफा", "easily reversible to the original password", "मूल पासवर्ड तक आसानी से उलटा जा सकने वाला", "always two bytes", "हमेशा दो बाइट", 0,
        "अच्छे हैश से मूल संदेश वापस निकालना व्यावहारिक नहीं होता।"))
    A(c("security", "Phishing is:", "फिशिंग है:",
        "tricking a user into revealing a secret", "उपयोगकर्ता को छलकर रहस्य बताने पर मजबूर करना", "a CPU scheduling algorithm", "एक CPU शेड्यूलिंग एल्गोरिथ्म", "a normal form in databases", "डेटाबेस की एक सामान्य रूप", 0,
        "फिशिंग नकली पृष्ठ या संदेश से पासवर्ड या ओटीपी लेती है।"))
    A(c("security", "SQL injection is prevented in applications mainly by:", "अनुप्रयोगों में SQL इंजेक्शन मुख्यतः कैसे रोका जाता है?",
        "parameterised queries", "पैरामीटरीकृत क्वेरी", "concatenating user input into SQL", "उपयोगकर्ता इनपुट को SQL में जोड़ देना", "turning off the database", "डेटाबेस बंद कर देना", 0,
        "तैयार कथनों में डेटा और SQL अलग रहते हैं, इसलिए इनपुट कमांड नहीं बन पाता।"))
    A(c("security", "In public-key encryption for confidentiality, the sender uses:", "गोपनीयता वाली सार्वजनिक-कुंजी एन्क्रिप्शन में प्रेषक इस्तेमाल करता है:",
        "the receiver’s public key", "प्राप्तकर्ता की सार्वजनिक कुंजी", "the receiver’s private key", "प्राप्तकर्ता की निजी कुंजी", "a hash as the only key", "केवल कुंजी के रूप में हैश", 0,
        "सार्वजनिक कुंजी से ताला लगता है और केवल प्राप्तकर्ता की निजी कुंजी खोलती है। हस्ताक्षर में निजी कुंजी से हस्ताक्षर होता है।"))
    A(c("security", "The CIA triad stands for:", "CIA त्रयी का अर्थ है:",
        "Confidentiality, Integrity, Availability", "गोपनीयता, अखंडता, उपलब्धता", "Central Intelligence Agency as a syllabus term of computer security", "कम्प्यूटर सुरक्षा के पाठ्यक्रम शब्द के रूप में केंद्रीय खुफिया एजेंसी", "Cache, Index, Address", "कैश, इंडेक्स, एड्रेस", 0,
        "सूचना सुरक्षा के तीन लक्ष्य गोपनीयता, अखंडता और उपलब्धता हैं।"))
    A(c("security", "A worm differs from a typical virus because a worm:", "वर्म सामान्य वायरस से भिन्न है क्योंकि वर्म:",
        "can spread without a host file", "होस्ट फाइल के बिना फैल सकता है", "cannot use a network", "नेटवर्क इस्तेमाल नहीं कर सकता", "is only a document", "केवल एक दस्तावेज है", 0,
        "वायरस किसी फाइल से चिपकता है। वर्म स्वयं नेटवर्क पर फैल सकता है।"))
    A(c("security", "Two-factor authentication uses:", "दो-कारक प्रमाणीकरण इस्तेमाल करता है:",
        "two different kinds of proof", "दो भिन्न प्रकार के प्रमाण", "the same password typed twice", "एक ही पासवर्ड दो बार", "only an IP address", "केवल IP पता", 0,
        "जैसे पासवर्ड (जानकारी) और फोन पर ओटीपी (अधिकार)। एक ही बात दो बार कहना दूसरा कारक नहीं है।"))

    # SE
    A(c("se", "The waterfall model is:", "वॉटरफॉल मॉडल है:",
        "a linear sequence of phases", "चरणों का रैखिक क्रम", "a model with no requirements phase", "बिना आवश्यकता-चरण का मॉडल", "a sorting algorithm", "एक सॉर्टिंग एल्गोरिथ्म", 0,
        "वॉटरफॉल में आवश्यकता, डिजाइन, कोड, परीक्षण और रखरखाव क्रम से होते हैं। पीछे लौटना कठिन माना जाता है।"))
    A(c("se", "SRS stands for:", "SRS का अर्थ है:",
        "Software Requirements Specification", "सॉफ्टवेयर रिक्वायरमेंट्स स्पेसिफिकेशन", "System Runtime Stack", "सिस्टम रनटाइम स्टैक", "Secure Routing Service", "सिक्योर रूटिंग सर्विस", 0,
        "SRS में यह लिखा जाता है कि सॉफ्टवेयर को क्या करना है।"))
    A(c("se", "Black-box testing is based on:", "ब्लैक-बॉक्स परीक्षण आधारित है:",
        "specification, without looking at the code", "विनिर्देश पर, कोड देखे बिना", "the internal path of every statement only", "केवल हर कथन के आंतरिक पथ पर", "the CPU clock", "CPU घड़ी", 0,
        "ब्लैक बॉक्स इनपुट और अपेक्षित आउटपुट देखता है। व्हाइट बॉक्स कोड की संरचना देखता है।"))
    A(c("se", "White-box testing uses:", "व्हाइट-बॉक्स परीक्षण इस्तेमाल करता है:",
        "knowledge of the internal code", "आंतरिक कोड का ज्ञान", "only the user manual’s colours", "केवल उपयोगकर्ता मैनुअल के रंग", "no test cases", "कोई परीक्षण प्रकरण नहीं", 0,
        "परीक्षक पथ, शाखाएँ और शर्तें देखकर केस बनाता है।"))
    A(c("se", "Unit testing focuses on:", "यूनिट परीक्षण केंद्रित होता है:",
        "a small module", "एक छोटे मॉड्यूल पर", "the whole deployed city network", "पूरे लगे हुए शहर-नेटवर्क पर", "only the printer hardware", "केवल प्रिंटर हार्डवेयर पर", 0,
        "यूनिट टेस्ट एक फलन या क्लास को अलग जाँचता है। इंटीग्रेशन कई मॉड्यूल जोड़कर जाँचता है।"))
    A(c("se", "High cohesion and low coupling are:", "उच्च कोहीजन और निम्न कपलिंग हैं:",
        "desirable design qualities", "वांछनीय डिजाइन गुण", "errors to be removed", "हटाने योग्य त्रुटियाँ", "types of computer virus", "कम्प्यूटर वायरस के प्रकार", 0,
        "मॉड्यूल के अंदर काम एक-दूसरे से जुड़े हों (कोहीजन) और मॉड्यूलों के बीच निर्भरता कम हो (कपलिंग)।"))
    A(c("se", "Agile development welcomes:", "एजाइल विकास स्वागत करता है:",
        "changing requirements in short iterations", "छोटे पुनरावृत्ति-चक्रों में बदलती आवश्यकताएँ", "a single frozen specification with no customer talk", "बिना ग्राहक-बातचीत के एक जमी हुई विनिर्देश", "writing no tests", "कोई परीक्षण न लिखना", 0,
        "एजाइल छोटे चक्रों में काम करता है और आवश्यकता के बदलने को सामान्य मानता है।"))
    A(c("se", "Cyclomatic complexity is based on:", "साइक्लोमैटिक जटिलता आधारित है:",
        "the number of independent paths in the control-flow graph", "नियंत्रण-प्रवाह ग्राफ के स्वतंत्र पथों की संख्या", "the number of comments", "टिप्पणियों की संख्या", "the screen size", "स्क्रीन का आकार", 0,
        "मैकेब की जटिलता निर्णय बिंदुओं से बढ़ती है और परीक्षण पथों की संख्या का अनुमान देती है।"))

    # web
    A(c("web", "HTML is used to:", "HTML इस्तेमाल होता है:",
        "describe the structure of a web page", "वेब पृष्ठ की संरचना बताना", "define only the colour and nothing of structure", "केवल रंग बताना, संरचना नहीं", "replace the operating system", "ऑपरेटिंग सिस्टम को बदलना", 0,
        "HTML पृष्ठ की संरचना है। रूप CSS से और व्यवहार जावास्क्रिप्ट से आता है।"))
    A(c("web", "CSS is used for:", "CSS किसके लिए है?",
        "presentation", "प्रस्तुति", "database storage", "डेटाबेस भंडारण", "CPU scheduling", "CPU शेड्यूलिंग", 0,
        "कैस्केडिंग स्टाइल शीट रंग, फ़ॉन्ट और लेआउट तय करती है।"))
    A(c("web", "HTTP is:", "HTTP है:",
        "stateless", "स्टेटलेस", "a protocol that keeps a permanent TCP session as part of the protocol definition itself", "ऐसा प्रोटोकॉल जो अपनी परिभाषा में स्थायी TCP सत्र रखे", "a programming language", "एक प्रोग्रामिंग भाषा", 0,
        "हर HTTP अनुरोध अपने आप पिछला अनुरोध याद नहीं रखता। अवस्था कुकी या सत्र से जोड़ी जाती है।"))
    A(c("web", "HTTP status 404 means:", "HTTP स्थिति 404 का अर्थ है:",
        "not found", "नहीं मिला", "OK", "ठीक", "server error", "सर्वर त्रुटि", 0,
        "200 सफल, 404 संसाधन नहीं मिला, 500 सर्वर की आंतरिक त्रुटि।"))
    A(c("web", "HTTP status 200 means:", "HTTP स्थिति 200 का अर्थ है:",
        "OK", "सफल", "Not found", "नहीं मिला", "Moved permanently", "स्थायी रूप से स्थानांतरित", 0,
        "200 का अर्थ है अनुरोध सफल रहा। 301 स्थायी स्थानांतरण है।"))
    A(c("web", "JSON is:", "JSON है:",
        "a text format for structured data", "संरचित डेटा का पाठ्य प्रारूप", "a CPU register", "एक CPU रजिस्टर", "an operating system", "एक ऑपरेटिंग सिस्टम", 0,
        "जावास्क्रिप्ट ऑब्जेक्ट नोटेशन हल्का डेटा-विनिमय प्रारूप है।"))
    A(c("web", "A cookie is stored:", "कुकी संचित होती है:",
        "on the client, by the browser", "क्लाइंट पर, ब्राउजर द्वारा", "only inside the CPU ALU", "केवल CPU के ALU में", "as a row that SQL forbids", "ऐसी पंक्ति के रूप में जिसे SQL मना करे", 0,
        "सर्वर सेट-कुकी भेजता है और ब्राउजर उसे सहेजकर अगले अनुरोध के साथ भेजता है।"))
    A(c("web", "Which of the following is correct?", "निम्न में कौन सही है?",
        "HTML describes structure", "HTML संरचना बताता है", "CSS describes presentation", "CSS प्रस्तुति बताता है", "CSS is a database engine", "CSS एक डेटाबेस इंजन है", 3,
        "(A) और (B) सही हैं। CSS डेटाबेस नहीं है। अतः (D)।"))

    # theory
    A(c("theory", "A regular language can be recognised by a:", "नियमित भाषा को पहचान सकता है:",
        "finite automaton", "परिमित ऑटोमेटन", "only a Turing machine and never a finite automaton", "केवल ट्यूरिंग मशीन, कभी परिमित ऑटोमेटन नहीं", "only a human", "केवल मानव", 0,
        "नियमित भाषाएँ ठीक वे हैं जिन्हें परिमित ऑटोमेटा पहचानते हैं।"))
    A(c("theory", "A language generated by a context-free grammar can be recognised by a:", "संदर्भ-मुक्त व्याकरण से बनी भाषा को पहचान सकता है:",
        "pushdown automaton", "पुशडाउन ऑटोमेटन", "finite automaton in every case, including {aⁿbⁿ}", "हर स्थिति में परिमित ऑटोमेटन, {aⁿbⁿ} सहित", "only a spreadsheet", "केवल स्प्रेडशीट", 0,
        "संदर्भ-मुक्त भाषाओं का यंत्र पुशडाउन ऑटोमेटन है। {aⁿbⁿ} नियमित नहीं है।"))
    A(c("theory", "The Church–Turing thesis concerns:", "चर्च-ट्यूरिंग थीसिस किससे संबंधित है?",
        "what can be computed by an effective procedure", "प्रभावी विधि से क्या गणना की जा सकती है", "the colour of a website", "वेबसाइट का रंग", "disk RPM", "डिस्क का RPM", 0,
        "यह कहती है कि एल्गोरिथ्म से गणना योग्य फलन ट्यूरिंग मशीन से गणना योग्य फलन ही हैं।"))
    A(c("theory", "Lexical analysis in a compiler produces:", "कम्पाइलर का शाब्दिक विश्लेषण बनाता है:",
        "tokens", "टोकन", "machine code directly with no other phase", "बिना किसी अन्य चरण के सीधे मशीन कोड", "an ER diagram", "एक ER आरेख", 0,
        "लेक्सर स्रोत को टोकनों में तोड़ता है। उसके बाद सिंटैक्स विश्लेषण आता है।"))
    A(c("theory", "A parser checks:", "पार्सर जाँचता है:",
        "whether the token stream matches the grammar", "टोकन धारा व्याकरण से मेल खाती है या नहीं", "only the battery level", "केवल बैटरी स्तर", "the user’s password strength by itself", "अपने आप पासवर्ड की मजबूती", 0,
        "सिंटैक्स विश्लेषण व्याकरण के विरुद्ध टोकनों की रचना जाँचता है।"))
    A(c("theory", "An NP-complete problem is, informally:", "NP-पूर्ण समस्या अनौपचारिक रूप से है:",
        "among the hardest problems in NP", "NP की सबसे कठिन समस्याओं में से", "solvable in constant time by a known linear scan always", "हमेशा ज्ञात रैखिक स्कैन से स्थिर समय में हल होने वाली", "not a decision problem by definition", "परिभाषा से निर्णय समस्या नहीं", 0,
        "NP की हर समस्या को बहुपद समय में NP-पूर्ण समस्या में बदला जा सकता है। SAT इसका उदाहरण है।"))

    # emerging / misc seen in TRE papers
    A(c("security", "Supervised learning uses:", "सुपरवाइज्ड लर्निंग इस्तेमाल करती है:",
        "labelled examples", "अंकित उदाहरण", "only unlabelled data with no target", "बिना लक्ष्य के केवल बिना अंकों वाला डेटा", "no data at all", "बिल्कुल कोई डेटा नहीं", 0,
        "सुपरवाइज्ड लर्निंग में इनपुट के साथ सही उत्तर दिया जाता है। अनसुपरवाइज्ड में लेबल नहीं होते।"))
    A(c("security", "K-means is an example of:", "K-मीन्स उदाहरण है:",
        "unsupervised clustering", "अनसुपरवाइज्ड क्लस्टरिंग", "a sorting algorithm", "एक सॉर्टिंग एल्गोरिथ्म", "a page-replacement policy", "एक पेज-रिप्लेसमेंट नीति", 0,
        "K-मीन्स बिना लेबल के बिंदुओं को K समूहों में बाँटता है।"))
    A(c("security", "MQTT is commonly used in:", "MQTT सामान्यतः इस्तेमाल होता है:",
        "IoT messaging", "IoT संदेशों में", "SQL normalisation", "SQL सामान्यीकरण", "CPU register renaming", "CPU रजिस्टर रीनेमिंग", 0,
        "MQTT हल्का पब्लिश-सबस्क्राइब प्रोटोकॉल है और IoT उपकरणों में लोकप्रिय है।"))
    A(c("web", "Which is a B2C example?", "B2C का उदाहरण कौन है?",
        "An online shop selling to a consumer", "उपभोक्ता को बेचने वाली ऑनलाइन दुकान", "A company buying raw material from another company only", "केवल एक कंपनी का दूसरी कंपनी से कच्चा माल खरीदना", "Two consumers forming a government", "दो उपभोक्ताओं का सरकार बनाना", 0,
        "B2C व्यवसाय से उपभोक्ता है। कंपनियों के बीच व्यापार B2B है।"))
    A(c("web", "B2B means:", "B2B का अर्थ है:",
        "business to business", "व्यवसाय से व्यवसाय", "business to browser as an OSI layer", "OSI परत के रूप में व्यवसाय से ब्राउजर", "binary to binary as a number system", "संख्या प्रणाली के रूप में बाइनरी से बाइनरी", 0,
        "B2B दो व्यवसायों के बीच का ई-कॉमर्स है।"))
    A(c("se", "Which is a multimedia authoring tool?", "मल्टीमीडिया ऑथरिंग टूल कौन है?",
        "Adobe Flash / Animate style tools", "एडोब फ्लैश / एनिमेट जैसी उपकरण-श्रेणी", "ping", "ping", "ls", "ls", 0,
        "ऑथरिंग टूल से मीडिया जोड़ा और समय-रेखा पर रखा जाता है। ping और ls नेटवर्क/शेल आदेश हैं।"))
    A(c("programming", "What does the following C snippet print?\nint x = 5;\nprintf(\"%d\", x++);\n",
        "निम्न C टुकड़ा क्या छापता है?\nint x = 5;\nprintf(\"%d\", x++);\n",
        "5", "5", "6", "6", "4", "4", 0,
        "पोस्ट-इन्क्रीमेंट पहले वर्तमान मान 5 देता है, फिर x को 6 कर देता है। प्रिंट 5 है।", True))
    A(c("programming", "What does this Python expression evaluate to?\nlen(\"tree\")",
        "यह पायथन व्यंजक कितना है?\nlen(\"tree\")",
        "4", "4", "5", "5", "3", "3", 0,
        "“tree” में चार वर्ण हैं, इसलिए len 4 देता है।", True))
    A(c("dbms", "Given Emp(id, name). The query SELECT COUNT(*) FROM Emp; returns:",
        "Emp(id, name) दी गई है। क्वेरी SELECT COUNT(*) FROM Emp; क्या लौटाती है?",
        "the number of rows", "पंक्तियों की संख्या", "the number of columns always equal to 2, not the rows", "हमेशा स्तम्भों की संख्या 2, पंक्तियाँ नहीं", "the sum of ids", "id का योग", 0,
        "COUNT(*) तालिका की पंक्तियाँ गिनता है, स्तम्भों की संख्या या id का योग नहीं।"))
    A(c("os", "FCFS may cause:", "FCFS पैदा कर सकता है:",
        "the convoy effect", "कॉन्वॉय प्रभाव", "Belady’s anomaly by itself", "अपने आप बेलेडी की विसंगति", "a guaranteed minimum response for every short job ahead of a long one", "लंबे काम से पहले हर छोटे काम का गारंटीशुदा न्यूनतम उत्तर", 0,
        "एक लंबा काम पहले आ जाए तो उसके पीछे छोटे काम रुक जाते हैं। इसे कॉन्वॉय प्रभाव कहते हैं।"))
    A(c("network", "The application-layer protocol that fetches web pages is:", "वेब पृष्ठ लाने वाला अनुप्रयोग-परत प्रोटोकॉल है:",
        "HTTP", "HTTP", "SMTP", "SMTP", "ICMP", "ICMP", 0,
        "वेब पृष्ठ HTTP/HTTPS से आते हैं। SMTP मेल भेजता है और ICMP नियंत्रण संदेश (जैसे ping) है।"))
    A(c("digital", "The number of different Boolean functions of 2 variables is:", "2 चरों के भिन्न बूलियन फलनों की संख्या है:",
        "16", "16", "4", "4", "8", "8", 0,
        "2 चरों की 4 पंक्तियाँ होती हैं और हर पंक्ति का आउटपुट 0 या 1 हो सकता है। कुल 2⁴ = 16 फलन।"))
    A(c("digital", "The number of different Boolean functions of 1 variable is:", "1 चर के भिन्न बूलियन फलनों की संख्या है:",
        "4", "4", "2", "2", "1", "1", 0,
        "एक चर की 2 पंक्तियाँ और हर पंक्ति का आउटपुट 2 तरह का: 2² = 4।"))
    A(c("coa", "A write-through policy updates:", "राइट-थ्रू नीति अपडेट करती है:",
        "cache and main memory together on a write", "लिखत पर कैश और मुख्य मेमोरी दोनों", "only the disk after a week", "एक सप्ताह बाद केवल डिस्क", "only the register file and never memory", "केवल रजिस्टर फाइल, कभी मेमोरी नहीं", 0,
        "राइट-थ्रू में हर स्टोर मुख्य मेमोरी तक पहुँचता है, इसलिए डेटा अधिक सुसंगत रहता है।"))
    A(c("ds", "A circular queue avoids the problem of:", "वृत्तीय कतार किस समस्या से बचाती है?",
        "wasted space in a linear queue after deletions", "हटाने के बाद रैखिक कतार में व्यर्थ जगह", "the need for a front index", "फ्रंट इंडेक्स की जरूरत", "all overflow forever", "हमेशा के लिए हर ओवरफ्लो", 0,
        "रैखिक ऐरे-कतार में आगे जगह खाली होने पर भी रियर अंत पर अटक सकता है। वृत्तीय कतार उस जगह को फिर इस्तेमाल करती है।"))
    A(c("algo", "Prim’s algorithm grows a:", "प्रिम का एल्गोरिथ्म बढ़ाता है:",
        "minimum spanning tree from a start vertex", "एक आरम्भिक शीर्ष से न्यूनतम स्पैनिंग ट्री", "shortest path that may include negative cycles", "ऐसा सबसे छोटा पथ जिसमें ऋणात्मक चक्र आ सकें", "hash index", "हैश इंडेक्स", 0,
        "प्रिम एक शीर्ष से शुरू कर सबसे सस्ता सुरक्षित किनारा जोड़ता रहता है।"))
    A(c("theory", "An interpreter:", "इंटरप्रेटर:",
        "executes source or intermediate code directly", "स्रोत या मध्यवर्ती कोड को सीधे चलाता है", "always produces a standalone machine-code file and then exits before running", "हमेशा अलग मशीन-कोड फाइल बनाता है और चलने से पहले समाप्त हो जाता है", "is a network switch", "एक नेटवर्क स्विच है", 0,
        "इंटरप्रेटर चलाते समय अनुवाद करता है। कम्पाइलर पहले लक्ष्य कोड बनाता है।"))
    A(c("oop", "Abstraction means:", "अमूर्तन का अर्थ है:",
        "showing essential features and hiding unnecessary detail", "जरूरी लक्षण दिखाना और अनावश्यक विवरण छिपाना", "copying every private field into global scope", "हर निजी फील्ड को वैश्विक दायरे में नकल करना", "removing all methods", "सभी विधियाँ हटाना", 0,
        "अमूर्तन उपयोगकर्ता को ‘क्या’ दिखाता है और ‘कैसे’ छिपाता है।"))
    A(c("os", "A mutex is:", "म्यूटेक्स है:",
        "a lock owned by one thread at a time", "एक ताला जो एक समय एक थ्रेड के पास रहता है", "a scheduling quantum", "एक शेड्यूलिंग क्वांटम", "a file allocation table", "एक फाइल आवंटन तालिका", 0,
        "म्यूचुअल एक्सक्लूजन लॉक एक समय केवल एक स्वामी को क्रिटिकल सेक्शन में जाने देता है।"))
    A(c("dbms", "DELETE differs from DROP because DELETE:", "DELETE, DROP से भिन्न है क्योंकि DELETE:",
        "removes rows and can be rolled back inside a transaction", "पंक्तियाँ हटाता है और लेनदेन में वापस लिया जा सकता है", "removes the table definition itself", "स्वयं तालिका की परिभाषा हटाता है", "creates an index", "इंडेक्स बनाता है", 0,
        "DELETE DML है। DROP TABLE ढाँचा मिटा देता है और DDL है।"))
    A(c("network", "Ping uses:", "Ping इस्तेमाल करता है:",
        "ICMP", "ICMP", "SMTP", "SMTP", "FTP", "FTP", 0,
        "ping ICMP इको अनुरोध भेजकर होस्ट की पहुँच जाँचता है।"))
    A(c("security", "A digital signature provides:", "डिजिटल हस्ताक्षर देता है:",
        "authentication and integrity", "प्रमाणीकरण और अखंडता", "a faster CPU", "तेज CPU", "automatic backup of disks", "डिस्क का स्वचालित बैकअप", 0,
        "निजी कुंजी से बना हस्ताक्षर बताता है कि संदेश किसने भेजा और वह बदला नहीं गया।"))
    A(c("web", "REST commonly exchanges data as:", "REST सामान्यतः डेटा भेजता है:",
        "HTTP resources, often in JSON", "HTTP संसाधन, प्रायः JSON में", "only FTP files named rest.txt", "केवल rest.txt नाम की FTP फाइलें", "CPU microcode", "CPU माइक्रोकोड", 0,
        "REST संसाधनों को HTTP क्रियाओं GET, POST, PUT, DELETE से सँभालता है।"))
    A(c("fundamentals", "Which of the following is correct?", "निम्न में कौन सही है?",
        "RAM is volatile", "RAM वोलेटाइल है", "ROM is non-volatile", "ROM अवाष्पशील है", "Cache is slower than a magnetic tape", "कैश चुंबकीय टेप से धीमा है", 3,
        "(A) और (B) सही हैं। कैश टेप से बहुत तेज होता है। अतः (D)।"))
    A(c("programming", "What is the value of x after this code?\nint x = 3;\nx = x * x + 1;",
        "इस कोड के बाद x का मान क्या है?\nint x = 3;\nx = x * x + 1;",
        "10", "10", "7", "7", "9", "9", 0,
        "3×3 + 1 = 10।", True))
    A(c("ds", "The maximum number of nodes in a binary tree with 3 levels (root at level 1) is:",
        "3 स्तरों वाले बाइनरी ट्री में अधिकतम नोड (रूट स्तर 1) हैं:",
        "7", "7", "6", "6", "8", "8", 0,
        "1 + 2 + 4 = 7, यानी 2³ − 1।"))
    A(c("algo", "A graph with 5 vertices that is a tree has how many edges?",
        "5 शीर्षों वाले ट्री में कितने किनारे होते हैं?",
        "4", "4", "5", "5", "10", "10", 0,
        "ट्री में किनारे = शीर्ष − 1 = 4। 10 पूर्ण ग्राफ K5 का मान होता।"))
    A(c("coa", "Which storage is non-volatile?", "कौन-सा भंडारण अवाष्पशील है?",
        "Flash memory", "फ्लैश मेमोरी", "DRAM", "DRAM", "SRAM", "SRAM", 0,
        "फ्लैश बिना बिजली डेटा रखती है। DRAM और SRAM नहीं रखते।"))
    A(c("os", "The ready queue contains processes that are:", "रेडी कतार में वे प्रोसेस होते हैं जो:",
        "waiting for the CPU", "CPU का इंतजार कर रहे हैं", "waiting for I/O completion only", "केवल I/O पूरा होने का इंतजार कर रहे हैं", "already terminated", "पहले ही समाप्त हो चुके हैं", 0,
        "रेडी अवस्था में प्रोसेस चलने के योग्य है और CPU खाली होने की प्रतीक्षा में है। I/O की प्रतीक्षा वेटिंग अवस्था है।"))
    A(c("network", "A subnet mask of 255.255.255.0 means the prefix is:", "सबनेट मास्क 255.255.255.0 का अर्थ प्रीफिक्स है:",
        "/24", "/24", "/16", "/16", "/8", "/8", 0,
        "255.255.255.0 में 24 बिट नेटवर्क के हैं, इसलिए /24।"))
    A(c("security", "Reinforcement learning learns from:", "रीइन्फोर्समेंट लर्निंग सीखती है:",
        "rewards and penalties from actions", "क्रियाओं पर मिलने वाले पुरस्कार और दंड", "a fully labelled table only, with no reward", "केवल पूरी तरह अंकित तालिका, बिना पुरस्कार", "sorting comparisons", "छँटाई की तुलनाएँ", 0,
        "एजेंट क्रिया करता है और वातावरण से इनाम पाकर नीति सुधारता है।"))
    A(c("dbms", "A transaction that is durable:", "जो लेनदेन टिकाऊ है वह:",
        "remains committed even after a crash", "क्रैश के बाद भी कमिटेड रहता है", "disappears when the power fails even after commit", "कमिट के बाद भी बिजली जाते ही गायब हो जाता है", "is never written to a log", "कभी लॉग में नहीं लिखा जाता", 0,
        "Durability का अर्थ है सफल COMMIT के बाद डेटा स्थायी भंडारण में बचा रहता है।"))
    A(c("se", "Regression testing checks that:", "रिग्रेशन परीक्षण जाँचता है कि:",
        "old features still work after a change", "बदलाव के बाद पुराने लक्षण अभी भी काम करते हैं", "only the new screen’s colour is pretty", "केवल नई स्क्रीन का रंग सुंदर है", "the compiler is installed", "कम्पाइलर स्थापित है", 0,
        "नई त्रुटि पुराना सही व्यवहार न तोड़ दे, यह रिग्रेशन टेस्ट देखता है।"))
    A(c("web", "The HTML tag for the largest standard heading is:", "सबसे बड़े मानक शीर्षक का HTML टैग है:",
        "h1", "h1", "h6", "h6", "p", "p", 0,
        "h1 सबसे बड़ा और h6 सबसे छोटा शीर्षक है। p अनुच्छेद है।"))
    A(c("theory", "A compiler’s code generator produces:", "कम्पाइलर का कोड जनरेटर बनाता है:",
        "target code", "लक्ष्य कोड", "only comments", "केवल टिप्पणियाँ", "an HTML form", "एक HTML फॉर्म", 0,
        "आखिरी चरण लक्ष्य मशीन या बाइटकोड के लिए निर्देश बनाता है।"))
    A(c("digital", "Which flip-flop toggles when both inputs are 1 (ignoring race)?", "कौन-सा फ्लिप-फ्लॉप दोनों इनपुट 1 होने पर टॉगल करता है (रेस छोड़कर)?",
        "JK", "JK", "SR, which treats 1,1 as set", "SR, जो 1,1 को सेट मानता है", "a buffer gate", "एक बफर गेट", 0,
        "JK में J=K=1 टॉगल है। SR में S=R=1 निषिद्ध या अवैध अवस्था मानी जाती है।"))
    A(c("ds", "A doubly linked list node stores:", "दोहरी लिंक्ड लिस्ट का नोड रखता है:",
        "pointers to both next and previous nodes", "अगले और पिछले दोनों नोड के पॉइंटर", "only the data and no pointer", "केवल डेटा, कोई पॉइंटर नहीं", "a hash of the whole database", "पूरे डेटाबेस का हैश", 0,
        "आगे और पीछे दोनों सूचक होने से दोनों दिशाओं में चला जा सकता है।"))
    A(c("algo", "Stable sort means:", "स्टेबल सॉर्ट का अर्थ है:",
        "equal keys keep their original relative order", "समान कुंजियाँ अपना मूल सापेक्ष क्रम रखती हैं", "the algorithm never uses memory", "एल्गोरिथ्म कभी मेमोरी नहीं लेता", "the output is always reverse sorted", "आउटपुट हमेशा उलटा क्रमबद्ध होता है", 0,
        "स्थिरता समान मान वाले रिकॉर्ड का आपसी क्रम बचाए रखती है। मर्जसॉर्ट स्थिर है, सामान्य हीपसॉर्ट नहीं।"))
    A(c("oop", "A Java interface can contain:", "जावा इंटरफेस में हो सकते हैं:",
        "abstract methods that a class must implement", "अमूर्त विधियाँ जिन्हें क्लास को लागू करना होता है", "a private constructor of a concrete object only", "केवल एक ठोस वस्तु का निजी कन्स्ट्रक्टर", "CPU microcode", "CPU माइक्रोकोड", 0,
        "इंटरफेस अनुबंध बताता है। क्लास implements द्वारा वे विधियाँ परिभाषित करती है।"))
    A(c("os", "Context switch means:", "कॉन्टेक्स्ट स्विच का अर्थ है:",
        "saving one process state and loading another", "एक प्रोसेस की स्थिति बचाना और दूसरी लादना", "formatting the disk", "डिस्क फॉर्मेट करना", "changing the monitor colour", "मॉनिटर का रंग बदलना", 0,
        "CPU एक प्रोसेस छोड़कर दूसरी चलाए, इससे पहले PCB में रजिस्टर और PC बचाए जाते हैं।"))
    A(c("network", "UDP is preferred when:", "UDP तब पसंद किया जाता है जब:",
        "low delay matters more than retransmission", "पुनःप्रेषण से अधिक कम विलंब मायने रखता है", "every byte must be retransmitted before the next can be sent, as in a file transfer that cannot tolerate loss", "हर बाइट का पुनःप्रेषण अगले से पहले जरूरी हो, जैसी फाइल में हानि सहन न हो", "a connection setup of three steps is mandatory for a one-packet query", "एक-पैकेट क्वेरी के लिए तीन-चरण कनेक्शन अनिवार्य हो", 0,
        "आवाज या गेम जैसे काम में देर से आया पुराना पैकेट उपयोगी नहीं होता, इसलिए UDP चुना जाता है। विश्वसनीय फाइल के लिए TCP बेहतर है।"))
    A(c("security", "Overfitting means a model:", "ओवरफिटिंग का अर्थ है कि मॉडल:",
        "memorizes training data and fails on new data", "प्रशिक्षण डेटा याद कर लेता है और नए डेटा पर असफल होता है", "is too simple to fit even the training data", "प्रशिक्षण डेटा पर भी फिट होने के लिए बहुत सरल है", "has no parameters", "उसका कोई पैरामीटर नहीं", 0,
        "ओवरफिट मॉडल प्रशिक्षण में बहुत अच्छा और नए उदाहरणों में कमजोर होता है। अंडरफिट दोनों में कमजोर होता है।"))
    A(c("fundamentals", "Unicode was designed to:", "यूनिकोड इसलिए बनाया गया ताकि:",
        "represent characters of many writing systems", "अनेक लिपियों के वर्ण दर्शाए जा सकें", "replace the ALU", "ALU को बदला जा सके", "compress video by itself", "अपने आप वीडियो संपीडित हो", 0,
        "ASCII मुख्यतः अंग्रेजी के लिए था। यूनिकोड दुनिया की लिपियों के लिए बड़ा कोड स्पेस देता है।"))
    A(c("dbms", "GROUP BY is used to:", "GROUP BY इस्तेमाल होता है:",
        "form groups for aggregate functions", "समुच्चय फलनों के लिए समूह बनाना", "delete a database user", "डेटाबेस उपयोगकर्ता मिटाना", "grant a privilege", "विशेषाधिकार देना", 0,
        "GROUP BY समान मान वाली पंक्तियों को समेटकर COUNT, SUM जैसी गणना करता है।"))
    A(c("se", "Coupling refers to:", "कपलिंग संकेत करती है:",
        "how much modules depend on each other", "मॉड्यूल एक-दूसरे पर कितना निर्भर हैं", "the comment style", "टिप्पणी की शैली", "the colour of the logo", "लोगो का रंग", 0,
        "कम कपलिंग का अर्थ है एक मॉड्यूल बदलने पर दूसरे कम टूटें।"))
    A(c("web", "Which HTTP method is intended to fetch a resource without changing it?", "कौन-सी HTTP विधि संसाधन को बदले बिना लाने के लिए है?",
        "GET", "GET", "DELETE", "DELETE", "PUT as a read", "पढ़ने के रूप में PUT", 0,
        "GET पढ़ता है। PUT अद्यतन और DELETE मिटाने के लिए है।"))
    A(c("theory", "Syntax analysis is also called:", "सिंटैक्स विश्लेषण को यह भी कहते हैं:",
        "parsing", "पार्सिंग", "linking", "लिंकिंग", "bootstrapping the OS", "OS का बूटस्ट्रैप", 0,
        "पार्सर व्याकरण के अनुसार वाक्य-रचना जाँचता है। लिंकर अलग वस्तु-फाइलें जोड़ता है।"))
    A(c("digital", "A decoder with 3 inputs can select one of:", "3 इनपुट वाला डिकोडर इनमें से एक चुन सकता है:",
        "8 outputs", "8 आउटपुट", "3 outputs", "3 आउटपुट", "2 outputs", "2 आउटपुट", 0,
        "n इनपुट वाला डिकोडर 2ⁿ आउटपुट में से एक सक्रिय करता है। 2³ = 8।"))
    A(c("coa", "Pipeline throughput improves when:", "पाइपलाइन थ्रूपुट सुधरता है जब:",
        "several instructions are in different stages together", "कई निर्देश एक साथ भिन्न चरणों में हों", "only one instruction is allowed in the whole CPU", "पूरे CPU में केवल एक निर्देश की अनुमति हो", "the clock is stopped", "घड़ी रोक दी जाए", 0,
        "पाइपलाइन चरणों को ओवरलैप करती है, इसलिए आदर्श स्थिति में प्रति चक्र एक निर्देश पूरा होने लगता है।"))
    A(c("ds", "Level order traversal of a tree uses a:", "ट्री का लेवल-ऑर्डर ट्रैवर्सल इस्तेमाल करता है:",
        "queue", "कतार", "stack only, with no queue", "केवल स्टैक, बिना कतार", "hash of the file name", "फाइल नाम का हैश", 0,
        "BFS की तरह पहले स्तर के नोड कतार में रखे जाते हैं, फिर उनके बच्चे।"))
    A(c("programming", "In Java, garbage collection reclaims:", "जावा में गार्बेज कलेक्शन वापस लेता है:",
        "objects that are no longer reachable", "वे वस्तुएँ जो अब पहुँच में नहीं हैं", "only comments", "केवल टिप्पणियाँ", "the source file from disk always", "हमेशा डिस्क से स्रोत फाइल", 0,
        "जिस वस्तु की ओर कोई संदर्भ नहीं बचा, उसे गार्बेज कलेक्टर बाद में मुक्त कर सकता है।"))
    A(c("os", "Starvation means:", "स्टार्वेशन का अर्थ है:",
        "a process waits indefinitely while others proceed", "एक प्रोसेस अनिश्चित काल प्रतीक्षा करे जबकि दूसरे आगे बढ़ें", "every process gets the CPU equally by force", "हर प्रोसेस को जबरदस्ती समान CPU मिले", "the disk is full of free space", "डिस्क खाली जगह से भरी है", 0,
        "कम प्राथमिकता वाला काम बार-बार पीछे छूट सकता है। एजिंग इस अन्याय को घटाती है।"))
    A(c("network", "The purpose of ARP is to:", "ARP का उद्देश्य है:",
        "find the MAC address for an IP address", "एक IP पते का MAC पता निकालना", "send email", "ईमेल भेजना", "compile Java", "जावा कम्पाइल करना", 0,
        "एड्रेस रेजोल्यूशन प्रोटोकॉल स्थानीय नेटवर्क पर IP से MAC पता पूछता है।"))
    A(c("security", "Symmetric encryption uses:", "सममित एन्क्रिप्शन इस्तेमाल करती है:",
        "the same secret key to encrypt and decrypt", "एन्क्रिप्ट और डिक्रिप्ट दोनों के लिए वही गुप्त कुंजी", "a public key only, with no shared secret", "केवल सार्वजनिक कुंजी, कोई साझा रहस्य नहीं", "no key", "कोई कुंजी नहीं", 0,
        "AES जैसी विधियों में दोनों पक्ष एक ही गुप्त कुंजी रखते हैं।"))
    A(c("se", "A use-case describes:", "यूज-केस वर्णन करता है:",
        "how an actor achieves a goal with the system", "एक अभिनेता सिस्टम से अपना लक्ष्य कैसे पाता है", "the CPU pipeline", "CPU पाइपलाइन", "a page-fault count", "पेज-फॉल्ट गिनती", 0,
        "यूज-केस उपयोगकर्ता के लक्ष्य और सिस्टम की प्रतिक्रिया को लिखता है।"))
    A(c("fundamentals", "Which of the following is an application software?", "निम्न में अनुप्रयोग सॉफ्टवेयर कौन है?",
        "A word processor", "वर्ड प्रोसेसर", "An operating system kernel", "ऑपरेटिंग सिस्टम की कर्नेल", "A bootstrap loader", "बूटस्ट्रैप लोडर", 0,
        "वर्ड प्रोसेसर उपयोगकर्ता का काम करता है। कर्नेल और बूट लोडर सिस्टम सॉफ्टवेयर हैं।"))
    A(c("dbms", "Isolation in ACID means:", "ACID में आइसोलेशन का अर्थ है:",
        "concurrent transactions should not see each other’s partial work improperly", "समानांतर लेनदेन एक-दूसरे का अधूरा काम अनुचित रूप से न देखें", "the database may be switched off", "डेटाबेस बंद किया जा सकता है", "keys must be strings", "कुंजियाँ स्ट्रिंग होनी चाहिए", 0,
        "आइसोलेशन स्तर तय करता है कि एक लेनदेन दूसरे के अधूरे बदलाव कितना देख सकता है।"))
    A(c("digital", "Odd parity means the total number of 1s, including the parity bit, is:", "विषम पैरिटी का अर्थ है कि पैरिटी बिट सहित 1 की कुल संख्या हो:",
        "odd", "विषम", "even", "सम", "always 8", "हमेशा 8", 0,
        "सम पैरिटी में 1 की संख्या सम और विषम पैरिटी में विषम रखी जाती है।"))
    A(c("coa", "The hit ratio of a cache is:", "कैश का हिट रेशियो है:",
        "hits divided by total references", "हिट को कुल संदर्भों से भाग", "misses only", "केवल मिस", "disk RPM", "डिस्क RPM", 0,
        "हिट रेशियो = हिट / (हिट + मिस)।"))
    A(c("algo", "A greedy algorithm builds a solution by:", "ग्रीडी एल्गोरिथ्म समाधान बनाता है:",
        "taking the locally best choice at each step", "हर कदम पर स्थानीय रूप से सर्वोत्तम विकल्प लेकर", "trying every subset exhaustively by definition of greedy", "ग्रीडी की परिभाषा से हर उपसमुच्चय को संपूर्ण रूप से आजमाकर", "random swaps only", "केवल यादृच्छिक अदला-बदली", 0,
        "ग्रीडी विधि पीछे नहीं हटती। वह हर कदम पर अभी का सर्वोत्तम चुनती है। हमेशा वैश्विक इष्टतम नहीं देती।"))
    A(c("os", "Paging removes:", "पेजिंग हटाती है:",
        "external fragmentation of variable-size holes", "परिवर्ती आकार के छिद्रों वाला बाहरी विखंडन", "all need for virtual addresses", "वर्चुअल पतों की सारी जरूरत", "the TLB concept from ever existing", "TLB की अवधारणा को हमेशा के लिए", 0,
        "समान आकार के पेज किसी भी फ्रेम में रखे जा सकते हैं, इसलिए बाहरी विखंडन नहीं बचता। आंतरिक विखंडन बच सकता है।"))
    A(c("programming", "What is printed?\nint s = 0;\nfor (int i = 1; i <= 4; i++) s += i;\nprintf(\"%d\", s);",
        "क्या छपेगा?\nint s = 0;\nfor (int i = 1; i <= 4; i++) s += i;\nprintf(\"%d\", s);",
        "10", "10", "4", "4", "8", "8", 0,
        "1+2+3+4 = 10।", True))
    A(c("network", "FTP control connection uses port:", "FTP नियंत्रण कनेक्शन पोर्ट इस्तेमाल करता है:",
        "21", "21", "80", "80", "443", "443", 0,
        "FTP का कमांड पोर्ट 21 है। डेटा के लिए प्रायः 20 इस्तेमाल होता रहा है।"))
    A(c("security", "A firewall’s basic job is to:", "फायरवॉल का बुनियादी काम है:",
        "filter traffic according to rules", "नियमों के अनुसार ट्रैफिक छानना", "compile source code", "स्रोत कोड कम्पाइल करना", "replace the primary key", "प्राथमिक कुंजी बदलना", 0,
        "फायरवॉल आने-जाने वाले पैकेटों पर नीति लगाकर अवांछित ट्रैफिक रोकता है।"))
    A(c("web", "JavaScript in the browser mainly:", "ब्राउजर में जावास्क्रिप्ट मुख्यतः:",
        "adds behaviour to a page", "पृष्ठ में व्यवहार जोड़ती है", "replaces the CPU", "CPU को बदल देती है", "is a database normal form", "एक डेटाबेस सामान्य रूप है", 0,
        "HTML संरचना, CSS रूप और जावास्क्रिप्ट व्यवहार देती है।"))
    A(c("ds", "Binary search on a sorted array of n elements takes:", "n तत्वों के क्रमबद्ध ऐरे पर बाइनरी सर्च लेती है:",
        "O(log n)", "O(log n)", "O(n²)", "O(n²)", "O(n log n) comparisons in the standard algorithm", "मानक एल्गोरिथ्म में O(n log n) तुलनाएँ", 0,
        "हर कदम पर आधा ऐरे छूटता है, इसलिए तुलनाएँ O(log n) हैं।"))
    A(c("theory", "Semantic analysis in a compiler checks things such as:", "कम्पाइलर का अर्थ-विश्लेषण ऐसी बातें जाँचता है जैसे:",
        "type agreement", "प्रकार का मेल", "only the number of spaces in comments", "केवल टिप्पणियों में स्पेस की संख्या", "disk speed", "डिस्क की गति", 0,
        "सिंटैक्स सही होने के बाद भी प्रकार, घोषणा और अर्थ की जाँच बाकी रहती है।"))
    A(c("fundamentals", "Cache memory sits between:", "कैश मेमोरी किसके बीच बैठती है?",
        "CPU and main memory", "CPU और मुख्य मेमोरी", "printer and paper", "प्रिंटर और कागज", "keyboard and mouse", "कीबोर्ड और माउस", 0,
        "कैश तेज और छोटी मेमोरी है जो CPU और धीमी RAM के बीच हाल का डेटा रखती है।"))
    A(c("oop", "Which of the following is correct?", "निम्न में कौन सही है?",
        "Encapsulation hides internal data", "एनकैप्सुलेशन आंतरिक डेटा छिपाता है", "Inheritance supports reuse", "इनहेरिटेंस पुनः उपयोग देता है", "A constructor is called when the object is destroyed", "कन्स्ट्रक्टर वस्तु नष्ट होते समय बुलाया जाता है", 3,
        "(A) और (B) सही हैं। नष्ट होते समय डिस्ट्रक्टर की बात होती है, कन्स्ट्रक्टर की नहीं। अतः (D)।"))

    seen = set()
    out = []
    for item in R:
        if item["q"] in seen:
            continue
        seen.add(item["q"])
        out.append(item)
    return out


if __name__ == "__main__":
    from collections import Counter
    b = build_cs()
    print("cs", len(b))
    print(Counter(x["topic"] for x in b))
