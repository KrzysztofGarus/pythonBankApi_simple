# pythonBankApi_simple


| Metoda | HTTP	ADRES	 | CO ROBI?                         |
| ------ | ----------- | -------------------------------- |
| POST   | /create?number={number}&balance={balance}	     | Tworzy nowe konto bankowe o podanym numerze i saldzie |
| GET	 | /accounts     | Wyświetla wszystkie istniejące konta |
| GET	   | /balance?number={number} | Wyświetla saldo danego konta|
| POST   | /deposit?number={number}&amonunt={amount}   | Obsługuje operacje wpłaty na konto |
| POST | /withdraw?number={number}&amonunt={amount}     | Obsługuje operacje wypłaty z konta |
| POST | /transfer?number_from={number}&number_to={number}&amonunt={amount}     | Obsługuje operacje przelewu między kontami |
