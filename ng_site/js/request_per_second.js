var request_per_second = echarts.init(document.getElementById('request_per_second'), 'dark');
request_per_second_option = {
    tooltip : {
        formatter: "{a} <br/>{c} {b}"
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    series: [{
        name:'每秒平均请求',
        type:'gauge',
        min:0,
        max:20,
        splitNumber:10,
        radius: '50%',
        data:[{value: 0, name: 'request/s'}]
    }]
};
