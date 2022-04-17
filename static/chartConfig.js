const title = id => {return {
    'text': `<h4>${id}</h4>`,
    'useHTML': true
}};

const plotOptions = {
    series:{
        showInNavigator: true
    }
};

const rangeSelector = { 
    buttons: [{
        type: 'hour',
        count: 1,
        text: '1h'
    }, {
        type: 'day',
        count: 1,
        text: '1d'
    }, {
        type: 'day',
        count: 3,
        text: '3d'
    }, {
        type: 'all',
        text: 'All'
    }],
    selected : 4
};

const tooltip = {
    pointFormat: '<span style="color:{series.color}">\
        {series.name}</span>: <b>{point.y}</b>',
    valueDecimals: 2,
    split: true
};

const yAxis = {
    title: {
        text:"Speed Km/h"
    }
};

const chart = {
    events: {
        load: function () {
            // set up the updating of the chart each second
            // let series = this.series[0];
            // series.update({'data':data});
        }
    }
};

const lang = {
    noData: "No Driving Speed Data"
};

const noData = {
    style: {
        fontWeight: 'bold',
        fontSize: '24px',
        color: '#303030'
    }
}


const monitor_seperate_config = (id,data) => {return{
    title:title(id),
    yAxis:yAxis,
    plotOptions:plotOptions,
    tooltip:tooltip,
    series: [{
        name:id,
        data:data.data,
        color:data.color
    }],
    rangeSelector:rangeSelector,
    chart:chart,
    lang:lang,
    noData:noData,
    navigator: { adaptToUpdatedData: true }
}};

const monitor_all_config = {
    title: {
        'text': `<h4>Real Time Driving Speed Monitor</h4>`,
        'useHTML': true
    },
    plotOptions: {
        series: {
            compare: 'percent',
            showInNavigator: true
        }
    },
    rangeSelector: rangeSelector,
    tooltip: {
        pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
        valueDecimals: 2,
        split: true
    },
    yAxis:yAxis,
    chart:chart,
    legend: {
        layout: 'horizontal',
        align: 'center',
        borderWidth: 0,
        enabled:true
    },
    lang:lang,
    noData:noData,
    navigator:{ adaptToUpdatedData: false }
};