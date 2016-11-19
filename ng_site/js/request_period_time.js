var request_period_time = echarts.init(document.getElementById('request_period_time'), 'dark');
request_period_time.showLoading();
/*
$.get('data/asset/data/confidence-band.json', function (data) {
    request_period_time.hideLoading();

    var base = -data.reduce(function (min, val) {
        return Math.floor(Math.min(min, val.l));
    }, Infinity);
    request_period_time.setOption(*/
request_period_time_option = {
    title: {
        text: '最近1小时请求数',
        left: 'center'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            animation: false
        },
        formatter: function (params) {
            return params[2].name + '<br />' + params[2].value;
        }
    },
    /*
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        */
        xAxis: {
            type: 'category',
            data: data.map(function (item) {
                return item.date;
            }),
            axisLabel: {
                formatter: function (value, idx) {
                    var date = new Date(value);
                    return idx === 0 ? value : [date.getMonth() + 1, date.getDate()].join('-');
                }
            },
            splitLine: {
                show: false
            },
            boundaryGap: false
        },
        yAxis: {
            axisLabel: {
                formatter: function (val) {
                    return (val - base) * 100 + '%';
                }
            },
            splitNumber: 3,
            splitLine: {
                show: false
            }
        },
    series: [{
        name: 'L',
        type: 'line',
        data: data.map(function (item) {
            return item.l + base;
        }),
        stack: 'confidence-band',
        symbol: 'none'
    }, {
        name: 'U',
        type: 'line',
        data: data.map(function (item) {
            return item.u - item.l;
        }),
        stack: 'confidence-band',
        symbol: 'none'
    }, {
        type: 'line',
        data: data.map(function (item) {
            return item.value + base;
        }),
        hoverAnimation: false,
        symbolSize: 6,
        showSymbol: false
    }]
};
