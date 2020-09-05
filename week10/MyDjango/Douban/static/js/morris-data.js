$(function() {
    let lg05 = $("#morris-donut-chart").attr('lg05')
    let lt05 = $("#morris-donut-chart").attr('lt05')
    let lz05 = $("#morris-donut-chart").attr('lz05')
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "正向评价",
            value: lg05
        }, {
            label: "负向评价",
            value: lt05
        },{
            label: "中性评价",
            value: lz05
        }],
        resize: true
    });


});
