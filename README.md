# CVE-2023-21554-PoC

CVE-2023-21554 Windows MessageQueuing PoC，分析见 https://www.zoemurmure.top/posts/cve_2023_21554/

poc 文件执行前需要自行修改目标机器 IP 地址

poc 成功的标志是 mqsvc.exe 进程的崩溃，并没有弹窗信息，需要在类似进程监控器的程序里看到

![](https://www.zoemurmure.top/img/2023-05-16-17-00-24.png)
