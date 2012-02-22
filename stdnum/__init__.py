# __init__.py - main module
# coding: utf-8
#
# Copyright (C) 2010, 2011, 2012 Arthur de Jong
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA

"""A Python module to parse, validate and reformat standard numbers
and codes in different formats.

Currently this package supports the following formats:

 * ISBN (International Standard Book Number)
 * ISSN (International Standard Serial Number)
 * ISMN (International Standard Music Number)
 * ISAN (International Standard Audiovisual Number)
 * EAN (International Article Number)
 * BSN (Burgerservicenummer, the Dutch national identification number)
 * Onderwijsnummer (Dutch school number)
 * BTW (the Dutch VAT number)
 * CPF (Cadastro de Pessoas Físicas, the Brazillian national identification
   number)
 * RČ (Rodné číslo, the Slovak and Czech birth number)
 * SIREN (Système d'Identification du Répertoire des Entreprises, a French
   company identification number)
 * SSN (U.S. Social Security Number)
 * HETU (Finnish personal identity code)
 * CIF (Certificado de Identificación Fiscal, Spanish tax identification
   number)
 * DNI (Documento nacional de identidad, Spanish personal identity codes)
 * NIE (Número de Identificación de Extranjeros, Spanish identification number
   for foreigners)
 * CNP (Cod Numeric Personal, Romanian Numerical Personal Code)
 * EGN (ЕГН, Единен граждански номер, Bulgarian personal identity codes)
 * PNF (ЛНЧ, Личен номер на чужденец, Bulgarian personal number of a foreigner)
 * OIB (Osobni identifikacijski broj, Croatian personal identification number)
 * NIF (Número de Identificación Fiscal, Spanish VAT number)
 * FPA, ΦΠΑ (Foros Prostithemenis Aksias, the Greek VAT number)
 * Ust ID Nr. (Umsatzsteur Identifikationnummer, the German VAT number)
 * BTW, TVA, NWSt (Belgian VAT number)
 * PVN (Pievienotās vērtības nodokļa, Latvian VAT number)
 * CVR (Momsregistreringsnummer, Danish VAT number)
 * TVA (Numéro d'identification à la taxe sur la valeur ajoutée,
   Luxembourgian VAT number)
 * CF (Cod de înregistrare în scopuri de TVA, Romanian VAT number)
 * Partita IVA (Italian VAT number)
 * Αριθμός Εγγραφής Φ.Π.Α. (Cypriot VAT number)
 * UID (Umsatzsteuer-Identifikationsnummer, Austrian VAT number)
 * NIF (Número de identificação fiscal, Portuguese VAT number)
 * IČ DPH (Identifikačné číslo pre daň z pridanej hodnoty, Slovak VAT number)
 * ALV nro (Arvonlisäveronumero, Finnish VAT number)
 * DIČ (Daňové identifikační číslo, Czech VAT number)
 * VAT (Irish VAT number)
 * ANUM (Közösségi adószám, Hungarian VAT number)
 * KMKR (Käibemaksukohuslase, Estonian VAT number)
 * PVM (Pridėtinės vertės mokestis mokėtojo kodas, Lithuanian VAT number)
 * TVA (Numéro d'identification à la taxe sur la valeur ajoutée, French
   VAT number)
 * VAT (Maltese VAT number)
 * NIP (Numer Identyfikacji Podatkowej, Polish VAT number)
 * ID za DDV (Davčna številka, Slovenian VAT number)
 * VAT (Moms, Mervärdesskatt, Swedish VAT number)
 * VAT (United Kingdom (and Isle of Man) VAT registration number)
 * VAT (Идентификационен номер по ДДС, Bulgarian VAT number)
 * VAT (European Union VAT number)
 * IMEI (International Mobile Equipment Identity)
 * IMSI (International Mobile Subscriber Identity)
 * MEID (Mobile Equipment Identifier)
 * GRid (Global Release Identifier)
 * IBAN (International Bank Account Number)
 * ISIL (International Standard Identifier for Libraries and Related
   Organizations)

Furthermore a number of generic check digit algorithms are available:

 * the Verhoeff algorithm
 * the Luhn and Luhn mod N algorithms
 * some algorithms described in ISO/IEC 7064: Mod 11, 2, Mod 37, 2,
   Mod 97, 10, Mod 11, 10 and Mod 37, 36
"""

# the version number of the library
__version__ = '0.6'
