import os
import sys

sys.path.append(os.environ['ceroot'])

from kpi import AccKpi
from kpi import DurationKpi

flowers_8_AllReduce_CPU_4_Cards_train_acc_kpi = AccKpi(
    'flowers_8_AllReduce_CPU_4_Cards_train_acc', 0.03, 0, actived=True)
flowers_8_AllReduce_CPU_4_Cards_train_speed_kpi = AccKpi(
    'flowers_8_AllReduce_CPU_4_Cards_train_speed', 0.06, 0, actived=True)

flowers_8_Reduce_CPU_4_Cards_train_acc_kpi = AccKpi(
    'flowers_8_Reduce_CPU_4_Cards_train_acc', 0.03, 0, actived=True)
flowers_8_Reduce_CPU_4_Cards_train_speed_kpi = AccKpi(
    'flowers_8_Reduce_CPU_4_Cards_train_speed', 0.06, 0, actived=True)

flowers_8_CPU_1_Cards_train_acc_kpi = AccKpi(
    'flowers_8_CPU_1_Cards_train_acc', 0.03, 0, actived=True)
flowers_8_CPU_1_Cards_train_speed_kpi = AccKpi(
    'flowers_8_CPU_1_Cards_train_speed', 0.06, 0, actived=True)

tracking_kpis = [
    flowers_8_AllReduce_CPU_4_Cards_train_acc_kpi,
    flowers_8_AllReduce_CPU_4_Cards_train_speed_kpi,
    flowers_8_Reduce_CPU_4_Cards_train_acc_kpi,
    flowers_8_Reduce_CPU_4_Cards_train_speed_kpi,
    flowers_8_CPU_1_Cards_train_acc_kpi,
    flowers_8_CPU_1_Cards_train_speed_kpi,
]
