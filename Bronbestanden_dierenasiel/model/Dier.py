import datetime

class Dier:
    
    def __init__(self, parname: str, parbirthdate: datetime, parregistrationdate: datetime, parrace: str, pargender: str, parcastrated: bool ) -> None:
        self.name = parname
        self.birthdate = parbirthdate
        self.registrationdate = parregistrationdate
        self.race = parrace
        self.gender = pargender
        self.castrated = parcastrated

        # ********** property name - (setter/getter) ***********
        @property
        def name(self) -> str:
            """ The name property. """
            return self.__name
        
        @name.setter
        def name(self, value: str) -> None:
            self.__name = value

        # ********** property birthdate - (setter/getter) ***********
        @property
        def birthdate(self) -> datetime:
            """ The birthdate property. """
            return self.__birthdate
        
        @birthdate.setter
        def birthdate(self, value: datetime) -> None:
            self.__birthdate = value
        
        # ********** property registrationdate - (setter/getter) ***********
        @property
        def registrationdate(self) -> datetime:
            """ The registrationdate property. """
            return self.__registrationdate
        
        @registrationdate.setter
        def registrationdate(self, value: datetime) -> None:
            self.__registrationdate = value
        
        # ********** property race - (getter only) ***********
        @property
        def race(self) -> str:
            """ The race property. """
            return self.__race
        
        # ********** property gender - (setter/getter) ***********
        @property
        def gender(self) -> str:
            """ The gender property. """
            return self.__gender
        
        @gender.setter
        def gender(self, value: str) -> None:
            self.__gender = value
        
        # ********** property castrated - (setter/getter) ***********
        @property
        def castrated(self) -> bool:
            """ The castrated property. """
            return self.__castrated
        
        @castrated.setter
        def castrated(self, value: bool) -> None:
            self.__castrated = value

        
        
        
        
        