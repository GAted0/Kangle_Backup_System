#### 这是一个基于Django的Kangle备份系统

这是一个基于Django的Kangle备份系统

在Kangle每日备份完后，用脚本将备份数据打包备份到备份服务器指定目录

可用于对接WHMCS和SWAPIDC，在开通和终止用户产品时调用备份系统的API创建和删除用户，看着插件源码对应着程序api自己改改就行

可以对接多个（不限数量）Kangle服务器，统一管理备份

本来想完整开发前后端的，但是写完前端后我发现勉强能用，Django自带数据库管理，后端的意义不是太大


![](https://ae01.alicdn.com/kf/U8e5ef803729e4c82a329f0af94ac1c85p.png)

![](https://ae01.alicdn.com/kf/U592befbbe7064bfdacf659f089e0cde3v.png)

![](https://ae01.alicdn.com/kf/U1746f4a19ba24f388c682146ddb8ec790.png)

