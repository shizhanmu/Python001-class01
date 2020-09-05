from django.shortcuts import render
from django.db.models import Avg, Count, Sum, Q

from .models import QipaoshuiCleaned, StatTable


def ranking(request):
    # 读取情感倾向排名表
    rankings = StatTable.objects.order_by('-mean', '-count').all()
    # 统计气泡水全部评论总量
    qipaoshuis = QipaoshuiCleaned.objects.all()
    counter_all = qipaoshuis.count()
    sent_avg_all = qipaoshuis.aggregate(total=Sum('sentiment'))['total'] / counter_all
    # 正向评价比例
    queryset = QipaoshuiCleaned.objects.values('sentiment')
    conditions = {'sentiment__gte': 2}
    plus_all = queryset.filter(**conditions).count()
    plus_all_share = plus_all/counter_all * 100
    # 负向评价比例
    queryset = QipaoshuiCleaned.objects.values('sentiment')
    conditions = {'sentiment': 0}
    minus_all = queryset.filter(**conditions).count()
    minus_all_share = minus_all/counter_all * 100
    # 中性数量
    queryset = QipaoshuiCleaned.objects.values('sentiment')
    conditions = {'sentiment': 1}
    neutral_all = queryset.filter(**conditions).count()
    # locals()自动将本函数中所有变量传递给模板文件
    return render(request, 'result_home.html', locals())

def detail(request, pid):
    # 通过 pid查询相应的评论列表
    p = StatTable.objects.get(id=pid)
    qipaoshuis = p.qipaoshuicleaned_set.order_by('-sentiment', '-qptime')
    counter = qipaoshuis.count()
    plus = qipaoshuis.filter(sentiment=2).count()
    plus_share = plus / counter * 100
    minus = qipaoshuis.filter(sentiment=0).count()
    minus_share = minus / counter * 100
    neutral = qipaoshuis.filter(sentiment=1).count()
    sent_avg = qipaoshuis.aggregate(total=Sum('sentiment'))['total'] / counter
    # locals()自动将本函数中所有变量传递给模板文件
    return render(request, 'result_detail.html', locals())

def search(request):
    # 搜索评论
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'result_home.html', {'error_msg': error_msg})

    qipaoshuis = QipaoshuiCleaned.objects.filter(Q(title__icontains=q) | Q(comment__icontains=q))
    return render(request, 'result_search.html', {'error_msg': error_msg,
                                               'qipaoshuis': qipaoshuis})