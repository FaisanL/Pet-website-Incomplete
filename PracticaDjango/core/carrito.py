class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, Producto):
        id = str(Producto.codigo)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id" : Producto.codigo,
                "nombre": Producto.nombre,
                "precio": Producto.precio,
                "cantidad": Producto.stock,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += Producto.precio
        self.guardar_carrito(self)

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, Producto):
        id = str(Producto.codigo)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    def restar(self, Producto):
        id = str(Producto.codigo)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= Producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Producto)
            self.guardar_carrito()
    def limpiar(self):
        self.session["carrito"] = {}
        self.carrito.modified =True