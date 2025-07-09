from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.TextField(
        'Название сообщества'
    )
    slug = models.SlugField(
        'Слаг сообщества',
        unique=True,
    )
    description = models.TextField(
        'Описание сообщества',
    )

    class Meta:
        verbose_name = 'сообщество'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Сообщество',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'пост'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField('Комментарий')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='subscriber',
    )
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        verbose_name = 'подписка'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_pair_user_following',
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='prevent_self_follow',
            ),
        ]

    def __str__(self):
        return (f'{self.user} подписан на {self.following}')
