import numpy as np
import matplotlib.pyplot as plt
# Constantes físicas de utilidad
MU_0 = 4 * np.pi * 1e-7 # H/m
c=3e8 # m/s
me=9.1e-31 # kg
eps_0=8.85e-12 # F/m
qe=1.6e-19 # C
# Objetos a evaluar y sus datos (se pueden introducir más)
objetos={
    "Jupiter": {
        "Radius": 71492, # km
        "B_surf": 9e-4, # T
        "Distance": 0.0000048, # pc
        "Obstacles": {
            "Io": {
            "Radius": 1787.3, # km
            "L": 5.9, # radios de Júpiter
            "Magnetic moment": 1.25e20, # J/T
            "Period": 1.77 # d
        }
                      },
        "Period": 0.41, # d
        "Electron concentration": 0.55*1e6, # m^-3
        "Solid angle": 0.55, # sr
        "Pedersen": 11, # S
        "Kinetic en.": 70 # keV, Delamere
    },
    "Saturno": {
        "Radius": 59338.36, # km
        "B_surf": 0.4e-4, # T
        "Distance": 0.0000096, # pc
        "Obstacles": {
            "Enceladus": {
                "Radius": 250.222, # km
                "L": 3.976, # radios de Saturno
                "Magnetic moment": 4.99e16, # J/T
                "Period": 1.37 # d
            }
        },
        "Period": 0.44, # d
        "Electron concentration": 0.001*1e+6, # m^-3
        "Solid angle": 0.55, # sr
        "Pedersen": 5.3, # S
        "Kinetic en.": 6 # keV, Gustin
    },
    "TVLM 513": {
        "Radius": 71492, # km
        "B_surf": 0.3, # T
        "Distance": 10.2, # pc
        "Obstacles": {
            "b": { #Se asumen las características de la Tierra
            "Radius": 6434.28, # km
            "L": 22, # radios de TVLM 513
            "Magnetic moment": 8e22, # J/T
            "Period": 1.5 # d
        },
            "blob": { #Se incluye una inhomogeneidad en el plasma
            "Radius": 70000, # ~radio de Júpiter, km
            "L": 30, # radios de TVLM 513
            "Magnetic moment": 1e27,# ~momento magnético de Júpiter, J/T
            "Relative speed": 250000 # m/s
            }
        },
        "Period": 0.08167, # d
        "Electron concentration": 1.25e5*1e+6, # m^-3
        "Solid angle": 0.05, # sr
        "Pedersen": 1.5, # S
        "Kinetic en.": 50 # keV, Khazanov
    },
    "WISE": {
        "Radius": 71492, # km
        "B_surf": 0.18, # T
        "Distance": 16.2, # pc
        "Obstacles": {
            "b": { #Se asumen las características de la Tierra
            "Radius": 6434.28, # km
            "L": 22, # radios de WISE J1122
            "Magnetic moment": 8e22, # J/T
            "Period": 1.5 # d
        },
            "blob": { #Se incluye una inhomogeneidad en el plasma
            "Radius": 70000, # ~radio de Júpiter, km
            "L": 30, # radios de WISE J1122
            "Magnetic moment": 1e27,# ~momento magnético de Júpiter, J/T
            "Relative speed": 250000 # m/s
            }
        },
        "Period": 0.08125, # d
        "Electron concentration": 1.25e5*1e+6, # m^-3
        "Solid angle": 0.05, # sr
        "Pedersen": 1.5, # S
        "Kinetic en.": 50 # keV, Khazanov
    },
"LSR J1835": {
        "Radius": 71492, # km
        "B_surf": 0.5, # T
        "Distance": 5.7, # pc
        "Obstacles": {
            "b": { #Se asumen las características de la Tierra
            "Radius": 6434.28, # km
            "L": 22, # Radios de LSR J1835
            "Magnetic moment": 8e22, # J/T
            "Period": 1.5 # d
        },
            "blob": { #Se incluye una inhomogeneidad en el plasma
            "Radius": 70000, # ~radio de Júpiter, km
            "L": 30, # Radios de LSR J1835
            "Magnetic moment": 1e27,# ~momento magnético de Júpiter, J/T
            "Relative speed": 250000 # m/s
            }
        },
        "Period": 0.1183882, # d
        "Electron concentration": 1.25e5*1e+6, # m^-3
        "Solid angle": 0.05, # sr
        "Pedersen": 1.5, # S
        "Kinetic en.": 50 # keV, Khazanov
    },
"LSPM J0036": {
        "Radius": 71492, # km
        "B_surf": 0.43, # T
        "Distance": 8.8, # pc
        "Obstacles": {
            "b": { #Se asumen las características de la Tierra
            "Radius": 6434.28, # km
            "L": 22, # radios de LSPM J0036
            "Magnetic moment": 8e22, # J/T
            "Period": 1.5 # d
        },
            "blob": { #Se incluye una inhomogeneidad en el plasma
            "Radius": 70000, # ~radio de Júpiter, km
            "L": 30, # radios de LSPM J0036
            "Magnetic moment": 1e27,# ~momento magnético de Júpiter, J/T
            "Relative speed": 250000 # m/s
            }
        },
        "Period": 0.1283, # d
        "Electron concentration": 1.25e5*1e+6, # m^-3
        "Solid angle": 0.05, # sr
        "Pedersen": 1.5, # S
        "Kinetic en.": 50 # keV, Khazanov
    },
    "AU Mic": {
        "Radius": 521892, # km
        "B_surf": 0.0745, # T
        "Distance": 9.8, # pc
        "Obstacles": {
            "b": { #Se asumen las características de la Tierra
            "Radius": 6434.28, # km
            "L": 3.014, # radios de AU Mic
            "Magnetic moment": 8e22, # J/T
            "Period": 1.5 # d
        },
            "blob": { #Se incluye una inhomogeneidad en el plasma
            "Radius": 70000, # ~radio de Júpiter, km
            "L": 30, # radios de AU Mic
            "Magnetic moment": 1e27,# ~momento magnético de Júpiter, J/T
            "Relative speed": 250000 # m/s
            }
        },
        "Period": 4.86, # d
        "Electron concentration": 1.25e5*1e6, # m^-3
        "Solid angle": 0.05, # sr
        "Pedersen": 1.5, # S
        "Kinetic en.": 50 # keV, Wang
    }
}
# Definición de métodos propios de la clase UCD
class UCD:
    def __init__(self, B_surf, radius): # Inicialización de atributos
        self.B_surf = B_surf # T
        self.radius = radius # km
    def Reff(self,mu,L,r_obst): # Radio efectivo del obstáculo
        B_surf=self.B_surf # T
        B_local= self.B_surf*(1/L)**3 # T
        if mu==0:
            r=r_obst*(B_local/B_surf)**(1/3) # km # Ecuación 62
        else:
            r=((MU_0*mu)/(4*np.pi*B_local))**(1/3) # km
        return r
    def v_relat(self,P_est, P_plan, L, R_central): # Velocidad relativa, sección 4.1.1
        t_rot = P_est * 86400 # s
        t_orb = P_plan * 86400 # s
        distancia_m = L * R_central*1000 # m
        v_plasma = (2*np.pi*distancia_m) / t_rot # m/s
        v_objeto = (2*np.pi*distancia_m) / t_orb # m/s
        v_rel = abs(v_plasma - v_objeto) # m/s
        return v_rel
    def ratio_Gamma(self,theta_k_deg,s): # Cociente de tasas de crecimiento temporales, sección 3.5
        theta=np.radians(theta_k_deg) # rad
        cos_theta=np.cos(theta)
        sin_theta=np.sin(theta)
        # s hace referencia al s-ésimo armónico de la ECMI
        if abs(cos_theta) < 1e-9:
            cos_theta=1e-9*np.sign(cos_theta)
        ratio_omega=1/s # ratio_omega=Omega_e/w
        x=(ratio_omega*sin_theta**2)/(2*cos_theta)
        T_X=-x+np.sqrt(x**2+1) # Ecuación 41
        T_O=-x-np.sqrt(x**2+1)
        den=1+(T_O)*cos_theta
        if abs(den)<1e-9: # Ajuste de estabilidad numérica
            den=1e-9
        return ((1+(T_O)**2)/(1+T_X**2))*((1+T_X*cos_theta)/den)**2
    def plot_ratio_Gamma(self):
        theta_deg=np.linspace(0,89.9,1000)
        ratio_s1=[self.ratio_Gamma(theta_k_deg=t,s=1) for t in theta_deg]
        ratio_s2=[self.ratio_Gamma(theta_k_deg=t,s=2) for t in theta_deg]
        plt.figure(figsize=(10,6))
        plt.plot(theta_deg,ratio_s1,label='Primer armónico',color='green')
        plt.plot(theta_deg,ratio_s2,label='Segundo armónico',color='red')
        plt.yscale('log')
        plt.title("Ratio de las tasas de crecimiento $\Gamma_X$ y $\Gamma_O$", fontsize=18)
        plt.xlabel("Ángulo de emisión (º)", fontsize=16)
        plt.ylabel("$\Gamma_X/\Gamma_O$", fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.legend()
        plt.show()
    def harmonic_weights(self,ne,B_Tesla):
        x1=0.15
        x2=0.3
        w_p=np.sqrt((ne*qe**2)/(me*eps_0)) # s^-1
        w_ce = 2 * np.pi * 28 * B_Tesla * 1e9  # s^-1
        x=w_p/w_ce # Selector de armónicos, secciones 3.4 y 5.1
        if x<=x1:
            weight_1,weight_2=1,0
        elif x>=x2:
            weight_1, weight_2 = 0, 1
        else:
            weight_1=(0.3-x)/0.15
            weight_2=1-weight_1
        return [weight_1,weight_2]
    def PPoynting(self, datos_objeto, rho_plasma, delta_B):
        p_mia_total = 0 # Inicialización
        p_saur_total = 0 # Inicialización
        sigma_p = datos_objeto.get("Pedersen") # S
        P_est=datos_objeto.get("Period") # d
        R_est=datos_objeto.get("Radius") # km
        obstaculos = datos_objeto.get("Obstacles", {})
        for nombre, datos in obstaculos.items():
            L = datos.get("L")
            Reff = self.Reff(mu=datos.get("Magnetic moment"), L=L, r_obst=datos.get("Radius")) # km
            B_local = self.B_surf * (1 / L) ** 3 # T # Ecuación 62
            v_a_local = B_local / np.sqrt(MU_0 * rho_plasma) # m/s # Ecuación 22
            sigma_a = 1 / (MU_0 * v_a_local) # S
            v_rel_prel=datos.get("Relative speed") #Inicialización, m/s
            if v_rel_prel is not None:
                v_rel=v_rel_prel # m/s
            else:
                P_plan = datos.get("Period") # d
                v_rel = self.v_relat(P_est, P_plan, L, R_est) # m/s
            alpha = sigma_p / (sigma_a * 2 + sigma_p) # Ecuación 53
            B_pole = self.B_surf # T
            v_a_pole = B_pole / np.sqrt(MU_0 * rho_plasma) # m/s
            R = Reff * np.sqrt(B_local / B_pole) # Ecuación 62, m
            area_pole = np.pi * R ** 2 # m^2
            s_para = (delta_B ** 2 * v_a_pole) / MU_0 # W/m^2, ecuación 55
            p_mia = s_para * 2 * area_pole # W
            p_saur = 2 * (area_pole / MU_0) * v_a_pole * ((v_rel / v_a_local) * alpha * B_local) ** 2 # W Ecuación 54
            p_mia_total += p_mia # W
            p_saur_total += p_saur # W
        print("Potencia disponible total: " + str(p_saur_total) + "W")
        return [p_mia_total, p_saur_total] # W

    def spectrum_frequencies(self, nombre, PPoyn, B_surf_Tesla, dist_pc, eff, ne, D_sr, energia):
        d_metros = dist_pc * 3.086e16 # m
        nu_ce = 28 * B_surf_Tesla * 1e9  # Hz, frecuencia electrón-ciclotrón
        nu_p = (np.sqrt((ne * qe ** 2) / (me * eps_0))) / (2 * np.pi)  # Hz, frecuencia de plasma
        gamma = 1 + (energia / 511) # Factor de Lorentz
        nu_ce_rel = nu_ce / gamma # Hz, frecuencia electrón-ciclotrón relativista, ecuación 29
        w_ce_rel = nu_ce_rel * (2 * np.pi) # s^-1, frecuencia electrón-ciclotrón relativista
        nu_max_s1 = nu_ce * 1.15 / 1e9  # GHz, ensanchamiento Doppler, sección 5.1
        nu_max_s2 = 2 * nu_max_s1  # GHz
        w_p = nu_p*(2 * np.pi) # s^-1
        lower_cut_X = (0.5 * w_ce_rel * (1 + np.sqrt(1 + (4 * w_p ** 2) / (w_ce_rel ** 2)))) / (2 * np.pi * 1e9) # GHz
        # Ecuación 39
        lower_cut_O = nu_p / 1e9 #GHz, ecuación 38
        nu_ghz = np.linspace(lower_cut_O * 0.1, nu_max_s2 * 2, 10000) #GHz
        nu_ce_rel_ghz=nu_ce_rel*1e-9 # GHz
        sigma_s1 = nu_ce_rel_ghz * 0.05 #GHz
        sigma_s2 = (2 * nu_ce_rel_ghz) * 0.05 #GHz
        sigma_X_s1 = sigma_s1 # GHz
        sigma_X_s2 = sigma_s2 # GHz
        sigma_O_s1 = 1.5*sigma_s1 # GHz
        sigma_O_s2 = 1.5*sigma_s2 #GHz
        perfil_X_s1 = np.exp(-(nu_ghz - nu_ce_rel*1e-9) ** 2 / (2 * sigma_X_s1 ** 2)) # Perfil Gaussiano de los picos resonantes
        perfil_X_s2 = np.exp(-(nu_ghz - 2*nu_ce_rel*1e-9) ** 2 / (2 * sigma_X_s2 ** 2)) # Sección 5.2.2
        perfil_O_s1 = np.exp(-(nu_ghz - nu_ce_rel*1e-9) ** 2 / (2 * sigma_O_s1 ** 2))
        perfil_O_s2 = np.exp(-(nu_ghz - 2*nu_ce_rel*1e-9) ** 2 / (2 * sigma_O_s2 ** 2))
        d_nu_1_X = (nu_max_s1 - lower_cut_X) * 1e9 # Hz # Ancho de banda de emisión
        d_nu_1_O = (nu_max_s1 - lower_cut_O) * 1e9 # Hz
        d_nu_2_X = (nu_max_s2 - lower_cut_X) * 1e9 # Hz
        d_nu_2_O = (nu_max_s2 - lower_cut_O) * 1e9 # Hz
        L = PPoyn * eff # W
        S_watts = L / (D_sr*d_metros ** 2) # W/m^2
        S_Jy = S_watts * 1e26 # Jy*Hz
        w1 = self.harmonic_weights(ne, B_surf_Tesla)[0]
        w2 = self.harmonic_weights(ne, B_surf_Tesla)[1]
        x = w_p / (nu_ce * 2 * np.pi) # Secciones 3.4 y 5.1
        if x < 0.05:
            wX_1, wX_2 = 0.8, 0.8
            wO_1, wO_2 = 0.2, 0.2
        elif x > 1.0:
            wX_1, wX_2 = 0.01, 0.8
            wO_1, wO_2 = 0.99, 0.2
        else:
            wX_1, wX_2 = 0.55, 0.8
            wO_1, wO_2 = 0.45, 0.2
        # Aplicamos simultáneamente los cortes frecuenciales y los perfiles resonantes Gaussianos
        rango_X_s1 = np.where((nu_ghz >= lower_cut_X) & (nu_ghz <= nu_max_s1), perfil_X_s1, 0.0)
        rango_X_s2 = np.where((nu_ghz >= lower_cut_X) & (nu_ghz <= nu_max_s2), perfil_X_s2, 0.0)
        rango_O_s1 = np.where((nu_ghz >= lower_cut_O) & (nu_ghz <= nu_max_s1), perfil_O_s1, 0.0)
        rango_O_s2 = np.where((nu_ghz >= lower_cut_O) & (nu_ghz <= nu_max_s2), perfil_O_s2, 0.0)
        # Paso a densidad de flujo radiante
        flujo_s1_X = w1 * S_Jy * wX_1 * rango_X_s1 / d_nu_1_X # Jy
        flujo_s1_O = w1 * S_Jy * wO_1 * rango_O_s1 / d_nu_1_O # Jy
        flujo_s2_X = w2 * S_Jy * wX_2 * rango_X_s2 / d_nu_2_X # Jy
        flujo_s2_O = w2 * S_Jy * wO_2 * rango_O_s2 / d_nu_2_O # Jy
        flujo_O = flujo_s1_O + flujo_s2_O # Jy
        flujo_X = flujo_s1_X + flujo_s2_X # Jy
        flujo_final = flujo_O + flujo_X #Jy
        plt.figure(figsize=(10, 6))
        plt.plot(nu_ghz, flujo_final, color='darkorange', lw=3, label='Espectro ECMI Total')
        plt.fill_between(nu_ghz, np.max(flujo_final) * 1e-5, flujo_O,
                         where=(nu_ghz >= lower_cut_O),
                         color='yellow', alpha=0.3, label='Contribución Modo O')
        plt.fill_between(nu_ghz, flujo_O, flujo_final,
                         where=(nu_ghz >= lower_cut_X),
                         color='blue', alpha=0.12, label='Contribución Modo X')
        plt.axvline(lower_cut_X, color='navy', linestyle='--', label=f'Corte modo X ({lower_cut_X:.2f} GHz)')
        plt.axvline(nu_max_s1, color='red', linestyle='--', label=f'Límite primer armónico ({nu_max_s1:.1f} GHz)')
        plt.yscale('log')
        plt.xlim(lower_cut_O*100, nu_max_s1 * 1.6)
        plt.ylim(np.max(flujo_final)*1e-5, np.max(flujo_final) * 4)
        plt.title(f"Espectro multimodo de {nombre} ({dist_pc} pc)", fontsize=18)
        plt.xlabel("Frecuencia (GHz)", fontsize=16)
        plt.ylabel("Densidad de flujo radiante (Jy)", fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.legend(loc='upper left')
        plt.show()
    def polarization(self,theta_k_deg):
        def polarization_purity(R,B,theta_k_deg,s):
            # Asumimos una cavidad auroral del tamaño del radio de la UCD
            L = R*1e3 # m
            B_Gauss = B * 1e4 # G
            # Tomamos el resultado de Melrose entre Gamma y omega para la Gamma_X
            omega_e = 2.8e6 * B_Gauss * 2 * np.pi # s^-1
            Gamma_X = 0.01 * omega_e # s^-1
            N=(Gamma_X*L)/c
            return np.tanh(N*(1-1/self.ratio_Gamma(theta_k_deg,s))) # Ecuación 66 para un ciclo de máser
        r_range = np.logspace(3, 7, 200) # km
        b_range = np.logspace(-9, 4, 200) # G
        r,b=np.meshgrid(r_range,b_range)
        P_primer=polarization_purity(r,b,theta_k_deg,s=1)
        P_segundo=polarization_purity(r,b,theta_k_deg,s=2)
        plt.figure(figsize=(10,6))
        cp = plt.pcolormesh(r, b, P_primer, shading='auto', cmap='magma', vmin=0, vmax=1)
        for nombre,datos in objetos.items():
            r_obj=datos["Radius"] # m
            b_obj=datos["B_surf"]*1e4 # G
            plt.scatter(r_obj,b_obj,edgecolors='black',s=100,label=nombre)
        plt.colorbar(cp, label='Pureza de polarización circular del primer armónico')
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Pureza de polarización del primer armónico (para $L=R_{UCD}$) \n para emisión a ' + str(theta_k_deg) + 'º y un ciclo de máser', fontsize=18)
        plt.xlabel('Radio de la fuente (km)',fontsize=16)
        plt.ylabel('Campo magnético superficial (G)',fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.legend(loc='lower right')
        plt.show()
        plt.figure(figsize=(10, 6))
        cp = plt.pcolormesh(r, b, P_segundo, shading='auto', cmap='magma', vmin=0, vmax=1)
        for nombre, datos in objetos.items():
            r_obj = datos["Radius"]
            b_obj = datos["B_surf"] * 1e4
            plt.scatter(r_obj, b_obj, edgecolors='black', s=100, label=nombre)
        plt.colorbar(cp, label='Pureza de polarización circular del segundo armónico')
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Pureza de polarización del segundo armónico (para $L=R_{UCD}$) \n para emisión a ' + str(theta_k_deg) + 'º y un ciclo de máser', fontsize=18)
        plt.xlabel('Radio de la fuente (km)', fontsize=16)
        plt.ylabel('Campo magnético superficial (G)',fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.legend(loc='lower right')
        plt.show()

    def saturacion(self, theta_k_deg, datos_objeto):
        plt.figure(figsize=(9, 6))
        nombres=['Júpiter','Saturno','TVLM 513-046546 ','WISE J112254.72+255022.2','LSR J1835+2359',
                 'LSPM J0036','AU Microscopii']
        for i, (nombre, datos) in enumerate(datos_objeto.items()):
            B_Tesla = datos.get("B_surf") # T
            B_Gauss = B_Tesla * 1e4 # G
            omega_e = 2.8e6 * B_Gauss * 2 * np.pi # s^-1
            Gamma_X = 0.01 * omega_e # s^-1
            ratio_gamma = self.ratio_Gamma(theta_k_deg, s=1) # Primer armónico, ecuación 41
            t_final = 5 / (Gamma_X * (1 - 1/ratio_gamma)) # s
            t = np.linspace(0, t_final, 1000) # s
            pureza_t = np.tanh(t * (Gamma_X * (1 - 1/ratio_gamma))) # Ecuación 64
            t_ns = t * 1e9 # ns
            plt.plot(t_ns, pureza_t, label=nombres[i], linewidth=2)
        plt.axhline(1.0, color='black', linestyle=':', alpha=0.6, label='Saturación teórica')
        plt.xlabel('Tiempo desde el inicio de la emisión (ns)', fontsize=16)
        plt.xscale('log')
        plt.ylabel('Pureza de la polarización circular $\mathbb{P}$', fontsize=16)
        plt.title('Evolución temporal de la saturación del máser (primer armónico)',fontsize=18)
        plt.grid(True, alpha=0.5)
        plt.ylim(-0.05, 1.05)
        plt.legend(loc='lower right')
        plt.show()
        lista_t_99=[]
        lista_x=[]
        for i,(nombre,datos) in enumerate(datos_objeto.items()):
            B_Tesla = datos.get("B_surf") # T
            ne = datos.get("Electron concentration") # m^-3
            B_Gauss = B_Tesla * 1e4 # G
            omega_e = 2.8e6 * B_Gauss * 2 * np.pi # s^-1
            Gamma_X = 0.01 * omega_e # s^-1
            ratio_gamma = self.ratio_Gamma(theta_k_deg, s=1)  # Primer armónico
            t_99 = 2.6466 * 1e9 / (Gamma_X * (1 - 1 / ratio_gamma)) # artanh(0.99) = 2.6466, ns
            lista_t_99.append(t_99)
            w_p = np.sqrt((ne * qe ** 2) / (me * eps_0)) # s^-1
            w_ce = omega_e # s^-1
            x = w_p / w_ce
            lista_x.append(x)
        plt.figure(figsize=(9,6))
        formas = ['o', 's', '^', 'D', 'X', 'v']
        for i in range(len(nombres)):
            plt.scatter(lista_x[i], lista_t_99[i],marker=formas[i % len(formas)], edgecolors='black',
                        s=120, label=nombres[i])
        plt.xlabel('Cociente de frecuencias $\omega_p / \omega_{ce}$', fontsize=16)
        plt.ylabel('Tiempo hasta saturación $\mathbb{P}_{99\%}$ (ns)', fontsize=16)
        plt.xscale('log')
        plt.yscale('log')
        plt.title('Influencia de la densidad del plasma en la saturación del máser',fontsize=18)
        plt.grid(True, alpha=0.5)
        plt.legend(loc='upper right')
        plt.show()

# Definición de objetos de clase
Jupiter = UCD(B_surf=objetos["Jupiter"]["B_surf"], radius=objetos["Jupiter"]["Radius"])
Saturno = UCD(B_surf=objetos["Saturno"]["B_surf"], radius=objetos["Saturno"]["Radius"])
wise=UCD(B_surf=objetos["WISE"]["B_surf"],radius=objetos["WISE"]["Radius"])
tvlm=UCD(B_surf=objetos["TVLM 513"]["B_surf"],radius=objetos["TVLM 513"]["Radius"])
lsr=UCD(B_surf=objetos["LSR J1835"]["B_surf"],radius=objetos["LSR J1835"]["Radius"])
lspm=UCD(B_surf=objetos["LSPM J0036"]["B_surf"],radius=objetos["LSPM J0036"]["Radius"])
aumic=UCD(B_surf=objetos["AU Mic"]["B_surf"],radius=objetos["AU Mic"]["Radius"])

# Potencias Poynting disponibles
powerjupiter = Jupiter.PPoynting(objetos["Jupiter"], 7e-17, 1e-6)[1]
powersaturno=Saturno.PPoynting(objetos["Saturno"],7e-18,1e-6)[1]
powerwise = wise.PPoynting(objetos["WISE"], 2e-17, 1e-6)[1]
powertvlm=tvlm.PPoynting(objetos["TVLM 513"],2e-17,1e-6)[1]
powerlsr=lsr.PPoynting(objetos["LSR J1835"],2e-17,1e-6)[1]
powerlspm=lspm.PPoynting(objetos["LSPM J0036"],2e-17,1e-6)[1]
poweraum=aumic.PPoynting(objetos["AU Mic"],1e-15,1e-6)[1]

# Representación del cociente de tasas de crecimiento
tvlm.plot_ratio_Gamma()

# Representación de espectros
Jupiter.spectrum_frequencies(nombre="Júpiter",PPoyn=powerjupiter,B_surf_Tesla=objetos["Jupiter"]["B_surf"], dist_pc=objetos["Jupiter"]["Distance"]
                          , eff=0.01,ne=objetos["Jupiter"]["Electron concentration"],D_sr=objetos["Jupiter"]["Solid angle"],energia=objetos["Jupiter"]["Kinetic en."])
Saturno.spectrum_frequencies(nombre="Saturno",PPoyn=powersaturno,B_surf_Tesla=objetos["Saturno"]["B_surf"], dist_pc=objetos["Saturno"]["Distance"], eff=0.01,ne=objetos["Saturno"]["Electron concentration"],D_sr=objetos["Saturno"]["Solid angle"],energia=objetos["Saturno"]["Kinetic en."])
wise.spectrum_frequencies(nombre="WISE J1122",PPoyn=powerwise,B_surf_Tesla=objetos["WISE"]["B_surf"], dist_pc=objetos["WISE"]["Distance"]
                           ,eff=0.01,ne=objetos["WISE"]["Electron concentration"], D_sr=objetos["WISE"]["Solid angle"],energia=objetos["WISE"]["Kinetic en."])
tvlm.spectrum_frequencies(nombre="TVLM 513",PPoyn=powertvlm,B_surf_Tesla=objetos["TVLM 513"]["B_surf"], dist_pc=objetos["TVLM 513"]["Distance"]
                           ,eff=0.01,ne=objetos["TVLM 513"]["Electron concentration"], D_sr=objetos["TVLM 513"]["Solid angle"],energia=objetos["TVLM 513"]["Kinetic en."])
lsr.spectrum_frequencies(nombre="LSR J1835",PPoyn=powerlsr,B_surf_Tesla=objetos["LSR J1835"]["B_surf"],dist_pc=objetos["LSR J1835"]["Distance"]
                        ,eff=0.01,ne=objetos["LSR J1835"]["Electron concentration"], D_sr=objetos["LSR J1835"]["Solid angle"],energia=objetos["LSR J1835"]["Kinetic en."])
lspm.spectrum_frequencies(nombre="LSPM J0036",PPoyn=powerlspm,B_surf_Tesla=objetos["LSPM J0036"]["B_surf"],dist_pc=objetos["LSPM J0036"]["Distance"]
                       ,eff=0.01,ne=objetos["LSPM J0036"]["Electron concentration"], D_sr=objetos["LSPM J0036"]["Solid angle"],energia=objetos["LSPM J0036"]["Kinetic en."])
aumic.spectrum_frequencies(nombre="AU Microscopii",PPoyn=poweraum,B_surf_Tesla=objetos["AU Mic"]["B_surf"],dist_pc=objetos["AU Mic"]["Distance"]
                       ,eff=0.01,ne=objetos["AU Mic"]["Electron concentration"], D_sr=objetos["AU Mic"]["Solid angle"],energia=objetos["AU Mic"]["Kinetic en."])

# Mapa de polarizaciones
Jupiter.polarization(theta_k_deg=70)

# Curvas de saturación
Jupiter.saturacion(theta_k_deg=70,datos_objeto=objetos)

# Dependencias de la potencia con el campo y el radio (definidas fuera de la clase por simplicidad)
campos_magneticos = np.array([objetos["Jupiter"]["B_surf"], objetos["Saturno"]["B_surf"], objetos["WISE"]["B_surf"],
                              objetos["TVLM 513"]["B_surf"], objetos["LSR J1835"]["B_surf"], objetos["LSPM J0036"]["B_surf"],
                              objetos["AU Mic"]["B_surf"]])
radios = np.array([objetos["Jupiter"]["Radius"], objetos["Saturno"]["Radius"], objetos["WISE"]["Radius"]
                      , objetos["TVLM 513"]["Radius"], objetos["LSR J1835"]["Radius"], objetos["LSPM J0036"]["Radius"],
                   objetos["AU Mic"]["Radius"]])
potencias_alfven = np.array([powerjupiter,powersaturno,powerwise,powertvlm,powerlsr,powerlspm,poweraum]) # potencias extraidas
# de PPoynting W
plt.figure(figsize=(10, 7))
formas = ['o', 's', '^', 'D', 'X', 'v']
nombres_objetos = ['Júpiter-Io', 'Saturno-Encélado', 'WISE J1122', 'TVLM 513', 'LSR J1835', 'LSPM J0036','AU Mic']
for i in range(len(nombres_objetos)):
    plt.scatter(campos_magneticos[i]*1e4, potencias_alfven[i], marker=formas[i % len(formas)], edgecolors='black', s=100,
                label=nombres_objetos[i])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Campo magnético superficial ($B_{surf}$ [G])',fontsize=16)
plt.ylabel('Potencia enviada por las alas de Alfvén ($P_{Alfven}$ [W])',fontsize=16)
plt.title('Dependencia de la potencia respecto \n al campo magnético',fontsize=18)
plt.grid(True, alpha=0.5)
plt.legend(loc='upper left')
plt.show()
plt.figure(figsize=(10, 7))
for i in range(len(nombres_objetos)):
    plt.scatter(radios[i], potencias_alfven[i], marker=formas[i % len(formas)], edgecolors='black', s=100,
                label=nombres_objetos[i])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Radio del objeto ($R_{est}$ [km])',fontsize=16)
plt.ylabel('Potencia enviada por las alas de Alfvén ($P_{Alfven}$ [W])',fontsize=16)
plt.title('Independencia de la potencia respecto \n al radio del objeto',fontsize=18)
plt.grid(True, alpha=0.5)
plt.legend(loc='lower right')
plt.show()
