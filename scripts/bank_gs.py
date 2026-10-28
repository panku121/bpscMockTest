"""Factual General Studies items. Static syllabus, bilingual, five options."""

from qutil import fixed

def g(topic, q, qh, a, ah, b, bh, c, ch, ans, ex):
    return fixed("gs", topic, q, qh, [a, b, c], [ah, bh, ch], ans, ex)


def build_gs():
    R = []
    A = R.append

    # ---- History ----
    A(g("history",
        "The Indian National Congress was founded in:",
        "भारतीय राष्ट्रीय कांग्रेस की स्थापना हुई:",
        "1885", "1885", "1905", "1905", "1857", "1857", 0,
        "कांग्रेस की स्थापना 1885 में ए. ओ. ह्यूम के प्रयास से बॉम्बे में हुई। 1905 बंगाल विभाजन और 1857 विद्रोह का वर्ष है।"))
    A(g("history",
        "Who was the first President of the Indian National Congress?",
        "भारतीय राष्ट्रीय कांग्रेस के पहले अध्यक्ष कौन थे?",
        "W. C. Bonnerjee", "डब्ल्यू. सी. बनर्जी", "Dadabhai Naoroji", "दादाभाई नौरोजी", "Surendranath Banerjee", "सुरेंद्रनाथ बनर्जी", 0,
        "1885 के पहले अधिवेशन के अध्यक्ष व्योमेश चंद्र बनर्जी थे।"))
    A(g("history",
        "The Partition of Bengal was announced in 1905 during the viceroyalty of:",
        "1905 का बंगाल विभाजन किस वायसराय के समय घोषित हुआ?",
        "Lord Curzon", "लॉर्ड कर्जन", "Lord Ripon", "लॉर्ड रिपन", "Lord Dalhousie", "लॉर्ड डलहौजी", 0,
        "बंगाल विभाजन लॉर्ड कर्जन ने 1905 में किया।"))
    A(g("history",
        "The Jallianwala Bagh massacre took place on:",
        "जलियाँवाला बाग हत्याकांड कब हुआ?",
        "13 April 1919", "13 अप्रैल 1919", "15 August 1947", "15 अगस्त 1947", "8 August 1942", "8 अगस्त 1942", 0,
        "13 अप्रैल 1919 को बैसाखी के दिन जलियाँवाला बाग में गोली चली। जनरल डायर जिम्मेदार था।"))
    A(g("history",
        "Who was the Viceroy of India at the time of the Jallianwala Bagh massacre?",
        "जलियाँवाला बाग कांड के समय भारत का वायसराय कौन था?",
        "Lord Chelmsford", "लॉर्ड चेम्सफोर्ड", "Lord Mountbatten", "लॉर्ड माउंटबेटन", "Lord Canning", "लॉर्ड कैनिंग", 0,
        "1916–1921 के वायसराय लॉर्ड चेम्सफोर्ड थे। माउंटबेटन आखिरी वायसराय थे।"))
    A(g("history",
        "Mahatma Gandhi’s first satyagraha in India was at:",
        "भारत में महात्मा गांधी का पहला सत्याग्रह कहाँ हुआ?",
        "Champaran", "चंपारण", "Dandi", "दांडी", "Bardoli", "बारदोली", 0,
        "1917 का चंपारण सत्याग्रह भारत में गांधी का पहला सत्याग्रह माना जाता है।"))
    A(g("history",
        "The Non-Cooperation Movement was started in:",
        "असहयोग आंदोलन कब शुरू हुआ?",
        "1920", "1920", "1930", "1930", "1942", "1942", 0,
        "असहयोग आंदोलन 1920 में शुरू हुआ। 1930 सविनय अवज्ञा और 1942 भारत छोड़ो आंदोलन है।"))
    A(g("history",
        "The Dandi March is associated with which movement?",
        "दांडी मार्च किस आंदोलन से जुड़ा है?",
        "Civil Disobedience", "सविनय अवज्ञा", "Non-Cooperation", "असहयोग", "Quit India", "भारत छोड़ो", 0,
        "1930 की दांडी यात्रा नमक कानून तोड़ने और सविनय अवज्ञा आंदोलन की शुरुआत थी।"))
    A(g("history",
        "The Quit India Movement was launched in:",
        "भारत छोड़ो आंदोलन कब शुरू हुआ?",
        "August 1942", "अगस्त 1942", "April 1919", "अप्रैल 1919", "March 1930", "मार्च 1930", 0,
        "8 अगस्त 1942 को बॉम्बे अधिवेशन में भारत छोड़ो प्रस्ताव पारित हुआ।"))
    A(g("history",
        "The leader of the Bardoli Satyagraha was:",
        "बारदोली सत्याग्रह के नेता कौन थे?",
        "Vallabhbhai Patel", "वल्लभभाई पटेल", "Jawaharlal Nehru", "जवाहरलाल नेहरू", "Bal Gangadhar Tilak", "बाल गंगाधर तिलक", 0,
        "1928 के बारदोली किसान सत्याग्रह का नेतृत्व वल्लभभाई पटेल ने किया।"))
    A(g("history",
        "The Revolt of 1857 began at:",
        "1857 का विद्रोह कहाँ से शुरू हुआ?",
        "Meerut", "मेरठ", "Delhi", "दिल्ली", "Kanpur", "कानपुर", 0,
        "10 मई 1857 को मेरठ में सिपाही विद्रोह शुरू हुआ और फिर दिल्ली पहुँचा।"))
    A(g("history",
        "Who founded the Mauryan Empire?",
        "मौर्य साम्राज्य की स्थापना किसने की?",
        "Chandragupta Maurya", "चंद्रगुप्त मौर्य", "Ashoka", "अशोक", "Harsha", "हर्ष", 0,
        "चंद्रगुप्त मौर्य ने चाणक्य की सहायता से मौर्य वंश की स्थापना की। अशोक उसके बाद के प्रसिद्ध शासक हैं।"))
    A(g("history",
        "The capital of the Mauryan Empire was:",
        "मौर्य साम्राज्य की राजधानी थी:",
        "Pataliputra", "पाटलिपुत्र", "Taxila", "तक्षशिला", "Ujjain", "उज्जैन", 0,
        "पाटलिपुत्र (आज का पटना) मौर्यों की राजधानी थी।"))
    A(g("history",
        "Gautam Buddha attained enlightenment at:",
        "गौतम बुद्ध को ज्ञान कहाँ प्राप्त हुआ?",
        "Bodh Gaya", "बोधगया", "Sarnath", "सारनाथ", "Lumbini", "लुम्बिनी", 0,
        "ज्ञान बोधगया में, पहला उपदेश सारनाथ में और जन्म लुम्बिनी में हुआ।"))
    A(g("history",
        "Mahavira attained nirvana at:",
        "महावीर को निर्वाण कहाँ प्राप्त हुआ?",
        "Pawapuri", "पावापुरी", "Vaishali", "वैशाली", "Rajgir", "राजगीर", 0,
        "जैन धर्म के 24वें तीर्थंकर महावीर का निर्वाण पावापुरी (नालंदा, बिहार) में माना जाता है।"))
    A(g("history",
        "The Battle of Plassey was fought in:",
        "प्लासी का युद्ध कब हुआ?",
        "1757", "1757", "1764", "1764", "1857", "1857", 0,
        "प्लासी 1757 में और बक्सर 1764 में लड़ा गया।"))
    A(g("history",
        "The Battle of Buxar was fought in:",
        "बक्सर का युद्ध कब हुआ?",
        "1764", "1764", "1757", "1757", "1526", "1526", 0,
        "बक्सर का युद्ध 1764 में हुआ। इसके बाद ईस्ट इंडिया कंपनी की स्थिति और मजबूत हुई।"))
    A(g("history",
        "Who introduced the silver rupee and developed the Grand Trunk Road?",
        "चाँदी का रुपया और ग्रांड ट्रंक रोड के विकास से कौन जुड़ा है?",
        "Sher Shah Suri", "शेर शाह सूरी", "Akbar", "अकबर", "Alauddin Khalji", "अलाउद्दीन खिलजी", 0,
        "शेर शाह सूरी ने रुपया चलाया और जी. टी. रोड को बेहतर करवाया। उसका मकबरा सासाराम में है।"))
    A(g("history",
        "The Constitution of India was adopted on:",
        "भारत का संविधान कब अंगीकृत हुआ?",
        "26 November 1949", "26 नवम्बर 1949", "26 January 1950", "26 जनवरी 1950", "15 August 1947", "15 अगस्त 1947", 0,
        "अंगीकरण 26 नवम्बर 1949 को हुआ और लागू 26 जनवरी 1950 को हुआ।"))
    A(g("history",
        "The Constitution of India came into force on:",
        "भारत का संविधान कब लागू हुआ?",
        "26 January 1950", "26 जनवरी 1950", "26 November 1949", "26 नवम्बर 1949", "15 August 1947", "15 अगस्त 1947", 0,
        "26 जनवरी 1950 को संविधान लागू हुआ और भारत गणतंत्र बना।"))
    A(g("history",
        "Who is known as the Napoleon of India?",
        "‘भारत का नेपोलियन’ किसे कहा जाता है?",
        "Samudragupta", "समुद्रगुप्त", "Ashoka", "अशोक", "Chandragupta II", "चंद्रगुप्त द्वितीय", 0,
        "सैन्य विजयों के कारण इतिहासकार वी. ए. स्मिथ ने समुद्रगुप्त को भारत का नेपोलियन कहा।"))
    A(g("history",
        "The second Buddhist council was held at:",
        "दूसरी बौद्ध संगीति कहाँ हुई?",
        "Vaishali", "वैशाली", "Rajgir", "राजगीर", "Pataliputra", "पाटलिपुत्र", 0,
        "पहली संगीति राजगृह में और दूसरी वैशाली में हुई।"))
    A(g("history",
        "Who among the following was associated with the foundation of the Gupta power?",
        "गुप्त शक्ति की स्थापना से कौन जुड़ा है?",
        "Sri Gupta / Chandragupta I line", "श्रीगुप्त / चंद्रगुप्त प्रथम की परम्परा", "Ashoka", "अशोक", "Harsha", "हर्ष", 0,
        "गुप्त वंश की शुरुआत श्रीगुप्त से मानी जाती है और चंद्रगुप्त प्रथम से साम्राज्य फैला। अशोक मौर्य और हर्ष वर्धन बाद के शासक हैं।"))
    A(g("history",
        "Which of the following is correct?",
        "निम्न में कौन-सा सही है?",
        "Plassey — 1757", "प्लासी — 1757", "Buxar — 1764", "बक्सर — 1764", "Plassey — 1764", "प्लासी — 1764", 3,
        "(A) और (B) दोनों सही हैं। प्लासी 1757 और बक्सर 1764 का युद्ध है। (C) गलत है, इसलिए (D)।"))
    A(g("history",
        "Which of the following is correct about Gautam Buddha?",
        "गौतम बुद्ध के बारे में कौन-सा सही है?",
        "Enlightenment at Bodh Gaya", "ज्ञान बोधगया में", "First sermon at Sarnath", "पहला उपदेश सारनाथ में", "Birth at Pawapuri", "जन्म पावापुरी में", 3,
        "जन्म लुम्बिनी में हुआ था, पावापुरी में नहीं। (A) और (B) सही हैं, अतः (D)।"))

    # ---- Bihar ----
    A(g("bihar",
        "Bihar Diwas is celebrated on:",
        "बिहार दिवस कब मनाया जाता है?",
        "22 March", "22 मार्च", "26 January", "26 जनवरी", "15 August", "15 अगस्त", 0,
        "22 मार्च 1912 को बंगाल से अलग होकर बिहार प्रांत बना। यही बिहार दिवस है।"))
    A(g("bihar",
        "The capital of Bihar is:",
        "बिहार की राजधानी है:",
        "Patna", "पटना", "Gaya", "गया", "Muzaffarpur", "मुजफ्फरपुर", 0,
        "पटना बिहार की राजधानी और सबसे बड़ा नगर है। यह गंगा के किनारे बसा है।"))
    A(g("bihar",
        "How many districts are there in Bihar?",
        "बिहार में जिलों की संख्या कितनी है?",
        "38", "38", "40", "40", "28", "28", 0,
        "बिहार में 38 जिले और 9 प्रमंडल हैं।"))
    A(g("bihar",
        "The number of seats in the Bihar Legislative Assembly is:",
        "बिहार विधानसभा की सीटें हैं:",
        "243", "243", "200", "200", "40", "40", 0,
        "विधानसभा में 243 सीटें हैं। लोकसभा की 40 सीटें अलग हैं।"))
    A(g("bihar",
        "Bihar sends how many members to the Lok Sabha?",
        "बिहार लोकसभा में कितने सदस्य भेजता है?",
        "40", "40", "16", "16", "243", "243", 0,
        "बिहार की लोकसभा सीटें 40 और राज्यसभा सीटें 16 हैं।"))
    A(g("bihar",
        "Bihar sends how many members to the Rajya Sabha?",
        "बिहार राज्यसभा में कितने सदस्य भेजता है?",
        "16", "16", "40", "40", "243", "243", 0,
        "राज्यसभा में बिहार की 16 सीटें हैं।"))
    A(g("bihar",
        "Which river is called the Sorrow of Bihar?",
        "बिहार का शोक किस नदी को कहा जाता है?",
        "Kosi", "कोसी", "Son", "सोन", "Damodar", "दामोदर", 0,
        "बाढ़ के कारण कोसी को बिहार का शोक कहते हैं। दामोदर बंगाल का शोक कहलाती रही है।"))
    A(g("bihar",
        "Valmiki National Park is in which district?",
        "वाल्मीकि राष्ट्रीय उद्यान किस जिले में है?",
        "West Champaran", "पश्चिमी चंपारण", "Gaya", "गया", "Bhagalpur", "भागलपुर", 0,
        "वाल्मीकि नेशनल पार्क और टाइगर रिजर्व पश्चिमी चंपारण में है।"))
    A(g("bihar",
        "The Mahabodhi Temple is located at:",
        "महाबोधि मंदिर कहाँ है?",
        "Bodh Gaya", "बोधगया", "Nalanda", "नालंदा", "Vaishali", "वैशाली", 0,
        "महाबोधि मंदिर बोधगया में है, जहाँ बुद्ध को ज्ञान प्राप्त हुआ। यह यूनेस्को स्थल है।"))
    A(g("bihar",
        "Vikramshila University was located near present-day:",
        "विक्रमशिला विश्वविद्यालय आज के किस क्षेत्र के निकट था?",
        "Bhagalpur", "भागलपुर", "Sasaram", "सासाराम", "Muzaffarpur", "मुजफ्फरपुर", 0,
        "पाल शासकों की विक्रमशिला भागलपुर क्षेत्र में थी। नालंदा अलग प्राचीन विश्वविद्यालय है।"))
    A(g("bihar",
        "Sher Shah Suri’s tomb is at:",
        "शेर शाह सूरी का मकबरा कहाँ है?",
        "Sasaram", "सासाराम", "Patna", "पटना", "Rajgir", "राजगीर", 0,
        "शेर शाह का मकबरा सासाराम (रोहतास) में है।"))
    A(g("bihar",
        "The first Chief Minister of Bihar was:",
        "बिहार के पहले मुख्यमंत्री कौन थे?",
        "Sri Krishna Sinha", "श्री कृष्ण सिंह", "Anugrah Narayan Sinha", "अनुग्रह नारायण सिंह", "Karpoori Thakur", "कर्पूरी ठाकुर", 0,
        "श्री कृष्ण सिंह बिहार के पहले मुख्यमंत्री थे। अनुग्रह नारायण सिंह उनके सहयोगी उपमुख्यमंत्री रहे।"))
    A(g("bihar",
        "Dr Rajendra Prasad was born at:",
        "डॉ. राजेंद्र प्रसाद का जन्म कहाँ हुआ था?",
        "Ziradei (Siwan)", "जीरादेई (सीवान)", "Patna", "पटना", "Gaya", "गया", 0,
        "भारत के पहले राष्ट्रपति डॉ. राजेंद्र प्रसाद का जन्म सीवान के जीरादेई में हुआ था।"))
    A(g("bihar",
        "The state bird of Bihar is:",
        "बिहार का राज्य पक्षी है:",
        "House sparrow", "गौरैया", "Peacock", "मोर", "Koel", "कोयल", 0,
        "बिहार का राज्य पक्षी गौरैया है। मोर भारत का राष्ट्रीय पक्षी है।"))
    A(g("bihar",
        "The state animal of Bihar is:",
        "बिहार का राज्य पशु है:",
        "Gaur", "गौर (भारतीय बाइसन)", "Tiger", "बाघ", "Elephant", "हाथी", 0,
        "बिहार का राज्य पशु गौर है। बाघ राष्ट्रीय पशु है।"))
    A(g("bihar",
        "The state flower of Bihar is:",
        "बिहार का राज्य पुष्प है:",
        "Marigold", "गेंदा", "Lotus", "कमल", "Rose", "गुलाब", 0,
        "राज्य पुष्प गेंदा और राज्य वृक्ष पीपल है। कमल भारत का राष्ट्रीय फूल है।"))
    A(g("bihar",
        "The state tree of Bihar is:",
        "बिहार का राज्य वृक्ष है:",
        "Peepal", "पीपल", "Banyan", "बरगद", "Mango", "आम", 0,
        "बिहार का राज्य वृक्ष पीपल है। आम राज्य फल है।"))
    A(g("bihar",
        "Bhagalpur is famous as the:",
        "भागलपुर किसलिए प्रसिद्ध है?",
        "Silk city", "रेशम नगरी", "Steel city", "इस्पात नगरी", "Pink city", "गुलाबी नगरी", 0,
        "भागलपुर रेशम उत्पादन के लिए सिल्क सिटी कहलाता है।"))
    A(g("bihar",
        "Muzaffarpur is especially famous for:",
        "मुजफ्फरपुर विशेष रूप से किसलिए प्रसिद्ध है?",
        "Litchi", "लीची", "Tea", "चाय", "Cotton", "कपास", 0,
        "मुजफ्फरपुर की शाही लीची प्रसिद्ध है।"))
    A(g("bihar",
        "Madhubani painting is associated with:",
        "मधुबनी चित्रकला किस क्षेत्र से जुड़ी है?",
        "Mithila", "मिथिला", "Bhojpur", "भोजपुर", "Magadh only as a modern school", "केवल आधुनिक मगध स्कूल", 0,
        "मधुबनी पेंटिंग मिथिला क्षेत्र की परम्परा है।"))
    A(g("bihar",
        "The Patna High Court was established in:",
        "पटना उच्च न्यायालय की स्थापना कब हुई?",
        "1916", "1916", "1950", "1950", "1912", "1912", 0,
        "पटना हाईकोर्ट 1916 में स्थापित हुआ। बिहार प्रांत 1912 में बना था।"))
    A(g("bihar",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Kosi is called the Sorrow of Bihar", "कोसी को बिहार का शोक कहते हैं", "Bihar has 38 districts", "बिहार में 38 जिले हैं", "Bihar has 40 Lok Sabha seats", "बिहार की 40 लोकसभा सीटें हैं", 3,
        "तीनों कथन सही हैं, इसलिए ‘एक से अधिक’ अर्थात (D) उत्तर है।"))
    A(g("bihar",
        "The Ganga divides Bihar broadly into:",
        "गंगा बिहार को मोटे तौर पर किस रूप में बाँटती है?",
        "North Bihar and South Bihar", "उत्तर बिहार और दक्षिण बिहार", "East Bihar only", "केवल पूर्व बिहार", "Coastal and inland Bihar", "तटीय और भीतरी बिहार", 0,
        "गंगा बिहार को उत्तर और दक्षिण बिहार में बाँटती है। बिहार तटीय राज्य नहीं है।"))
    A(g("bihar",
        "Jayaprakash Narayan is associated with which movement of 1974?",
        "1974 के किस आंदोलन से जयप्रकाश नारायण जुड़े हैं?",
        "Bihar movement / Total Revolution", "बिहार आंदोलन / सम्पूर्ण क्रांति", "Dandi March", "दांडी मार्च", "Bardoli", "बारदोली", 0,
        "1974 का बिहार आंदोलन और सम्पूर्ण क्रांति का आह्वान जयप्रकाश नारायण से जुड़ा है।"))
    A(g("bihar",
        "The official language of Bihar is Hindi. The second official language is:",
        "बिहार की राजभाषा हिंदी है। दूसरी राजभाषा है:",
        "Urdu", "उर्दू", "Bengali", "बंगाली", "English only as the sole second language by statute of 1912", "केवल 1912 के कानून से अंग्रेजी", 0,
        "बिहार की राजभाषा हिंदी है और उर्दू दूसरी राजभाषा है।"))

    # ---- Geography ----
    A(g("geography",
        "The Tropic of Cancer does NOT pass through:",
        "कर्क रेखा किससे नहीं गुजरती?",
        "Bihar", "बिहार", "Gujarat", "गुजरात", "Jharkhand", "झारखंड", 0,
        "कर्क रेखा बिहार से नहीं गुजरती। वह गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा और मिजोरम से गुजरती है।"))
    A(g("geography",
        "Indian Standard Time is based on the meridian of:",
        "भारतीय मानक समय किस याम्योत्तर पर आधारित है?",
        "82°30′ E", "82°30′ पूर्व", "0°", "0°", "90° E", "90° पूर्व", 0,
        "82°30′ पूर्व याम्योत्तर इलाहाबाद (मिर्जापुर) के निकट है। IST, GMT से 5 घंटे 30 मिनट आगे है।"))
    A(g("geography",
        "IST is ahead of GMT by:",
        "IST, GMT से कितना आगे है?",
        "5 hours 30 minutes", "5 घंटे 30 मिनट", "4 hours 30 minutes", "4 घंटे 30 मिनट", "6 hours", "6 घंटे", 0,
        "भारतीय मानक समय ग्रीनविच से 5 घंटे 30 मिनट आगे है।"))
    A(g("geography",
        "The highest peak of India, lying fully in India, is generally taken as:",
        "भारत में स्थित सर्वोच्च चोटी किसे माना जाता है?",
        "Kangchenjunga", "कंचनजंगा", "Mount Everest", "माउंट एवरेस्ट", "Anaimudi", "अनाइमुडी", 0,
        "कंचनजंगा भारत की सबसे ऊँची चोटी है। एवरेस्ट नेपाल में है। अनाइमुडी प्रायद्वीपीय भारत की ऊँची चोटी है।"))
    A(g("geography",
        "The highest peak of the Western Ghats / south India is:",
        "पश्चिमी घाट / दक्षिण भारत की सबसे ऊँची चोटी है:",
        "Anaimudi", "अनाइमुडी", "Doda Betta", "डोडा बेट्टा", "Mahendragiri", "महेंद्रगिरि", 0,
        "अनाइमुडी केरल की अन्नामलाई पहाड़ियों में है और पश्चिमी घाट की सबसे ऊँची चोटी है।"))
    A(g("geography",
        "The river called Dakshin Ganga is:",
        "दक्षिण गंगा किस नदी को कहते हैं?",
        "Godavari", "गोदावरी", "Krishna", "कृष्णा", "Kaveri", "कावेरी", 0,
        "लंबाई और विस्तार के कारण गोदावरी को दक्षिण गंगा कहते हैं।"))
    A(g("geography",
        "Which of these rivers flows west into the Arabian Sea through a rift valley?",
        "इनमें कौन-सी नदी दरार घाटी से होकर पश्चिम में अरब सागर में गिरती है?",
        "Narmada", "नर्मदा", "Mahanadi", "महानदी", "Godavari", "गोदावरी", 0,
        "नर्मदा और तापी दरार घाटी में पश्चिम की ओर बहती हैं। गोदावरी और महानदी बंगाल की खाड़ी में जाती हैं।"))
    A(g("geography",
        "Hirakud dam is built on the river:",
        "हीराकुड बाँध किस नदी पर है?",
        "Mahanadi", "महानदी", "Godavari", "गोदावरी", "Krishna", "कृष्णा", 0,
        "हीराकुड ओडिशा में महानदी पर है।"))
    A(g("geography",
        "Bhakra Nangal dam is on the river:",
        "भाखड़ा नांगल बाँध किस नदी पर है?",
        "Sutlej", "सतलुज", "Beas", "ब्यास", "Ravi", "रावी", 0,
        "भाखड़ा नांगल सतलुज पर है।"))
    A(g("geography",
        "The Sardar Sarovar project is on the river:",
        "सरदार सरोवर परियोजना किस नदी पर है?",
        "Narmada", "नर्मदा", "Tapi", "तापी", "Mahi", "माही", 0,
        "सरदार सरोवर नर्मदा पर बनाया गया है।"))
    A(g("geography",
        "Chilika Lake is in:",
        "चिल्का झील कहाँ है?",
        "Odisha", "ओडिशा", "Kerala", "केरल", "Rajasthan", "राजस्थान", 0,
        "चिल्का ओडिशा में, वेम्बनाड केरल में और सांभर राजस्थान में है।"))
    A(g("geography",
        "Sambhar Lake is in:",
        "सांभर झील कहाँ है?",
        "Rajasthan", "राजस्थान", "Odisha", "ओडिशा", "Bihar", "बिहार", 0,
        "सांभर भारत की बड़ी खारे पानी की झील है और राजस्थान में है।"))
    A(g("geography",
        "India has how many states?",
        "भारत में राज्यों की संख्या कितनी है?",
        "28", "28", "29", "29", "25", "25", 0,
        "जम्मू-कश्मीर पुनर्गठन के बाद भारत में 28 राज्य और 8 केंद्रशासित प्रदेश हैं।"))
    A(g("geography",
        "Black soil of the Deccan is most suitable for:",
        "दक्कन की काली मिट्टी मुख्यतः किस फसल के लिए उपयुक्त है?",
        "Cotton", "कपास", "Jute", "जूट", "Tea", "चाय", 0,
        "रेगुर या काली मिट्टी कपास के लिए प्रसिद्ध है। जूट जलोढ़ और चाय पहाड़ी ढलान चाहती है।"))
    A(g("geography",
        "The Ganga originates from:",
        "गंगा का उद्गम कहाँ से माना जाता है?",
        "Gangotri glacier", "गंगोत्री हिमनद", "Yamunotri", "यमुनोत्री", "Mansarovar only as the Bhagirathi source", "केवल मानसरोवर को भागीरथी का स्रोत", 0,
        "भागीरथी का उद्गम गंगोत्री हिमनद से होता है। यमुना यमुनोत्री से निकलती है।"))
    A(g("geography",
        "Which soil is formed by intense leaching in heavy rainfall areas?",
        "अधिक वर्षा वाले क्षेत्रों में तीव्र निक्षालन से कौन-सी मिट्टी बनती है?",
        "Laterite", "लैटेराइट", "Alluvial", "जलोढ़", "Desert", "मरुस्थलीय", 0,
        "लैटेराइट मिट्टी भारी वर्षा में खनिजों के बह जाने से बनती है। जलोढ़ नदियों की लाई मिट्टी है।"))
    A(g("geography",
        "The standard meridian of India passes close to:",
        "भारत की मानक याम्योत्तर किसके निकट से गुजरती है?",
        "Mirzapur", "मिर्जापुर", "Kolkata", "कोलकाता", "Mumbai", "मुंबई", 0,
        "82°30′ पूर्व रेखा उत्तर प्रदेश के मिर्जापुर के निकट मानी जाती है।"))
    A(g("geography",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Godavari is called Dakshin Ganga", "गोदावरी को दक्षिण गंगा कहते हैं", "Narmada flows west", "नर्मदा पश्चिम की ओर बहती है", "Chilika is in Kerala", "चिल्का केरल में है", 3,
        "(A) और (B) सही हैं। चिल्का ओडिशा में है, केरल में नहीं। अतः (D)।"))

    # ---- Polity ----
    A(g("polity",
        "Article 21 of the Constitution deals with:",
        "संविधान का अनुच्छेद 21 किससे संबंधित है?",
        "Protection of life and personal liberty", "प्राण और दैहिक स्वतंत्रता की रक्षा", "Abolition of untouchability", "अस्पृश्यता का अंत", "Right to constitutional remedies", "संवैधानिक उपचारों का अधिकार", 0,
        "अनुच्छेद 21 प्राण और दैहिक स्वतंत्रता की रक्षा करता है। अस्पृश्यता 17 और उपचार 32 में हैं।"))
    A(g("polity",
        "Article 17 of the Constitution deals with:",
        "अनुच्छेद 17 किससे संबंधित है?",
        "Abolition of untouchability", "अस्पृश्यता का अंत", "Freedom of speech", "वाक् स्वतंत्रता", "Right to education", "शिक्षा का अधिकार", 0,
        "अनुच्छेद 17 अस्पृश्यता का अंत करता है। शिक्षा का अधिकार 21A है।"))
    A(g("polity",
        "Right to Education is provided under Article:",
        "शिक्षा का अधिकार किस अनुच्छेद में है?",
        "21A", "21A", "19", "19", "32", "32", 0,
        "86वें संशोधन से अनुच्छेद 21A जोड़ा गया, जो 6 से 14 वर्ष की शिक्षा का अधिकार देता है।"))
    A(g("polity",
        "Article 32 is related to:",
        "अनुच्छेद 32 किससे संबंधित है?",
        "Right to constitutional remedies", "संवैधानिक उपचार का अधिकार", "Directive Principles", "नीति निदेशक तत्व", "Emergency", "आपातकाल", 0,
        "डॉ. आंबेडकर ने अनुच्छेद 32 को संविधान का हृदय कहा है। यह उपचारों का अधिकार है।"))
    A(g("polity",
        "Fundamental Duties are contained in:",
        "मौलिक कर्तव्य किसमें हैं?",
        "Article 51A", "अनुच्छेद 51A", "Article 14", "अनुच्छेद 14", "Article 370", "अनुच्छेद 370", 0,
        "42वें संशोधन से भाग IV-A में अनुच्छेद 51A जोड़ा गया। वर्तमान में 11 मौलिक कर्तव्य हैं।"))
    A(g("polity",
        "How many Fundamental Duties are there at present?",
        "वर्तमान में मौलिक कर्तव्यों की संख्या कितनी है?",
        "11", "11", "10", "10", "6", "6", 0,
        "शुरुआत में 10 कर्तव्य थे। 86वें संशोधन ने 11वाँ कर्तव्य (6–14 वर्ष के बच्चों को शिक्षा का अवसर) जोड़ा।"))
    A(g("polity",
        "The words ‘Socialist’ and ‘Secular’ were added to the Preamble by the:",
        "प्रस्तावना में ‘समाजवादी’ और ‘पंथनिरपेक्ष’ किस संशोधन से जोड़े गए?",
        "42nd Amendment", "42वाँ संशोधन", "44th Amendment", "44वाँ संशोधन", "86th Amendment", "86वाँ संशोधन", 0,
        "42वाँ संशोधन, 1976, प्रस्तावना में समाजवादी, पंथनिरपेक्ष और अखंडता शब्द जोड़ता है।"))
    A(g("polity",
        "A Money Bill can be introduced only in:",
        "धन विधेयक केवल कहाँ पुरःस्थापित हो सकता है?",
        "Lok Sabha", "लोकसभा", "Rajya Sabha", "राज्यसभा", "Supreme Court", "उच्चतम न्यायालय", 0,
        "अनुच्छेद 110 वाला धन विधेयक केवल लोकसभा में पेश होता है।"))
    A(g("polity",
        "The Election Commission is provided under Article:",
        "निर्वाचन आयोग किस अनुच्छेद में है?",
        "324", "324", "280", "280", "148", "148", 0,
        "अनुच्छेद 324 निर्वाचन आयोग, 280 वित्त आयोग और 148 नियंत्रक एवं महालेखापरीक्षक से संबंधित है।"))
    A(g("polity",
        "The minimum age for election as President of India is:",
        "भारत के राष्ट्रपति बनने की न्यूनतम आयु है:",
        "35 years", "35 वर्ष", "25 years", "25 वर्ष", "30 years", "30 वर्ष", 0,
        "राष्ट्रपति और राज्यपाल के लिए 35 वर्ष, लोकसभा के लिए 25 और राज्यसभा के लिए 30 वर्ष निर्धारित हैं।"))
    A(g("polity",
        "The minimum age to become a member of the Lok Sabha is:",
        "लोकसभा सदस्य बनने की न्यूनतम आयु है:",
        "25 years", "25 वर्ष", "30 years", "30 वर्ष", "35 years", "35 वर्ष", 0,
        "लोकसभा 25 वर्ष और राज्यसभा 30 वर्ष।"))
    A(g("polity",
        "National emergency under Article 352 can be proclaimed on the ground of:",
        "अनुच्छेद 352 का राष्ट्रीय आपातकाल किस आधार पर लगाया जा सकता है?",
        "War, external aggression or armed rebellion", "युद्ध, बाह्य आक्रमण या सशस्त्र विद्रोह", "Failure of state government only", "केवल राज्य सरकार की विफलता", "Financial instability only", "केवल वित्तीय अस्थिरता", 0,
        "352 राष्ट्रीय आपातकाल है। राज्य सरकार की विफलता 356 और वित्तीय आपातकाल 360 है।"))
    A(g("polity",
        "President’s Rule in a state is related to Article:",
        "राज्य में राष्ट्रपति शासन किस अनुच्छेद से संबंधित है?",
        "356", "356", "352", "352", "360", "360", 0,
        "अनुच्छेद 356 राज्य में संवैधानिक तंत्र की विफलता पर राष्ट्रपति शासन से जुड़ा है।"))
    A(g("polity",
        "The 73rd Constitutional Amendment is related to:",
        "73वाँ संविधान संशोधन किससे संबंधित है?",
        "Panchayats", "पंचायतें", "Municipalities", "नगरपालिकाएँ", "GST", "जीएसटी", 0,
        "73वाँ संशोधन पंचायतों और 74वाँ नगरपालिकाओं के बारे में है। दोनों 1992 के हैं।"))
    A(g("polity",
        "The 74th Constitutional Amendment is related to:",
        "74वाँ संविधान संशोधन किससे संबंधित है?",
        "Municipalities", "नगरपालिकाएँ", "Panchayats", "पंचायतें", "Fundamental duties", "मौलिक कर्तव्य", 0,
        "74वाँ संशोधन शहरी स्थानीय निकायों यानी नगरपालिकाओं से संबंधित है।"))
    A(g("polity",
        "GST was introduced by which constitutional amendment?",
        "जीएसटी किस संविधान संशोधन से आया?",
        "101st Amendment", "101वाँ संशोधन", "42nd Amendment", "42वाँ संशोधन", "86th Amendment", "86वाँ संशोधन", 0,
        "101वाँ संशोधन जीएसटी का आधार है। इसे 1 जुलाई 2017 से लागू किया गया।"))
    A(g("polity",
        "Right to Property is at present:",
        "संपत्ति का अधिकार अभी क्या है?",
        "A legal right under Article 300A", "अनुच्छेद 300A के तहत विधिक अधिकार", "A Fundamental Right under Article 19", "अनुच्छेद 19 के तहत मौलिक अधिकार", "A Fundamental Duty", "मौलिक कर्तव्य", 0,
        "44वें संशोधन के बाद संपत्ति का अधिकार मौलिक अधिकार नहीं रहा। अब यह अनुच्छेद 300A का विधिक अधिकार है।"))
    A(g("polity",
        "Who is the constitutional head of the State executive?",
        "राज्य की कार्यपालिका का संवैधानिक प्रमुख कौन है?",
        "Governor", "राज्यपाल", "Chief Minister", "मुख्यमंत्री", "Chief Justice of the High Court", "उच्च न्यायालय का मुख्य न्यायाधीश", 0,
        "संवैधानिक प्रमुख राज्यपाल हैं। वास्तविक कार्यपालिका मुख्यमंत्री के नेतृत्व में मंत्रिपरिषद है।"))
    A(g("polity",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Article 17 abolishes untouchability", "अनुच्छेद 17 अस्पृश्यता समाप्त करता है", "Article 21A is the right to education", "अनुच्छेद 21A शिक्षा का अधिकार है", "Article 32 is about panchayats", "अनुच्छेद 32 पंचायतों के बारे में है", 3,
        "(A) और (B) सही हैं। अनुच्छेद 32 संवैधानिक उपचारों का है, पंचायतों का नहीं। अतः (D)।"))
    A(g("polity",
        "Uniform Civil Code is mentioned in:",
        "समान नागरिक संहिता का उल्लेख कहाँ है?",
        "Article 44, Directive Principles", "अनुच्छेद 44, नीति निदेशक तत्व", "Article 21, Fundamental Rights", "अनुच्छेद 21, मौलिक अधिकार", "Article 51A, Fundamental Duties", "अनुच्छेद 51A, मौलिक कर्तव्य", 0,
        "समान नागरिक संहिता अनुच्छेद 44 में नीति निदेशक तत्व के रूप में है, मौलिक अधिकार के रूप में नहीं।"))

    # ---- Economy / environment ----
    A(g("economy",
        "GST in India was implemented from:",
        "भारत में जीएसटी कब से लागू हुआ?",
        "1 July 2017", "1 जुलाई 2017", "1 April 2017", "1 अप्रैल 2017", "26 January 1950", "26 जनवरी 1950", 0,
        "वस्तु एवं सेवा कर 1 जुलाई 2017 से लागू हुआ।"))
    A(g("economy",
        "The Reserve Bank of India was established in:",
        "भारतीय रिज़र्व बैंक की स्थापना कब हुई?",
        "1935", "1935", "1947", "1947", "1950", "1950", 0,
        "RBI की स्थापना 1 अप्रैल 1935 को हुई थी।"))
    A(g("economy",
        "Who is called the father of Green Revolution in India?",
        "भारत में हरित क्रांति के जनक किसे कहा जाता है?",
        "M. S. Swaminathan", "एम. एस. स्वामीनाथन", "Verghese Kurien", "वर्गीज कुरियन", "C. Rangarajan", "सी. रंगराजन", 0,
        "एम. एस. स्वामीनाथन हरित क्रांति से जुड़े हैं। वर्गीज कुरियन श्वेत क्रांति से जुड़े हैं।"))
    A(g("economy",
        "The White Revolution is associated with:",
        "श्वेत क्रांति किससे जुड़ी है?",
        "Milk", "दूध", "Eggs", "अंडे", "Cotton", "कपास", 0,
        "श्वेत क्रांति दुग्ध उत्पादन से जुड़ी है। ऑपरेशन फ्लड वर्गीज कुरियन से जुड़ा है।"))
    A(g("economy",
        "NABARD is related to:",
        "नाबार्ड किससे संबंधित है?",
        "Rural and agricultural credit", "ग्रामीण और कृषि ऋण", "Space research", "अंतरिक्ष अनुसंधान", "Film certification", "फिल्म प्रमाणन", 0,
        "नाबार्ड कृषि और ग्रामीण विकास का वित्तपोषण देखता है।"))
    A(g("economy",
        "The Planning Commission was replaced by:",
        "योजना आयोग के स्थान पर क्या बना?",
        "NITI Aayog", "नीति आयोग", "Finance Commission", "वित्त आयोग", "Election Commission", "निर्वाचन आयोग", 0,
        "2015 में योजना आयोग के स्थान पर नीति आयोग बना।"))
    A(g("environment",
        "The ozone layer is found mainly in the:",
        "ओजोन परत मुख्यतः कहाँ पाई जाती है?",
        "Stratosphere", "समताप मंडल", "Troposphere only as its home", "केवल क्षोभमंडल उसका घर है", "Inner core of the earth", "पृथ्वी की आंतरिक क्रोड", 0,
        "ओजोन परत समताप मंडल में है और पराबैंगनी किरणों से रक्षा करती है।"))
    A(g("environment",
        "Chipko movement is associated with:",
        "चिपको आंदोलन किससे जुड़ा है?",
        "Protection of trees", "वृक्षों की रक्षा", "Construction of dams only", "केवल बाँध निर्माण", "Ban on all farming", "सभी खेती पर रोक", 0,
        "चिपको आंदोलन में लोग वृक्ष काटने से रोकने के लिए उनसे लिपटते थे।"))
    A(g("environment",
        "Project Tiger was launched in:",
        "प्रोजेक्ट टाइगर कब शुरू हुआ?",
        "1973", "1973", "1986", "1986", "1951", "1951", 0,
        "बाघ संरक्षण का प्रोजेक्ट टाइगर 1973 में शुरू हुआ।"))
    A(g("environment",
        "Which gas is the chief contributor to the natural greenhouse effect among these?",
        "इनमें प्राकृतिक ग्रीनहाउस प्रभाव का प्रमुख योगदान किसका है?",
        "Carbon dioxide", "कार्बन डाइऑक्साइड", "Oxygen", "ऑक्सीजन", "Nitrogen as a strong greenhouse gas", "नाइट्रोजन एक प्रबल ग्रीनहाउस गैस के रूप में", 0,
        "कार्बन डाइऑक्साइड प्रमुख ग्रीनहाउस गैस है। नाइट्रोजन और ऑक्सीजन इस भूमिका में मुख्य नहीं हैं।"))
    A(g("environment",
        "Kaziranga National Park is famous for:",
        "काजीरंगा राष्ट्रीय उद्यान किसलिए प्रसिद्ध है?",
        "One-horned rhinoceros", "एक सींग वाला गैंडा", "Asiatic lion", "एशियाई शेर", "Snow leopard as its main species", "मुख्य प्रजाति के रूप में हिम तेंदुआ", 0,
        "काजीरंगा, असम, एक सींग वाले गैंडे के लिए प्रसिद्ध है। एशियाई शेर गिर में हैं।"))

    # ---- Physics conceptual (numerics are generated) ----
    A(g("physics",
        "The SI unit of force is:",
        "बल का SI मात्रक है:",
        "Newton", "न्यूटन", "Joule", "जूल", "Watt", "वाट", 0,
        "बल का मात्रक न्यूटन, ऊर्जा का जूल और शक्ति का वाट है।"))
    A(g("physics",
        "The SI unit of electric current is:",
        "विद्युत धारा का SI मात्रक है:",
        "Ampere", "ऐम्पियर", "Volt", "वोल्ट", "Ohm", "ओम", 0,
        "धारा ऐम्पियर, विभवांतर वोल्ट और प्रतिरोध ओम में मापा जाता है।"))
    A(g("physics",
        "Sound cannot travel through:",
        "ध्वनि किसमें नहीं चल सकती?",
        "Vacuum", "निर्वात", "Steel", "इस्पात", "Water", "जल", 0,
        "ध्वनि को माध्यम चाहिए। निर्वात में वह नहीं चलती। ठोस और द्रव में चलती है।"))
    A(g("physics",
        "A light-year is a unit of:",
        "प्रकाश-वर्ष किसका मात्रक है?",
        "Distance", "दूरी", "Time", "समय", "Speed", "चाल", 0,
        "प्रकाश-वर्ष वह दूरी है जो प्रकाश एक वर्ष में तय करता है। यह समय का मात्रक नहीं है।"))
    A(g("physics",
        "Which lens is used to correct myopia?",
        "निकट दृष्टि दोष (मायोपिया) किस लेंस से ठीक किया जाता है?",
        "Concave lens", "अवतल लेंस", "Convex lens", "उत्तल लेंस", "Plane glass only", "केवल समतल काँच", 0,
        "मायोपिया में प्रतिबिंब रेटिना से पहले बनता है। अवतल लेंस किरणों को फैलाकर सुधार करता है। दूरदृष्टि में उत्तल लेंस लगता है।"))
    A(g("physics",
        "Which lens is used to correct hypermetropia?",
        "दूरदृष्टि दोष किस लेंस से ठीक होता है?",
        "Convex lens", "उत्तल लेंस", "Concave lens", "अवतल लेंस", "Cylindrical lens only in every case", "हर स्थिति में केवल बेलनाकार लेंस", 0,
        "हाइपरमेट्रोपिया में उत्तल लेंस लगता है, क्योंकि वह किरणों को अभिसारित करता है।"))
    A(g("physics",
        "The human eye forms the image of an object at the:",
        "मानव नेत्र वस्तु का प्रतिबिंब कहाँ बनाता है?",
        "Retina", "रेटिना", "Cornea", "कॉर्निया", "Iris", "परितारिका", 0,
        "प्रतिबिंब रेटिना पर बनता है। कॉर्निया प्रकाश को मोड़ता है और आइरिस प्रकाश की मात्रा नियंत्रित करती है।"))
    A(g("physics",
        "Fleming’s left-hand rule is used for:",
        "फ्लेमिंग का बाएँ हाथ का नियम किसके लिए है?",
        "The force on a current-carrying conductor in a magnetic field", "चुंबकीय क्षेत्र में धारावाही चालक पर बल", "The direction of induced current", "प्रेरित धारा की दिशा", "The colour of light", "प्रकाश का रंग", 0,
        "बायाँ हाथ मोटर प्रभाव (बल) बताता है। दायाँ हाथ जनरेटर में प्रेरित धारा की दिशा बताता है।"))
    A(g("physics",
        "The frequency of the AC supply in India is:",
        "भारत में प्रत्यावर्ती धारा की आवृत्ति है:",
        "50 Hz", "50 हर्ट्ज", "60 Hz", "60 हर्ट्ज", "100 Hz", "100 हर्ट्ज", 0,
        "घरेलू आपूर्ति 220 V और 50 Hz की होती है।"))
    A(g("physics",
        "Which colour deviates the most when white light passes through a prism?",
        "प्रिज्म में श्वेत प्रकाश का कौन-सा रंग सबसे अधिक मुड़ता है?",
        "Violet", "बैंगनी", "Red", "लाल", "Yellow", "पीला", 0,
        "बैंगनी का तरंगदैर्घ्य कम होने से विचलन सबसे अधिक और लाल का सबसे कम होता है।"))
    A(g("physics",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Myopia is corrected by a concave lens", "मायोपिया अवतल लेंस से ठीक होता है", "Hypermetropia is corrected by a convex lens", "दूरदृष्टि उत्तल लेंस से ठीक होती है", "Sound travels fastest in vacuum", "ध्वनि निर्वात में सबसे तेज चलती है", 3,
        "(A) और (B) सही हैं। ध्वनि निर्वात में नहीं चलती। अतः (D)।"))

    # ---- Chemistry ----
    A(g("chemistry",
        "The chemical formula of water is:",
        "जल का रासायनिक सूत्र है:",
        "H2O", "H2O", "CO2", "CO2", "NaCl", "NaCl", 0,
        "जल H2O, कार्बन डाइऑक्साइड CO2 और नमक NaCl है।"))
    A(g("chemistry",
        "The pH of a neutral solution at 25°C is:",
        "25°C पर उदासीन विलयन का pH है:",
        "7", "7", "0", "0", "14", "14", 0,
        "pH 7 उदासीन, 7 से कम अम्लीय और 7 से अधिक क्षारीय होता है।"))
    A(g("chemistry",
        "Baking soda is chemically:",
        "बेकिंग सोडा रासायनिक रूप से है:",
        "Sodium hydrogen carbonate", "सोडियम हाइड्रोजन कार्बोनेट", "Sodium chloride", "सोडियम क्लोराइड", "Calcium oxide", "कैल्शियम ऑक्साइड", 0,
        "बेकिंग सोडा NaHCO3 है। खाने का नमक NaCl और चूना CaO है।"))
    A(g("chemistry",
        "Washing soda is:",
        "धोने का सोडा है:",
        "Sodium carbonate", "सोडियम कार्बोनेट", "Sodium bicarbonate", "सोडियम बाइकार्बोनेट", "Calcium sulphate", "कैल्शियम सल्फेट", 0,
        "वॉशिंग सोडा Na2CO3 है। बेकिंग सोडा NaHCO3 है।"))
    A(g("chemistry",
        "Bleaching powder is:",
        "ब्लीचिंग पाउडर है:",
        "Calcium oxychloride", "कैल्शियम ऑक्सीक्लोराइड", "Sodium chloride", "सोडियम क्लोराइड", "Calcium carbonate", "कैल्शियम कार्बोनेट", 0,
        "ब्लीचिंग पाउडर CaOCl2 है। चूना पत्थर CaCO3 है।"))
    A(g("chemistry",
        "The most abundant gas in the Earth’s atmosphere is:",
        "पृथ्वी के वायुमंडल में सबसे प्रचुर गैस है:",
        "Nitrogen", "नाइट्रोजन", "Oxygen", "ऑक्सीजन", "Carbon dioxide", "कार्बन डाइऑक्साइड", 0,
        "वायुमंडल में नाइट्रोजन लगभग 78% और ऑक्सीजन लगभग 21% है।"))
    A(g("chemistry",
        "Rusting of iron requires:",
        "लोहे में जंग लगने के लिए चाहिए:",
        "Both oxygen and water", "ऑक्सीजन और जल दोनों", "Only nitrogen", "केवल नाइट्रोजन", "Only carbon dioxide in the absence of water", "जल के बिना केवल कार्बन डाइऑक्साइड", 0,
        "जंग के लिए ऑक्सीजन और नमी दोनों जरूरी हैं। सूखी हवा या ऑक्सीजन-रहित पानी अकेले काफी नहीं।"))
    A(g("chemistry",
        "The atomic number of an element is equal to the number of:",
        "किसी तत्व की परमाणु संख्या बराबर होती है:",
        "Protons", "प्रोटॉन", "Neutrons only", "केवल न्यूट्रॉन", "Neutrons plus electrons always as the definition", "परिभाषा के रूप में हमेशा न्यूट्रॉन जमा इलेक्ट्रॉन", 0,
        "परमाणु संख्या प्रोटॉनों की संख्या है। उदासीन परमाणु में इलेक्ट्रॉन भी उतने ही होते हैं।"))
    A(g("chemistry",
        "Isotopes of an element have the same:",
        "किसी तत्व के समस्थानिकों में समान होता है:",
        "Atomic number", "परमाणु संख्या", "Mass number", "द्रव्यमान संख्या", "Number of neutrons", "न्यूट्रॉनों की संख्या", 0,
        "समस्थानिकों का परमाणु क्रमांक समान और द्रव्यमान संख्या भिन्न होती है, क्योंकि न्यूट्रॉन अलग होते हैं।"))
    A(g("chemistry",
        "Diamond and graphite are allotropes of:",
        "हीरा और ग्रेफाइट किसके अपरूप हैं?",
        "Carbon", "कार्बन", "Silicon", "सिलिकॉन", "Sulphur", "सल्फर", 0,
        "हीरा और ग्रेफाइट कार्बन के अपरूप हैं।"))
    A(g("chemistry",
        "An acid and a base react to form:",
        "अम्ल और क्षार की अभिक्रिया से बनता है:",
        "Salt and water", "लवण और जल", "Only oxygen", "केवल ऑक्सीजन", "Only a metal", "केवल धातु", 0,
        "उदासीनीकरण में अम्ल + क्षार → लवण + जल।"))
    A(g("chemistry",
        "The ore of aluminium is:",
        "ऐलुमिनियम का अयस्क है:",
        "Bauxite", "बॉक्साइट", "Haematite", "हेमाटाइट", "Galena", "गैलेना", 0,
        "बॉक्साइट ऐलुमिनियम, हेमाटाइट लोहा और गैलेना सीसा का अयस्क है।"))
    A(g("chemistry",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Baking soda is NaHCO3", "बेकिंग सोडा NaHCO3 है", "Washing soda is Na2CO3", "धोने का सोडा Na2CO3 है", "Common salt is H2SO4", "साधारण नमक H2SO4 है", 3,
        "(A) और (B) सही हैं। साधारण नमक NaCl है, H2SO4 सल्फ्यूरिक अम्ल है। अतः (D)।"))

    # ---- Biology ----
    A(g("biology",
        "The powerhouse of the cell is:",
        "कोशिका का ऊर्जा गृह है:",
        "Mitochondria", "माइटोकॉन्ड्रिया", "Nucleus", "केंद्रक", "Ribosome", "राइबोसोम", 0,
        "माइटोकॉन्ड्रिया में श्वसन से ATP बनती है, इसलिए इसे ऊर्जा गृह कहते हैं।"))
    A(g("biology",
        "Photosynthesis takes place in:",
        "प्रकाश संश्लेषण कहाँ होता है?",
        "Chloroplast", "हरितलवक", "Mitochondria", "माइटोकॉन्ड्रिया", "Nucleus", "केंद्रक", 0,
        "हरितलवक में क्लोरोफिल होता है और वहीं प्रकाश संश्लेषण होता है।"))
    A(g("biology",
        "The number of chromosomes in a human somatic cell is:",
        "मानव की कायिक कोशिका में गुणसूत्रों की संख्या है:",
        "46", "46", "23", "23", "48", "48", 0,
        "कायिक कोशिका में 46 गुणसूत्र (23 जोड़े) होते हैं। युग्मक में 23 होते हैं।"))
    A(g("biology",
        "Haemoglobin is present in:",
        "हीमोग्लोबिन कहाँ होता है?",
        "Red blood cells", "लाल रक्त कणिकाएँ", "Platelets", "प्लेटलेट्स", "Plasma only as its main home", "मुख्य स्थान के रूप में केवल प्लाज्मा", 0,
        "हीमोग्लोबिन लाल रक्त कणिकाओं में होता है और ऑक्सीजन ढोता है। प्लेटलेट्स थक्का बनाने में मदद करती हैं।"))
    A(g("biology",
        "Which component of blood helps in clotting?",
        "रक्त का कौन-सा घटक थक्का बनाने में मदद करता है?",
        "Platelets", "प्लेटलेट्स", "Red blood cells", "लाल रक्त कणिकाएँ", "Plasma proteins only with no platelets", "बिना प्लेटलेट्स केवल प्लाज्मा", 0,
        "प्लेटलेट्स या थ्रोम्बोसाइट्स रक्त का थक्का जमाने में आवश्यक हैं।"))
    A(g("biology",
        "The largest gland in the human body is:",
        "मानव शरीर की सबसे बड़ी ग्रंथि है:",
        "Liver", "यकृत", "Pancreas", "अग्न्याशय", "Thyroid", "थायरॉइड", 0,
        "यकृत शरीर की सबसे बड़ी ग्रंथि है। अग्न्याशय इंसुलिन बनाता है।"))
    A(g("biology",
        "Insulin is secreted by the:",
        "इंसुलिन का स्राव कौन करता है?",
        "Pancreas", "अग्न्याशय", "Liver", "यकृत", "Kidney", "वृक्क", 0,
        "अग्न्याशय की बीटा कोशिकाएँ इंसुलिन बनाती हैं। इसकी कमी मधुमेह से जुड़ी है।"))
    A(g("biology",
        "Deficiency of vitamin C causes:",
        "विटामिन C की कमी से होता है:",
        "Scurvy", "स्कर्वी", "Rickets", "रिकेट्स", "Beri-beri", "बेरी-बेरी", 0,
        "विटामिन C की कमी से स्कर्वी, D से रिकेट्स और B1 से बेरी-बेरी होता है।"))
    A(g("biology",
        "Deficiency of vitamin D causes:",
        "विटामिन D की कमी से होता है:",
        "Rickets", "रिकेट्स", "Scurvy", "स्कर्वी", "Night blindness", "रतौंधी", 0,
        "विटामिन D की कमी से बच्चों में रिकेट्स होता है। रतौंधी विटामिन A से जुड़ी है।"))
    A(g("biology",
        "Night blindness is caused by deficiency of:",
        "रतौंधी किस विटामिन की कमी से होती है?",
        "Vitamin A", "विटामिन A", "Vitamin C", "विटामिन C", "Vitamin K", "विटामिन K", 0,
        "विटामिन A की कमी से रतौंधी होती है। विटामिन K रक्त का थक्का जमाने में काम आता है।"))
    A(g("biology",
        "Xylem in plants mainly transports:",
        "पौधों में जाइलम मुख्यतः क्या ढोता है?",
        "Water", "जल", "Food", "भोजन", "Only hormones downward", "केवल हार्मोन नीचे की ओर", 0,
        "जाइलम जल और खनिज ढोता है। फ्लोएम भोजन ढोता है।"))
    A(g("biology",
        "The anther of a flower produces:",
        "पुष्प का परागकोश क्या बनाता है?",
        "Pollen grains", "परागकण", "Ovules", "बीजाण्ड", "Seeds directly without pollination", "परागण के बिना सीधे बीज", 0,
        "परागकोश में परागकण बनते हैं। बीजाण्ड अंडाशय में होता है।"))
    A(g("biology",
        "Amoeba reproduces by:",
        "अमीबा जनन करता है:",
        "Binary fission", "द्विखंडन", "Budding", "मुकुलन", "Spore formation only", "केवल बीजाणु", 0,
        "अमीबा द्विखंडन से और हाइड्रा मुकुलन से जनन करता है।"))
    A(g("biology",
        "The functional unit of the kidney is:",
        "वृक्क की क्रियात्मक इकाई है:",
        "Nephron", "नेफ्रॉन", "Alveolus", "कूपिका", "Neuron", "न्यूरॉन", 0,
        "नेफ्रॉन वृक्क की इकाई है। कूपिका फेफड़े और न्यूरॉन तंत्रिका की इकाई है।"))
    A(g("biology",
        "Universal donor blood group is generally:",
        "सार्वत्रिक दाता रक्त समूह सामान्यतः है:",
        "O negative", "O निगेटिव", "AB positive", "AB पॉजिटिव", "A positive", "A पॉजिटिव", 0,
        "O निगेटिव को सार्वत्रिक दाता और AB पॉजिटिव को सार्वत्रिक ग्राही कहा जाता है।"))
    A(g("biology",
        "Which of the following is correct?",
        "निम्न में कौन सही है?",
        "Scurvy is due to lack of vitamin C", "स्कर्वी विटामिन C की कमी से होता है", "Rickets is due to lack of vitamin D", "रिकेट्स विटामिन D की कमी से होता है", "Night blindness is due to lack of vitamin C", "रतौंधी विटामिन C की कमी से होती है", 3,
        "(A) और (B) सही हैं। रतौंधी विटामिन A की कमी से होती है। अतः (D)।"))
    A(g("biology",
        "Mendel conducted his experiments on:",
        "मेंडल ने अपने प्रयोग किस पर किए?",
        "Pea plant", "मटर का पौधा", "Drosophila", "ड्रोसोफिला", "Maize only", "केवल मक्का", 0,
        "ग्रेगर मेंडल ने मटर के पौधे पर वंशागति के प्रयोग किए।"))
    A(g("biology",
        "Stomata help mainly in:",
        "रंध्र मुख्यतः किसमें सहायता करते हैं?",
        "Exchange of gases and transpiration", "गैसों के आदान-प्रदान और वाष्पोत्सर्जन", "Absorption of minerals from soil directly by leaves only", "केवल पत्तियों द्वारा मिट्टी से खनिज सोखना", "Production of pollen", "पराग बनाना", 0,
        "रंध्रों से गैसों का आदान-प्रदान और वाष्पोत्सर्जन होता है।"))

    # more mixed static that often appears with GS in TRE
    A(g("history",
        "Who gave the slogan ‘Do or Die’?",
        "‘करो या मरो’ का नारा किसने दिया?",
        "Mahatma Gandhi", "महात्मा गांधी", "Subhash Chandra Bose", "सुभाष चंद्र बोस", "Bhagat Singh", "भगत सिंह", 0,
        "1942 के भारत छोड़ो आंदोलन में गांधी ने ‘करो या मरो’ कहा।"))
    A(g("history",
        "Subhash Chandra Bose formed the:",
        "सुभाष चंद्र बोस ने किसकी स्थापना की?",
        "Indian National Army (Azad Hind Fauj)", "आजाद हिंद फौज", "Indian National Congress in 1885", "1885 में भारतीय राष्ट्रीय कांग्रेस", "Brahmo Samaj", "ब्रह्म समाज", 0,
        "सुभाष चंद्र बोस आजाद हिंद फौज से जुड़े। कांग्रेस की स्थापना ह्यूम के प्रयास से हुई थी।"))
    A(g("history",
        "The Simon Commission arrived in India in:",
        "साइमन कमीशन भारत कब आया?",
        "1928", "1928", "1919", "1919", "1942", "1942", 0,
        "साइमन कमीशन 1928 में भारत आया। इसमें कोई भारतीय सदस्य नहीं था, इसलिए विरोध हुआ।"))
    A(g("polity",
        "The Chairman of the Rajya Sabha is:",
        "राज्यसभा का सभापति होता है:",
        "The Vice-President of India", "भारत का उपराष्ट्रपति", "The Speaker", "लोकसभा अध्यक्ष", "The Chief Justice", "मुख्य न्यायाधीश", 0,
        "उपराष्ट्रपति राज्यसभा का पदेन सभापति होता है। लोकसभा अध्यक्ष अलग पद है।"))
    A(g("polity",
        "How many schedules were there originally in the Constitution, and how many are there now? Choose the present number.",
        "संविधान में वर्तमान में अनुसूचियों की संख्या कितनी है?",
        "12", "12", "8", "8", "10", "10", 0,
        "मूल संविधान में 8 अनुसूचियाँ थीं। वर्तमान में 12 अनुसूचियाँ हैं।"))
    A(g("geography",
        "The longest river of India is:",
        "भारत की सबसे लंबी नदी है:",
        "Ganga", "गंगा", "Godavari", "गोदावरी", "Yamuna", "यमुना", 0,
        "भारत की सीमा में गंगा सबसे लंबी नदी मानी जाती है। गोदावरी प्रायद्वीप की सबसे लंबी है।"))
    A(g("geography",
        "Which state is the largest producer of coffee in India?",
        "भारत में कॉफी का सबसे बड़ा उत्पादक राज्य कौन-सा है?",
        "Karnataka", "कर्नाटक", "Assam", "असम", "Punjab", "पंजाब", 0,
        "कर्नाटक भारत में कॉफी का प्रमुख उत्पादक है। असम चाय के लिए प्रसिद्ध है।"))
    A(g("bihar",
        "Sonepur cattle fair is held in:",
        "सोनपुर पशु मेला कहाँ लगता है?",
        "Saran district, near the Gandak-Ganga confluence", "सारण जिला, गंडक-गंगा संगम के निकट", "Gaya", "गया", "Bhagalpur", "भागलपुर", 0,
        "सोनपुर मेला सारण जिले में हरिहर क्षेत्र के निकट लगता है और एशिया के बड़े पशु मेलों में गिना जाता है।"))
    A(g("economy",
        "UPI, used for instant payments in India, is operated under the framework of:",
        "तत्काल भुगतान वाला UPI किसके ढाँचे से जुड़ा है?",
        "NPCI", "एनपीसीआई", "ISRO", "इसरो", "UGC", "यूजीसी", 0,
        "यूनिफाइड पेमेंट्स इंटरफेस नेशनल पेमेंट्स कॉर्पोरेशन ऑफ इंडिया (NPCI) का उत्पाद है।"))
    A(g("environment",
        "The Wildlife Protection Act was passed in:",
        "वन्यजीव संरक्षण अधिनियम कब बना?",
        "1972", "1972", "1986", "1986", "2000", "2000", 0,
        "वन्यजीव संरक्षण अधिनियम 1972 का है। पर्यावरण संरक्षण अधिनियम 1986 का है।"))
    A(g("physics",
        "The device based on electromagnetic induction used to increase or decrease AC voltage is:",
        "प्रत्यावर्ती वोल्टता घटाने-बढ़ाने वाला, विद्युत्चुंबकीय प्रेरण पर आधारित यंत्र है:",
        "Transformer", "ट्रांसफॉर्मर", "Dynamo only for DC storage", "केवल डीसी भंडारण के लिए डायनमो", "Ammeter", "अमीटर", 0,
        "ट्रांसफॉर्मर AC वोल्टता बदलता है। यह अन्योन्य प्रेरण पर काम करता है।"))
    A(g("chemistry",
        "The gas released when a metal reacts with an acid is usually:",
        "धातु और अम्ल की अभिक्रिया में सामान्यतः कौन-सी गैस निकलती है?",
        "Hydrogen", "हाइड्रोजन", "Oxygen", "ऑक्सीजन", "Nitrogen", "नाइट्रोजन", 0,
        "सक्रिय धातु अम्ल से क्रिया कर हाइड्रोजन गैस देती है।"))
    A(g("biology",
        "The process by which green plants prepare food is:",
        "हरी पत्तियों द्वारा भोजन बनाने की प्रक्रिया है:",
        "Photosynthesis", "प्रकाश संश्लेषण", "Transpiration", "वाष्पोत्सर्जन", "Respiration", "श्वसन", 0,
        "प्रकाश संश्लेषण में कार्बन डाइऑक्साइड और जल से प्रकाश की उपस्थिति में भोजन बनता है। वाष्पोत्सर्जन जल की हानि है।"))
    A(g("history",
        "Who was the first Governor-General of independent India?",
        "स्वतंत्र भारत के पहले गवर्नर-जनरल कौन थे?",
        "Lord Mountbatten", "लॉर्ड माउंटबेटन", "C. Rajagopalachari", "सी. राजगोपालाचारी", "Rajendra Prasad", "राजेंद्र प्रसाद", 0,
        "स्वतंत्र भारत के पहले गवर्नर-जनरल माउंटबेटन थे। सी. राजगोपालाचारी पहले भारतीय गवर्नर-जनरल थे। राजेंद्र प्रसाद पहले राष्ट्रपति थे।"))
    A(g("polity",
        "The idea of Fundamental Rights in the Indian Constitution is borrowed mainly from:",
        "भारतीय संविधान के मौलिक अधिकार मुख्यतः कहाँ से लिए गए हैं?",
        "The Constitution of the USA", "संयुक्त राज्य अमेरिका का संविधान", "The British Crown", "ब्रिटिश क्राउन", "The Canadian federation only for rights", "अधिकारों के लिए केवल कनाडा", 0,
        "मौलिक अधिकार अमेरिकी संविधान से प्रेरित हैं। संसदीय प्रणाली ब्रिटेन से और संघीय ढाँचा कनाडा से प्रभावित है।"))
    A(g("geography",
        "Which of the following states does the Tropic of Cancer pass through?",
        "कर्क रेखा निम्न में से किस राज्य से गुजरती है?",
        "Jharkhand", "झारखंड", "Bihar", "बिहार", "Odisha", "ओडिशा", 0,
        "कर्क रेखा झारखंड से गुजरती है, बिहार और ओडिशा से नहीं।"))
    A(g("bihar",
        "Nalanda Mahavihara is a UNESCO World Heritage Site in:",
        "नालंदा महाविहार यूनेस्को विश्व धरोहर किस जिले में है?",
        "Nalanda", "नालंदा", "Siwan", "सीवान", "Katihar", "कटिहार", 0,
        "प्राचीन नालंदा महाविहार नालंदा जिले में है।"))
    A(g("economy",
        "Who is associated with the White Revolution in India?",
        "भारत की श्वेत क्रांति से कौन जुड़े हैं?",
        "Verghese Kurien", "वर्गीज कुरियन", "M. S. Swaminathan", "एम. एस. स्वामीनाथन", "Norman Borlaug", "नॉर्मन बोरलॉग", 0,
        "वर्गीज कुरियन को श्वेत क्रांति का जनक कहा जाता है। स्वामीनाथन हरित क्रांति से जुड़े हैं।"))

    # dedupe
    seen = set()
    out = []
    for item in R:
        if item["q"] in seen:
            continue
        seen.add(item["q"])
        out.append(item)
    return out


if __name__ == "__main__":
    b = build_gs()
    from collections import Counter
    print("gs", len(b), Counter(x["topic"] for x in b))
