
<?php
    // Obtener el nombre del formulario
    $ticket = isset($_POST['ticket']) ? strtoupper($_POST['ticket']) : '';
    $remito = isset($_POST['remito']) ? strtoupper($_POST['remito']) : '';
    $producto = isset($_POST['producto']) ? strtoupper($_POST['producto']) : '';
    $origen = isset($_POST['origen']) ? strtoupper($_POST['origen']) : '';
    $horaSalida = isset($_POST['horaSalida']) ? strtoupper($_POST['horaSalida']) : '';
    $entrada = isset($_POST['entrada']) ? intval($_POST['entrada']) : 0;
    $salida = isset($_POST['salida']) ? intval($_POST['salida']) : 0;
    $fecha = date("d/m/Y");
    $timestamp = time() + 72000; // 18000 segundos equivalen a 3 horas (-3 UTC)
    $horaEntrada = date("H:i", $timestamp);

    $resultado = $entrada - $salida;

    // Mostrar el nombre
    echo '
    <script>
        // Función para mostrar la ventana de información
        function mostrarVentana() {
            window.alert("CHIQUITA LA TANIA!!!");
        }
    </script>
    <table cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
        <!-- Resto del código HTML aquí -->
    </table>
    <p style="margin-top:0pt; margin-bottom:0pt;">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkIAAAACCAYAAAC0YLNFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAfSURBVFhH7cMBDQAADAIg+5f+7SFspE5VdTAAwKrkAVuUPt72ZWByAAAAAElFTkSuQmCC" width="578" height="2" alt=""><br>
    </p>
    <p style="margin-top:0pt; margin-bottom:0pt;">&nbsp;</p>
<table cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
    <tbody>
        <tr>
            <td style="width:415.3pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                <h1 style="margin-top:3.85pt; margin-left:7.85pt; margin-bottom:0pt; font-size:14pt;"><span style="font-family:Arial;">Panificadora Veneziana</span></h1>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width:415.3pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                <table cellspacing="0" cellpadding="0" style="margin-left:0.25pt; border-collapse:collapse;">
                    <tbody>
                        <tr>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:4.7pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Ticket: ' . $ticket . ' </p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Chofer:<span style="letter-spacing:-0.15pt;">&nbsp;PANIF. VENEZIANA</span></p>
                            </td>
                        </tr>
                        <tr>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:3.7pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Dominio: VEN001</p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:3.7pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Producto: ' . $producto . '</p>
                            </td>
                        </tr>
                        <tr style="height:14.7pt;">
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Transporte: VENEZIANA</p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Origen: ' . $origen . '</p>
                            </td>
                        </tr>
                        <tr>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:3.7pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Tipo: --</p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:3.65pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Destino: VENEZIANA RIO IV</p>
                            </td>
                        </tr>
                        <tr>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:3.7pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Remito: ' . $remito . '</p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:justify; font-size:10pt;">Observaci&oacute;n:</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
            </td>
        </tr>
        <tr>
            <td style="width:415.3pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                <table cellspacing="0" cellpadding="0" style="margin-left:0.25pt; border-collapse:collapse;">
                    <tbody>
                        <tr>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                                <table cellspacing="0" cellpadding="0" style="border:1.5pt solid #000000; border-collapse:collapse;">
                                    <tbody>
                                        <tr>
                                            <td style="width:185.8pt; padding-right:4.65pt; padding-left:4.65pt; vertical-align:top;">
                                                <table cellspacing="0" cellpadding="0" style="margin-left:0.25pt; border-collapse:collapse;">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:center; font-size:10pt;"><br><strong><span style="font-family:Arial;">Entrada</span></strong></p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:10pt;">Fecha: ' . $fecha . '</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:10pt;">Hora: ' . $horaEntrada . '</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; line-height:11.5pt;"><span style="font-size:10pt;">Operario: TURNO1</span></p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:3.65pt; margin-bottom:0pt; font-size:10pt;">Kilos: ' . $entrada . '</p>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
                            </td>
                            <td style="width:196.85pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                                <table cellspacing="0" cellpadding="0" style="border:1.5pt solid #000000; border-collapse:collapse;">
                                    <tbody>
                                        <tr>
                                            <td style="width:185.8pt; padding-right:4.65pt; padding-left:4.65pt; vertical-align:top;">
                                                <table cellspacing="0" cellpadding="0" style="margin-left:0.25pt; border-collapse:collapse;">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; text-align:center; font-size:10pt;"><br><strong><span style="font-family:Arial;">Salida</span></strong></p>
                                                            </td>
                                                        </tr>
                                                        <tr style="height:10.2pt;">
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:10pt;">Fecha: ' . $fecha . '</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:10pt;">Hora: ' . $horaSalida . '</p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:0pt; margin-bottom:0pt; line-height:11.5pt;"><span style="font-size:10pt;">Operario: TURNO1</span></p>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="width:173.5pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:middle;">
                                                                <p style="margin-top:3.65pt; margin-bottom:0pt; font-size:10pt;">Kilos: ' . $salida . '</p>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
            </td>
        </tr>
        <tr>
            <td style="width:415.3pt; padding-right:5.4pt; padding-left:5.4pt; vertical-align:top;">
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                <table cellspacing="0" cellpadding="0" style="margin-left:6.05pt; border:0.75pt solid #000000; border-collapse:collapse;">
                    <tbody>
                        <tr>
                            <td style="width:391.95pt; padding-right:5.03pt; padding-left:5.03pt; vertical-align:top;">
                                <p style="margin-top:9.2pt; margin-left:8.55pt; margin-bottom:0pt; font-size:10pt;"><strong><span style="font-family:Arial;">BRUTO: ' . $entrada . '</span></strong><span style="width:65.18pt; display:inline-block;">&nbsp;</span><strong><span style="font-family:Arial;">TARA:</span></strong><strong><span style="width:18.5pt; font-family:Arial; display:inline-block;">&nbsp;</span></strong><strong><span style="font-family:Arial;">' . $salida . '</span></strong><span style="width:57.24pt; display:inline-block;">&nbsp;</span><strong><span style="font-family:Arial;">NETO: ' . $resultado . '</span></strong></p>
                                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;">&nbsp;</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <p style="margin-top:0pt; margin-bottom:0pt; font-size:11pt;"><br></p>
            </td>
        </tr>
    </tbody>
</table>
<p style="margin-top:0pt; margin-bottom:0pt;"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkIAAAACCAYAAAC0YLNFAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAfSURBVFhH7cMBDQAADAIg+5f+7SFspE5VdTAAwKrkAVuUPt72ZWByAAAAAElFTkSuQmCC" width="578" height="2" alt=""><br></p>
<p style="margin-top:0pt; margin-bottom:0pt;">&nbsp;</p>';
echo '<script>mostrarVentana();</script>';
?>
