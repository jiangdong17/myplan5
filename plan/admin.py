from django.contrib import admin
# Register your models here.

from .models import Plans,Students
@admin.register(Plans)#使用装饰器注册，同时取消admin.site.register(Plans,PlansAdmin)#注册数据表
class PlansAdmin(admin.ModelAdmin):
    #列表属性

    list_display = ['pk','pname','pp_start_time','pp_long','pstart_time','pover_time','plong','pscore','pstudent']
    search_fields = ['pname']
    list_filter = ['pname']
    #list_fields = 5
    list_per_page = 5
   # field = ['pname','pp_start_time','pp_start_time','pp_long','pstart_time','pover_time','plong','pscore','pstudent']
    fieldsets = [
        ('time',{'fields':['pp_start_time','pp_long','pstart_time','pover_time','plong']}),
        ('base',{'fields':['pname','pscore','pstudent']}),
    ]

#admin.site.register(Plans,PlansAdmin)#注册数据表
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gen(self):
        if self.xgender:
            return '男'
        else:
            return '女'
    def dele(self):
        if self.isDelete:
            return "删除"
        else:
            return '删除'
    gen.short_description= "性别"
    #xid.short_description = "学号"


    list_display = ['xid', 'xschool', 'xgrade', 'xclass', 'xname', 'xage', gen,dele]
    search_fields = ['xname']
    list_filter = ['xname']
    #list_fields = 5
    list_per_page = 5
    field = ['xid', 'xschool', 'xgrade', 'xclass', 'xname', 'xage', 'xgender','isDelete']
    actions_on_bottom = True
    actions_on_top = False

#admin.site.register(Students,StudentsAdmin)#注册数据表