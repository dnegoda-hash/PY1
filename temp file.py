"""
CryptoTracker  — десктопное приложение для мониторинга курсов криптовалют.
Разработано в соответствии с Техническим заданием от 2026 года.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests


class CryptoTrackerApp:
    """Главный класс приложения CryptoTracker."""

    API_URL = "https://api.coingecko.com/api/v3/simple/price"
    COINS = "bitcoin,ethereum,tether,binancecoin,solana,cardano"
    COIN_NAMES = {
        "bitcoin": "Bitcoin (BTC)",
        "ethereum": "Ethereum (ETH)",
        "tether": "Tether (USDT)",
        "binancecoin": "Binance Coin (BNB)",
        "solana": "Solana (SOL)",
        "cardano": "Cardano (ADA)",
    }

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CryptoTracker")
        self.root.geometry("480x380")
        self.root.resizable(False, False)

        self.setup_ui()
        self.fetch_data()  # Автозагрузка при старте

    def setup_ui(self) -> None:
        """Настройка графического интерфейса."""
        style = ttk.Style()
        style.theme_use("clam")

        # Верхняя панель
        header = ttk.Frame(self.root)
        header.pack(fill="x", padx=15, pady=15)

        ttk.Label(
            header,
            text="📈 Курсы популярных криптовалют к USD",
            font=("Segoe UI", 12, "bold"),
        ).pack(side="left")

        self.btn = ttk.Button(
            header, text="🔄 Обновить", command=self.fetch_data, width=15
        )
        self.btn.pack(side="right")

        # Таблица
        self.tree = ttk.Treeview(
            self.root, columns=("Crypto", "Price"), show="headings", height=8
        )
        self.tree.heading("Crypto", text="Валюта")
        self.tree.heading("Price", text="Цена (USD)")
        self.tree.column("Crypto", width=250, anchor="w")
        self.tree.column("Price", width=150, anchor="e")
        self.tree.pack(pady=10, padx=15, fill="both", expand=True)

        # Строка статуса
        self.status = ttk.Label(
            self.root, text="Инициализация...", foreground="gray",
            font=("Segoe UI", 9),
        )
        self.status.pack(pady=5)

    def fetch_data(self) -> None:
        """Получение данных с CoinGecko API и обновление интерфейса."""
        self.btn.config(state="disabled", text="⏳ Загрузка...")
        self.status.config(text="Подключение к API CoinGecko...", foreground="blue")
        self.root.update()

        try:
            response = requests.get(
                self.API_URL,
                params={"ids": self.COINS, "vs_currencies": "usd"},
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for coin_id, coin_data in data.items():
                price = coin_data.get("usd", 0)
                name = self.COIN_NAMES.get(coin_id, coin_id.capitalize())
                self.tree.insert("", "end", values=(name, f"${price:,.2f}"))

            self.status.config(text="✅ Данные успешно обновлены", foreground="black")

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                messagebox.showwarning(
                    "Лимит запросов",
                    "Превышен лимит бесплатных запросов CoinGecko. Подождите минуту.",
                )
            else:
                messagebox.showerror("Ошибка HTTP", f"Ошибка сервера: {e}")
            self.status.config(text="❌ Ошибка обновления", foreground="red")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка сети", "Проверьте подключение к интернету.")
            self.status.config(text="❌ Нет подключения к сети", foreground="red")

        except requests.exceptions.Timeout:
            messagebox.showerror("Таймаут", "Превышено время ожидания ответа.")
            self.status.config(text="❌ Таймаут запроса", foreground="red")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Непредвиденная ошибка:\n{e}")
            self.status.config(text="❌ Ошибка", foreground="red")

        finally:
            self.btn.config(state="normal", text="🔄 Обновить")


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoTrackerApp(root)
    root.mainloop()