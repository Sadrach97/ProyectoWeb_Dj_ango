class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.idProducto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "idProducto": producto.idProducto,
                "nombre": producto.nombreProducto,
                "precio": producto.precio,
                "cantidad": 1,
            }


    def eliminar(self, producto):
        id = str(producto.idProducto)
        if id in self.carrito:
            del self.carrito[id]