from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import User


@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        if instance.designation == 'Admin':
            admin, created = Group.objects.get_or_create(name='Admin')
            instance.groups.add(admin)
        if instance.designation == 'Director':
            director, created = Group.objects.get_or_create(name='Director')
            instance.groups.add(director)
        if instance.designation == 'Account Manager':
            account_manager, created = Group.objects.get_or_create(name='Account Manager')
            instance.groups.add(account_manager)
        if instance.designation == 'Hr Manager':
            hr_manager, created = Group.objects.get_or_create(name='Hr Manager')
            instance.groups.add(hr_manager)
        if instance.designation == 'Team Leader':
            team_leader, created = Group.objects.get_or_create(name='Team Leader')
            instance.groups.add(team_leader)
        if instance.designation == 'Recruiter':
            recruiter, created = Group.objects.get_or_create(name='Recruiter')
            instance.groups.add(recruiter)
    else:
        if instance.designation == 'Admin':
            admin, created = Group.objects.get_or_create(name='Admin')
            instance.groups.add(admin)
        if instance.designation == 'Director':
            director, created = Group.objects.get_or_create(name='Director')
            instance.groups.add(director)
        if instance.designation == 'Account Manager':
            account_manager, created = Group.objects.get_or_create(name='Account Manager')
            instance.groups.add(account_manager)
        if instance.designation == 'Hr Manager':
            hr_manager, created = Group.objects.get_or_create(name='Hr Manager')
            instance.groups.add(hr_manager)
        if instance.designation == 'Team Leader':
            team_leader, created = Group.objects.get_or_create(name='Team Leader')
            instance.groups.add(team_leader)
        if instance.designation == 'Recruiter':
            recruiter, created = Group.objects.get_or_create(name='Recruiter')
            instance.groups.add(recruiter)
