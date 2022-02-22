from django.contrib import admin
from .models import Home, CvDownload, Profile, Project, Category, Skills, Social, Certificates, Company_certificates, Flag
admin.site.register(Home)

# Skills
class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInLine
    ]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Social)
admin.site.register(CvDownload)
admin.site.register(Certificates)
admin.site.register(Company_certificates)
admin.site.register(Flag)
