import { Component, OnInit } from '@angular/core';
import { WarehouseService } from 'src/app/services/warehouse.service';

@Component({
  selector: 'add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent implements OnInit {

  products = {
    id_producto: 0,
    nombre: '',
    descripcion: ''
  }
  constructor(private productService: WarehouseService) {}


  ngOnInit() {
  }
  saveProduct(){
    const data = {
      id_producto: this.products.id_producto,
      nombre: this.products.nombre,
      descripcion: this.products.descripcion
    };

    this.productService.create(data)
      .subscribe(
        response => {
          console.log(response);
        },
        error => {
          console.log(error);
        });
  }
  newProduct() {
    this.products = {
      id_producto: 0,
      nombre: '',
      descripcion: ''
    };
  }
}
