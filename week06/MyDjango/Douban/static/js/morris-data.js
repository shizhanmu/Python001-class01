$(function() {
    let lg05 = $("#morris-donut-chart").attr('lg05')
    let lt05 = $("#morris-donut-chart").attr('lt05')
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "四星五星",
            value: lg05
        }, {
            label: "三星以下",
            value: lt05
        }],
        resize: true
    });


});
