from django.db import models
from django.urls import reverse
    

# class Trainer(models.Model):
#     first_name = models.CharField(max_length=30, help_text='Enter first name')
#     last_name = models.CharField(max_length=30, help_text='Enter last name')
#     price_per_hour = models.IntegerField(max_length=3, help_text='Pprice per hour of training')
#     specialization = models.TextField(max_length=150, help_text='Info about treiner specialization')

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'
    

class Schedule(models.Model):
    open_time = models.TimeField(auto_now=False, auto_now_add=False, help_text='Gym opening time', default='09:00')
    close_time = models.TimeField(auto_now=False, auto_now_add=False, help_text='Gym closing time', default='21:00')
    is_works_on_weekends = models.BooleanField(help_text='Is it works on weekends', default=False)

    def __str__(self) -> str:
        return f'Open time: {self.open_time}, Close time: {self.close_time}'
    

class GymMembership(models.Model):
    name = models.CharField(max_length=20, help_text='Name of gym membership')
    description = models.TextField(max_length=200, help_text='Description of gym membership')
    cost = models.IntegerField(help_text='Cost of the gym membership')

    def get_absolute_url(self):
        return reverse('gym_membership_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.name}'
    

class Gym(models.Model):
    name = models.CharField(max_length=20, help_text='Name of the gym')
    address = models.CharField(max_length=30, help_text='Address of the gym')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, help_text='Schedule of the gym', null=True, related_name='gyms')
    gym_membership = models.ManyToManyField(GymMembership, help_text='Gym membership of the gym', blank=True, related_name='gyms')

    def get_absolute_url(self):
        return reverse('fitnessclub_core:gym_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.name}'
    

class GroupClass(models.Model):
    name = models.CharField(max_length=20, help_text='Name of the group class')
    description = models.TextField(max_length=200, help_text='Description of the group class')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, help_text='Gym of the group class', null=True, related_name='group_classes')
    cost = models.IntegerField(help_text='Cost of the group class', default=0)
    # trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, help_text='Trainer of the group class', null=True)

    def get_absolute_url(self):
        return reverse('fitnessclub_core:group_class_detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.name}'

    