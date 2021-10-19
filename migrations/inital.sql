CREATE TABLE "Movimientos" IF NOT EXISTS(
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"moneda_from"	TEXT NOT NULL,
	"cantidad_from"	REAL NOT NULL,
	"moneda_to"	TEXT NOT NULL,
	"cantidad_to"	REAL NOT NULL,
	"pu"           REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)

CREATE TABLE "saldo" IF NOT EXISTS(
	"ETH"	REAL NOT NULL,
	"LTC"	REAL NOT NULL,
	"BNB"	REAL NOT NULL,
	"EOS"	REAL NOT NULL,
	"XLM"	REAL NOT NULL,
	"TRX"	REAL NOT NULL,
	"BTC"	REAL NOT NULL,
	"XRP"	REAL NOT NULL,
	"BCH"	REAL NOT NULL,
	"USDT"	REAL NOT NULL,
	"BSV"	REAL NOT NULL,
	"ADA"	REAL NOT NULL,
)