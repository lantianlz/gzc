
//股票详情数据抓取
//SELECT code FROM `www`.`stock_stock` where belong_market=0 ORDER BY id   LIMIT 300, 150
var codes = ["600517","600376","600458","600486","600663","600767","600052","600850","600894","601919","600697","600305","600456","600201","600516","600513","600114","600128","600084","600383","600616","600029","600730","600652","600157","600133","600086","600889","600096","601018","600115","600779","600416","600141","601012","600266","600601","600292","600005","600539","600275","601718","600469","600420","600489","600150","601618","600760","600432","600596","601901","600980","600362","600805","600696","601899","600419","600072","600385","600268","601799","600559","600429","600970","600661","600438","600708","600360","600234","600523","601199","600717","600260","600195","600132","600743","600818","600155","600674","600769","600858","600844","600098","600990","601009","600545","600761","603288","601567","600219","600055","600864","600027","600506","600071","600218","601872","600026","600973","600183","600067","600461","600480","600816","600967","600624","600576","600182","601866","601099","600881","601179","601766","600785","600611","601139","600649","600839","600075","600057","601800","601555","600090","601801","600105","601390","603077","600120","600823","601313","600704","601333","601288","600845","601311","600113","600011","600058","600961","600074","601336","600097","600829","600988","600689","600119","600877","601126","600590","600749"];
for(i in codes)
{
    var params = {
            url: "/crawltools/add?site=http://www.zhixuan.com/",
            data: {"sid":"2528332", "type":"pc", "url":"http://www.zhixuan.com/stock/" + codes[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}






//股票动态数据抓取
var feed_ids = ["7201","14632","14633","16683","24376","5969","25688","1638","17511","24947","1652","22412","15514","23470","14543","13784","16895","7171","8531","2977","18941","16896","22551","18715","20513","16686","22152","923","22939","674","12726","6359","13534","25061","1259","16386","18436","18440","12327","24111","832","4674","17733","22603","12620","5230","12697","12698","9375","17325","6322","19664","19677","4831","20199","7204","11606","12903","15497","1475","19172","5607","7153","12032","5641","12329","5427","2615","2619","18494","19774","23116","24981","2710","2202","7589","15326","12547","20232","21769","20287","8513","14145","19271","6749","12382","12383","1149","12669","8329","655","914","14237","23979","20915","16839","21960","22998","21987","22248","24808","21508","18189","22797","22798","18202","18204","1060","23335","6217","15999","896","12930","15510","12703","20128","19120","23738","12733","19203","21507","19204","15898","7200","19525","16717","848","22352","10325","11876","12904","10867","22912","18305","665","23974","4785","18371","1509","5624","6392","9735","20260","12325","4655","11065","24125","21849","10593","13927","16744","12905","24456","19346","12445","25770","4795","7370","9435","21477","15407","11066","16724","10849","17253","17258","20851","898","649","24205","22932","7322","941","20159","4824","8411","4829","2796","12781","11047","23365","21845","855","23142","19341","12701","1214","2244","14024","13271","25815","4832","23271","12295","16656","16657","21010","14625","19751","24656","19030","7257","17508","1128","15987","12436","10652","9373","17361","730","19424","17384","8434","23362","2905","8883","26038","22711","752","12023","8706","15923","18498","13892","8518","13894","8532","8793","10330","20364","2207","9386","12750","12751","21764","5647","4896","12326","15910","2855","15406","24112","5205","16742","24941","22930","8596","12738","22978","3032","17123","12792","9466","19454","12293","22808","22809","11828","5225","4218","4219","8318","14226","9369","25277","10697","24781","22245","1267","16635","20247","6680","1311","16673","3106","11831","4164","4441","23390","5727","3945","8561","15986","10897","15506","12444","8608","10918","4263","23978","8705","13587","1561","23076","12590","15922","13895","15442"];
for(i in feed_ids)
{
    var params = {
            url: "/crawltools/add?site=http://www.zhixuan.com/",
            data: {"sid":"2528332", "type":"pc", "url":"http://www.zhixuan.com/stock/feed/" + feed_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}


//头条文章抓取
//SELECT id FROM `www`.`toutiao_article` where is_silence = 0 and state=1  ORDER BY id   LIMIT 149
var codes = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","38","40","43","45","46","47","48","49","50","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","75","76","77","78","79","80","81","82","83","84","88","89","92","96","97","98","99","100","101","102","103","104","116","117","118","119","120","121","122","123","124","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","222","223","224","225","226","227","228","229","230","241","242","243","244","245","246","247","248","249","250"];
for(i in codes)
{
    var params = {
            url: "/crawltools/add?site=http://www.zhixuan.com/",
            data: {"sid":"2528332", "type":"pc", "url":"http://www.zhixuan.com/toutiao/article/" + codes[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}




//提问数据抓取
var question_ids = ["375","374","373","372","284","362","371","367","370","364","369","366","340","368","348","365","363","358","177","361","279","353",
"359","360","357","354","356","355","351","350","352","349","332","346","347","345","343","344","342","341","261","339","331","338","337","336","335",
"124","334","333","322","323","329","325","324","330","328","319","326","327","315","321","320","318","247","309","243","317","316","314","313","312",
"311","308","305","310","307","306","304","303","302","301","300","299","296","298","291","297","282","289","295","294","293","292","290","288","17","287","286","281"];
for(i in question_ids)
{
    var params = {
            url: "/crawltools/add?site=http://www.zhixuan.com/",
            data: {"sid":"2528332", "type":"pc", "url":"http://www.zhixuan.com/question/" + question_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}




//重庆营业部数据抓取
//SELECT id FROM `kaihu`.`kaihu_department` where city_id = 1932
var d_ids = ["4149","1080","788","829","813","990","950","5900","5809","5865","5857","5781","5877","5787","5810","5785","5764","6028","5618","5244","5439",
"5442","5523","5453","5408","5335","5668","6103","6113","4534","1444","1303","1443","1430","1439","1422","4972","2990","2905","3378","3388","3187","3160","3168",
"3462","3426","3471","3435","3134","3714","3764","3716","2196","2298","2024","2139","1990","2134","2077","2126","2178","2008","1823","1966","1922","47","40",
"2688","2804","4070","3810","1548","1577","1590","1701","5067","5125","4827","1279","4027","3677","5205","5227","5218","2416","2567","183","4770","7","4282",
"4294","4317","4258","743","2850","5036","4723","4704","4680","4685","4694","4698","4660","4656","4671","4716","4676","4688","4724","4684","4702","4720","4666",
"4665","4662","4710","4703","4652","4712","4686","4650","4718","4667","4717","4689","4725","4678","4663","4722","4687","4679","4673","4700","4711","4692","396",
"500","434","584","568","3901","3832"];
for(i in d_ids)
{
    var params = {
            url: "/crawltools/add?site=http://chongqing.zhixuan.com/",
            data: {"sid":"2528361", "type":"pc", "url":"http://chongqing.zhixuan.com/kaihu/department_detail/" + d_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}

//重庆理财资讯数据抓取
//SELECT id FROM `kaihu`.`kaihu_article`  where city_id = "1932"
var a_ids = ["1","2","3","7","9","10","11","12","13","16","17","18","19","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37",
"38","39","40","41","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","60","64","65","66","67","68","69","71","72"];
for(i in a_ids)
{
    var params = {
            url: "/crawltools/add?site=http://chongqing.zhixuan.com/",
            data: {"sid":"2528361", "type":"pc", "url":"http://chongqing.zhixuan.com/kaihu/article/" + a_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}






//成都营业部数据抓取
//SELECT id FROM `kaihu`.`kaihu_department` where city_id = 1974
var d_ids = ["26","58","152","450","520","566","605","632","634","714","907","1069","1083","1273","1360","1538","1726","1731","1799","1837","1838","1840","1842",
"1846","1847","1850","1851","1856","1857","1860","1863","1864","1867","1868","1924","1940","2082","2115","2147","2148","2253","2276","2455","2469","2578","2681",
"2687","2689","2693","2694","2701","2702","2706","2711","2775","2792","2958","2981","3163","3227","3254","3259","3270","3296","3339","3416","3439","3455","3459",
"3474","3480","3486","3488","3489","3594","3605","3622","3668","3811","3895","4019","4215","4239","4241","4253","4259","4271","4275","4364","4375","4377","4387",
"4397","4446","4450","4451","4475","4476","4477","4507","4533","4571","4644","4701","4730","4731","4740","4788","4809","4823","4864","4924","4965","5028","5105",
"5172","5257","5260","5361","5410","5510","5534","5535","5608","5617","5655","5794","5795","5814","5830","6029","6144"];
for(i in d_ids)
{
    var params = {
            url: "/crawltools/add?site=http://chengdu.zhixuan.com/",
            data: {"sid":"2528359", "type":"pc", "url":"http://chengdu.zhixuan.com/kaihu/department_detail/" + d_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}


//成都理财资讯数据抓取
//SELECT id FROM `kaihu`.`kaihu_article`  where city_id = "1974"
var a_ids = ["4","5","6","8","14","15","20","42","43","59","61","62","63","70"];
for(i in a_ids)
{
    var params = {
            url: "/crawltools/add?site=http://chongqing.zhixuan.com/",
            data: {"sid":"2528359", "type":"pc", "url":"http://chongqing.zhixuan.com/kaihu/article/" + a_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}




//开户频道营业部新闻
var a_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 
102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 
130, 131, 132, 133, 134, 135, 136, 137];
for(i in a_ids)
{
    var params = {
            url: "/crawltools/add?site=http://kaihu.zhixuan.com/",
            data: {"sid":"2528358", "type":"pc", "url":"http://kaihu.zhixuan.com/kaihu/news/" + a_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}










//易钱财经
//SELECT id FROM `eqcj`.`article_article` ORDER BY id DESC  LIMIT 200
var a_ids = ["27985","27982","27980","27979","27978","27977","27973","27967","27965","27964","27963","27962","27960","27959","27954","27953",
"27952","27951","27948","27947","27946","27945","27942","27941","27940","27939","27938","27937","27936","27935","27934","27932","27931",
"27929","27928","27926","27925","27924","27923","27920","27917","27916","27915","27914","27913","27912","27900","27899","27898","27897",
"27896","27895","27894","27893","27892","27891","27890","27889","27888","27887","27886","27885","27884","27883","27882","27881","27874","27861",
"27860","27859","27858","27857","27856","27855","27854","27853","27852","27851","27850","27849","27848","27847","27846","27845","27844","27843",
"27842","27841","27834","27833","27832","27831","27830","27829","27828","27827","27826","27825","27824","27823","27822","27821","27820","27819",
"27812","27811","27810","27809","27808","27807","27806","27805","27804","27803","27802","27801","27800","27799","27798","27797","27796","27795",
"27794","27793","27792","27791","27790","27789","27788","27787","27786","27785","27784","27783","27782","27781","27780","27779","27778","27777",
"27776","27775","27774","27773","27772","27771","27770","27769","27768","27767","27766","27765","27764","27763","27762","27761","27748","27747",
"27746","27734","27727","27726","27725","27718","27717","27710","27709","27708","27707","27694","27693","27692","27691","27690","27689","27688",
"27687","27686","27685","27684","27683","27682","27681","27680","27679","27678","27677","27676","27675","27674","27673","27672","27671","27670",
"27669","27668","27667","27666","27665","27664"];
for(i in a_ids)
{
    var params = {
            url: "/crawltools/add?site=http://www.eqcj.com/",
            data: {"sid":"2652287", "type":"pc", "url":"http://www.eqcj.com/article/" + a_ids[i]},
            type: 'POST',
            success: function(data){},
        };
    $.ajax(params);
}

var a_ids = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19];
var atypes = ["tgn", "tgj", "tgs", "tzq"];
for(var i in a_ids)
{
    for(var j in atypes)
    {
        var params = {
                url: "/crawltools/add?site=http://www.eqcj.com/",
                data: {"sid":"2652287", "type":"pc", "url":"http://www.eqcj.com/" + atypes[j] + "/" + a_ids[i]},
                type: 'POST',
                success: function(data){},
            };
        $.ajax(params);
    }
}


