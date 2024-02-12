from sqlalchemy import create_engine, String, Float
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, Session



class Base(DeclarativeBase):
	pass


class Product(Base):
	__tablename__ = "product"

	id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
	name: Mapped[str] = mapped_column(String(256))
	price: Mapped[float] = mapped_column(Float(precision=3), nullable=False)
	image_url: Mapped[str] = mapped_column(String(256), nullable=True)



if __name__ == "__main__":
	engine = create_engine("mysql://takiy:password@localhost/elt_test_db")

	print(engine)

	Base.metadata.create_all(bind=engine)


	session = Session(bind=engine)

	products = [
					Product(name="RDB Comptuer Mouse", price=12.8, image_url="http://example.com/mouse.jpg"),
					Product(name="RDB Keyboard", price=19.99, image_url="http://example.com/keyboard.jpg"),
					Product(name="RDB Gadget", price=49.95, image_url="http://example.com/gadget.jpg"),
					Product(name="RDB Essential Kit", price=34.50, image_url="http://example.com/kit.jpg"),
					Product(name="RDB Headphones", price=79.99, image_url="http://example.com/headphones.jpg"),
					Product(name="RDB Backpack", price=55.00, image_url="http://example.com/backpack.jpg"),
					Product(name="RDB Microphone", price=70.99, image_url="http://example.com/smartwatch.jpg"),
					Product(name="RDB Speaker", price=39.99, image_url="http://example.com/speaker.jpg"),
					Product(name="RDB Water Bottle", price=14.99, image_url="http://example.com/waterbottle.jpg"),
					Product(name="RDB Portable Charger", price=29.99, image_url="http://example.com/charger.jpg"),
				]
	

	# session.add_all(products)

	# session.commit()



