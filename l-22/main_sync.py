from sqlalchemy.orm import joinedload

from blog_app.models import Base, User, Post, Tag
from blog_app.models.database import engine, Session



def create_admin_user():
    user = User(username="admin", is_staff=True)
    print("User: ", user)

    session.add(user)
    session.commit()
    print("created admin user", user)



def get_first_user():
    user = session.query(User).get(1)
    print("user 1", user)


def create_user(username: str) -> User:
    """
    :param username:
    :return: User
    """

    user = User(username=username)
    print("creating user", user)
    session.add(user)
    session.commit()
    print("created user", user)

    return user

def create_post(author: User, title: str) -> Post:
    """
    :param author:
    :param title:
    :return:
    """
    post = Post(
        # author_id=author.id,
        author=author,
        title=title,
    )
    print("prepare post", post)
    session.add(post)
    session.commit()
    print("created post", post)

def create_tags():

    tag1 = Tag(name="news")
    tag2 = Tag(name="python")
    tag3 = Tag(name="flask")
    tag4 = Tag(name="django")

    session.add_all([
        tag1,
        tag2,
        tag3,
        tag4
    ])

    session.commit()



def get_user(username: str) -> User:
    """
    :param username:
    :return: User
    """
    # 100% username is in DB
    user = session.query(User).filter_by(username=username).one()
    # if user isn't in DB return none
    # user = session.query(User).filter_by(username=username).one_or_none()
    # return first user
    # user = session.query(User).filter_by(username=username).first()

    return user

def get_posts_by_author() -> list[Post]:
    posts = (
        session
        .query(Post)
        .join(User)
        .filter(
            User.username == "John",
            Post.title.ilike("%lesson%"),
        )
        .options(joinedload(Post.author).joinedload(User.posts))
        .all()
    )
    print("posts", posts)

    for post in posts:
        author: User = post.author
        print("post author", author)
        print("author posts", author.posts)


    return posts

def add_tags_to_posts():

    q_tag = session.query(Tag)
    tag_news: Tag = q_tag.filter_by(name="news").one()
    tag_python: Tag = q_tag.filter_by(name="python").one()
    tag_flask: Tag = q_tag.filter_by(name="flask").one()
    tag_django: Tag = q_tag.filter_by(name="django").one()

    posts: list[Post] = session.query(Post).all()

    for post in posts:
        tag_news.posts.append(post)
        tag_python.posts.append(post)
        if "flask" in post.title.lower():
            post.tags.append(tag_flask)
        if "django" in post.title.lower():
            post.tags.append(tag_django)

    session.commit()


def fetch_posts_and_users_by_tags():

    users: list[User] = (
        session
        .query(User)
        .join(Post)
        .join(Tag, Post.tags)
        .filter(Tag.name == "flask")
        .options(joinedload(User.posts).joinedload(Post.tags))
        .all()
    )
    print("user writing about flask:", users)

    for user in users:
        print("user", user)
        posts: list[Post] = user.posts
        for post in posts:
            print("-- post", post)
            print("--- with tags", post.tags)


if __name__ == "__main__":
    # don't use global vars!
    session = Session()

    Base.metadata.create_all(bind=engine)
    create_admin_user()
    get_first_user()

    create_user("John")
    create_user("Sam")

    user_john = get_user("John")
    user_sam = get_user("Sam")
    print(user_john)
    print(user_sam)

    create_post(user_john, "Flask lesson")
    create_post(user_sam, "Djan lesson")
    create_post(user_john, "Flask demo")

    get_posts_by_author()

    create_tags()

    add_tags_to_posts()

    fetch_posts_and_users_by_tags()

    session.close()
