import xmlrpc.client

class ClinicClient:
    def __init__(self, server_address):
        self.server = xmlrpc.client.ServerProxy(server_address)

    def register_patient(self, clinic_name, patient_info):
        result = self.server.register_patient(clinic_name, patient_info)
        print(result)

    def get_queue_status(self, clinic_name):
        status = self.server.get_queue_status(clinic_name)
        print(f"Queue Status for {clinic_name}: {status}")

if __name__ == "__main__":
    server_address = "http://192.168.100.9:8000"  # Replace <server-ip> with the actual IP address of the server device
    client = ClinicClient(server_address)


    
    print("""Selamat Datang di Antredis
Klinik tersedia:
1. Klinik A
2. Klinik B
3. Klinik C
0. Keluar Aplikasi""")
    
    pilihan_menu = int(input("Pilihan menu: "))
    while pilihan_menu <= 3 and pilihan_menu >= 1:
        if pilihan_menu == 1:
            clinic_name = "Klinik A"
        if pilihan_menu == 2:
            clinic_name = "Klinik B"
        if pilihan_menu == 3:
            clinic_name = "Klinik C"

        medic_record_number = int(input("Nomor rekam medis: "))
        name = input("Nama Lengkap: ")
        dob = input("Tanggal Lahir (contoh: 30-01-2003): ")

        patient_info = {"medic_record_number": medic_record_number, "name": name, "dob": dob}
        client.register_patient(clinic_name, patient_info)
        client.get_queue_status(clinic_name)


        print("""Selamat Datang di Antredis
Klinik tersedia:
1. Klinik A
2. Klinik B
3. Klinik C
0. Keluar Aplikasi""")
