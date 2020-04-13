#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        CIF_emis = self.request.get("edCIFEmis", "Desconocido")
        nombre_emis = self.request.get("edNombreEmis", "Desconocido")
        dir_emis = self.request.get("edDirEmis", "Desconocido")
        pob_emis = self.request.get("edPobEmis", "Desconocido")
        prov_emis = self.request.get("edProvEmis", "Desconocido")
        cp_emis = self.request.get("edCPEmis", "Desconocido")
        pais_emis = self.request.get("edPaisEmis", "Desconocido")
        persona_cont_emis = self.request.get("edPersonaContEmis", "Desconocido")
        email_emis = self.request.get("edEmailEmis", "Desconocido")
        telefono_emis = self.request.get("edTelefonoEmis", "Desconocido")

        CIF_cliente = self.request.get("edCIFCliente", "Desconocido")
        nombre_cliente = self.request.get("edNombreCliente", "Desconocido")
        dir_cliente = self.request.get("edDirCliente", "Desconocido")
        pob_cliente = self.request.get("edPobCliente", "Desconocido")
        prov_cliente = self.request.get("edProvCliente", "Desconocido")
        cp_cliente = self.request.get("edCPCliente", "Desconocido")
        pais_cliente = self.request.get("edPaisCliente", "Desconocido")
        persona_cont_cliente = self.request.get("edPersonaContCliente", "Desconocido")
        email_cliente = self.request.get("edEmailCliente", "Desconocido")
        telefono_cliente = self.request.get("edTelefonoCliente", "Desconocido")

        concepto = self.request.get("edConcepto", "Desconocido")
        ppu = self.request.get("edPrecioUnidad", "Desconocido")
        uds = self.request.get("edUds", "Desconocido")
        bruto = self.request.get("edBruto", "Desconocido")
        iva = self.request.get("edIVA", "Desconocido")
        total = self.request.get("edTotal", "Desconocido")

        jinja = jinja2.get_jinja2(app=self.app)

        if len(CIF_emis.strip()) == 0:
            CIF_emis = "Desconocido"
        if len(nombre_emis.strip()) == 0:
            nombre_emis = "Desconocido"
        if len(dir_emis.strip()) == 0:
            dir_emis = "Desconocido"
        if len(pob_emis.strip()) == 0:
            pob_emis = "Desconocido"
        if len(prov_emis.strip()) == 0:
            prov_emis = "Desconocido"
        if len(cp_emis.strip()) == 0:
            cp_emis = "Desconocido"
        if len(pais_emis.strip()) == 0:
            pais_emis = "Desconocido"
        if len(persona_cont_emis.strip()) == 0:
            persona_cont_emis = "Desconocido"
        if len(email_emis.strip()) == 0:
            email_emis = "Desconocido"
        if len(telefono_emis.strip()) == 0:
            telefono_emis = "Desconocido"
        if len(CIF_cliente.strip()) == 0:
            CIF_cliente = "Desconocido"
        if len(nombre_cliente.strip()) == 0:
            nombre_cliente = "Desconocido"
        if len(dir_cliente.strip()) == 0:
            dir_cliente = "Desconocido"
        if len(pob_cliente.strip()) == 0:
            pob_cliente = "Desconocido"
        if len(prov_cliente.strip()) == 0:
            prov_cliente = "Desconocido"
        if len(cp_cliente.strip()) == 0:
            cp_cliente = "Desconocido"
        if len(pais_cliente.strip()) == 0:
            pais_cliente = "Desconocido"
        if len(persona_cont_cliente.strip()) == 0:
            persona_cont_cliente = "Desconocido"
        if len(email_cliente.strip()) == 0:
            email_cliente = "Desconocido"
        if len(telefono_cliente.strip()) == 0:
            telefono_cliente = "Desconocido"
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        if len(ppu.strip()) == 0:
            ppu = "Desconocido"
        if len(uds.strip()) == 0:
            uds = "Desconocido"
        if len(bruto.strip()) == 0:
            bruto = "Desconocido"
        if len(iva.strip()) == 0:
            iva = "Desconocido"
        if len(total.strip()) == 0:
            total = "Desconocido"

        valores_plantilla = {
            "CIF_emis": CIF_emis,
            "nombre_emis": nombre_emis,
            "dir_emis": dir_emis,
            "pob_emis": pob_emis,
            "prov_emis": prov_emis,
            "cp_emis": cp_emis,
            "pais_emis": pais_emis,
            "persona_cont_emis": persona_cont_emis,
            "email_emis": email_emis,
            "telefono_emis": telefono_emis,
            "CIF_cliente": CIF_cliente,
            "nombre_cliente": nombre_cliente,
            "dir_cliente": dir_cliente,
            "pob_cliente": pob_cliente,
            "prov_cliente": prov_cliente,
            "cp_cliente": cp_cliente,
            "pais_cliente": pais_cliente,
            "persona_cont_cliente": persona_cont_cliente,
            "email_cliente": email_cliente,
            "telefono_cliente": telefono_cliente,
            "concepto": concepto,
            "ppu": ppu,
            "uds": uds,
            "bruto": bruto,
            "iva": iva,
            "total": total
        }

        self.response.write(jinja.render_template("answer.html", **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/practica2', MainHandler)
], debug=True)
