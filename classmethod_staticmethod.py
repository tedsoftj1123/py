class Practice:

    # python class에는 크게 인스턴스 메서드, 클래스 메서드, 스태틱 메서드로 3가지 종류가 있다.
    # 인스턴스 메서드의 첫번째 인자로 클래스의 객체(인스턴스)가 넘어오게된다
    def instance_method(self, args):
        self.뭐뭐 = 뭐뭐  # 인스턴스의 필드에 값을 할당 또는 업데이트

    # 클래스 메서드는 함수 선언식 위에 @classmethod를 달아서 표시하며 첫번째 인자로 클래스 자체가 넘어오게된다.
    @classmethod
    def class_method(cls, args):
        new_practice = cls()  # 클래스 자체이기 때문에 이런식으로 인스턴스화할 수 있다.

    # 스태틱 메서드는 함수 선언식 위에 @staticmehtod를 달아서 표시하며 인터프리터를 통해 특별한 인자를 추가로 제공받지 않는다.
    @staticmethod
    def static_method(args):
        print("You Called Static Method")


# static method vs class method
# 사실 자바 개발자로서 이 둘은 그냥 같은 클래스 맴버로 보이는데 python에서는 어떤 차이점이 존재할까?
# 사실 특벌한 경우가 아니라면 class method와 static method는 인자값을 넘겨주냐 안념겨주냐의-
# 차이가 있기에 이로 인해 파생되는 여러 차이점들이 발생하게된다.(자세한 경우 생략)

# 그래서 보통 class methdo는 팩토리 메서드를 구현할 때 사용하고 static method는 유틸성 함수를 구현할떄 사용하는것 같다.

